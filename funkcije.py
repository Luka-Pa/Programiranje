def ispisi_izbornik():
    # Izbornik za kalkulator
    print("----------------------")
    print("Izbornik za kalkulator")
    print("----------------------")
    print("1. Izračun napona struje")
    print("2. Izračun otpora struje")
    print("3. Izračun jakosti struje")
    print("0. Izlaz")
    print("----------------------")

def izracunaj_napon(jakost, otpor):
    return jakost * otpor

def izracunaj_otpor(napon, jakost):
    return napon / jakost

def izracunaj_jakost(napon, otpor):
    return napon / otpor

while True:
    ispisi_izbornik()

    try:
        opcija = int(input("Izaberite operaciju (1 / 2 / 3 / 0):"))
    except Exception as greska:
        print(f"Pogrešan unos: {greska}. Molimo unesite brojeve od 1 do 3. \nOdaberite 0 za izlaz.")
        continue

    #Struktura grananja
    if opcija == 1:     # == != < > <> >= <= - operatori usporedbe
        print("Izračun napona struje")
        try:
            jakost = int(input("Upiši jakost struje: "))
            otpor = int(input("Upiši otpor: "))
            
            napon = izracunaj_napon(jakost, otpor)

        except ValueError as greska:
            print("Molimo unesite brojeve.")
            continue
        except ZeroDivisionError as greska:
            print("Ne mogu dijeliti s nulom.")
            continue
        except Exception as greska:
            print(f"Pogrešan unos: {greska}. \nMolimo unesite brojeve.")
            continue


        print(f"Napon struje je: {napon} V")
    elif opcija == 2:
        print("Izračun otpora struje")
        try:
            napon = int(input("Upiši napon: "))
            jakost = int(input("Upiši jakost struje: "))

            otpor = izracunaj_otpor(napon, jakost)

        except ValueError as greska:
            print("Molimo unesite brojeve.")
            continue
        except ZeroDivisionError as greska:
            print("Ne mogu dijeliti s nulom.")
            continue
        except Exception as greska:
            print(f"Greška: {greska}. \nMolimo unesite brojeve.")
            continue
        print(f"Otpor je: {otpor} Ohm")
    elif opcija == 3:
        print("Izračun jakosti struje")
        try:
            napon = int(input("Upiši napon: "))
            otpor = int(input("Upiši otpor: "))

            jakost = izracunaj_jakost(napon, otpor)

        except ValueError as greska:
            print("Molimo unesite brojeve.")
            continue
        except ZeroDivisionError as greska:
            print("Ne mogu dijeliti s nulom.")
            continue
        except Exception as greska:
            print(f"Greška: {greska}. \nMolimo unesite brojeve.")
            continue
        print(f"Jakost struje je: {jakost} A")
    elif opcija == 0:
        print("Hvala na korištenju kalkulatora.")
        break
    else:
        print("Pogrešan unos")
        