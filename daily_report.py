import datetime
import json
import os

import slack

PDT = -7
JST = +9
hour = 9
minute = 28
channel = '#rpt-ryo'

time_difference = JST - PDT
# FIXME
time_difference = 0
current_timestamp = datetime.datetime.today()


text = f"""
Ryo's daily report for:
{current_timestamp.year}/{current_timestamp.month}/{current_timestamp.day}

Do:

• hogehoge

Did:

• foobar

"""


def create_timestamp():
    timestamp = int(datetime.datetime(
        current_timestamp.year,
        current_timestamp.month,
        current_timestamp.day,
    hour, minute,
    ).timestamp())
    return timestamp + 60 * 60 * time_difference


def main():
    client = slack.WebClient(token=os.environ['SLACK_AUTH_CODE'])
    response = client.api_call(
        'chat.scheduleMessage',
        json={
            'channel': channel,
            'blocks': json.dumps([{
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': text,
                },
            }]),
            'post_at': create_timestamp(),
        }
    )
    assert response['ok']


if __name__ == '__main__':
    main()
