number = int(input('please enter n ='))
s = 0
for i in range(0, number):
    if number % i ==0:
        s += i 
    if s == number:
        print(number,' là số hoàn hảo')
