
# Clase madre de animales

class Animal:
    # Constructor de la clase animal general
    def __init__(self, nombre:str, edad: int, peso: str):
        self.nombre = nombre
        self.edad  = edad
        self.peso = peso

   # Métodos correspondientes a la clase animal general
    def mostrar_datos(self):
        print(f"""El nombre de este animal es {self.nombre} yy 
              tiene la edad de {self.edad} años y pesa {self.peso}""")

    def comer(self):
        print(f" {self.nombre} esta comiendo!! ")

# Clases hijas (Herencia)

class Perro (Animal):
    # Metodo constructor de Perro
    def __init__(self, nombre, edad, peso, raza):
        super().__init__(nombre, edad, peso)
        self.raza = raza

    # Metodo (Función)
    def ladrar(self):
        print("Guof! Guof! Guof!")

# Clase Gato

class Gato (Animal):
    # Metodo constructor de Gato
    def __init__(self, nombre, edad, peso, color):
        super().__init__(nombre, edad, peso)
        self.color = color

    # Metodo (Función)
    def maullar(self):
        print("Miua! Miua!")

# Clase Ave 
class Ave (Animal):
    # Metodo constructor de Ave
    def __init__(self, nombre, edad, peso, tipo_de_ala):
        super().__init__(nombre, edad, peso)
        self.tipo_de_ala = tipo_de_ala

    # Metodo (Función)
    def volar(self):
        print(f"El ave {self.nombre} esta volando !!!!")

# Clase Conejo
class Conejo (Animal):
    # Metodo constructor de Conejo
    def __init__(self, nombre, edad, peso, orejas):
        super().__init__(nombre, edad, peso)
        self.orejas = orejas
    
    # Metodo (Función)
    def saltar_peludo (self):
        print("El conejo salta alto y quiere una zanahoria 🥕")


# Creando Objetos

# Perros

perro1 = Perro("Luna",3, "25 kg", "Doger")
perro1.mostrar_datos()
print(f"El nombre del perro es {perro1.nombre}")

perro2 = Perro("Max", 4, "20 kg", "Charmander" )
perro2.mostrar_datos()

# Gatos

gato1 = Gato("Mishi", 2, "30 kg", "Verde")
gato1.mostrar_datos()

gato2 = Gato("Nube", 3, "15 kg", "Morado")
gato2.mostrar_datos()

# Aves

ave1 = Ave("Paco", 2, "10 kg", "velocidad")
ave1.mostrar_datos()

ave2 = Ave("Kiwi", 3, "10 kg", "Planeo dinamico" )
ave2.mostrar_datos()

# Conejo

conejo1 = Conejo("Daniela", 8, "15kg", "Cortas")
conejo1.mostrar_datos()
conejo1.saltar_peludo()

conejo2 = Conejo("Luis", 16, "18 kg", "Largas")
conejo2.mostrar_datos()

# Comentaria añaido de referencia