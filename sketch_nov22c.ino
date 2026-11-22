char oznakaKucista = 'T';          // Znak 'T' zahtijeva točno 1 bajt memorije (char)
bool termickaZastita = false;      // Logička vrijednost (true/false) stane u bool
unsigned int ulazniNapon = 12500;  // 12500 mV stane u unsigned int (do 65535)
unsigned int izlazniNapon = 5000;  // 5000 mV stane u unsigned int (do 65535)
unsigned int strujaTrosila = 450;  // 450 mA stane u unsigned int (do 65535)
unsigned long vrijemeRada = 86400; // 86400 s premašuje int, nužan unsigned long

void setup() {
  Serial.begin(9600);

  // 1. Izračun pada napona na regulatoru u voltima (V)
  float U_pad = (ulazniNapon - izlazniNapon) / 1000.0;

  // 2. Izračun disipirane (toplinske) snage u vatima (W)
  float P_dis = U_pad * (strujaTrosila / 1000.0);

  // 3. Izračun ukupno oslobođene toplinske energije u džulima (J)
  float E_toplina = P_dis * vrijemeRada;

  // 4. Izračun ukupnog zauzeća SRAM-a svih ulaznih i izlaznih varijabli (u bajtovima)
  byte ukupnoSRAM = sizeof(oznakaKucista) + sizeof(termickaZastita) + 
                    sizeof(ulazniNapon) + sizeof(izlazniNapon) + 
                    sizeof(strujaTrosila) + sizeof(vrijemeRada) + 
                    sizeof(U_pad) + sizeof(P_dis) + sizeof(E_toplina);
 
  Serial.print("Oznaka kucista: TO-220 (");
  Serial.print(oznakaKucista);
  
  Serial.print("Termicka zastita aktivna: ");
  Serial.println(termickaZastita ? "DA" : "NE");
  
  Serial.print("1. Pad napona (U_pad): ");
  Serial.print(U_pad, 2);
  Serial.println(" V");

  Serial.print("2. Disipirana snaga (P_dis): ");
  Serial.print(P_dis, 3);
  Serial.println(" W");

  Serial.print("3. Oslobodena toplinska energija (E_toplina): ");
  Serial.print(E_toplina, 1);
  Serial.println(" J");
 
  Serial.print("4. Ukupno zauzece SRAM-a: ");
  Serial.print(ukupnoSRAM);
 
  
}

void loop(){
  
}
