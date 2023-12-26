class Duck:
  def swim(self):
    print("I can swim")

  def talk(self):
    print("Kwack kwack")


class Dog:
  def swim(self):
    print("I can swim")

  def talk(self):
    print("wof woof")

def traits(obj):
  obj.swim()
  obj.talk()
  print("Done\n")

d = Duck()
dg = Dog()
traits(d)
traits(dg)