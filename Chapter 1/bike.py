# lets define the class Bike

class Bike:
    def __init__(self, colour, frame_material):
        self.colour = colour
        self.frame_material = frame_material

    def brake(self):
        print ("Braking!")

# let's create a couple of instances
red_bike = Bike('Red', 'Carbon Fiber')
blue_bike = Bike('Blue', 'Steel')

# lets inspect the objects we have, instances of the Bike class
print (red_bike.colour)
print (red_bike.frame_material)
print (blue_bike.colour)
print (blue_bike.frame_material)

# let's brake!
red_bike.brake()
blue_bike.brake()