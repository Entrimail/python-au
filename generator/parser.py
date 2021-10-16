import os


def read_header():
    f = open('file.txt', 'r')
    h1 = f.readline()[:-1]
    h2 = f.readline()[:-1]
    new_h2 = h2.split('/')
    string = f'\n## {h1}\n{h2}\n'
    f.close()
    return string


def add_links():
    f = open('array.md', 'r')
    f1 = open('file.txt', 'r')
    h1 = f1.readline()[:-1]
    h2 = f1.readline()[:-1]
    copy_f = f.readlines()
    new_h2 = h2.split('/')
    for element in range(1, len(copy_f)):
        if '##' in copy_f[element]:
            copy_f[element - 1] += f'+ [{h1}]#({new_h2[-2]})\n\n'
            break
    f.close()
    f = open('array.md', 'w')
    f.writelines(copy_f)
    f1.close()
    f.close()


def write_data():
    f = open('array.md', 'a')
    f.write(read_header())
    f.write(read_code())
    f.close()


def read_code():
    f = open('file.txt', 'r').readlines()
    code = f[3:]
    s = ''
    s += code[0][8:]
    for e in code[1:]:
        s += e[12:]
    new_s = f'\n```python\n{s}\n```\n'
    return new_s


if os.stat('file.txt').st_size == 0:
    print('INPUT FILE IS EMPTY')
else:
    if __name__ == '__main__':
        write_data()
        add_links()

