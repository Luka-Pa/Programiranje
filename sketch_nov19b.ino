unsigned int adc = 612;
byte postotak;
unsigned int napon_mV;
byte donjiBajt;

void setup()
{
  Serial.begin(9600);
  postotak = (adc * 100UL) /1023;
  Serial.print("Postotak: "); Serial.println(postotak);
  napon_mV = (adc * 5000UL) / 1023;
  donjiBajt = adc;
  Serial.print("Napon: "); Serial.println(napon_mV);
  Serial.print("Decimalni byte: ");
  Serial.println(donjiBajt, DEC);
  Serial.print("Heksadecimalni byte: ");
  Serial.println(donjiBajt, HEX);
  Serial.print("Binarni byte: ");
  Serial.println(donjiBajt, BIN);
}
void loop()
{
  
}