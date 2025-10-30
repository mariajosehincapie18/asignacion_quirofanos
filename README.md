# asignacion_quirofanos
practica 4 

Sistema de asignación de quirófanos para cirugías de emergencia
Restricciones Técnicas
Únicamente se pueden utilizar la clase de árboles binarios que fue construida en clase, que
es un nodo con enlace a hijo izquierdo y derecho. No utilizar la clase base que utiliza una
lista.
El uso de otra clase base afectará la nota en –2 unidades. No se permite documentación
sobre el código, de ningún tipo.
Para esta práctica, está prohibido el uso de estructuras auxiliares como listas, pilas u otros
contenedores preconstruidos. Excepción colas si se va utilizar para recorrido level order,
únicamente en este caso y debe ser con la clase base de colas construida en clase.
La implementación debe trabajar únicamente sobre nodos enlazados, utilizando punteros a
hijos para todas las operaciones, y opcionalmente al padre.
presentar la práctica sobre otra colección no cumple con lo solicitado por lo que la nota
será de 0.
La práctica debe cumplir con la totalidad de los puntos solicitados, cada punto que no se
presente, disminuirá la nota en 1 por punto no presentado.
El entregable de la práctica debe estar de modo tal que con la ejecución del código se
ejecute de forma autónoma cada uno de los puntos, no cumplir con este punto afectará la
nota en –2 unidades.
Descripción:
Diseñar e implementar un sistema que administre la asignación de quirófanos para
pacientes que requieren cirugía de emergencia en un hospital. Cada paciente tiene un nivel
de emergencia asociado (1 a 5, donde 1 = máxima prioridad). El sistema debe atender
primero a los pacientes más urgentes y, en caso de empate en el nivel de emergencia,
respetar el orden de llegada.
Requerimientos:
El sistema debe implementar un Heap binario mínimo utilizando nodos enlazados con
atributos valor, hijo_izquierdo, hijo_derecho, y padre (este último solo si se requiere para
facilitar operaciones).

