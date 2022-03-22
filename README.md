# Ejercicios_de_agregacion_composicion

## Repositorio:

El link del repositorio es https://github.com/Barroso03/Entrega_por_parejas_POO



## Tarea:

La tarea que hemos realizado estaba basada en resolver unos ejercicios aplicando determinadas pautas que nos indican los ejercicios y además en la adjunción de UML´s.

## Integrantes:
 
1. [Barroso](https://github.com/Barroso03)



## Ejercicio a :

```
class destruccion():
  def __init__(self, ciudades):
    self.ciudades = ciudades
  def ciudad(New_York):
   while True:
     print("Que ciudad quieres destruir")
     eleccion = str(input("Elige una ciudad entre New_York o Los_Angeles:"))
     break
   if eleccion == New_York:
     print("Se ha destruido New_York")
     print("Se ha destruido los edificios A y B")
     print("Mueren Sr.Salim y Sr.Martin ")
   else:
     print("Se ha destruido Los_Angeles")
     print("Se ha destruido el edificio C")
     print("Muere Sra.Xing ")
print("EJERCICIO 1:")
print(destruccion.ciudad("New_York"))

````
UML:





## Ejercicio b:

```
class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
 
print("EJERCICIO 2:")
yin = Yin() 
yang = Yang() 
yin.yang = yang 
print(yang) 

print(yang is yin.yang) 

del(yang) 
print("?")
#Solucion: lo que hace el del(yang) es imprimirte yang antes que el print(?) y yang es la clase Yang()y esta clase lo que hace es imprimier Yang destruido 


```

UML:





## Ejercicio c:

```

class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion
        self.ventanas = []

class Ventana:
    def __init__(self, pared, superficie, proteccion):
        self.pared = pared
        self.superficie = superficie
        self.pared.ventanas.append(self)
        if proteccion is None:
            raise Exception("Protección obligatoria")
        self.proteccion = proteccion

class Casa:
    def __init__(self, paredes):
        self.paredes = paredes

    def superficie_cristal(self):
        superficie = 0
        for pared in self.paredes:
            for ventana in pared.ventanas:
                superficie += ventana.superficie
        return superficie

print("EJERCICIO 3:")
pared_norte = Pared("NORTE")
pared_oeste = Pared("OESTEE")
pared_sur = Pared("SUR")
pared_este = Pared("ESTE")
ventana_norte = Ventana(pared_norte, 0.5, "persiana")
ventana_oeste = Ventana(pared_oeste, 1, "persiana")
ventana_sur = Ventana(pared_sur, 2, "store vénitien")
ventana_este = Ventana(pared_este, 1, "persiana")
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
print(casa.superficie_cristal())


class ParedCortina(Pared, Ventana):
    def __init__(self, orientacion, superficie):
        Pared.__init__(self, orientacion)
        Ventana.__init__(self, self, superficie, "Ninguna")

pared_cortina = ParedCortina("SUR", 10)
casa.paredes[2] = pared_cortina
print(casa.superficie_cristal())  

```


UML:
