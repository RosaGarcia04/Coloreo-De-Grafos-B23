def coloreo_grafo_voraz():
    print("Coloreo de Grafos: Metodo Voraz (Greedy)")
    import random
    import time
    inicio = time.time()
    cantidad = int(input("Ingrese la cantidad de nodos a generar: "))
    elementos = []

    for i in range(cantidad):
        elemento = str(i + 1)
        elementos.append(elemento)
         
    colores = ["Verde","Rojo","Azul"]
    maximo_nodos=(len(elementos))
    maximo_volumen=5
    minimo_volumen=2
    nodos=dict(nombre=list(("X"*maximo_nodos)),volumen=list(("0"*maximo_nodos)),color=list(("Amarillo"*maximo_nodos)))
    
    for a in range(0,maximo_nodos):
            nodos["nombre"][a]=elementos[a]
            nodos["volumen"][a]=random.randrange(minimo_volumen,(maximo_volumen+1))
            nodos["color"][a]=colores[random.randrange(0,len(colores))]
            while nodos["color"][a]==nodos["color"][(a-1)] or nodos["color"][a]==nodos["color"][(a+1)]:
                nodos["color"][a]=colores[random.randrange(0,len(colores))]
            print("Nombre del nodo: "+nodos["nombre"][a]+" Color: "+nodos["color"][a]+" Volumen: "+str(nodos["volumen"][a]))
    fin = time.time()
    print(fin-inicio)
    return
coloreo_grafo_voraz()



