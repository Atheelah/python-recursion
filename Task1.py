# programme to display first 20 fibonnachi

def fibo(number):
    if number <= 1:
        return number
    else:
        return(fibo(number-1) + fibo(number-2))

number = 20
if number <= 0:
   print("Enter positive number :")
else:
    print("fibonacci numbers :")
for i in range(number):
       print(fibo(i), end=", ")

