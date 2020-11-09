#Este algoritmo puede adimitir a los usuarios que quieras
#que se almacenen en un archivo json y despues se mostrarn en diferentes maneras
import json
import pprint
a=int(input('Cuantas personas deseas ingresar? '))

direct={}
direct['alumnos']=[]

o=0
while o<a:
    
    n=input('Nombre completo: ')
    e=int(input('Edad: '))
    c=input('Ciudad: ')
    t=input('Telefono: ')

    directorio={'nombre':None,'edad':None,'ciudad':None,'telefono':None}

    directorio['nombre']=n
    directorio['edad']=e
    directorio['ciudad']=c
    directorio['telefono']=t

    direct['alumnos'].append(directorio)

    o=o+1

with open('Directorio.json','w') as acceso:
    json.dump(direct,acceso,indent=a)

with open('Directorio.json','r') as acceso1:
    dato=json.load(acceso1)
    
print('#############################################################')    
print('Tipos de salidas')
print('#############################################################')
print(dato)
print('#############################################################')

ordenado=json.dumps(dato,indent=2,separators=(',',':'),sort_keys=True)
print(ordenado)
print('#############################################################')

acomodar=pprint.PrettyPrinter(indent=2,width=40,compact=False)
acomodar.pprint(dato)
print('#############################################################')

for y in dato['alumnos']:
    print('Nombre:',y['nombre'])
    print('Edad:',y['edad'])
    print('Ciudad:',y['ciudad'])
    print('Telefono:',y['telefono'])
    print('`````````````````````````````````````````````````````````````` ')


        






    



