const int PIN_TRIG = 9;
const int PIN_ECHO = 10;
const int PIN_LED = 6;

void setup() {
  Serial.begin(9600);
  pinMode(PIN_TRIG, OUTPUT);
  pinMode(PIN_ECHO, INPUT);
  pinMode(PIN_LED, OUTPUT);
  analogWrite(PIN_LED, 0);
}

void loop() {
  digitalWrite(PIN_TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(PIN_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIG, LOW);

  long duracao = pulseIn(PIN_ECHO, HIGH);
  int distancia = duracao * 0.034 / 2;

  if (distancia < 2) distancia = 2;
  if (distancia > 35) distancia = 35;

  Serial.print("Distancia: ");
  Serial.print(distancia);
  Serial.println(" cm");

  int brilho = map(distancia, 5, 30, 255, 0);
  brilho = constrain(brilho, 0, 255);
  analogWrite(PIN_LED, brilho);

  delay(100);
}
