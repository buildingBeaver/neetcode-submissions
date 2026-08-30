def add_two_numbers() -> int:
    ui = input()
    str_l = ui.split(",")
    int_l = [int(n) for n in str_l]
    return int_l[0] + int_l[1]



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
