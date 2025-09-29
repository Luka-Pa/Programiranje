# Izbornik za kalkulator
print("----------------------")
print("Izbornik za kalkulator")
print("----------------------")
print("1. Izračun napona struje")
print("2. Izračun jakosti struje")
print("3. Izračun otpora struje")
print("4. Serijski spoj")
print("5. Paralelni spoj")
print("----------------------")
opcija = int(input("Izaberite opceraciju(1/2/3/4/5):"))
#Strukture grananja
if opcija == 1:     # == !=< > <> >= <= - operatori usporedbe1
    print("Izračun napona struje")
    jakost=int(input("Unesite jakost struje: "))
    otpor=int(input("Upiši otpor:"))
    napon=jakost*otpor
    print(f"Napon je:, {napon} V")
elif opcija == 2:
    print("Izračun otpora struje")
    napon=int(input("Unesite napon: "))
    jakost=int(input("Unesite jakost struje: "))
    otpor=napon/jakost
    print(f"Otpor je:, {otpor} Ω")
elif opcija == 3:
    print("Izračun jakosti struje")
    napon=int(input("Unesite napon: "))
    otpor=int(input("Upiši otpor:"))
    jakost=napon/otpor
    print(f"Jakost je:, {jakost} A")
elif opcija == 4:
    print("Serijski spoj")
    R1=int(input("Unesite otpor R1: "))
    R2=int(input("Unesite otpor R2: "))
    Rs=R1+R2
    print(f"Ukupni otpor serijskog spoja je:, {Rs} Ω")
elif opcija == 5:
    print("Paralelni spoj")
    R1=int(input("Unesite otpor R1: "))
    R2=int(input("Unesite otpor R2: "))
    Rp=(R1*R2)/(R1+R2)
    print(f"Ukupni otpor paralelnog spoja je:, {Rp} Ω")

else:
    print("Pogrešan unos, pokušajte ponovo")