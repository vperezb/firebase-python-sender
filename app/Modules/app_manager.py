import firebase_admin
from firebase_admin import messaging, credentials

default_service_credentials_path = [os.path.join(os.path.expanduser('~'), '.credentials', 'service_credentials.json'), '.credentials/service_credentials.json']

__FIREBASE_API_KEY = 'AAAABJLe5KY:APA91bFW8AEoTC0Jru5-7qmpUZuGcyNbKLh-hPK07qw0jeqiv-hLfmB0y1ff735ZwWS6TVjJOB0JCZUy_juw-461a1Czs_km6cEXK4yGBB75S_ONSarQspFG8WbZMbAin6wuCbFbvtCS'


def initialize_app(service_credentials_path = None):
    if not service_credentials_path:
        service_credentials_path = default_service_credentials_path
    return firebase_admin.initialize_app(credentials.Certificate(service_credentials_path))
