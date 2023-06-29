def suma(*numeros):
  total = 0
  for numero in numeros:
    total = total + int(numero)
  return str(total)


total = suma(5,5,10,3)
print(total)
