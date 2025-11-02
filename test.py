otpornici = [100, 220, 330]
ukupni_otpor = 0 # Krećemo od nule

print("Zbrajam otpornike:")

# "Za svaki 'jedan_otpornik' U listi 'otpornici'..."
for jedan_otpornik in otpornici:
    print(f"  Dodajem: {jedan_otpornik}")
    ukupni_otpor = ukupni_otpor + jedan_otpornik
    # kraći zapis: ukupni_otpor += jedan_otpornik

print(f"Ukupni serijski otpor je: {ukupni_otpor} Ohma")
