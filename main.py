class Persona:
    def __init__(self, param_nombre, param_email):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def asistencia_clase(self):
        self.asistencia += 1

class Materia:
    def __init__(self, param_nombre, param_aula, param_horario):
        self.nombre = param_nombre
        self.aula = param_aula
        self.horario = param_horario

class Profesor(Persona):
    def __init__(self, param_nombre, param_email, legajo_empleado):
        self.legajo_empleado = legajo_empleado
        super().__init__(param_nombre, param_email)

class Alumno(Persona):
    def __init__(self, param_nombre, param_email, numero_alumno):
        self.numero_alumno = numero_alumno
        self.materias_cursando = []
        super().__init__(param_nombre, param_email)

    def cursando(self, Materia):
        self.materias_cursando.append(Materia.nombre)

class Materia:
    def __init__(self, param_nombre, param_aula, param_horario):
        self.nombre = param_nombre
        self.aula = param_aula
        self.horario = param_horario



Compu = Materia("Computación", "Computo", "8 am")

alumno_nicolas = Alumno("Nicolás", "n.panella@alumno.um.edu.ar", 59080)
print(id(alumno_nicolas))
print("El nombre es: ", alumno_nicolas.nombre)
print("El email es: ", alumno_nicolas.email)
print("El legajo es: ", alumno_nicolas.numero_alumno)
alumno_nicolas.asistencia_clase()
alumno_nicolas.cursando(Compu)
print("La alumno fue a clase, su asistencia es: ", alumno_nicolas.asistencia)
print("La alumno cursa: ", alumno_nicolas.materias_cursando)
print(id(Compu))

profesor_pepe = Profesor("Pepe", "pepe@gmail.com", 50315)
print(id(profesor_pepe))
print("El nombre es: ", profesor_pepe.nombre)
print("El email es: ", profesor_pepe.email)
print("El legajo es: ", profesor_pepe.legajo_empleado)
print("Su asistencia es: ", profesor_pepe.asistencia)
profesor_pepe.asistencia_clase()
print("El profesor fue a clase, su asistencia es: ", profesor_pepe.asistencia)