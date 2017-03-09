"""
  This is a class Car that will be used in instantiation of  Car objects
"""

class Car(object):
  

  def __init__(self, name='General', model='GM', car_type=None,speed = 0):
    
    self.name = name
    self.model = model
    self.car_type = car_type
    self.speed = speed


    if self.name in ['Porshe', 'Koenigsegg']:
      
       self.num_of_doors = 2
      
    else:
      
      self.num_of_doors = 4
      
      

    if self.is_saloon() is False:
      
      self.num_of_wheels = 8
      
    else:
      
      self.num_of_wheels = 4


  def is_saloon(self):
    
    if self.car_type == 'trailer':

       return False

    else:
        
       return True
        
  

  def drive(self, speed):
     
        if  self.is_saloon() is False:
          
            self.speed = speed * 11
            
        else:
          
            self.speed = 10 ** speed

        return Car()

