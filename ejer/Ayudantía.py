import random

class Dado:

    def __init__(self, caras):
        """
        El init entrega el valor de las caras del dado, y se guarda en self.dado
        """
        self.caras = caras

    def lanzar(self):
        """
        Se arroja un numero entre 1 y la cantidad de caras que posee el dado.
        """
        return random.randint(1, self.caras)

    def __repr__(self):
        # Con esto printeamos el dado.
        return 'Dado de ' + str(self.caras)

class Aventurero:

    def __init__(self, nombre, año, gremio):
        """
        Un aventurero posee nombre, año, gremio, y dados. Estos últimos
        son agregados después de crear la clase, utilizando los metodos
        agregar_dado y agregar_dado_numero.

        """
        self.nombre = nombre
        self.año = año
        self.gremio = gremio
        self.dados = []

    def agregar_dado(self, dado):
        """
        Agrega el dado que se le entrega.
        """
        self.dados.append(dado)

    def agregar_dado_numero(self, numero):
        """
        Crea un dado con cantidad de caras igual al numero indicado
        y lo agrega a los dados del aventurero.
        """
        dado = Dado(numero)
        self.dados.append(dado)

    def lanzar_todos_los_dados(self):
        """
        Se recorren todos los dados del jugador con un ciclo for,
        sumando los valores que se obtienen y formando un string
        con todos los numeros que se obtuvieron.
        """
        cantidad_total = 0
        string = ""
        for dado in self.dados:
            lanzamiento = dado.lanzar()
            string = string + " " + str(lanzamiento)
            cantidad_total += lanzamiento
        print(string)
        return cantidad_total

    def __repr__(self):
        """
        Representamos al aventurero como la primera nota de su nombre
        en mayúscula.
        """
        return self.nombre[0].upper()


class Tablero:

    def __init__(self):
        """
        El tablero corresponde a una lista de listas, siendo los " " espacios
        libres y las X obstáculos.
        """
        self.tablero = [["X", " ", " ", " ", " ", " ", " ", "X"],
                        ["X", " ", "X", "X", "X", "X"," ", "X"],
                        ["X", " ", "X", "X", "X", "X", " ", "X"],
                        ["X", " ", "X", " ", " ", "X", " ", "X"],
                        ["X", " ", "X", " ", " ", "X", " ", "X"],
                        ["X", " ", "X", " ", " ", "X", " ", "X"],
                        ["X", " ", "X", " ", " ", "X", " ", "X"],
                        ["X", "X", "X", " ", " ", " ", " ", "X"]
                        ]

    def mostrar_tablero(self):
        """
        Esta función nos permite mostrar el tablero en consola para
        poder comprender mejor los metodos que se mostrarán a continuación.
        """
        print("    0   1   2   3   4   5   6   7")
        print("  +---+---+---+---+---+---+---+---+")
        columna = 0
        for linea in self.tablero:
            print("{} | {} | {} | {} | {} | {} | {} | {} | {} |".format(columna,
                                                                        linea[0],
                                                                           linea[1],
                                                                           linea[2],
                                                                           linea[3],
                                                                           linea[4],
                                                                           linea[5],
                                                                           linea[6],
                                                                           linea[7]))
            print("  +---+---+---+---+---+---+---+---+")
            columna += 1

        return

    def recorrer_paso_a_paso(self):
        """
        Esta función se usó como ejemplo para mostrar el
        orden en el que se recorría el tablero.
        """
        x = 0
        y = 0
        for fila in self.tablero:
            for espacio in fila:
                self.tablero[y][x] = '*'
                x += 1
                self.mostrar_tablero()  # Marcar esta linea en el debuggeador para ver.
            y += 1
            x = 0

    def buscar_en_tablero(self, buscado):
        """
        Dado algo para buscar en el tablero (podría ser una X, un aventurero,
        u otra cosa), este se recorre con dos ciclos for para buscar su
        posición espacio por espacio. Finalmente entrega la posición como
        un par ordenado (x,y).
        """
        x = 0
        y = 0
        for fila in self.tablero:
            for espacio in fila:
                if espacio == buscado:
                    return (x,y)
                x += 1
            y += 1
            x = 0
        return -1

    def marcar_linas(self, aventurero):
        """
        Esta función marca con un *  las direcciones a las que se puede mover
        un aventurero de forma vertical y horizontal.
        """
        posicion_init = self.buscar_en_tablero(aventurero)
        # Usamos la función definida anteriormente para saber de donde partir.
        x = posicion_init[0]
        y = posicion_init[1]
        while True:
            try:    # La sentencia try ejecuta el codigo y el programa no se cae si tira error.
                x += 1      # Como vamos a la derecha, sumamos 1 a x.
                if self.tablero[y][x] != " ":
                    break
                self.tablero[y][x] = '*'
            except:     # Si el código en try tira error esto se ejecutará en vez de caerse el programa.
                break   # Fin al cabo queremos marcar los espacios hasta que nos salgamos de la lista y tire
                        # un error para activar el break presente en except y seguir con la siguiente dirección.

        y = posicion_init[1]    # Es importante redefinir las variables al punto de partida.
        x = posicion_init[0]
        while True:
            try:
                x -= 1      # Lo mismo que el anterior, pero ahora restamos 1 para ir a la izquieda.
                if x < 0:   # Si x se vuelve negativo le damos la vuelta a la lista, y no queremos eso.
                    break
                if self.tablero[y][x] != " ":   # Si nos encontramos con un obstáculo queremos detenernos.
                    break                       # Un obstáculo será cualquier cosa que no sea un espacio " ".
                self.tablero[y][x] = "*"
            except:
                break

        y = posicion_init[1]
        x = posicion_init[0]
        while True:
            try:
                y -= 1  # Lo mismo, pero ahora variamos y para marcar las filas superiores.
                if y < 0:   # y no puede ser negativo al igual que en el caso del x.
                    break
                if self.tablero[y][x] != " ":
                    break
                self.tablero[y][x] = "*"
            except:
                break

        y = posicion_init[1]
        x = posicion_init[0]
        while True:
            try:
                y += 1  # Lo mismo, pero para las filas inferiores.
                if self.tablero[y][x] != " ":
                    break
                self.tablero[y][x] = "*"
            except:
                break

        self.mostrar_tablero()  # Mostramos cómo quedó.

    def marcar_diagonales(self, aventurero):
        """
        Esta función sigue la misma lógica que la de las rectas,
        solo que variamos tanto el x como el y.
        """
        posicion_init = self.buscar_en_tablero(aventurero)

        x = posicion_init[0]
        y = posicion_init[1]
        while True:
            try:
                x += 1      # Diagonal Derecha - Arriba
                y -= 1
                if self.tablero[y][x] != " ":
                    break
                if y < 0:
                    break
                self.tablero[y][x] = '*'
            except:
                break

        x = posicion_init[0]
        y = posicion_init[1]
        while True:
            try:
                x -= 1      # Diagonal Izquierda - Arriba
                y -= 1
                if self.tablero[y][x] != " ":
                    break
                if y < 0 or x < 0:
                    break
                self.tablero[y][x] = '*'
            except:
                break

        x = posicion_init[0]
        y = posicion_init[1]
        while True:
            try:
                x -= 1      # Diagonal Izquierda - Abajo
                y += 1
                if self.tablero[y][x] != " ":
                    break
                if x < 0:
                    break
                self.tablero[y][x] = '*'
            except:
                break

        x = posicion_init[0]
        y = posicion_init[1]
        while True:
            try:
                x += 1      # Diagonal Derecha - Abajo
                y += 1
                if self.tablero[y][x] != " ":
                    break
                self.tablero[y][x] = '*'
            except:
                break

        self.mostrar_tablero()  # Mostramos el resultado

    def mover_pieza(self, pieza, x, y):
        """
        Marcamos los lugares válidos para mover una pieza con los *,
        por lo tanto el punto (x,y) debe corresponder a un * para que
        un movimiento sea válido. Después de realizar un movimiento se
        ejecuta la función limpiar para eliminar los * que sobran.
        """
        inicial = self.buscar_en_tablero(pieza)
        self.marcar_linas(pieza)
        self.marcar_diagonales(pieza)
        if self.tablero[y][x] == "*":   # Solo válido si es un *.
            self.tablero[y][x] = pieza
            self.tablero[inicial[1]][inicial[0]] = " "
        self.limpiar()
        self.mostrar_tablero()

    def limpiar(self):
        """
        Recorremos con un doble for y buscamos * para que los
        reemplacemos por espacios " ".
        """
        x = 0
        y = 0
        for fila in self.tablero:
            for espacio in fila:
                if espacio == "*":
                    self.tablero[y][x] = " "
                x += 1
            y += 1
            x = 0


# A partir de aquí se ejecuta el código #

# Creacion de dados #
d6 = Dado(6)
d20 = Dado(20)
print(d6.lanzar())
print(d20.lanzar())

# Creacion de aventurero #

M = Aventurero('Matias', 3, 'DCC')
M.agregar_dado(d20)
M.agregar_dado_numero(30)
print(M.nombre, M.año, M.gremio, M.dados)

# Manejo del tablero #

t1 = Tablero()
t1.tablero[5][3] = M
t1.mover_pieza(M, 4, 5)

# Sacar los # para probar el codigo de movimiento.
#while True:
#    try:
#        x = int(input("Seleccionar X: "))
#        y = int(input("Seleccionar Y: "))
#        t1.mover_pieza(M, x, y)
#    except:
#        print("_WRONG_INPUT_")
# Ejemplo lanzamiento de dados #

M.agregar_dado_numero(8)
M.agregar_dado_numero(4)
M.agregar_dado_numero(2)
M.agregar_dado_numero(10)
M.agregar_dado_numero(100)
print(M.lanzar_todos_los_dados())