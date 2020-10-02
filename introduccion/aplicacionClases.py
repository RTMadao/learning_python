class Persona:
    #atributos de clase (estatico)
    _especie = 'humana' # "_" convencion para indicar una variable como constante

    #metodos estaticos
    @staticmethod
    def identificarse():
        print('soy una persona')

    #metodos de instancia
    def __init__(self, nombre, apellido, edad, sexo, mensaje): #constructor
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.__mensajeSecreto = mensaje #atributos privados

    @property
    def mensajeSecreto(self):
        return self.__mensajeSecreto

    @mensajeSecreto.setter
    def mensajeSecreto(self, valor):
        self.__mensajeSecreto = valor

    def saludar(self):
        self.__cambiarMensaje()
        print(f'hola, soy {self.nombre} mi mensaje es {self.__mensajeSecreto}')
    
    def __cambiarMensaje(self): #metodos privados
        self.__mensajeSecreto = 'nuevo mensaje'

class Estudiante(Persona):

    def __init__(self, nombre, apellido, edad, sexo, carrera):
        Persona.__init__(self, nombre, apellido, edad, sexo, carrera)
        self.carrera = carrera

    def estudiar(self):
        print(f'{self.nombre} comienza a estudiar {self.carrera}')

    @classmethod
    def hablar(cls):
        print(f'mi soy {cls._especie}')

usuario = Persona('Carlos','Bello',20,'Masculino', 'este es mi mensaje')
usuario.saludar()

print(Persona._especie + ' es igual a '+ usuario._especie)

usuario.mensajeSecreto = "modificadores de acceso"
print(usuario.mensajeSecreto)

Persona.identificarse()

est = Estudiante('Daniel','Hernandez',21,'Masculino','Ing. sistemas')
est.estudiar()
Estudiante.hablar()