def search(list,n):
    i = 0
    while i < len(list):
        if list[i] == n:
            return True
        i += 1
    return False

list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(list)
num = int(input("Enter number you wanted to search: "))

if search(list,num):
    print("Fount")
else:
    print("Not Found")