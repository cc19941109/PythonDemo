def factorial(n):
    result= n
    for i in range(1,n):
        result *=i
    return result


print(factorial(5))

def factorial2(n):
    if n==1:
        return 1
    else:
        return n*factorial2(n-1)

print(factorial2(5))

def power(x,n):
    if n ==1:
        return x
    else:
        return x*power(x,n-1)

print(power(2,4))