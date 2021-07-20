
class Person:
    def __init__(self):
        self.__age = None
        self.__nationality = None

    def set_values(self, age, nationality):
        if age < 0:
            print("Age cannot be negative")
            exit()
        if type(nationality) != str:
            print("Nationality should be a string")
            exit()

        self.__age = age
        self.__nationality = nationality.lower()

    def get_age(self):
        return self.__age

    def get_nationality(self):
        return self.__nationality

    def adhaar(self):
        if self.get_age() >= 18 and self.get_nationality() == 'indian':
            print("Eligible for Aadhaar")
        elif self.get_age() < 18 and self.get_nationality() == 'indian':
            print(
                "Not eligible for Aadhaar, despite being Indian as the person is below 18")
        elif self.get_age() >= 18 and self.get_nationality() != 'indian':
            print(
                "Not eligible for Aadhaar, despite being adult as the person is not Indian")
        elif self.get_age() < 18 and self.get_nationality() != 'indian':
            print(
                "Not eligible for Aadhaar, as the indiviual is neither Indian nor an adult")
        else:
            print("Something went wrong!")


raj = Person()
raj.set_values(int(input("Enter the age")), input("Enter Nationality"))

raj.adhaar()
