import random

def juegajuan():
    #Se tiran ambos dados
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    
    #En caso de que el primer dado sea 4 y el segundo no
    if dado1 == 4 and dado2 != 4:
        #Si el segundo dado es menor o igual a 3 se tira de nuevo
        if dado2 <= 3:
            nuevoDado = random.randint(1,6)
            return nuevoDado
        else:
            return dado2
    #En caso de que el segundo dado sea 4 y el primero no
    elif dado1 != 4 and dado2 == 4:
        #Si el primer dado es menor o igual a 3 se tira de nuevo
        if dado1 <= 3:
            nuevoDado = random.randint(1,6)
            return nuevoDado
        else:
            return dado1
    #En caso de que ambos dados sean 4
    elif dado1 == 4 and dado2 == 4:
        return dado1
    #En caso de que ninguno de los dos dados sea 4
    else:
        #Se tiran de nuevo los dos dados
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        #Si el primer dado es 4 y el segundo no, se retorna el valor del segundo dado
        if dado1 == 4 and dado2 != 4:
            return dado2
        #Si el segundo dado es 4 y el primero no, se retorna el valor del primer dado
        elif dado1 != 4 and dado2 == 4:
            return dado1
        #Si ambos dados son 4, se retorna 4
        elif dado1 == 4 and dado2 == 4:
            return 4
        #Si ninguno de los dos dados es 4, se retorna 0
        else:
            return 0

def juegamaria(resultadojuan):
    #Se tiran ambos dados
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    
    #En caso de que el primer dado sea 4 y el segundo no
    if dado1 == 4 and dado2 != 4:
        #Si el dado de Maria es mayor al de Juan no se vuelve a tirar
        if dado2 > resultadojuan:
            return dado2
        #Si el dado de maria es igual al de Juan y es menor o igual a 3 se tira de nuevo
        if dado2 == resultadojuan:
            if dado2 <= 3:
                nuevoDado = random.randint(1,6)
                return nuevoDado
            else:
                return dado2
        #Si el dado de Maria es menor al de Juan se tira de nuevo
        else:
            nuevoDado = random.randint(1,6)
            return nuevoDado
    #En caso de que el segundo dado sea 4 y el primero no
    elif dado1 != 4 and dado2 == 4:
        #Si el dado de Maria es mayor al de Juan no se vuelve a tirar
        if dado1 > resultadojuan:
            return dado1
        #Si el dado de maria es igual al de Juan y es menor o igual a 3 se tira de nuevo
        if dado1 == resultadojuan:
            if dado1 <= 3:
                nuevoDado = random.randint(1,6)
                return nuevoDado
            else:
                return dado1
        #Si el dado de Maria es menor al de Juan se tira de nuevo
        else:
            nuevoDado = random.randint(1,6)
            return nuevoDado
    #En caso de que ambos dados sean 4
    elif dado1 == 4 and dado2 == 4:
        #Si el dado de Maria es mayor al de Juan no se vuelve a tirar
        if dado2 > resultadojuan:
            return dado2
        #Si el dado de maria es igual al de Juan
        if dado2 == resultadojuan:
            return dado2
        #Si el dado de Maria es menor al de Juan se tira de nuevo
        else:
            nuevoDado = random.randint(1,6)
            return nuevoDado
    #En caso de que ninguno de los dos dados sea 4
    else:
        #Se tiran de nuevo los dos dados
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        #Si el primer dado es 4 y el segundo no, se retorna el valor del segundo dado
        if dado1 == 4 and dado2 != 4:
            return dado2
        #Si el segundo dado es 4 y el primero no, se retorna el valor del primer dado
        elif dado1 != 4 and dado2 == 4:
            return dado1
        #Si ambos dados son 4, se retorna 4
        elif dado1 == 4 and dado2 == 4:
            return 4
        #Si ninguno de los dos dados es 4, se retorna 0
        else:
            return 0

def juego():
    resultadojuan = juegajuan()
    resultadomaria = juegamaria(resultadojuan)
    #print("Juan: ", resultadojuan)
    #print("Maria: ", resultadomaria)
    if resultadojuan > resultadomaria:
        #print("Gana Juan")
        return 1
    elif resultadojuan < resultadomaria:
        #print("Gana Maria")
        return 2
    else:
        #print("Empate")
        return 0


"""
PRINTS DE LAS SIMULACIONES
"""

### RESULTADOS PARA 1000 ###
resultados1000 = []
for i in range(1000):
  resultados1000.append(juego())

print("Resultados de 1000 juegos (Frecuencia Relativa):")
print("Juan gana: ", resultados1000.count(1)/1000)
print("Maria gana: ", resultados1000.count(2)/1000)
print("Empates: ", resultados1000.count(0)/1000)

print("\n")

### RESULTADOS PARA 10000 ###
resultados10000 = []
for i in range(10000):
  resultados10000.append(juego())

print("Resultados de 10000 juegos (Frecuencia Relativa): ")
print("Juan gana: ", resultados10000.count(1)/10000)
print("Maria gana: ", resultados10000.count(2)/10000)
print("Empates: ", resultados10000.count(0)/10000)

print("\n")

### RESULTADOS PARA 100000 ###
resultados100000 = []
for i in range(100000):
  resultados100000.append(juego())

print("Resultados de 100000 juegos (Frecuencia Relativa): ")
print("Juan gana: ", resultados100000.count(1)/100000)
print("Maria gana: ", resultados100000.count(2)/100000)
print("Empates: ", resultados100000.count(0)/100000)
