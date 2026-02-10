class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        education_status = (
            "есть высшее образование"
            if self.higher_education
            else "нет высшего образования"
        )
        print(
            f"Привет, меня зовут {self.name}, "
            f"я родился {self.birth_date}, "
            f"моя профессия — {self.occupation}, "
            f"у меня {education_status}."
        )


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        education_status = (
            "есть высшее образование"
            if self.higher_education
            else "нет высшего образования"
        )
        print(
            f"Меня зовут {self.name}, я учусь в группе {self.group_name}, "
            f"я одноклассник Азима, родился {self.birth_date}, "
            f"моя профессия — {self.occupation}, "
            f"у меня {education_status}."
        )


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        education_status = (
            "есть высшее образование"
            if self.higher_education
            else "нет высшего образования"
        )
        print(
            f"Меня зовут {self.name}, мое хобби — {self.hobby}, "
            f"я друг Азима, родился {self.birth_date}, "
            f"моя профессия — {self.occupation}, "
            f"у меня {education_status}."
        )


classmate = Classmate("Макс", "10.09.2007", "программист", False, "ПИ-3-25")
friend = Friend("Даниэль", "15.05.2007", "официант", False, "воркаут")

classmate.introduce()
friend.introduce()
