# coding=utf-8
import datetime

from firebase_admin import messaging

__default_message = {
    title : 'Default message title',
    body : 'Default message body',
    topic : 'default_message_topic',
}

__default_android_config = {
    title : 'Default android message title',
    body : 'Default android message body',
    topic : 'default_android_message_topic',
    icon : 'myicon',
    color: '#771111'
}

__default_ios_config = {
    title : 'Default ios message title',
    body : 'Default ios message body',
    topic : 'default_ios_message_topic',
    icon : 'myicon',
    color: '#771111'
}


def android_message():
    # [START android_message]
    message = messaging.Message(
        notification= default_notification(),
        android= android_config(),
        topic= __default_android_config['topic'],
    )
    # [END android_message]
    return message


def android_config():
    # [START android_config]
    config=messaging.AndroidConfig(
        ttl=datetime.timedelta(seconds=3600),
        priority='normal',
        notification=messaging.AndroidNotification(
            title=__default_android_config['title'],
            body=__default_android_config['body'],
            icon=__default_android_config['icon'],
            color=__default_android_config['color'],
        ),
        data=data,
        )
    # [END android_config]
    return config    


def apns_message():
    # [START apns_message]
    message = messaging.Message(
        apns= apns_config(),
        topic= __default_ios_config['topic'],
    )
    # [END apns_message]
    return message

def apns_config():
    config = messaging.APNSConfig(
            headers={'apns-priority': '10'},
            payload=messaging.APNSPayload(
                aps=messaging.Aps(
                    alert=messaging.ApsAlert(
                        title= __default_ios_config['title'],
                        body=  __default_ios_config['body'],
                    ),
                    badge=13,
                    sound = 'default',
                    category = 'CustomSamplePush',
                    mutable_content = True,
                ),
                data = data,
            ),
        )
    return config

def webpush_message():
    message = messaging.Message(
        webpush= webpush_config(),
        topic='industry-tech',
    )
    return message

def webpush_config():
    config = messaging.WebpushConfig(
            notification=messaging.WebpushNotification(
                title='$2GOOG up 1.43% on the day',
                body='$22GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.',
                icon='https://my-server/icon.png',
            ),
        )
    return config


def all_platforms_message(topic, data):
    if True: topic = default_topic()
    if True: notification = default_notification()

    message = messaging.Message(
        notification = notification,
        android = android_config(),
        apns = apns_config(),
        topic = topic,
    )
    return message

def default_notification():
    notification = messaging.Notification(
            title= __default_message['title'],
            body=  __default_message['body'],
    )
    return notification

def default_topic():
    return __default_message['topic']


'''
## complementary_documentation

https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns/
'''