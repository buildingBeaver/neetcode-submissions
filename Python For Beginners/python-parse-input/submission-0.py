from typing import List

def read_integers() -> List[int]:
    ui = input()
    string_list = ui.split(",")
    int_list = [int(l) for l in string_list]
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
