def sum(items):
    head,*tail=items
    return head + sum(tail) if tail else head

line = [1,2,4,5]
print(sum(line))