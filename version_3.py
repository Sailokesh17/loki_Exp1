with open(r'C:\Users\Sai Lokesh\OneDrive\Desktop\SW Lab\Exp_1\data.txt', 'r') as file:
    a = float(file.readline())
    b = float(file.readline())
    c = float(file.readline())
    x = float(file.readline())

y = a * x * x + b * x + c
print('The value of y is:', y)
