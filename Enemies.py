import random


# Constantes del juego
TOTAL_TILES = 100
NUM_COMPILADORES = 7
NUM_BUGS = 9
NUM_ENEMIGOS = 25

class ObjetoJuego:
    def __init__(self, tipo, posicion):
        """
        tipo: 'compilador', 'bug' o 'enemigo'
        posicion: índice de la casilla (0-99)
        """
        self.tipo = tipo
        self.posicion = posicion
        self.activo = True  # True si el objeto aún no ha sido usado (para los que deben desaparecer)

def generar_objetos():
    """
    Genera una lista de objetos de juego con posiciones aleatorias.
    Se asegura de que no haya posiciones duplicadas.
    """
    posiciones_disponibles = list(range(1, TOTAL_TILES - 1))  # Evitamos casilla 0 y la final
    random.shuffle(posiciones_disponibles)

    objetos = []

    # Generar compiladores amigos
    for _ in range(NUM_COMPILADORES):
        pos = posiciones_disponibles.pop()
        objetos.append(ObjetoJuego("compilador", pos))

    # Generar bugs traicioneros
    for _ in range(NUM_BUGS):
        pos = posiciones_disponibles.pop()
        objetos.append(ObjetoJuego("bug", pos))

    # Generar enemigos (quiz)
    for _ in range(NUM_ENEMIGOS):
        pos = posiciones_disponibles.pop()
        objetos.append(ObjetoJuego("enemigo", pos))

    return objetos
