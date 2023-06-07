class Knight:
# We set the constructor
    def __init__(self, name, hitPoints):
        self.__name = name
        self.__hitPoints = hitPoints

# This function names the Knight
    def name(self):
        return self.__name

# This function sets 'hit points' aka health
    def hitPoints(self):
        return self.__hitPoints

# This function takes damage
# If damage goes over the limit, the damage taken will decrease to 25
# If not, the damage will be taken
# If IP it goes below zero, it will remain at zero
    def damage(self, points):
        maxDamage = 25
        if points > maxDamage:
            self.__hitPoints = self.__hitPoints - maxDamage
        else:
            self.__hitPoints = self.__hitPoints - points

        if self.__hitPoints < 1:
            self.__hitPoints = 0

# This function takes healing and determines whether alive or dead
    def heal(self, points):
        maxHeal = 25
        if not self.isDead():
            if points > maxHeal:
                self.__hitPoints = self.__hitPoints + maxHeal
            else:
                self.__hitPoints = self.__hitPoints + points

# function states "no hit points" if dead
    def isDead(self):
        return self.__hitPoints == 0

# Set a constructor to determine whether dead or alive
    def __str__(self):
        if self.isDead():
            return self.name() + "is dead!"
        else:
            return self.name() + "is alive!"


def driver():
    Kara = Knight()
    Kara.name()
    print(Kara.name())
    Kara.damage()
    print(Kara.damage())
    Kara.heal()
    print(Kara.heal())
    Kara.hitPoints()
    print(Kara.hitPoints())
    Kara.isDead()
    print(Kara.isDead())

if __name__ == '__main__':
    driver()
