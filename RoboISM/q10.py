a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))

print('Values Before Swapping')
print('a = ',a, 'and b = ',b)

a = a ^ b
b = a ^ b
a = a ^ b
print('Values After Swapping')
print('a = ',a, 'and b = ',b)