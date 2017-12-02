#include <Servo.h> 

int servo1Pin = 3;
int servo2Pin = 4;
int servo3Pin = 5;
Servo Servo1, Servo2, Servo3;

void setup()
{
  Servo1.attach(servo1Pin);
  Servo2.attach(servo2Pin); 
  Servo3.attach(servo3Pin); 
  Serial.begin(9600);
}

void loop()
{
  Servo1.write(0);
  Servo2.write(0);
  Servo3.write(0);
  delay(1000);   
    if(Serial.available())
  {
    switch(Serial.read())
    {
      case '1':Servo1.write(90);
               delay(6000);
               Servo1.write(0);
      break;
      case '2':Servo2.write(90);
               delay(6000);
               Servo2.write(0);
      break;
      case '3':Servo3.write(90);
               delay(6000);
               Servo3.write(0);
      break;
      default: break;
    }
  }
}

