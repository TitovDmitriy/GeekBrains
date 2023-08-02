class AnimalCreationError(Exception):
    pass


class Animal:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print("Это неизвестное животное.")


class Fish(Animal):
    def __init__(self, name, habitat):
        super().__init__(name)
        self.habitat = habitat

    def display_info(self):
        print(f"Это рыба по имени {self.name}. Она живет в {self.habitat}.")


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def display_info(self):
        print(f"Это птица по имени {self.name}. Ее размах крыльев составляет {self.wingspan}.")


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name, **kwargs):
        if animal_type == "Fish":
            return Fish(name, kwargs.get("habitat"))
        elif animal_type == "Bird":
            return Bird(name, kwargs.get("wingspan"))
        elif animal_type == "Animal":
            return Animal(name)
        else:
            raise AnimalCreationError(f"Тип животного '{animal_type}' не поддерживается.")


try:
    fish = AnimalFactory.create_animal("Fish", "Немо", habitat="океане")
    fish.display_info()

    bird = AnimalFactory.create_animal("Bird", "Орел", wingspan="2 метра")
    bird.display_info()

    animal = AnimalFactory.create_animal("Animal", "Неизвестное животное")
    animal.display_info()

    # Попытка создать животное с неизвестным типом:
    unknown_animal = AnimalFactory.create_animal("Unknown", "Алиса")
    unknown_animal.display_info()

except AnimalCreationError as e:
    print(f"Ошибка при создании животного: {e}")
