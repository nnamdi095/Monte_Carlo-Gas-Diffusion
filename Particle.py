class Position:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


class Kecepatan:
    def __init__(self,vx,vy,vz):
        self.vx = vx
        self.vy = vy
        self.vz = vz

class Hole:
    def __init__(self,a,b,r):
        self.a = a
        self.b = b
        self.r = r


class Particle:
    def __init__(self,position,velocity):
        self.position = position
        self.velocity = velocity
        self.isInside = 1

    def update_position(self,position):
        self.position = position

    def update_velocity(self,velocity):
        self.velocity = velocity

    def print_position(self):
        print("Position: ("  + str(self.position.x) + "," + str(self.position.y) + "," + str(self.position.z) + ")" )

    def print_velocity(self):
        print("velocity: (" + str(self.velocity.vx) + "," + str(self.velocity.vy) + "," + str(self.velocity.vz) + ")")