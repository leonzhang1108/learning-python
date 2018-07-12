def fibonacci(n, sum, last):
  if n == 1:
    return sum
  else:
    return fibonacci(n - 1, last, sum + last)

print(fibonacci(100, 1, 1) / fibonacci(90, 1, 1))
print(fibonacci(80, 1, 1))