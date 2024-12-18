class Car:
    company_name=0
    color=0
    price=0
    def car_details(self):
 
        print("company name=",self.company_name,"\n color=",self.color,"\n price=",self.price)
print("*** DETAIL OF CAR 1***")
Car_1=Car()
Car_1.company_name="toyota"
Car_1.color="black"
Car_1.price="2500000"
Car_1.car_details()

print("\n")
print("*** DETAIL OF CAR 2***")


Car_2=Car()
Car_2.company_name="kia"
Car_2.color="white"
Car_2.price="3500000"
Car_2.car_details()
print("\n")

print("*** DETAIL OF CAR 3***")

Car_3=Car()
Car_3.company_name="shift"
Car_3.color="red"
Car_3.price="3500000"
Car_3.car_details()
