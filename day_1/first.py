some_value = input("Podaj Licbę: ")
# some_value = int(some_value)

print(some_value)
print(some_value[1:4])
print(some_value[:4])
print(some_value[-3:])
print(some_value[:])
print(some_value[1:7:2])
print(some_value[::2])
print(some_value[::-1])

for x in some_value:
    print(x, end=" ")

print("Koniec")
# efekt działania
# 6 7 8 4 3
