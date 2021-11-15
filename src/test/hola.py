# escribir
Nombre = 'Udemy'
# con f delante se formatea el string
#print(f'Hola {Nombre}')


#formatear string

#trabajando con arreglos
array = ['Venezuela','Argentina','Chile','Perú']
#añadir un valor a un arreglo
#array.append('Bolivia')
#print(array[4])

i=0
for pais in array:
    print(pais)
    if pais == "Argentina":
        print(f'{Nombre}, vive en {pais}')
       # break rompe el proceso del loop
        continue #pasa al siguiente
    if pais == "Chile":
        array[i] = "Aguante la educacion"
        print(array[i])
        continue  # pasa al siguiente
    i++1


#validar = insistance(array,lits)


#trabajando con diccionarios
dicc = {'Nombre ' : 'Carlos', 'edad':'32','cursos':['java','django']}
Nombre = dicc['Nombre ']

print(f'Hola {Nombre}')

#acces token = dicc('access_token')


#validar = insistante (dicc,dict)