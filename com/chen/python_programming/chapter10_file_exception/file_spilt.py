path = 'text_files/alice.txt'

def calcwords(path):
    try:
        with open(path) as file:
            contents = file.read()
    except FileNotFoundError:
            msg = "Sorry, the file " + path + " does not exist."
            print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + path + " has about " + str(num_words) + " words.")


def count(path,word):
    try:
        with open(path) as file:
            contents = file.read()
    except FileNotFoundError:
            msg = "Sorry, the file " + path + " does not exist."
            print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.lower().split()
        num_words = len(words)
        print("The file " + path + " has about " + str(num_words) + " words.")
        x = words.count(word.lower())
        print("the file has",x,word)


count(path,'the')


