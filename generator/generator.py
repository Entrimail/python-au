import os


def read_data():
    d = open('file.txt', 'r').readlines()
    
    return d


def processing_data():
    d = read_data()
    h1 = d[0][:-1]
    h2 = d[1][:-1]
    header = f'\n## {h1}\n{h2}\n'
    code = d[3:]
    s = ''
    s += code[0][8:]
    for e in code[1:]:
        s += e[12:]
    code_n = f'\n```python\n{s}\n```\n'
    
    return code_n, header


def create_link():
    name = read_data()[0][0:-1]
    header = processing_data()[1]
    array = header.split()
    link = array[-1].split('/')[-2]
    link_new = f'+ [{name}](#{link})\n'

    return link_new


def create_file_without_link():
    code = processing_data()[0]
    header = processing_data()[1]

    file = header + code

    return file


def add_link():
    link = create_link()
    file = open('array.md', 'r').readlines()
    for element in range(1, len(file)):
        if '##' in file[element]:
            file[element - 1] += link + '\n'
            break
    f = open('array.md', 'w')
    f.writelines(file)


def write_data():
    data = create_file_without_link()
    f = open('array.md', 'a')
    f.write(data)
    f.close()


if os.stat('file.txt').st_size == 0:
    print('INPUT FILE IS EMPTY')
else:
    if __name__ == '__main__':
        write_data()
        add_link()

