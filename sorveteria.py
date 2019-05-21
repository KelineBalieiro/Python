class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())

    def open_restaurante(self):
        print("O " + self.restaurant_name.title() + " está aberto")

restaurante = Restaurant('Chimarrão', 'Churrasco')

print("O nome do restaurante é " + restaurante.restaurant_name.title())
print("O tipo de comida servida é " + restaurante.cuisine_type.title())
restaurante.open_restaurante()


class IceCreamStand(Restaurant):
    def __init__(self, flavors):
        self.flavors = flavors

list_flavors = IceCreamStand (['Morango', 'Creme', 'Chocolate', 'Framboesa'])
print("Sabores disponíveis: " + str(list_flavors.flavors))
