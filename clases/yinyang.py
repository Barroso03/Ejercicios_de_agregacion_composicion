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
 
