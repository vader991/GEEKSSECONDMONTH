class Person:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession

    def introduce(self):
        print(f"Меня зовут {self.name}, моя профессия — {self.profession}.")


class Classmate(Person):
    def __init__(self, name, profession, group_name):
        super().__init__(name, profession)
        self.group_name = group_name

    def introduce(self):
        print(
            f"Меня зовут {self.name}, я учусь в группе {self.group_name}, "
            f"моя будущая профессия — {self.profession}."
        )


class Friend(Person):
    def __init__(self, name, profession, hobby):
        super().__init__(name, profession)
        self.hobby = hobby

    def introduce(self):
        print(
            f"Меня зовут {self.name}, я работаю как {self.profession}, "
            f"а в свободное время увлекаюсь {self.hobby}."
        )


# Создание объектов Classmate
classmate1 = Classmate("Азим", "программист", "IT-101")
classmate2 = Classmate("Ильяс", "аналитик", "IT-101")

# Создание объектов Friend
friend1 = Friend("Азамат", "дизайнер", "рисованием")
friend2 = Friend("Руслан", "инженер", "шахматами")

# Вызов метода introduce()
classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()

class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation

    def introduce(self):
        print(
            f"Привет, меня зовут {self.name}, "
            f"я родился {self.birth_date}, "
            f"работаю {self.occupation}."
        )


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name):
        super().__init__(name, birth_date, occupation)
        self.group_name = group_name

    def introduce(self):
        print(
            f"Меня зовут {self.name}, я учусь в группе {self.group_name}, "
            f"родился {self.birth_date}, моя профессия — {self.occupation}."
        )


class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby):
        super().__init__(name, birth_date, occupation)
        self.hobby = hobby

    def introduce(self):
        print(
            f"Меня зовут {self.name}, моё хобби — {self.hobby}, "
            f"я родился {self.birth_date}, работаю {self.occupation}."
        )


# Объекты
classmate1 = Classmate("Азим", "05.05.2007", "программист", "IT-101")
classmate2 = Classmate("Ильяс", "12.03.2007", "аналитик", "IT-101")

friend1 = Friend("Азамат", "20.08.2006", "дизайнер", "рисование")
friend2 = Friend("Руслан", "14.01.2006", "инженер", "шахматы")

# Вызовы
classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()

