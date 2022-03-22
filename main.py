from clases.destruccion import destruccion
from clases.yinyang import Yin
from clases.yinyang import Yang
from clases.casa import Pared
from clases.casa import Ventana
from clases.casa import Casa
from clases.casa import ParedCortina 


if __name__ == "__main__":
  print(destruccion.ciudad("New_York"))
if __name__ == "__main__":
  yin = Yin() 
  yang = Yang() 
  yin.yang = yang 
  print(yang) 

  print(yang is yin.yang) 

  del(yang) 
  print("?")
if __name__ == "__main__":
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
pared_cortina = ParedCortina("SUR", 10)
casa.paredes[2] = pared_cortina
print(casa.superficie_cristal())
  



  
  
  
  