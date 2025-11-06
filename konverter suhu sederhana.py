print("Program Konverter Suhhu Sederhana")

Celcius = float(input("Suhu dalam Celcius: "))
Reamur = (4/5) * Celcius 
Fahrenheit = (9/5) * Celcius + 32
Kelvin = Celcius + 273

print(f"""Suhu {round(Celcius, 2)} derajat celcius \
sama dengan {round(Reamur, 2)} derajat Reamur \n\
{round(Fahrenheit, 2)} derajat Fahrenheit \n\
{round(Kelvin, 2)} derajat Kelvin""")
