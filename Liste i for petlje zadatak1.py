
#  KALKULATOR V1.0 – Elektronički kalkulator otpornika


# ---------- RADNICI (Definiranje funkcije) ----------

def izracunaj_serijski_otpor(r1, r2):
    """Zbraja dva otpornika u seriji."""
    return r1 + r2


def izracunaj_paralelni_otpor(r1, r2):
    """Računa paralelni spoj dvaju otpornika."""
    return (r1 * r2) / (r1 + r2)

def izracunaj_napon(i, r):
    """Računa napon prema Ohmovom zakonu (U = I * R)."""
    return i * r


def izracunaj_sumu_liste(lista_vrijednosti):
    """Prima listu brojeva i vraća njihovu sumu."""
    suma = 0
    for vrijednost in lista_vrijednosti:
        suma += vrijednost
    return suma


# ---------- ČISTAČ (Izbornik) ----------

def ispisi_izbornik():
    print("\n=== ELEKTRONIČKI KALKULATOR OTPORNIKA v1.0 ===")
    print("Odaberite opciju:")
    print("  1. Izračun serijskog otpora (2 otpornika)")
    print("  2. Izračun paralelnog otpora (2 otpornika)")
    print("  3. Izračun napona (U = I * R)")
    print("  4. Izračun ukupnog serijskog otpora (N otpornika)")
    print("  0. Izlaz")
    print("--------------------------------------------")


# ---------- ŠEF (glavna petlja programa) ----------

while True:
    ispisi_izbornik()
    opcija = input("Unesite broj opcije: ")

    
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
            r1 = float(input("Unesite R1 (Ω): "))
            r2 = float(input("Unesite R2 (Ω): "))
            rezultat = izracunaj_paralelni_otpor(r1, r2)
            print(f"Ukupni otpor u paraleli je: {rezultat:.4f} Ω")
        except ValueError:
            print("GREŠKA: Unos mora biti broj!")

        input("\nPritisnite Enter za povratak na glavni izbornik...")

    
    elif opcija == "3":
        print("\n--- Izračun napona (U = I * R) ---")
        try:
            i = float(input("Unesite struju I [A]: "))
            r = float(input("Unesite otpor R [Ω]: "))
            rezultat = izracunaj_napon(i, r)
            print(f"Napon U iznosi: {rezultat:.4f} V")
        except ValueError:
            print("GREŠKA: Unos mora biti broj!")
    elif opcija == "4":
        print("\n--- Izračun serijskog otpora (N otpornika) ---")

    
    elif opcija == "4":
        print("\n--- Izračun serijskog otpora (N otpornika) ---")

        lista_otpora = []

        while True:
            print(f"   Trenutni otpornici u listi: {[f'{x:.2f} Ω' for x in lista_otpora]}")
            unos_str = input("Unesite vrijednost otpora (ili 'kraj' za izračun): ")

            if unos_str.lower() == 'kraj':
                break

            try:
                vrijednost = float(unos_str)
                if vrijednost <= 0:
                    print("GREŠKA: Otpor mora biti pozitivan broj.")
                else:
                    lista_otpora.append(vrijednost)
                    print(f"   -> Dodan otpornik: {vrijednost:.2f} Ω")
            except ValueError:
                print("GREŠKA: Unos mora biti broj ili riječ 'kraj'.")

        if len(lista_otpora) > 0:
            ukupni_otpor = izracunaj_sumu_liste(lista_otpora)
            print(f"\nREZULTAT: Ukupan serijski otpor za {len(lista_otpora)} otpornika je: {ukupni_otpor:.4f} Ω")
        else:
            print("\nNiste unijeli nijedan otpornik. Povratak na izbornik.")

        input("\nPritisnite Enter za povratak na glavni izbornik...")

    else:
        print("Nepoznata opcija! Pokušajte ponovno.")


