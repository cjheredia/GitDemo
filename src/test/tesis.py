#ternas asociativas en el plano Fano
asociativas = ['1,2,3', '1,4,5', '6,2,4', '3,4,7', '7,2,5', '1,7,6', '5,3,6']

#El usuario introduce los Octoniones
x = input ("Introduzca el primer elemento mulpliplicador")
y = input ("Introduzca el segundo elemento mulpliplicador")

#se separan los octoniones quedando solo listas con los valores numéricos
octonion1 = x.split (sep="+")
octonion2 = y.split (sep="+")

#variables auxiliares
lista = []
multiplicado = []
q = 0
m = 0
myoctonion = ''
preoctonion = ''


# función que multilica las bases de los octoniones, utilizando las ternas asociativas, se le pasa parámetros
#las dos bases de los octoniones y devuelve el producto de estas.
def octonionmultiplier(alpha, bheta):
    #declaración de variables auxiliares
    i = 0
    j = 0
    delta = 0
    phi = 0
    cont = 0
    paridad = 1
    compr = ""
    producto = 0
    k = 0
    resultado = []
    #si las bases son iguales el resultado es -1
    if alpha == bheta:
        phi = 0
        delta = 1
        resultado = [(-1) * delta, 0]
    #si las bases son diferentes se procede a multiplicar de acuerdo a la lista de ternas establecidas y la
    #definición de multiplicación de los octoniones
    else:
        #mientras que la cantidad de ternas recorrida sea menor que 7, encontrar la terna que contiene las dos
        #bases dadas por parámetros
        #Una vez encontrada la terna el resultado del producto será el tercer elemento de la terna y el signo será
        #positivo si las permutaciones en la terna son pares
        #negativo si las permutaciones son impares
        while i < 7:
            setc = asociativas[i].split (sep=',')
            while j < 3:
                compr = setc[j]
                if compr == bheta:
                    cont = cont + 1
                    pos2 = setc.index (bheta)
                elif compr == alpha:
                    cont = cont + 1
                    pos1 = setc.index (alpha)
                if cont == 2:
                    while k < 3:
                        if (setc[k] == setc[pos1] or setc[k] == setc[pos2]):
                            paridad = paridad + 1
                        else:
                            producto = int (setc[k])
                            paridad = paridad + 1
                            if (pos1 > pos2):
                                producto = (-1) * producto
                            break
                        k = k + 1
                j = j + 1
                if producto != 0:
                    break
            j = 0
            cont = 0
            if producto != 0:
                break
            i = i + 1
        if paridad % 2 == 0:
            phi = 1
        else:
            phi = -1
        resultado = [(-1) * delta + phi * producto, 1]
    return resultado


# realiza la multiplicación distributiva de los dos octoniones
# los dos octoniones son guardados en listas y se realiza la multiplicación distributiva
# mediante la función octonionmultiplier(alpha, bheta)

while q < 8:
    aux = octonion1[q]
    aux = aux.split (sep="e")
    if len (aux) == 1 or aux[1] == '0':
        img1 = 0
    else:
        img1 = aux[1]
    real1 = int (aux[0])
    while m < 8:
        aux2 = octonion2[m].split (sep='e')
        real2 = int (aux2[0])
        realresult = real1 * real2
        if (len (aux2) == 1 or aux2[1] == '0') and (len (aux) == 1 or aux[1] == '0'):
            lista = [realresult, 0]
        elif len (aux2) == 2 and (len (aux) == 1 or aux[1] == '0'):
            lista = [realresult, aux2[1]]
        elif len (aux) == 2 and (len (aux2) == 1 or aux2[1] == '0'):
            lista = [realresult, aux[1]]
        else:
            img2 = aux2[1]
            result = octonionmultiplier (img1, img2)
            if result[1] == 0:
                realresult = realresult * (-1)
                lista = [realresult, result[1]]
            else:
                lista = [realresult, result[0]]
        multiplicado.append (lista)
        m = m + 1
    q = q + 1
    m = 0



#En este ciclo se realiza la suma de los elementos que tienen la misma base y se
# devuelve el resultado del producto de los dos octoniones

#se recorre la lista y se eliminan los elementos ya sumados, evitándose así que se sumen dobles
n = 0
m = 1
p = 0
listaauxliar = multiplicado.copy ()

while len (multiplicado) != 0:
    elemento = multiplicado[0]
    valor = int (elemento[1])
    real = int (elemento[0])
    new = real
    if len (multiplicado) != 0:
        multiplicado.remove (elemento)
    if valor == 0:
        while m < len (multiplicado):
            elemento2 = multiplicado[m]
            if valor == int (elemento2[1]):
                new = new + int (elemento2[0])
                multiplicado.remove (elemento2)
            else:
                m = m + 1
        m = 0
    else:
        while m < len (multiplicado):
            elemento2 = multiplicado[m]
            if valor == int (elemento2[1]):
                new = real + int (elemento2[0])
                multiplicado.remove (elemento2)
            elif (-1) * valor == int (elemento2[1]) or valor == (-1) * (int (elemento2[1])):
                new = real - int (elemento2[0])
                multiplicado.remove (elemento2)
            else:
                m = m + 1
    numeroo = str (new)
    if int (valor) < 0 and new < 0:
        preoctonion = '+' + str ((-1) * new) + 'e' + str ((-1) * valor)
    elif int (valor) < 0:
        unidad = 'e' + str ((-1) * valor)
        preoctonion = '-' + numeroo + unidad
    elif new < 0:
        unidad = 'e' + str (valor)
        preoctonion = '-' + str ((-1) * new) + unidad
    else:
        preoctonion = '+' + str (new) + 'e' + str (valor)
    if myoctonion == '':
        myoctonion = preoctonion
    else:
        myoctonion += preoctonion
    m = 0
    n = n + 1
    preoctonion = ''

    # p = 0

print (myoctonion)
