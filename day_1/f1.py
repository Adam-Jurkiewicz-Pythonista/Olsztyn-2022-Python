

def main(args):
    wynik = args + 4
    print(f"Wynik to {wynik}")

def main2(args):
    wynik = args + 4
    return wynik

def main3(args):
    wynik = args * 4
    return wynik

main(20)
w = main(4)
print(w)

w2 = main2(14.3)
print(w2)

w3 = main3("12.43")
print(w3)
