# SmartWaste - Monitoramento Volumétrico com Arduino e Gateway Python

O **SmartWaste** é um protótipo físico de lixeira inteligente para monitoramento em tempo real do nível de resíduos urbanos, totalmente alinhado com o **ODS 11 da ONU (Cidades e Comunidades Sustentáveis)**. 

Este repositório contém a documentação e os códigos da versão física implementada em bancada, utilizando uma arquitetura de Gateway Serial-USB para conectar o microcontrolador à internet através do protocolo MQTT.

---

## 🛠️ Descrição do Hardware
* **Plataforma de Desenvolvimento:** Arduino UNO R3.
* **Sensor:** Sensor Ultrassônico HC-SR04 (Mede o nível de preenchimento de 5cm a 30cm).
* **Atuador:** Fita de LED 12V com controle de intensidade adaptativo.
* **Componente de Potência:** Transistor MOSFET (Configurado com GND comum).
* **Fonte de Alimentação:** Fonte Externa de 12V para alimentação dos LEDs.

---

## 💻 Arquitetura de Software e Linguagens
O projeto utiliza duas camadas de software trabalhando em conjunto:
1. **Firmware (C++):** Roda direto no Arduino Uno. Realiza a leitura do sensor HC-SR04, calcula a distância, ajusta o brilho do LED via sinal PWM (Pino ~6) e envia o dado bruto via comunicação Serial (`Serial.println`).
2. **Gateway de IoT (Python):** Roda no computador local. Abre a porta COM (USB), captura a string de distância vinda do Arduino e utiliza o protocolo MQTT para transmitir o dado para a nuvem.

---

## 🌐 Protocolos e Comunicação de Rede
* **Interface Local:** Serial-USB (Barramento UART a 9600 bps).
* **Camada de Rede:** TCP/IP via conexão local do Gateway.
* **Protocolo de Aplicação de IoT:** **MQTT** (Message Queuing Telemetry Transport).
* **Broker Utilizado:** HiveMQ Público (`broker.hivemq.com` na porta 1883).
* **Tópico do Projeto:** `MACKENZIE/SMARTWASTE/VOLUMETRIA`
