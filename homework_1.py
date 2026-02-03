class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education_status = (
            "высшее образование есть"
            if self.higher_education
            else "высшего образования нет"
        )

        print(
            f"Меня зовут {self.name}, я родился {self.birth_date}, "
            f"по профессии {self.occupation}, {education_status}."
        )



person1 = Person("Азим", "05-05-2007", "студент", False)
person2 = Person("Адиль", "05-12-2000", "программист", True)
person3 = Person("Азат", "23-05-1999", "дизайнер", True)


people = [person1, person2, person3]

for person in people:
    print("Имя:", person.name)
    print("Дата рождения:", person.birth_date)
    print("Профессия:", person.occupation)
    print("Высшее образование:", person.higher_education)
    person.introduce()
    print()
