import json
from django.conf import settings
from paho.mqtt import publish

# MQTT
def mqtt_publish(topic, payload):
    auth = {
        'username': settings.MQTT_USER,
        'password': settings.MQTT_PASS
    }
    payload = json.dumps(payload).encode('utf-8')
    if settings.MQTT_TOPIC_PREFIX != '':
        topic = f'{settings.MQTT_TOPIC_PREFIX.rstrip("/")}/{topic}'
        # rstrip remove trailing slash

    publish.single(
        hostname=settings.MQTT_HOST,
        port=1883,
        auth=auth,
        topic=topic,
        payload=payload,
        retain=True,
        qos=0
    )
    print(f'single publish to {topic}')
