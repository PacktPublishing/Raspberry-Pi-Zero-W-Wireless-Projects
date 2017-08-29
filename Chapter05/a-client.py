def send_message(channel_id, message):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='pythonbot',
        icon_emoji=':robot_face:'
    )
    
if __name__ == '__main__':
    channels = list_channels()
    if channels:
        print("Channels: ")
        for channel in channels:
            print(channel['name'] + " (" + channel['id'] + ")")
            detailed_info = channel_info(channel['id'])
            if detailed_info:
                print('Latest text from ' + channel['name'] + ":")
                print(detailed_info['latest']['text'])
            if channel['name'] == 'general':
                send_message(channel['id'], "Hello " +
                             channel['name'] + "! It worked!")
        print('-----')
    else:
        print("Unable to authenticate.")
