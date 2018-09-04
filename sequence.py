#Alli algorithmi
#1 asks how many numbers (n) of sequence should output
#2 starts by printing first 3 numbers in sequence, (1,2,3)
#3 repeat n-3 times 
# print next number in sequence as the sum of 3 previous numbers.
n = int(input("Enter the length of the sequence: ")) # Do not change this line
n1 = 1
n2 = 2
n3 = 3

if n == 1:
    print(n1)
elif n == 2:
    print(n1) 
    print(n2)
else: 
    print(n1)
    print(n2)
    print(n3)

for i in range(0, n-3):
    next_n = n1 + n2 + n3 
    print(next_n)
    n1 = n2 
    n2 = n3
    n3 = next_n
    i += 1