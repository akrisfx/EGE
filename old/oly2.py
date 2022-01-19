first = int(input())
second = int(input())
N = int(input())
if (N % (first + second)) == 0:
   print(int((N / (first + second)) * 2))
else:
   if (N % (first + second)) <= second:
       print(int(((N//(first + second)) * 2) + 1))
   else:
       print(int(((N//(first + second)) * 2) + 2))
