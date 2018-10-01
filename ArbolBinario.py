from __future__ import print_function

class Binario():
    def __init__(self,valor,izq=None,der=None):
        self.valor=valor
        self.izq=izq
        self.der=der
        
def buscar(arbol,valor):
    if arbol==None:
        return False
    elif arbol.valor==valor:
        return True
    elif arbol.valor>valor:
        return buscar(arbol.izq,valor)
    else:
        return buscar(arbol.der,valor)
    
def agregar(arbol,valor):
    if arbol.valor!=None and arbol.izq==None and arbol.der==None:
        if valor>arbol.valor:
            arbol.der=Binario(valor)
            return arbol.der
        else:
            arbol.izq=Binario(valor)
            return arbol.izq
    else:
        if valor>arbol.valor:
            return Binario(arbol.valor,arbol.izq,agregar(arbol.der,valor))
        else:
            return Binario(arbol.valor,agregar(arbol.izq,valor),arbol.der)
       
def in_Orden(arbol):
    if arbol!=None:
        print (arbol.valor,end="  ")
        in_Orden(arbol.izq)
        in_Orden(arbol.der)
    
        
def pre_Orden(arbol):
    if arbol!=None:
        pre_Orden(arbol.izq)
        print (arbol.valor,end="  ")
        pre_Orden(arbol.der)
     
def pos_Orden(arbol):
    if arbol!=None:
        pos_Orden(arbol.izq)
        pos_Orden(arbol.der)
        print (arbol.valor,end="  ")

def imprimirOrdenes(arbol):
    print("Lista In Orden: ")
    in_Orden(arbol)
    print("\nLista Pre Orden: ")
    pre_Orden(arbol)
    print("\nLista Pos Orden: ")
    pos_Orden(arbol)
    print("")
        
           
a = Binario(15, Binario(10, Binario(4)), Binario(25))

imprimirOrdenes(a)
agregar(a,2)
print(buscar(a,2))
agregar(a,30)
print(buscar(a,30))
imprimirOrdenes(a)

