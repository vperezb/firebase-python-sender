# coding=utf-8
import datetime
import json
import os

import time

import firebase_admin
from firebase_admin import messaging, credentials

__FIREBASE_API_KEY = 'AAAABJLe5KY:APA91bFW8AEoTC0Jru5-7qmpUZuGcyNbKLh-hPK07qw0jeqiv-hLfmB0y1ff735ZwWS6TVjJOB0JCZUy_juw-461a1Czs_km6cEXK4yGBB75S_ONSarQspFG8WbZMbAin6wuCbFbvtCS'


def send_message_to_token(message, token, app, validate_only=True):
    # [START send_to_token]
    # See documentation on defining a message payload.
    message = messaging.Message(
        data=data,
        token=token
    )
    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message, validate_only, app)
    # Response is a message ID string.
    # [END send_to_token]
    return ('Successfully sent message by token:', response)


def send_to_token(data, token, app, validate_only=True):
    # [START send_to_token]
    # See documentation on defining a message payload.
    message = messaging.Message(
        data=data,
        token=token
    )
    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message, validate_only, app)
    # Response is a message ID string.
    # [END send_to_token]
    return ('Successfully sent message by token:', response)


def send_to_topic(topic, data, app, validate_only=False):
    # [START send_to_topic]
    # See documentation on defining a message payload.
    message = messaging.Message(
        data=data,
        topic=topic,
    )
    # Send a message to the devices subscribed to the provided topic.
    response = messaging.send(message, validate_only, app)
    # Response is a message ID string.
    # [END send_to_topic]
    return('Successfully sent message by topic:', response)


def subscribe_to_topic(topic, tokens, app):
    # [START subscribe]
    # Subscribe the devices corresponding to the registration tokens to the
    # topic.
    response = messaging.subscribe_to_topic(tokens, topic, app)
    # See the TopicManagementResponse reference documentation
    # for the contents of response.
    return response.success_count
    # [END subscribe]


def unsubscribe_from_topic(topic, tokens, app):
    # [START unsubscribe]
    # Unubscribe the devices corresponding to the registration tokens from the
    # topic.
    response = messaging.unsubscribe_from_topic(tokens, topic, app)
    # See the TopicManagementResponse reference documentation
    # for the contents of response.
    return response.success_count
    # [END unsubscribe]
