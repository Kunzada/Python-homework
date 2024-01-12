# Задание №1
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели, год выпуска,
#  производителя, объем двигателя, цвет машины, цену. Реализуйте методы класса для ввода данных, вывода данных,
# реализуйте доступ к отдельным полям через методы класса.
class Car:
    nameofModel="Toyota"
    yearOfIssue=2020
    manufacturer="Toyota Motor Corporation"
    volume=5
    colorOfCar="White"
    price=300_000

    def __init__(self):
        pass

    def __init__(self,nameofModel,yearOfIssue,manufacturer,volume,colorOfCar,price):
        self.nameofModel=nameofModel
        self.yearOfIssue=yearOfIssue
        self.manufacturer=manufacturer
        self.volume=volume
        self.colorOfCar=colorOfCar
        self.price=price

    def input(self):
        self.nameofModel=input("Enter name of model: ")
        self.yearOfIssue=int(input("Enter year of issue: "))
        self.manufacturer=input("Enter manufacturer of car: ")
        self.volume=float(input("Enter volume of car: "))
        self.colorOfCar=input("Enter color of car: ")
        self.price=int(input("Enter price of car: "))

    def __str__(self):
        return "Name of model: %s \n"\
        "Year of Issue: %i \n"\
        "Manufactoruer: %s \n"\
        "Volume of car: %s \n"\
        "Color of car: %s  \n"\
        "Price: %i"%(self.nameofModel,self.yearOfIssue,self.manufacturer,self.volume,self.colorOfCar,self.price)
    
    def getNameOfModel(self):
        return self.nameofModel
    
    def setNameOfModel(self,value):
        self.nameofModel=value

    def getYearOfIssue(self):
        return self.yearOfIssue

    def setYearOfIssue(self,value):
        self.yearOfIssue=value

    def getManufacturer(self):
        return self.manufacturer
    
    def setManufacturer(self,value):
        self.manufacturer=value 

    def getVolume(self):
        return self.volume
    
    def setVolume(self,value):
        self.volume=value

    def getColorOfcar(self):
        return self.colorOfCar
    
    def setColorOfcar(self,value):
        self.colorOfCar=value
    
    def getPrice(self):
        return self.price
    
    def setPrice(self,price):
        self.price=price

# Задание №2
# Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год выпуска, 
# издателя, жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте 
# доступ к отдельным полям через модификаторы доступа и свойства (@property).

class Book:
    _nameOfBook=""
    _yearOfIssue=2020
    _publisher=""
    _genre=""
    _author=""
    _price=200

    def __init__(self,name,year,publisher,genre,author,price):
        self._nameOfBook=name
        self._yearOfIssue=year
        self._publisher=publisher
        self._genre=genre
        self._author=author
        self._price=price
    
    def input(self):
        self._nameOfBook=input("Enter name of book: ")
        self._yearOfIssue=int(input("Enter year of issue: "))
        self._publisher=input("Enter publisher: ")
        self._genre=input("Enter genre: ")
        self._author=input("Enter author: ")
        self._price=int(input("Enter price of book: "))

    def __str__(self):
        return "Name of book: %s\n"\
        "Year of issue: %i\n"\
        "Publisher: %s\n"\
        "Genre: %s\n"\
        "Author: %s\n"\
        "Price: %i" %(self._nameOfBook,self._yearOfIssue,self._publisher,self._genre,self._author,self._price)

    @property
    def nameOfBook(self):
        return self.nameOfBook
    
    @nameOfBook.setter
    def nameOfBook(self,name):
        self.nameOfBook=name

    @property
    def yearOfIssue(self):
        return self._yearOfIssue

    @yearOfIssue.setter
    def yearOfIssue(self,value):
        self._yearOfIssue=value

    @property 
    def publisher(self):
        return self._publisher
    
    @publisher.setter
    def publisher(self,value):
        self._publisher=value

    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self,value):
        self._genre=value
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,value):
        self._author=value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        self._price=value

if __name__== "__main__":
    car=Car("BMW",2010,"Bayerische",3.5,"White",200_000)
    print(car.__str__())
    # car.input()
    # print(car.__str__())
    book=Book("Wild apple",2002,"atamura","vowel","Sayun Muratbekov",1600)
    print(book.__str__())

