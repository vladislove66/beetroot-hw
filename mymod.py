def count_lines():
    name = input('Enter name of file for lines counting: ')
    full = name + '.txt'

    with open(full, 'r') as file:
        lines = file.readlines()
        print(f"The file contains {len(lines)} lines.")



def count_chars():
    name = input("Enter name of file for chars counting: ")
    full = name + '.txt'

    with open (full, 'r' ) as file:
        chars = file.read().replace(' ', '').replace('\n', '')
        print(f"The file contains {len(chars)} chars.")


def test():
    count_lines()
    count_chars()

