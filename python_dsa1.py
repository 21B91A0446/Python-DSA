'''
Python program to find HCF of two numbers
'''
def HCF(n1,n2):
    l1 = []
    for i in range(2,n1+1):
        if n1%i == 0:
            l1.append(i)
    l2 = []
    for j in range(2,n2+1):
        if n2%j == 0:
            l2.append(j)
    cf = []
    for k in l1:
        if k in l2:
            cf.append(k)
    return cf[-1]
a = int(input("Enter any number: "))
b = int(input("Enter any number: "))
print(HCF(a,b))