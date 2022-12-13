def sort(arr):
    def change(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    bool = True
    
    x = -1
    while bool:
        bool = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                change(i - 1, i)
                bool = True
    return arr

mylist = []
print("Введите количество элементов: ")
while True:
    try:
        n = input()
        n = int(n)
        if (n<0):
            print("Введите положительное число: ")
            continue
        break
    except:
        print("Это не число! Введите число: ")

print("Введите элементы списка по одному: ")
for i in range(n):
    while True:
        try:
            x = input()
            x = float(x)
            mylist.append(x)
            break
        except:
            print("Это не число! Введите число: ")

print("Исходный список: ")
print(mylist)
print("Новый список: ")
print(sort(mylist))
