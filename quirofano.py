from arbol import BinaryTreeNode, Queue,printTree

class Paciente:
    def __init__(self, id:int, cod_paciente:str, nivel_emergencia:int, time_stamp: int):
        self.id = id
        self.cod_paciente = cod_paciente
        self.nivel_emergencia = nivel_emergencia
        self.time_stamp = time_stamp

    def __repr__(self):
        return f"(id={self.id}, cod={self.cod_paciente}, niv={self.nivel_emergencia}, t={self.time_stamp})"

class Quirofano:

    def __init__(self):
        self.quirofano = BinaryTreeNode(None)

    def registrar_paciente(self, id:int, cod_paciente:str, nivel_emergencia:int, time_stamp:int):
        nuevo_paciente = Paciente(id, cod_paciente, nivel_emergencia, time_stamp )
        nuevo_nodo = BinaryTreeNode(nuevo_paciente)

        if self.quirofano.data is None:
            self.quirofano.data = nuevo_paciente
            return
        
        cola_aux = Queue()
        cola_aux.enqueue(self.quirofano)
        while not cola_aux.is_empty():
            current = cola_aux.dequeue()

            if current.leftchild is None:
                current.leftchild = nuevo_nodo
                break
            
            elif current.rightchild is None:
                current.rightchild =nuevo_nodo
                break

            cola_aux.enqueue(current.rightchild)
            cola_aux.enqueue(current.rightchild)


        intercambio = True
        while intercambio:
            intercambio = False
            cola = Queue()
            cola.enqueue(self.quirofano)

            while not cola.is_empty():
                padre = cola.dequeue()

                if padre.leftchild is not None:
                    hijo = padre.leftchild
                    if hijo.data.nivel_emergencia < padre.data.nivel_emergencia:
                        padre.data, hijo.data = hijo.data, padre.data
                        intercambio = True
                        break
                    elif (hijo.data.nivel_emergencia == padre.data.nivel_emergencia and
                          hijo.data.time_stamp < padre.data.time_stamp):
                        padre.data, hijo.data = hijo.data, padre.data
                        intercambio= True
                        break
                    cola.enqueue(hijo)

                if padre.rightchild is not None:
                    hijo = padre.rightchild
                    if hijo.data.nivel_emergencia < padre.data.nivel_emergencia:
                        padre.data, hijo.data = hijo.data, padre.data
                        intercambio = True
                        break
                    elif (hijo.data.nivel_emergencia == padre.data.nivel_emergencia and
                          hijo.data.time_stamp < padre.data.time_stamp):
                        padre.data, hijo.data = hijo.data, padre.data
                        intercambio= True
                        break
                    cola.enqueue(hijo)





q = Quirofano()

q.registrar_paciente(1,"p01",3,10)
q.registrar_paciente(2,"p02",2,11)
q.registrar_paciente(3,"p03",1,20)
q.registrar_paciente(4,"p04",3,8)

print(q.quirofano)
printTree(q.quirofano)






