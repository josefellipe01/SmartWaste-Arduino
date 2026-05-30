import time
import serial
import paho.mqtt.client as mqtt

PORTA_SERIAL = 'COM3'  # Ajuste para a sua porta COM se for diferente
BAUD_RATE = 9600
BROKER_MQTT = "broker.hivemq.com"
PORTA_MQTT = 1883
TOPICO_PROJETO = "MACKENZIE/SMARTWASTE/VOLUMETRIA"

print("Conectando ao Broker MQTT HiveMQ...")
cliente_mqtt = mqtt.Client()

try:
    cliente_mqtt.connect(BROKER_MQTT, PORTA_MQTT, 60)
    cliente_mqtt.loop_start()
    print("Conexão com o MQTT estabelecida!")
except Exception as e:
    print(f"Erro no MQTT: {e}")
    exit()

print(f"Abrindo a porta serial {PORTA_SERIAL}...")
try:
    conexao_serial = serial.Serial(PORTA_SERIAL, BAUD_RATE, timeout=1)
    time.sleep(2)
    print("Aguardando dados do sensor...")
except Exception as e:
    print(f"Erro na Serial: {e}")
    cliente_mqtt.loop_stop()
    exit()

try:
    while True:
        if conexao_serial.in_waiting > 0:
            linha_bruta = conexao_serial.readline()
            try:
                linha_texto = inline_bruta.decode('utf-8').strip()
                if "Distancia:" in linha_texto:
                    print(f"[Arduino]: {linha_texto}")
                    dados_filtrados = ''.join(filter(str.isdigit, linha_texto))
                    if dados_filtrados:
                        distancia = int(dados_filtrados)
                        cliente_mqtt.publish(TOPICO_PROJETO, payload=str(distancia), qos=0)
                        print(f"➡️ [MQTT Enviado]: {distancia} cm no tópico {TOPICO_PROJETO}")
            except UnicodeDecodeError:
                pass
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nEncerrando Gateway...")
finally:
    conexao_serial.close()
    cliente_mqtt.loop_stop()
    cliente_mqtt.disconnect()
