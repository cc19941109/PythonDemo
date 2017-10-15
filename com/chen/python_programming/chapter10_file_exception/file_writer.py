path = 'text_files/hello.txt'
path1 = 'hello.txt'

def write(path):
    with open(path,'w') as file:
        file.write("cc love programming!\n")
        file.write('hello world\n')
    print('test...')


def add(path,str=''):
    with open(path,'a') as file:
        file.write(str+'\n')


def writeName():
    name = input('your name:')
    add(path,name)

writeName()

