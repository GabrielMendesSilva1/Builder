class Car:
  #atributos
    def __init__(self):
        self.model = None
        self.engine = None
        self.color = None

    def __str__(self):
        return f"Carro: {self.model}, Motor: {self.engine}, Cor: {self.color}"


class CarBuilder:
  #objetos
    def __init__(self):
        self.car = Car()

    def set_model(self, model):
        self.car.model = model

    def set_engine(self, engine):
        self.car.engine = engine

    def set_color(self, color):
        self.car.color = color

    def get_car(self):
        return self.car


class Director:
  #coordena a construção
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self, model, engine, color):
        self.builder.set_model(model)
        self.builder.set_engine(engine)
        self.builder.set_color(color)
        return self.builder.get_car()


# Função principal do programa
def main():
    builder = CarBuilder()
    director = Director(builder)

    model = input("Digite o modelo do carro: ")
    engine = input("Digite o motor do carro: ")
    color = input("Digite a cor do carro: ")

    car = director.construct_car(model, engine, color)

    print("Carro construído:")
    print(car)


# Executa o programa
if __name__ == "__main__":
    main()
