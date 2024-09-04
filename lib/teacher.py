# teacher.py

from user import User

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        # Initialize with some default knowledge
        self.knowledge = ["Introduction to Python", "Advanced Algorithms"]

    def teach(self):
        # Return the first element from the knowledge list
        return self.knowledge[0]
