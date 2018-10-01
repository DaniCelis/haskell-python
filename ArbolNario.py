from __future__ import print_function
class ArbolNario:
    def __init__(self,valor,hijos=[]):
        self.valor = valor
        self.hijos = hijos

def buscarN(arbol,valor):
    if arbol.valor == valor:
        return True
    else:
        return buscar_hijos(arbol.hijos,valor)
    
def buscar_hijos(lista,valor):
    if lista == []:
        return False
    else:
        return (buscarN(lista[0],valor) or buscar_hijos(lista[1:],valor))

##Agrega un elemento a un nivel  
def agregarANivel(arbol,valor, nivel):
    if nivel==2:
        return arbol.hijos.append(ArbolNario(valor))
    else:
        return agregarANivel(arbol.hijos[0],valor, nivel-1)
    
## Agrega un elemento como hijo a un nodo
def agregarANodo(arbol,valor, nodo):
    if nodo==arbol.valor:
        return arbol.hijos.append(ArbolNario(valor))
    else:
        return agregarNodoAux(arbol.hijos,valor,nodo)
        
def agregarNodoAux(lista,valor,nodo):
    if lista==[]:
        return False
    else:
        return agregarANodo(lista[0],valor,nodo) or agregarNodoAux(lista[1:],valor,nodo)    
        
##Devuelve el numero de niveles del arbol  
def niveles(arbol):
    if arbol.hijos==[]:
        return 1
    else:
        return niveles(arbol.hijos[0]) + 1

def imprimirArbol(arbol):
    if arbol.hijos==[]:
        print(arbol.valor, end="  ")
    else:
        impHijos(arbol.hijos)
        print(arbol.valor, end="  ")
      
def impHijos(lista):
    if lista!=[]:
        return imprimirArbol(lista[0]) or impHijos(lista[1:])
        
        
        
arbol = ArbolNario(2, [ ArbolNario(4,[ ArbolNario(45,[]), ArbolNario(60,[]),
        ArbolNario(200,[])]), ArbolNario(20,[])])

imprimirArbol(arbol)
print("")
print(niveles(arbol))
agregarANivel(arbol,100,3)
print(buscarN(arbol,100))
print(buscarN(arbol,75))
agregarANodo(arbol,150, 200)
agregarANodo(arbol,80, 20)
agregarANodo(arbol,8,45)
agregarANodo(arbol,15,60)
agregarANodo(arbol,25,60)
agregarANodo(arbol,10,60)
print(buscarN(arbol,150))
imprimirArbol(arbol)
print("")
print (niveles(arbol))

