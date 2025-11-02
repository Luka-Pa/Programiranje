#-----Radnik-----
def izracunaj_serijski_otpor(R1, R2):
    return R1 + R2
def izracunaj_paralelni_otpor(R1, R2):
    return 1 / ((1 / R1) + (1 / R2))
def izracunaj_sumu_liste(lista_vrijednosti):
    """Prima listu brojeva i vraća njihovu sumu."""
    suma = 0
    for vrijednost in lista_vrijednosti:
        suma += vrijednost
    return suma
#-----Čistač-----
def ispisi_izbornik():
    print("\n=== KALKULATOR OTPORNIKA v1.0 ===")
    print("Odaberite opciju:")
    print("----------------------------------")
    print("  1. Izračun serijskog otpora (2 otpornika)")
    print("  2. Izračun paralelnog otpora (2 otpornika)")
    print("  3. O programu")
    print("  4. Izračun ukupnog serijskog otpora (N otpornika)")
    print("  0. Izlaz")
    print("----------------------------------")
    #-----Šef-----
while True:
    ispisi_izbornik()
    izbor = input("Unesite vaš izbor (0-4): ")
    if opcija == "0":
        print("Hvala što ste koristili kalkulator! Doviđenja!")
        break
    elif opcija == "1":
        print("\n--- Serijski spoj dvaju otpornika ---")
        try:
            r1 = float(input("Unesite R1 (Ω): "))
            r2 = float(input("Unesite R2 (Ω): "))
            rezultat = izracunaj_serijski_otpor(r1, r2)
            print(f"Ukupni otpor u seriji je: {rezultat:.4f} Ω")
        except ValueError:
            print("GREŠKA: Unos mora biti broj!")

        input("\nPritisnite Enter za povratak na glavni izbornik...")
        elif opcija == "2":
        print("\n--- Paralelni spoj dvaju otpornika ---")
        try:
            R1 = float(input("Unesite R1 (Ω): "))
            R2 = float(input("Unesite R2 (Ω): "))
            rezultat = izracunaj_paralelni_otpor(R1, R2)
            print(f"Ukupni otpor u paraleli je: {rezultat:.4f} Ω")
        except ValueError:
            print("GREŠKA: Unos mora biti broj!")

        input("\nPritisnite Enter za povratak na glavni izbornik...")

      
