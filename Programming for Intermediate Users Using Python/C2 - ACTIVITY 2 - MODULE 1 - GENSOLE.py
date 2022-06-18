
class ClubMembers:
    def __init__(self, name, birthday, age, favorite_food, goal):
        self.name = name
        self. birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal

    def display(self):
        print("Name:", self.name)
        print("Birthday:", self.birthday)
        print("Favorite food:", self.favorite_food)
        print("Goal:", self.goal)

class ClubOfficers(ClubMembers):
    #__init__ method of Admin subclass overrides __init__method of User base class

    def __init__(self, name, birthday, age, favorite_food, goal, position):
        self.position = position
        ClubMembers.__init__(self, name, birthday, age, favorite_food, goal)

    def display(self):
        print("Name:", self.name)
        print("Birthday:", self.birthday)
        print("Favorite food:", self.favorite_food)
        print("Goal:", self.goal)
        print("Position:", self.position)

n_1 = ClubMembers("Tom", "January 16", 14, "Ice cream", "To be happy")
o_4 = ClubOfficers("Vera", "June 22", 16, "Beef straganoff", "To be the world's greatest chef", "Treasurer")

n_1.display1()
o_4.display2()