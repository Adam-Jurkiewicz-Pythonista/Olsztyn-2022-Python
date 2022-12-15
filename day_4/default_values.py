def fun_dod( a: float, b: float):
    return a + b

def fun_dziel( a: float, b: float):
    return a / b

def fun_dod2( a: float, b: float = 10):
    return a + b

def fun_dod3( a: float, b: float = 10, c=30):
    return a + b * c

def fun4(a, b=3):
    return a+b

def wypisz(tekst):
    print(tekst)

def funkcja(a="AAA ", b="BBB ", c=...):
    if c is Ellipsis:
        c = "NIC"
    print(a+b+c)

print(fun_dod(3, 5))
print(fun_dziel(3, 5))
print(fun_dziel(a=3, b=5))
print(fun_dziel(5, 3))
print(fun_dod2(3, 5))
print(fun_dod2(3))
print(fun_dod2(3,))
print(fun_dod3(3))
print(fun_dod3(3,c=5))
wypisz("cosik")
funkcja(a="Wynik", b="działania")
funkcja(a="Wynik 2 ", b="działania - ", c=wypisz("Error"))