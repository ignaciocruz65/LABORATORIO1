#define B 12
#define A 13
#define C 7
#define D 8
#define E 9
#define F 10
#define G 11
#define interruptor 2
#define APAGADOS 0
#define UNIDAD A0
#define DECENA A1
#define sensortmp A2
#define fototstor A5
#define TIMEDISPLAYON 1
#define motor 3
#define UPbttn 4
#define DOWNbttn 5

void setup()
{
  pinMode(A, OUTPUT);
  pinMode(B, OUTPUT);
  pinMode(C, OUTPUT);
  pinMode(D, OUTPUT);
  pinMode(E, OUTPUT);
  pinMode(F, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(interruptor, INPUT_PULLUP);
  pinMode(UPbttn, INPUT_PULLUP);
  pinMode(DOWNbttn, INPUT_PULLUP);
  pinMode(motor, OUTPUT);
  pinMode(UNIDAD, OUTPUT);
  pinMode(DECENA, OUTPUT);
  digitalWrite(UNIDAD, 0);
  digitalWrite(DECENA, 0);
  Serial.begin(9600);
}

int countDigit = 0;
int sube = 1;
int baja = 1;
int subePrevia = 1;
int bajaPrevia = 1;
int countP = 0;
int lectura = 0;
float temperatura = 0;
int valortstor;

void prenderLed(int led)
{
  digitalWrite(led, HIGH);
}

int keypressed(void)
{
  sube = digitalRead(UPbttn);
  baja = digitalRead(DOWNbttn);
  if (sube == 1)
    subePrevia = 1;
  if (baja)
    bajaPrevia = 1;
  if (sube == 0 && sube != subePrevia)
  {
    subePrevia = sube;
    return UPbttn;
  }
  if (baja == 0 && baja != bajaPrevia)
  {
    bajaPrevia = baja;
    return DOWNbttn;
  }
  return 0;
}

void printCount(int count)
{
  prendeDigito(APAGADOS);
  printDigit(count / 16);
  prendeDigito(DECENA);
  prendeDigito(APAGADOS);
  printDigit(count % 16);
  prendeDigito(UNIDAD);
}

void printDigit(int digit)
{
  digitalWrite(A, LOW);
  digitalWrite(B, LOW);
  digitalWrite(C, LOW);
  digitalWrite(D, LOW);
  digitalWrite(E, LOW);
  digitalWrite(F, LOW);
  digitalWrite(G, LOW);

  switch (digit)
  {
    case 0:
      prenderLed(A);
      prenderLed(B);
      prenderLed(C);
      prenderLed(D);
      prenderLed(E);
      prenderLed(F);
      break;
    case 1:
      prenderLed(B);
      prenderLed(C);
      break;
    case 2:
      prenderLed(A);
      prenderLed(B);
      prenderLed(G);
      prenderLed(E);
      prenderLed(D);
      break;
    case 3:
      prenderLed(A);
      prenderLed(B);
      prenderLed(G);
      prenderLed(C);
      prenderLed(D);
      break;
    case 4:
      prenderLed(B);
      prenderLed(F);
      prenderLed(G);
      prenderLed(C);
      break;
    case 5:
      prenderLed(A);
      prenderLed(F);
      prenderLed(G);
      prenderLed(C);
      prenderLed(D);
      break;
    case 6:
      prenderLed(A);
      prenderLed(E);
      prenderLed(G);
      prenderLed(C);
      prenderLed(D);
      prenderLed(F);
      break;
    case 7:
      prenderLed(A);
      prenderLed(B);
      prenderLed(C);
      break;
    case 8:
      prenderLed(A);
      prenderLed(B);
      prenderLed(C);
      prenderLed(F);
      prenderLed(G);
      prenderLed(D);
      prenderLed(E);
      break;
    case 9:
      prenderLed(A);
      prenderLed(B);
      prenderLed(C);
      prenderLed(F);
      prenderLed(G);
      break;
    case 10: // A en hexadecimal
      prenderLed(A);
      prenderLed(B);
      prenderLed(C);
      prenderLed(E);
      prenderLed(F);
      prenderLed(G);
      break;
    case 11: // B en hexadecimal
      prenderLed(C);
      prenderLed(D);
      prenderLed(E);
      prenderLed(F);
      prenderLed(G);
      break;
    case 12: // C en hexadecimal
      prenderLed(A);
      prenderLed(D);
      prenderLed(E);
      prenderLed(F);
      break;
    case 13: // D en hexadecimal
      prenderLed(B);
      prenderLed(C);
      prenderLed(D);
      prenderLed(E);
      prenderLed(G);
      break;
    case 14: // E en hexadecimal
      prenderLed(A);
      prenderLed(D);
      prenderLed(E);
      prenderLed(F);
      prenderLed(G);
      break;
    case 15: // F en hexadecimal
      prenderLed(A);
      prenderLed(E);
      prenderLed(F);
      prenderLed(G);
      break;
  }
}

void prendeDigito(int digito)
{
  if (digito == UNIDAD)
  {
    digitalWrite(UNIDAD, LOW);
    digitalWrite(DECENA, HIGH);
    delay(TIMEDISPLAYON);
  }
  else if (digito == DECENA)
  {
    digitalWrite(UNIDAD, HIGH);
    digitalWrite(DECENA, LOW);
    delay(TIMEDISPLAYON);
  }
  else
  {
    digitalWrite(UNIDAD, HIGH);
    digitalWrite(DECENA, HIGH);
  }
}

void loop()
{
  int pressed = keypressed();
  int modo = digitalRead(interruptor);
  lectura = analogRead(sensortmp);
  temperatura = map(lectura, 0, 1023, -5000, 45000);
  temperatura = temperatura / 100.00;
  valortstor = analogRead(fototstor);

  if (modo == 1)
  {
    if (temperatura >= 0 && temperatura <= 30)
    {
      digitalWrite(motor, HIGH);
    }
    else if (temperatura > 30)
    {
      Serial.println("La temperatura es demasiado alta, el motor se detuvo");
      digitalWrite(motor, LOW);
    }
    else
    {
      digitalWrite(motor, LOW);
      Serial.println("La temperatura no es óptima");
    }

    if (pressed == UPbttn)
    {
      countDigit++;
      if (countDigit > 99)
      {
        countDigit = 0;
      }
    }
    else if (pressed == DOWNbttn)
    {
      countDigit--;
      if (countDigit < 0)
      {
        countDigit = 99;
      }
    }

    if (valortstor > 60)
    {
      printCount(countDigit);
    }
    else if (valortstor < 40)
    {
      digitalWrite(UNIDAD, LOW);
      digitalWrite(DECENA, LOW);
      prendeDigito(APAGADOS);
    }
  }
  else if (modo == 0)
  {
    digitalWrite(motor, LOW);
    if (valortstor > 40)
    {
      printCount(countP);
    }
    else if (valortstor < 40)
    {
      digitalWrite(UNIDAD, LOW);
      digitalWrite(DECENA, LOW);
      prendeDigito(APAGADOS);
    }

    if (pressed == UPbttn)
    {
      countP++;
      if (countP > 15)
      {
        countP = 0;
      }
    }
    else if (pressed == DOWNbttn)
    {
      countP--;
      if (countP < 0)
      {
        countP = 15;
      }
    }
  }
}