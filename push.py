# Importa o publish do paho-mqtt
import paho.mqtt.publish as publish
# Publica
topic = 'Senac/202/seu_nome'
broker = 'test.mosquitto.org'

while(True):
    msg = input('Digite sua mensagem para enviar: ')
    publish.single(topic, msg, hostname = broker)
