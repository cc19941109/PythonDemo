from  collections import deque


def search(lines,parttern,history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if parttern in line :
            yield line,previous_lines
        previous_lines.append(line)

if __name__ =="__main__":
    with open('1.txt') as f:
        for line,prevlies in search(f,'python',5):
            for pline in prevlies:
                print(pline,end='')
            print(line ,end ='')
            print('-'*20)

