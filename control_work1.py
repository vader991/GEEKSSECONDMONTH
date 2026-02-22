class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age= age

    def set_name(self, name):
        if not name:
            raise ValueError ("Имя не может быть пустым")
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age < 0 or age > 40:
            raise ValueError ("Возраст не может быть меньше 0 и больше 40")
        self.__age = age

    def get_age(self):
        return self.__age


    def make_sound(self):
        print("животное издает звуки")


class Dog(Animal):
    def make_sound(self):
        print("ГАВ")


class Cat(Animal):
    def make_sound(self):
        print("МЯУ")

dog = Dog("Заза", "5")
cat = Cat("Зуза", "2")

dog.make_sound()
cat.make_sound()

dog.set_age(0)
cat.set_age(4)
cat.set_name("Муза")

print(f"{dog.get_name()} исполнилось {dog.get_age()} лет")
print(f"Кота теперь зовут {cat.get_name()}, ему {cat.get_age()}  года")
