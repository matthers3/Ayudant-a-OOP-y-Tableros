
Ayudant�a OOP y Tableros
========================

El objetivo de esta ayundant�a es aprender sobre el uso de la programaci�n orientada a objetos y el uso de listas de listas de forma abstracta para hacer tableros.

Se realizar� un problema propuesto en la ayudant�a, el cual se ir� desarrollando a lo largo de la hora. Este integrar� los conocimientos propuestos.


OOP
===

OOP es la sigla de "Object Oriented Programming" (Programaci�n orientada a objetos), el cual es un paradigma de programaci�n. Los "Objetos" pueden manipular los datos que se les entregan de forma distintiva, entregando a cada tipo de objeto (Clase) funcionalidades especiales.

Por ejemplo, si queremos representar perros en python, los cuales poseen un nombre y una raza, ser�an representados de la siguiente manera:

    Class Perro:
    
        def __init__(self, nombre, raza):
            self.nombre = nombre
            self.raza = raza
            
El metodo " init " inicializa un objeto de la clase al ser creado, otorgandole un nombre y una raza a nuestro perro, aqu� un ejemplo de un perro: 
         
    Class Perro:
        
        def __init__(self, nombre, raza):
            self.nombre = nombre
            self.raza = raza
            
    perro1 = Perro("Lou", "Beagle")     # Estamos creando un perro de raza Beagle llamado Lou
    print(perro1.nombre)
    print(perro1.raza)
    
    """
    El output esperado ser�a:
    Lou
    Beagle
    """
    
Ahora queremos que nuestro perro pueda hacer cosas, por ejemplo, ladrar. Vamos a implementar un metodo "ladrar" en nuestra clase perro para que este pueda muestrar en consola que est� ladrando.

    Class Perro:
        
        def __init__(self, nombre, raza):
            self.nombre = nombre
            self.raza = raza
        
        def ladrar(self):
            print(self.nombre + " ladra con emoci�n!")
            
    perro1 = Perro("Lou", "Beagle")     # Estamos creando un perro de raza Beagle llamado Lou
    perro1.ladrar()
    
    """
    El output esperado:
    Lou ladra con emoci�n!
    """
    
Por ultimo, podemos hacer que dos perros jueguen entre si. Vamos a implementar el metodo "jugar" que har� que un perro juegue con otro.

     Class Perro:
        
        def __init__(self, nombre, raza):
            self.nombre = nombre
            self.raza = raza
        
        def ladrar(self):
            print(self.nombre + " ladra con emoci�n!")
            
        def jugar(self, otro_perro):
            print(self.nombre + " juega con " + otro_perro.nombre + "!")
            
    perro1 = Perro("Lou", "Beagle")     # Estamos creando un perro de raza Beagle llamado Lou
    perro2 = Perro("", "")

Tableros
========


    """
    
Ahora queremos que nuestro perro pueda hacer cosas, por ejemplo, ladrar. Vamos a implementar un metodo "ladrar" en nuestra clase perro para que este pueda muestrar en consola que est� ladrando.

    Class Perro:
        
        def __init__(self, nombre, raza):
            self.nombre = nombre
            self.raza = raza
        
        def ladrar(self):
            print(self.nombre + " ladra con emoci�n!")
            
    perro1 = Perro("Lou", "Beagle")     # Estamos creando un perro de raza Beagle llamado Lou
    perro1.ladrar()
    
    """
    El output esperado:
    Lou ladra con emoci�n!
    """
    
Por ultimo, podemos hacer que dos perros jueguen entre si. Vamos a implementar el metodo "jugar" que har� que un perro juegue con otro.

     Class Perro:
        
        def __init__(self, nombre, raza):
            self.nombre = nombre
            self.raza = raza
        
        def ladrar(self):
            print(self.nombre + " ladra con emoci�n!")
            
        def jugar(self, otro_perro):
            print(self.nombre + " juega con " + otro_perro.nombre + "!")
            
    perro1 = Perro("Lou", "Beagle")     # Estamos creando un perro de raza Beagle llamado Lou
    perro2 = Perro("", "")

Tableros
========


    Lou
    Beagle
    """
    
Ahora queremos que nuestro perro pueda hacer cosas, por ejemplo, ladrar. Vamos a implementar un metodo "ladrar" en nuestra clase perro para que este pueda muestrar en consola que est� ladrando.

    Class Perro:
        
        def __init__(self, nombre, raza):
            self.nombre = nombre
            self.raza = raza
        
        def ladrar(self):
            print(self.nombre + " ladra con emoci�n!")
            
    perro1 = Perro("Lou", "Beagle")     # Estamos creando un perro de raza Beagle llamado Lou
    perro1.ladrar()
    
    """
    El output esperado:
    Lou ladra con emoci�n!
    """
    

