c++
unsigned long otpornik = 100000;
float kapacitet = 47e-6;
float tau;
float vrijemePunjenja;

void setup()
{
  Serial.begin(9600);
  tau = otpornik * kapacitet;
  
  Serial.println(tau, 3);
  vrijemePunjenja = (5 * tau);
  Serial.print("Vrijeme punjenja: ");
  Serial.println(vrijemePunjenja);
}

void loop()
{
  
}