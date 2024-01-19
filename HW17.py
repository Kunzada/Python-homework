# Задание №1
# Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных операторов:
# Проверка на равенство радиусов двух окружностей (операция = =);
# Сравнения длин двух окружностей (операции >, <, <=,>=);
# Пропорциональное изменение размеров окружности, путем изменения ее радиуса (операции + - += -=).
class Circle:
    def __init__(self,radius):
        if not isinstance(radius,float):
            raise TypeError("Радиус должен быть вещественным числом")
        self.radius=radius
    
    def __str__(self):
        return f"Radius of circle: {self.radius}"

    @classmethod
    def __verify_data(cls,other):
        if not isinstance(other,(Circle,float)):
            raise TypeError("Операнд справа должен иметь тип float или Circle")
        return other if isinstance(other,float)else other.radius

    def __eq__(self,other):
        cr=self.__verify_data(other)
        return self.radius==cr
    
    def __lt__(self,other): # <
        cr=self.__verify_data(other)
        return self.radius<cr
    
    def __gt__(self,other):# >
        cr=self.__verify_data(other)
        return self.radius>cr
    
    def __le__(self,other): #<=
        cr=self.__verify_data(other)
        return self.radius<=cr 
    
    def __ge__(self,other):
        cr=self.__verify_data(other)
        return self.radius>=cr

    def __add__(self,other): 
        cr=self.__verify_data(other)
        return Circle(self.radius+cr)

    def __sub__(self,other):
        cr=self.__verify_data(other)
        return self.radius-cr 
    
    def __iadd__(self,other):
        cr=self.__verify_data(other)
        self.radius+=cr
        return self

    def __isub__(self,other):
        cr=self.__verify_data(other)
        self.radius-=cr
        return self

circle=Circle(4.2)
circle1=Circle(9.3)
result1=circle<circle1
result2=circle-circle1
result3=circle>=circle1
circle+=circle1
print(circle)
circle1-=circle
print(result1)
print(circle1)
print(result2)
print(result3)
# Задание №2
# Вам необходимо создать класс Airplane (самолет). 
# С помощью перегрузки операторов реализовать: 
# Проверка на равенство типов самолетов (операция = =); 
# Увеличение и уменьшение пассажиров в салоне самолета (операции +  - +=  -=);
# Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции > <  <=  >=).

class Airplane:
    def __init__(self,type_airplane,cnt_passenger,max_cnt_pass):
        if not isinstance(type_airplane,str):
            raise TypeError("Тип самолета должен быть строкой")
        self.type_airplane=type_airplane
        if not isinstance((cnt_passenger),int):
            raise TypeError("Тип данных количество пассажиров должен быть int")
        self.cnt_passenger=cnt_passenger
        if not isinstance(max_cnt_pass,int):
            raise TypeError("Тип данных int")
        self.max_cnt_pass=max_cnt_pass

    def __str__(self):
        return f"Самолет {self.type_airplane}\n"\
        f"Количеству пассажиров {self.cnt_passenger}"
    
    def __eq__(self,other):
        if not isinstance(other,Airplane):
            raise TypeError("Операнд справа должен иметь тип Airplane")
        air= other if isinstance(other,str) else other.type_airplane 
        return self.type_airplane==air

    @classmethod
    def verify__data(cls,other):
        if not isinstance(other,(Airplane,int)):
            raise TypeError("Операнд справа должен иметь тип Airplane")
        
        return other if isinstance(other,int) else other.cnt_passenger
    
    def __add__(self,other):
        cnt_pass=self.verify__data(other)
        return Airplane(self.type_airplane,self.max_cnt_pass,self.cnt_passenger+cnt_pass)
    
    def __sub__(self,other):
        cnt_pass=self.verify__data(other)
        return Airplane(self.type_airplane,self.max_cnt_pass,self.cnt_passenger-cnt_pass)

    def __iadd__(self,other):
        cnt_pass=self.verify__data(other)
        self.cnt_passenger+=cnt_pass
        return self
    
    def __isub__(self,other):
         cnt_pass=self.verify__data(other)
         self.cnt_passenger-=cnt_pass
         return self
    
    @classmethod 
    def verify_max_pass(cls,other):
        if not isinstance(other,Airplane):
            raise TypeError("Операнд справа должен иметь тип Airplane")
        return other if isinstance(other,int) else other.max_cnt_pass
    
    def __lt__(self,other): # <
        max_cnt=self.verify_max_pass(other)
        return self.max_cnt_pass<max_cnt

    def __gt__(self,other): #>
        max_cnt=self.verify_max_pass(other)
        return self.max_cnt_pass>max_cnt

    def __le__(self,other): # <=
        max_cnt=self.verify_max_pass(other)
        return self.max_cnt_pass<=max_cnt

    def __ge__(self,other): # >=
        max_cnt=self.verify_max_pass(other)
        return self.max_cnt_pass >= max_cnt 

a1=Airplane("Jets",45,80)
a2=Airplane("Gliders",45,69)
print(a1+a2)
print(a1==a2)
print(a1<=a2)
a1+=a2

print(a1.__str__())

# Задание №3
# Создайте класс Roman (РимскоеЧисло), представляющий римское число и поддерживающий операции +, -, *, /.
# При реализации класса:
# операции +, -, *, / реализуйте как специальные методы 
# методы преобразования как статические методы.
class Roman :
    def __init__(self,number):
        self.number=number 

    def __add__(self,other_num):
        if isinstance(other_num,Roman):
            number=other_num if isinstance(other_num,int) else other_num.number
            return self.convert_to_Roman(self.number+number)
        else:
            raise ValueError("Ошибка в типе данных")

    def __sub__(self,other):
        if isinstance(other,Roman):
            number=number if isinstance(other,int) else other.number
            return self.convert_to_Roman(self.number-number)
        else:
            raise ValueError("Ошибка в типе данных")

    def __mul__(self,other):
        if isinstance(other,Roman):
            number=number if isinstance(other,int) else other.number
            return self.convert_to_Roman(self.number*number)
        else:
            raise ValueError("Ошибка в типе данных")

    def __truediv__(self,other):
        if isinstance(other,Roman):
            number=number if isinstance(other,int) else other.number
            result=self.number/number
            return self.convert_to_Roman(int(result))
        else:
            raise ValueError("Ошибка в типе данных") 
    
    @staticmethod
    def convert_to_Roman(number):
        ones=["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hunds=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thous=["","M","MM","MMM","MMMM"]
        t=thous[number//1000]
        h=hunds[number//100%10]
        te=tens[number//10%10]
        o=ones[number%10]
        roman_num=t+h+te+o
        return roman_num

number1=Roman(6)
number2=Roman(3)
result=number1+number2
result2=number1-number2
result3=number1*number2
result4=number1/number2
print(result)
print(result2)
print(result3)
print(result4)