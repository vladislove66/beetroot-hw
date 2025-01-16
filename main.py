# sss = [42, "apple", True, {"name": "John Doe"}, (1, 2, 3), [3.14, 2.78]]
#
# print(sss[3]['name'])



def up(word):
    print(word.upper())

def down(word):
    print(word.lower())

def default(*args, **kwargs):
    print("XZ")

def process(command):
    command_dict = {
        'up': up,
        'down': down,
    }

    if command in command_dict:
        return command_dict[command]

    else:
        return default

process('up')('hoa')