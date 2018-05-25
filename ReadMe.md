
Ayudantía OOP y Tableros
========================

El objetivo de esta ayundantía es aprender sobre el uso de la programación orientada a objetos y el uso de listas de listas de forma abstracta para hacer tableros.

Se realizará un problema propuesto en la ayudantía, el cual se irá desarrollando a lo largo de la hora. Este integrará los conocimientos propuestos.


OOP
===

OOP es la sigla de "Object Oriented Programming" (Programación orientada a objetos), el cual es un paradigma de programación. Los "Objetos" pueden manipular los datos que se les entregan de forma distintiva, entregando a cada tipo de objeto (Clase) funcionalidades especiales.

Por ejemplo, si queremos representar perros en python, los cuales poseen un nombre y una raza, serían representados de la siguiente manera:

    Class Perro:
    
        def __init__(self, nombre, raza):
            self.nombre = nombre
            self.raza = raza
            
El metodo " init " inicializa un objeto de la clase al ser creado, otorgandole un nombre y una raza a nuestro perro, aquí un ejemplo de un perro: 
         
    Class Perro:
        
        def __init__(self, nombre, raza):
            self.nombre = nombre
            self.raza = raza
            
    perro1 = Perro("Lou", "Beagle")     # Estamos creando un perro de raza Beagle llamado Lou
    print(perro1.nombre)
    print(perro1.raza)
    
    """
    El output esperado sería:
    Lou
    Beagle
    """
    
Ahora queremos que nuestro perro pueda hacer cosas, por ejemplo, ladrar. Vamos a implementar un metodo "ladrar" en nuestra clase perro para que este pueda muestrar en consola que está ladrando.

    Class Perro:
        
        def __init__(self, nombre, raza):
            self.nombre = nombre
            self.raza = raza
        
        def ladrar(self):
            print(self.nombre + " ladra con emoción!")
            
    perro1 = Perro("Lou", "Beagle")     # Estamos creando un perro de raza Beagle llamado Lou
    perro1.ladrar()
    
    """
    El output esperado:
    Lou ladra con emoción!
    """
    
Por ultimo, podemos hacer que dos perros jueguen entre si. Vamos a implementar el metodo "jugar" que hará que un perro juegue con otro.

     Class Perro:
        
        def __init__(self, nombre, raza):
            self.nombre = nombre
            self.raza = raza
        
        def ladrar(self):   # No la usamos en este ejemplo
            print(self.nombre + " ladra con emoción!")
            
        def jugar(self, otro_perro):
            print(self.nombre + " juega con " + otro_perro.nombre + "!")
            
    perro1 = Perro("Lou", "Beagle")     # Estamos creando un perro de raza Beagle llamado Lou
    perro2 = Perro("Rex", "Pastor Alemán")
    perro1.jugar(perro2)
    
    """
    El output esperado:
    Lou juega con Rex!
    """

Tableros
========

Se pueden utilizar listas de listas para representar de forma abstracta un tablero. 

Digamos que poseemos un tablero de ajedrez:

![alt text](https://github.com/matthers3/Ayudant-a-OOP-y-Tableros/blob/master/img/tablero.png)

La cual podemos dividir por filas:

![alt text](https://github.com/matthers3/Ayudant-a-OOP-y-Tableros/blob/master/img/tablero_separado.png)

Y, ¿qué pasaría si cada una de estas filas se encontraran dentro de una lista?:

![alt text](https://github.com/matthers3/Ayudant-a-OOP-y-Tableros/blob/master/img/tablero_separado_lista.png)

Ahora escribimos cómo se vería esta representación en python:


![alt text](https://github.com/matthers3/Ayudant-a-OOP-y-Tableros/blob/master/img/Captura.PNG)


Ya tenemos definido nuestro tablero.

En esta ayudantía programaremos un juego al estilo Calabozos&Dragones en un tablero para comprender cómo trabajar con estos. Este ejercicio se encuentra en la carpeta ejer.
