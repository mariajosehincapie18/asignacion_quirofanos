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

            cola_aux.enqueue(current.leftchild)
            cola_aux.enqueue(current.rightchild)
        
        self.reorganizar_heap(self.quirofano)


    def reorganizar_heap(self, root):
        if root is None:
            return
        
        menor = root
     

        if root.leftchild:
            if (root.leftchild.data.nivel_emergencia < menor.data.nivel_emergencia) or (root.leftchild.data.nivel_emergencia == menor.data.nivel_emergencia 
                and root.leftchild.data.time_stamp < menor.data.time_stamp): 
                menor = root.leftchild                       
                    
        if root.rightchild:
            if (root.rightchild.data.nivel_emergencia < menor.data.nivel_emergencia) or (root.rightchild.data.nivel_emergencia == menor.data.nivel_emergencia 
                and root.rightchild.data.time_stamp < menor.data.time_stamp):
                menor = root.rightchild

        
        if menor != root:
            root.data, menor.data = menor.data, root.data
            self.reorganizar_heap(menor)

        if root.leftchild and root.rightchild:
            hijo_izq = root.leftchild
            hijo_der= root.rightchild

            if (hijo_der.data.nivel_emergencia < hijo_izq.data.nivel_emergencia) or (hijo_der.data.nivel_emergencia == hijo_izq.data.nivel_emergencia 
                and hijo_der.data.time_stamp < hijo_izq.data.time_stamp):
                hijo_izq.data, hijo_der.data = hijo_der.data, hijo_izq.data
            
            self.reorganizar_heap(hijo_izq)
            self.reorganizar_heap(hijo_der)
        
        elif root.leftchild:
            self.reorganizar_heap(root.leftchild)
        elif root.rightchild:
            self.reorganizar_heap(root.rightchild)

   

    


    def consultar_paciente_siguiente(self,root):
        if root is None:
            print("no hay pacientes")
            return None
        else:
            return(root.data)
        

    def programar_cirujia(self, root):
        if root is None:
            print("No hay pacientes en la sala de espera")
            return
        
        paciente_programado = root.data

        cola_aux = Queue()
        cola_aux.enqueue(root)
        ultimo= None

        while not cola_aux.is_empty():
            current = cola_aux.dequeue()
            ultimo = current

            if current.leftchild is not None:
                cola_aux.enqueue(current.leftchild)

            if current.rightchild is not None:
                cola_aux.enqueue(current.rightchild)
            

        if ultimo is not None:
            root.data = ultimo.data


        cola_aux_2= Queue()
        cola_aux_2.enqueue(root)
        while not cola_aux_2.is_empty():
            current = cola_aux_2.dequeue()
            if current.leftchild == ultimo:
                current.leftchild = None
                break
            if current.rightchild == ultimo:
                current.rightchild = None
                break

            if current.leftchild is not None:
                cola_aux_2.enqueue(current.leftchild)
                
            if current.rightchild is not None:
                cola_aux_2.enqueue(current.rightchild)

        
        self.reorganizar_heap(self.quirofano)
                    
                   

        return paciente_programado
        
    def mostrar_todos_pacientes(self, root):
        if root is None:
            print("no hay pacientes para mostrar")
            return
        
        cola= Queue()
        cola.enqueue(root)
        while not cola.is_empty():
            current= cola.dequeue()
            print(current.data)
            if current.leftchild is not None:
                cola.enqueue(current.leftchild)
            if current.rightchild is not None:
                cola.enqueue(current.rightchild)

    def mostrar_pacientes_por_nivel_emergencia(self, root, nivel_emergencia:int):
        if root is None:
            return
        if root:
            if root.data.nivel_emergencia == nivel_emergencia:
                print(root.data)
            self.mostrar_pacientes_por_nivel_emergencia(root.leftchild, nivel_emergencia)
            self.mostrar_pacientes_por_nivel_emergencia(root.rightchild, nivel_emergencia)

       





q = Quirofano()

q.registrar_paciente(1,"p01",1,10)
q.registrar_paciente(2,"p02",2,11)
q.registrar_paciente(3,"p03",3,20)
q.registrar_paciente(4,"p04",4,20)
q.registrar_paciente(5,"p05",4,6)
q.registrar_paciente(6,"p06",5,10)
q.registrar_paciente(7,"p07",5,8)


print("sala de espera")
printTree(q.quirofano)
print("pacientes esperando", q.mostrar_todos_pacientes(q.quirofano))
print("pacientes por nivel", q.mostrar_pacientes_por_nivel_emergencia(q.quirofano,2))

print("consultar paciente siguiente",q.consultar_paciente_siguiente(q.quirofano))

print("programar cirujia: ",q.programar_cirujia(q.quirofano))
print("quirofano despues de comenzar a operar")
printTree(q.quirofano)
print("consultar paciente siguiente",q.consultar_paciente_siguiente(q.quirofano))
print("programar cirujia_2: ",q.programar_cirujia(q.quirofano))
printTree(q.quirofano)






