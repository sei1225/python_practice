class Rider:
    def __init__(self,n):
        self.name = n

class Horse:
    def __init__(self,n,r):
       self.name =  n
       self.rider = r

rider = Rider("Okabe")
horse = Horse("HaruUrara",rider)
print(horse.rider.name)