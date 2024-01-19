# Задание №1
# Создайте класс Device, который содержит информацию об устройстве. 
# С помощью механизма наследования, реализуйте класс CoffeeMachine (содержит информацию о кофемашине),
#  класс Blender (содержит информацию о блендере), класс MeatGrinder (содержит информацию о мясорубке).
#  Каждый из классов должен содержать необходимые для работы методы.

class Device(object):
    def __init__(self,modelOfDevice,brandOfDevice,power,price):
        self.modelOfDevice=modelOfDevice
        self.brandOfDevice=brandOfDevice
        self.power=power
        self.price=price

class CoffeMachine(Device):
    def __init__(self,modelOfDevice,brandOfDevice,power,price,coffeeUsed):
        super(CoffeMachine,self).__init__(modelOfDevice,brandOfDevice,power,price) 
        self.coffeeUsed=coffeeUsed 

    def make_coffee(self):
        return \
        f"Making coffee with {self.brandOfDevice}\n"\
        f"Model:{self.modelOfDevice}\n"\
        f"Power:{self.power}\n"\
        f"Price:{self.price}\n"\
        f"Coffee used:{self.coffeeUsed}"

class Blender(Device):
    def __init__(self,modelOfDevice,brandOfDevice,power,price,cntAttachments):
        super(Blender,self).__init__(modelOfDevice,brandOfDevice,power,price)
        self.cntAttachments=cntAttachments
    
    def blend(self):
        return "Blending with %s\nModel of device: %s\nPower: %i\nPrice: %i\nCount attachments: %i"%(self.brandOfDevice,self.modelOfDevice,self.power,self.price,self.cntAttachments)

class MeatGrinder(Device):
    def __init__(self,modelOfDevice,brandOfDevice,power,price,mainsCordLength):
        super(MeatGrinder,self).__init__(modelOfDevice,brandOfDevice,power,price)
        self.mainsCordLength=mainsCordLength

    def grind_meat(self):
        return "Grinding meat with %s \n"\
        "Model of device: %s\n"\
        "Power: %i\n"\
        "Price: %i\n"\
        "Mains cord length: %i"%(self.brandOfDevice,self.modelOfDevice,self.power,self.price,self.mainsCordLength)
coffee_machine = CoffeMachine("CM123", "CoffeeMaster", 1200, 150, "Arabica")
coffee_result = coffee_machine.make_coffee()
print(coffee_result)

blender = Blender("BL456", "SuperBlender", 800, 80, 3)
blend_result = blender.blend()
print(blend_result)

meat_grinder = MeatGrinder("MG789", "MeatMaster", 500, 50, 1)
grind_result = meat_grinder.grind_meat()
print(grind_result)

# Задание №2
# Используя механизм множественного наследования разработайте класс “Автомобиль”, который наследует от 
# классов «Колеса», «Двигатель», «Двери».

class Doors:
    def __init__(self,cnt_doors,type_doors,opening_method):
        self.cnt_doors=cnt_doors
        self.type_doors=type_doors
        self.opening_methond=opening_method


class Wheels:
    def __init__(self,seasonality,rim_type,load_index):
        self.seasonality=seasonality
        self.rim_type=rim_type
        self.load_index=load_index

class Motor:
    def __init__(self,volume,power,type):
        self.volume=volume
        self.power=power
        self.type=type 

class Car(Doors, Wheels, Motor):
    def __init__(self, cnt_doors, type_doors, opening_method,  seasonality, rim_type, load_index, volume, power, motor_type, color):
        Doors.__init__(self, cnt_doors, type_doors, opening_method)
        Wheels.__init__(self, seasonality, rim_type, load_index)
        Motor.__init__(self, volume, power, motor_type)
        self.color = color

    def __str__(self):
        return f"Car Information:\n" \
               f"  Doors: {self.cnt_doors} {self.type_doors} doors ({self.opening_methond})\n" \
               f"  Wheels: {self.seasonality} season tires, {self.rim_type} rims, Load Index: {self.load_index}\n" \
               f"  Motor: {self.volume}L {self.power}HP {self.type} motor\n" \
               f"  Color: {self.color}"

car1 = Car(cnt_doors=4, type_doors="sedan", opening_method="automatic",
           seasonality="summer", rim_type="alloy", load_index="XL", volume=2.0, power=150, motor_type="gasoline",
           color="blue")

print(str(car1))

# Задание №3
# Создайте базовый класс Shape для рисования плоских фигур. 
# Определите методы: 
# Show() — вывод на экран информации о фигуре; 
# Save() — сохранение фигуры в файл; 
# Load() — считывание фигуры из файла. 
# Определите производные классы: 
# Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны; 
# Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами; 
# Circle — окружность с заданными координатами центра и радиусом; 
# Ellipse — эллипс с заданными координатами верхнего угла, описанного вокруг него прямоугольника со сторонами, параллельными осям координат, и размерами этого прямоугольника. Создайте список фигур, сохраните фигуры в файл, загрузите в другой список и отобразите информацию о каждой из фигур.

class Shape:
    def __init__(self,type):
        self.type=type 

    def Show():
        pass 

    def Save(self):
        with open("Shape.txt","a")as file:
            file.write(self.Show()+"\n")
            
    def Load(self):
        with open ("Shape.txt","r")as file:
            lines=file.readlines()
            for i in lines:
                print(i.strip())            



class Square(Shape):
    def __init__(self,x,y,side_length):
        self.x=x
        self.y=y 
        self.side_length=side_length

    def Show(self):
        return f"Square: x:{self.x},"\
        f"y:{self.y},"\
        f"length:{self.side_length}"


class Rectangle(Shape):
    def __init__(self,x,y,width,height):
         self.x=x
         self.y=y
         self.width=width
         self.height=height

    def Show(self):
        return f"Ellipse: X={self.x}, Y={self.y}, Width={self.width}, Height={self.height}" 

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def Show(self):
        return f"Circle: Radius: {self.radius}" 

class Ellipse(Shape):
    def __init__(self,x,y,width,height):
         self.x=x
         self.y=y
         self.width=width
         self.height=height 

    def Show(self):
        return f"Ellipse: X={self.x}, Y={self.y}, Width={self.width}, Height={self.height}"
    
shapes_list=[
    Square(2,2,4),
    Rectangle(2,3,5,6),
    Circle(3),
    Ellipse(4,5,7,8)
]

for shape in shapes_list:
    shape.Save()

for shape in shapes_list:
    shape.Load()

for shape in shapes_list:
    shape.Show()
    
