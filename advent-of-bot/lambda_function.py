import json
import requests
import os
from datetime import datetime

PRIZES = {
    30: 'biobiljetter och bubbel',
    120: 'ost-, chark- och vinkorg',
    300: 'ölprovning, vinprovning och whiskyprovning för två',
    420: 'knivset och helkroppsmassage',
    600: 'matlagningskurs för två',
    750: 'middag för två',
    1000: 'weekendresa för två i Europa',
    1500: 'Hejareteslan',
    9999: 'Det Oändliga'
}

def get_results(leaderboard_url, session):
    res = requests.get(
        url=leaderboard_url,
        cookies={'session': session}
    )

    return res.json()

def format_results(payload):
    results = []
    for member_id, member_data in payload['members'].items():
        results.append(
            {
                'total_score': member_data['local_score'],
                'stars': member_data['stars'],
                'latest_completed': int(member_data['last_star_ts']),
                'name': member_data['name']
            })
    return results

def format_row(obj, name_col_width, score_col_width, stars_col_width):
    name = obj['name']
    score = obj['total_score']
    stars = obj['stars']
    latest = datetime.fromtimestamp(obj['latest_completed']).strftime('%a %-d %b %H:%M')
    
    return (
        f"{name}{' ' * (1 + name_col_width - len(name))}"
        f"{score}{' ' * (1 + score_col_width - len(str(score)))}"
        f"{stars}{' ' * (1 + stars_col_width - len(str(stars)))}"
        f"{latest}")

def format_leaderboard(members):
    members_sorted = sorted(members, key=lambda m: m['total_score'], reverse=True)
    
    longest_name = max(members, key=lambda m: len(m['name']))['name']
    longest_score = max(members, key=lambda m: m['total_score'])['total_score']
    longest_stars = max(members, key=lambda m: m['stars'])['stars']

    name_col_width = max(len('Namn'), len(longest_name))
    score_col_width = max(len('Totalt'), len(str(longest_score)))
    stars_col_width = max(len('Stjarnor'), len(str(longest_stars)))
    msg_arr = [
        f"Namn{' ' * (1 + name_col_width - 4)}"
        f"Totalt{' ' * (1 + score_col_width - 6)}"
        f"Stjärnor{' ' * (1 + stars_col_width - 8)}"
        f"Senaste test"
    ]
    
    members_formatted = [
        format_row(m, name_col_width, score_col_width, stars_col_width)
        for m in members_sorted
    ]
    msg_arr.extend(members_formatted)
    
    return '\n'.join(msg_arr)

def format_prizes(members):
    total_stars = sum([m['stars'] for m in members])
    reached_level = -1
    next_level = -1
    levels = list(PRIZES.keys())
    for i in range(len(levels)):
        if total_stars > levels[i]:
            reached_level = levels[i]
            next_level = levels[i+1]

    return f"Wooow :tada::tada: *{total_stars} stjärnor!* :tada::tada: Det är ju som bäst *{PRIZES[reached_level]}* och nästan *{PRIZES[next_level]}*!!"

def post_to_slack(text, leaderboard_mkdwn, slack_hook):
    req_body = {
        'text': text,
        'blocks': [
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': text
                }
            },
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': 'Och inte för att det spelar nån roll för någon men här är ställningen:'
                }
            },
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': f"```{leaderboard_mkdwn}```"
                }
            }
        ]
    }
    
    requests.post(
        url=slack_hook,
        json=req_body,
        headers={'content-type': 'application/json'}
    )

def lambda_handler(event, context):
    payload = get_results(
        os.environ['LEADERBOARD_URL'],
        os.environ['SESSION']
    )
    
    formatted = format_results(payload)
    
    leaderboard = format_leaderboard(formatted)
    prizes = format_prizes(formatted)
    post_to_slack(prizes, leaderboard, os.environ['SLACK_HOOK'])
    return {
        'statusCode': 200,
        'body': json.dumps(formatted)
    }

if __name__ == '__main__':
    lambda_handler(None, None)
