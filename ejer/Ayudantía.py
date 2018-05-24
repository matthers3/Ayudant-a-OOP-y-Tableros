import random

class Dado:

    def __init__(self, caras):
        self.caras = caras

    def lanzar(self):
        return random.randint(1, self.caras)

    def __repr__(self):
        # Con esto printeamos el dado.
        return 'Dado de ' + str(self.caras) + " caras."

class Aventurero:

    def __init__(self, nombre, año, gremio):
        self.nombre = nombre
        self.año = año
        self.gremio = gremio
        self.dados = []

    def agregar_dado(self, dado):
        self.dados.append(dado)

    def agregar_dado_numero(self, numero):
        dado = Dado(numero)
        self.dados.append(dado)

    def lanzar_todos_los_dados(self):
        cantidad_total = 0
        string = ""
        for dado in self.dados:
            lanzamiento = dado.lanzar()
            string = string + " " + str(lanzamiento)
            cantidad_total += lanzamiento
        print(string)
        return cantidad_total

    def __repr__(self):
        return self.nombre[0].upper()


class Tablero:

    def __init__(self):

        self.tablero = [[" ", " ", " ", " ", " ", " ", " ", " "],
                        ["X", " ", "X", "X", "X", "X"," ", "X"],
                        ["X", " ", "X", "X", " ", "X", " ", " "],
                        ["X", " ", "X", " ", " ", "X", " ", " "],
                        ["X", " ", "X", " ", " ", "X", " ", " "],
                        ["X", " ", "X", " ", " ", "X", " ", " "],
                        ["X", " ", "X", " ", " ", "X", " ", " "],
                        ["X", " ", "X", " ", " ", " ", " ", " "]
                        ]

    def mostrar_tablero(self):

        print("  0    1    2    3    4    5    6   7")
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
        x = 0
        y = 0
        for fila in self.tablero:
            for espacio in fila:
                self.tablero[y][x] = '*'
                x += 1
                self.mostrar_tablero()
            y += 1
            x = 0

    def buscar_en_tablero(self, buscado):
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
        posicion_init = self.buscar_en_tablero(aventurero)

        x = posicion_init[0]
        y = posicion_init[1]
        while True:
            try:
                x += 1
                if self.tablero[y][x] != " ":
                    break
                self.tablero[y][x] = '*'
            except:
                break

        y = posicion_init[1]
        x = posicion_init[0]
        while True:
            try:
                x -= 1
                if x < 0:
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
                y -= 1
                if y < 0:
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
                y += 1
                if self.tablero[y][x] != " ":
                    break
                self.tablero[y][x] = "*"
            except:
                break

        self.mostrar_tablero()

    def marcar_diagonales(self, aventurero):
        posicion_init = self.buscar_en_tablero(aventurero)

        x = posicion_init[0]
        y = posicion_init[1]
        while True:
            try:
                x += 1
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
                x -= 1
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
                x -= 1
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
                x += 1
                y += 1
                if self.tablero[y][x] != " ":
                    break
                self.tablero[y][x] = '*'
            except:
                break

        self.mostrar_tablero()

    def mover_pieza(self, pieza, x, y):
        inicial = self.buscar_en_tablero(pieza)
        self.marcar_linas(pieza)
        self.marcar_diagonales(pieza)
        if self.tablero[y][x] == "*":
            self.tablero[y][x] = pieza
            self.tablero[inicial[1]][inicial[0]] = " "
        self.limpiar()
        self.mostrar_tablero()

    def limpiar(self):
        x = 0
        y = 0
        for fila in self.tablero:
            for espacio in fila:
                if espacio == "*":
                    self.tablero[y][x] = " "
                x += 1
            y += 1
            x = 0

d6 = Dado(6)
d20 = Dado(20)

print(d6.lanzar())
print(d20.lanzar())
M = Aventurero('Matias', 3, 'DCC')
L = Aventurero('Lucas', 3, 'Ingeniería Química')


M.agregar_dado(d20)
M.agregar_dado_numero(30)
print(M.nombre, M.año, M.gremio, M.dados)

t1 = Tablero()
t1.tablero[5][3] = M
t1.tablero[2][3] = L
t1.mover_pieza(M, 4, 5)

M.agregar_dado_numero(8)
M.agregar_dado_numero(4)
M.agregar_dado_numero(2)
M.agregar_dado_numero(10)
M.agregar_dado_numero(100)
print(M.lanzar_todos_los_dados())