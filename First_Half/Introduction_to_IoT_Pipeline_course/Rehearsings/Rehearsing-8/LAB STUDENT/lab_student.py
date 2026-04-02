class LABStudent:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        return f"I'm {self.name}, {self.age} years old, majoring in {self.major}"
    
    def study(self):
        return f"{self.name} is studying {self.major}."