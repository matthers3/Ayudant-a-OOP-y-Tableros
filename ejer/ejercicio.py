import random


class Dado:

    def __init__(self, caras):
        self.caras = caras

    def lanzar(self):
        return random.randint(1, self.caras)


class Aventurero:

    def __init__(self, nombre, año, gremio):
        self.nombre = nombre
        self.año = año
        self.gremio = gremio
        self.dados = []
        self.x = 0
        self.y = 0

    def lanzar_dados(self):
        total_obtenido = 0
        for dado in self.dados:
            total_obtenido += dado.lanzar()

    def __str__(self):
        return self.nombre[0].capitalize()


class Enemigo:

    def __init__(self):
        self.nombre = 'Enemigo'
        self.x = 0
        self.y = 0

class Tablero:

    def __init__(self):
        self.tablero = [[" ", " ", " ", " ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " ", "X", " ", " "],
                        [" ", " ", " ", " ", "X", " ", " ", " "],
                        [" ", " ", "X", " ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ", " "],
                        [" ", " ", " ", " ", " ", "X", " ", " "],
                        [" ", " ", " ", " ", " ", " ", " ", " "]
                        ]

    def mover_pieza(self, x1, y1, x2, y2):
        if self.tablero[y2][x2] == " ":
            a_mover = self.tablero[y1][x1]
            self.tablero[y2][x2] = a_mover
            self.tablero[y1][x1] = " "
        return


    def buscar_posicion(self, buscado):
        x = 0
        y = 0
        for fila in self.tablero:
            for espacio in fila:
                if buscado == espacio:
                    return (x,y)
                x += 1
            y += 1
            x = 0

    def buscar_posicion_index(self, buscado):

        for fila in self.tablero:
            if buscado in fila:
                return (fila.index(buscado), self.tablero.index(fila))

    def contar_piezas(self):
        contador = 0
        for fila in self.tablero:
            for espacio in fila:
                if espacio != " ":
                    contador += 1
        return contador

    def mostrar_paso_a_paso(self):
        x = 0
        y = 0
        for fila in self.tablero:
            for espacio in fila:
                self.tablero[y][x] = "*"
                print(t1.mostrar_tablero())
                x += 1
            y += 1
            x = 0

    def mostrar_caminos(self, aventurero):

        inicial = self.buscar_posicion(aventurero)

        y = inicial[1]
        x = inicial[0]
        while True:
            try:
                y -= 1
                if self.tablero[y][x] != " " or y < 0:
                    break
                self.tablero[y][x] = "*"
            except:
                break

        y = inicial[1]
        x = inicial[0]
        while True:
            try:
                y+= 1
                if self.tablero[y][x] != " ":
                    break
                self.tablero[y][x] = "*"
            except:
                break

        y = inicial[1]
        x = inicial[0]
        while True:
            try:
                x -= 1
                if self.tablero[y][x] != " " or x < 0:
                    break
                self.tablero[y][x] = "*"
            except:
                break

        y = inicial[1]
        x = inicial[0]
        while True:
            try:
                x += 1
                if self.tablero[y][x] != " ":
                    break
                self.tablero[y][x] = "*"
            except:
                break


        return

    def mostrar_diagonales(self, aventurero):

        inicial = self.buscar_posicion(aventurero)

        x = inicial[0]
        y = inicial[1]
        for fila in self.tablero[:y]:
            try:
                x += 1
                y -= 1
                if self.tablero[y][x] != " " or y < 0:
                    break
                self.tablero[y][x] = '*'
            except:
                break

        x = inicial[0]
        y = inicial[1]
        for fila in self.tablero[:y]:
            try:
                x -= 1
                y -= 1
                if self.tablero[y][x] != " " or x < 0 or y < 0:
                    break
                self.tablero[y][x] = '*'
            except:
                break

        x = inicial[0]
        y = inicial[1]
        for fila in self.tablero[y:]:
            try:
                x += 1
                y += 1
                if self.tablero[y][x] != " ":
                    break
                self.tablero[y][x] = '*'
            except:
                break

        x = inicial[0]
        y = inicial[1]
        for fila in self.tablero[y:]:
            try:
                x -= 1
                y += 1
                if self.tablero[y][x] != " " or x < 0:
                    break
                self.tablero[y][x] = '*'
            except:
                break
        return

    def limpiar_tablero(self):
        x = 0
        y = 0
        for fila in self.tablero:
            for espacio in fila:
                if espacio == "*":
                    self.tablero[y][x] = " "
                x += 1
            y += 1
            x = 0
        return

    def mostrar_movimientos(self, aventurero):
        self.mostrar_caminos(aventurero)
        self.mostrar_diagonales(aventurero)
        self.mostrar_tablero()
        self.limpiar_tablero()

    def mostrar_tablero(self):

        print("+---+---+---+---+---+---+---+---+")
        for line in self.tablero:
            print("| {} | {} | {} | {} | {} | {} | {} | {} |".format(line[0], line[1],
                                                                     line[2], line[3],
                                                                     line[4], line[5],
                                                                     line[6], line[7]))
            # print("| {} | {} | {} | {} | {} | {} | {} | {} |".format(*line))
            print("+---+---+---+---+---+---+---+---+")


t1 = Tablero()
M = Aventurero('Matias', '3', 'DCC')
L = Aventurero('Lucas', '3', 'Química')
t1.tablero[3][5] = M
t1.tablero[1][2] = L
t1.mostrar_tablero()
print(t1.buscar_posicion_index(M))
print(t1.contar_piezas())

t1.mostrar_movimientos(L)