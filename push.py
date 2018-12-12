# Importa o publish do paho-mqtt
import paho.mqtt.publish as publish
# Publica
publish.single("topico/teste", "Oi, aqui é um teste", hostname="IP_OU_URL_BROKER")
