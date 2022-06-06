ll=int(input('Enter Lower limit of range:'))
ul=int(input('Enter Upper limit of range:'))

for num in range(ll, ul + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)