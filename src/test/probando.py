asociativas = [[1, 2, 3], [1, 4, 5], [2, 4, 6], [3, 4, 7], [2, 5, 7], [1, 6, 7], [5, 3, 6]]
i=0
j=0
cont=0
alpha = input (print ('Introduzca el primer elemento mulpliplicador'))
bheta = input (print ('Introduzca el segundo elemento mulpliplicador'))
while i<7:
  aux = asociativas[i]
  while j <= 3:
      if (aux[j] == alpha) or (aux[j] == bheta):
          # aux.append (setc[j])
          cont = cont + 1
          if cont == 2:
              paridad = j
              producto = j + 1
              break
      j = j + 1
  i= i+1

print(producto)
