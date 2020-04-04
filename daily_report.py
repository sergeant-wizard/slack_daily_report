import datetime
import os

import slack

PDT = -7
JST = +9
time_difference = JST - PDT

# FIXME
time_difference = 0

current_timestamp = datetime.datetime.today()
timestamp = int(datetime.datetime(
    current_timestamp.year,
    current_timestamp.month,
    current_timestamp.day,
    8,
    52,
).timestamp())
timestamp += 60 * 60 * time_difference
text = f"""
Ryo's daily report for:
{current_timestamp.year}/{current_timestamp.month}/{current_timestamp.day}

Do:
- hoge
Did:
- bar
"""
client = slack.WebClient(token=os.environ['SLACK_AUTH_CODE'])
response = client.chat_scheduleMessage(
    channel='#rpt-ryo',
    text={
        'type': 'mrkdwn',
        'text': text,
    },
    post_at=timestamp,
)
assert response['ok']
assert response['message']['text'] == text