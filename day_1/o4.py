print("Hej - mój pierwszy program")
print("-----")
# print("Jak masz na imię?")
my_name = input("Jak masz na imię?")
print("Hej", my_name, "Ja jestem Python")
print("Hej " + my_name + " Ja jestem Python")
print(f"Hej {my_name} Ja jestem Python")

birthday = input("Podaj rok urodzenia: ")
birthday = int(birthday)
year = 2022
age = year - birthday
print(f"Masz {age} lat.")
