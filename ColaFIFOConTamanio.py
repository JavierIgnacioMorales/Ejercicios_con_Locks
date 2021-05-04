import threading


class ColaFIFOConTamanio:

    def __init__(self, size):
        self.elementos = []
        self.size = size
        self.condition = threading.Condition()

    def insertar(self, dato):
        self.condition.acquire()
        while self.size == self.cantidad_elementos():
            self.condition.wait()
        self.elementos.append(dato)
        self.condition.notify()
        self.condition.release()

    def extraer(self):
        self.condition.acquire()
        while self.cantidad_elementos() == 0:
            self.condition.wait()
        elemento = self.elementos.pop(0)
        self.condition.notify()
        self.condition.release()
        return elemento


    def ultimo(self):
        return self.elementos[-1]

    def primero(self):
        return self.elementos[0]

    def cola_vacia(self):
        return len(self.elementos) == 0

    def cantidad_elementos(self):
        return len(self.elementos)


def main():
    cola = ColaFIFOConTamanio(2)

    # check if esta_vacia()

    print(cola.cola_vacia())

    for i in range (1,6):
        cola.insertar(i)

    print(cola.cola_vacia())
    print(cola.cantidad_elementos())

    print(cola.primero(),cola.ultimo())
    cola.extraer()
    print(cola.primero(),cola.ultimo())


    cola.extraer()
    cola.extraer()
    cola.extraer()
    cola.extraer()

    print(cola.cola_vacia())
    print(cola.cantidad_elementos())

if __name__ == '__main__':
    main()
