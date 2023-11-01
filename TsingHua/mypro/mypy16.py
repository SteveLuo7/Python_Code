def factoria(n):

     if n ==1:
         return 1
     else:
         return n * factoria(n - 1)


result = factoria(5)
print(result)