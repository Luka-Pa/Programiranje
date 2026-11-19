// C++ code
//
unsigned int napon_mV = 3750;
unsigned int kapacitet_mAh = 2600;
float naponV;
float kapacitet_Ah;
unsigned long ukupna_energija;
void setup()
{
  Serial.begin(9600);
  ukupna_energija = (unsigned long) napon_mV * kapacitet_mAh;
  
  naponV = (float)napon_mV / 1000;
  kapacitet_Ah = (float)kapacitet_mAh / 1000;
  
  Serial.print("Ukupna energija: ");
  Serial.println(ukupna_energija);
  
  Serial.print("Napon u V: ");
  Serial.println(naponV);
  
  Serial.print("Kapacitet u Ah: ");
  Serial.println(kapacitet_Ah);
  
}

void loop()
{
  
}