
file_path2 = '/Users/chencheng/PycharmProjects/PythonDemo/com/chen/python_programming/chapter10_file_exception/text_files/readme.txt'
file_path = 'text_files/readme.txt'

def readAll():
    with open(file_path) as file_object:
        contents = file_object.read()
        print(contents)


def readByLine(path):
    with open(path) as file_object:
        for line in file_object:
            # 每行的末尾都有一个看不见的换行符
            print(line.rstrip())
        return file_object.readlines()


def readPI(path):
    s = ''
    with open(path) as file:
        for line in file:
            s += line.strip()
    return  s


def print_pi_inshort():
    s = readPI('text_files/pi_million_digits.txt')
    print(s[:52],'...')
    print('len =',len(s))
    return s

def hasBirthday():
    s =print_pi_inshort()
    x = input('your birthday:')
    if x in s:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Your birthday does not appear in the first million digits of pi.")

