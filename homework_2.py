class Person:
    def __init__(self, name, birth_date, occupation):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation


    def introduce (self):
           print(f"Привет,меня зовут {self.name}, я родился {self.birth_date}, работаю {self.occupation}")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, group_name ):
            super().__init__ (name, birth_date, occupation )
            self.group_name = group_name

    def introduce(self):

            print(
                f"Меня зовут {self.name}, я учусь в группе {self.group_name}, "
                f"я одноклассник Азима, родился {self.birth_date}, "
                f"моя профессия — {self.occupation}"
            )


class Friend(Person):
    def __init__(self, name, birth_date, occupation, hobby):
            super().__init__ ( name,birth_date, occupation, )
            self.hobby = hobby

    def introduce(self):
        print(f" Меня зовут { self.name}, мое хобби - {self.hobby}, я друг Азима, я родился {self.birth_date}, профессия -  {self.occupation}.")






classmate = Classmate("Макс", "10.09.2007", "программист", "ПИ-3-25")

friend = Friend("Даниэль", "15.05.2007", "официант", "воркаут")

classmate.introduce()
friend.introduce()


