some_value = input("Podaj Licbę: ")
some_value = int(some_value)


while some_value > 0:
	one_sign = some_value % 10
	print(one_sign, end=" ")
	# print(one_sign)
	some_value = some_value // 10

print("Koniec")
# efekt działania
# 6 7 8 4 3
