value = 10
list_data = [1, 2, 3]


def fn_test():
    value = 20
    list_data = 30
    list_data = [30, 30]
    print(f"{value}, {list_data}")


def fn_test2(data):
    value = data
    print(f"{value}, {list_data}")


def fn_test3():
    list_data.append(33)
    print(f"{value}, {list_data}")


def fn_test4():
    list_data[2] = 444
    value = 3
    print(f"{value}, {list_data}")


fn_test()
fn_test2(value)
fn_test3()
fn_test4()