print("Anas Ahmed (18B-116-cs)")
print("LAB08_Programming exercise 3")
print("12/DEC/2018")

def even(n):
    for i in range(2,n+1):
        if i%2 ==0 and i%3 ==0:
            print(i, "is divisible by both 2 and 3")
        elif i%2 ==0:
            print(i,"is divisible by 2")
        elif i%3 ==0:
            print(i,"is divisible 3")
even(17)
