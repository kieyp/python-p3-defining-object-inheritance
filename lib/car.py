from vehicle import Vehicle

class Car(Vehicle):
    
  def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    
    
    
    
    
    
my_car=Car(wheel_size=1,wheel_number=2)

print(my_car.go())

print(my_car.fill_up_tank())