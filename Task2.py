class Dog:
    age_factor = 7

    def __init__(self, age_dog):
        self.age_dog = age_dog

    def human_age(self):
      age_dog_like_human = self.age_dog * Dog.age_factor
      print(age_dog_like_human)

age = Dog(age_dog = 5)
age.human_age()