import os
from slackclient import SlackClient

SLACK_TOKEN = os.environ.get('SLACK_TOKEN', None)
slack_client = SlackClient(SLACK_TOKEN)


def list_channels():
    channels_call = slack_client.api_call("channels.list")
    if channels_call['ok']:
        return channels_call['channels']
    return None


def channel_info(channel_id):
    channel_info = slack_client.api_call("channels.info", channel=channel_id)
    if channel_info:
        return channel_info['channel']
    return None

if __name__ == '__main__':
    channels = list_channels()
    if channels:
        print("Channels: ")
        for c in channels:
            print(c['name'] + " (" + c['id'] + ")")
            detailed_info = channel_info(c['id'])
            if detailed_info:
                print(detailed_info['latest']['text'])
    else:
        print("Unable to authenticate.")

