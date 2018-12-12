# Importa o publish do paho-mqtt
import paho.mqtt.publish as publish
# Publica
topic = 'topico/test'
broker = 'IP_OU_URL_BROKER'

while(True):
    msg = input('Digite sua mensagem para enviar: ')
    publish.single(topic, msg, hostname = broker)
