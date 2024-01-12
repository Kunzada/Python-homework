# Задания №1
# Создайте классы Book и Article, которые реализуют метод word_count. Напишите функцию total_words,
#  которая принимает список документов и возвращает общее количество слов.
class Book:
    def __init__(self,desc):
        self.description=desc
    def word_count(self):
        return len(self.description)
    
class Article:
    def __init__(self,content):
        self.content=content
    def word_count(self):
        return len(self.content)
def total_words(document):
    total_words=0
    for d in document:
        total_words+=d.word_count()
    return total_words

book1=Book("Tassay")
article=Article("Apple")
document=[book1,article]
print(total_words(document))
# Задания №2
# Создайте классы Box и Cylinder, которые реализуют метод volume. Напишите функцию total_volume, 
# которая принимает список контейнеров и возвращает общий объем.
class Box():
    def __init__(self,length,width,height):
        self.length=length
        self.width=width
        self.height=height

    def volume(self):
        return self.length*self.width*self.height
from math import pi
class Cylinder():
    def __init__(self,radius,height):
        self.r=radius
        self.h=height

    def volume(self):
        return self.r*self.r*self.h*pi
def total_volume(container):
    total=0
    for i in container:
        total+=i.volume()
    return total
box=Box(5,5,5)
box2=Box(30,30,30)
cylinder=Cylinder(3,9)
container=[box,box2,cylinder]
print(total_volume(container))
# Задания №3
# Создайте классы Dog и Cat, которые реализуют метод make_sound. Напишите функцию play_sounds,
#  которая принимает список объектов и вызывает метод make_sound если объект является экземпляром классов 
# Dog или Cat. Используйте функцию isinstance. 

class Dog:
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        return "Bark"
class Cat:
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        return "Meow"

def play_sounds(animals):
    for animal in animals:
        if isinstance(animal, (Dog, Cat)):
            print(animal.make_sound())

cat=Cat("Luis")
dog=Dog("Amal")
animals=[cat,dog]
play_sounds(animals)