terms = int(input("number of turns: "))
n1 = 0
n2 = 1
sum = 0
if terms <= 0:
   print("Please enter a positive integer")
elif terms == 1:
   print("Fibonacci sequence upto",terms,"terms:")
   print(n1)
else:
   print("Fibonacci sequence upto", terms, "are :")
   while sum < terms:
       print(n1)
       x = n1 + n2
       n1 = n2
       n2 = x
       sum += 1
