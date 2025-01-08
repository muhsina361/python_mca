class ElectricityBill:
    slab1_rate = 3.50 
    slab2_rate = 4.50  
    slab3_rate = 6.00

    def __init__(self, units):
        self.units = units
    def calculate_bill(self):
        if self.units<= 100:
            bill_amount = self.units* self.slab1_rate
        elif self.units<= 200:
            bill_amount = (100 * self.slab1_rate) + ((self.units- 100) * self.slab2_rate)
        else:
            bill_amount = (100 * self.slab1_rate) + (100 * self.slab2_rate) + ((self.units- 200) * self.slab3_rate)
        return bill_amount

units = int(input("Enter the number of units consumed: "))
bill = ElectricityBill(units)
total_amount = bill.calculate_bill()
print(f"The total electricity bill for {units} units is: ₹{total_amount:.2f}")
