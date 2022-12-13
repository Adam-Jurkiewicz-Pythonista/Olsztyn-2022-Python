def read_datas():
    h_start = float(input("Wys w m: "))
    v_start = float(input("Prędk w m/s: "))

    if h_start < 10:
        print("Za mała wartość")
        return None

    if v_start < 2:
        print("Za mała wartość")
        return None

    return (h_start, v_start)

initial_values = None
while initial_values is None:
    print("Podaj dane:")
    initial_values = read_datas()

print(f"Wczytano: {initial_values}")
h, v = initial_values
print(f"{h=}, {v=}")  # od Python 3.8
