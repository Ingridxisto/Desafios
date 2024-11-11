def inverter_string(texto):
    invertida = ""
    for caracter in texto:
        invertida = caracter + invertida
    return invertida


texto = "Acredite em si mesmo e você será imparável"

print("String invertida:", inverter_string(texto))
