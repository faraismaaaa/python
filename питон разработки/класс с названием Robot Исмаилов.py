class Robot (object):
    def __init__(self, color, speed, city):
        self.color = color
        self.speed = speed
        self.city = city
    def vor(color, speed, city):
        return "Я еду на %s машине, со скоростью %s, по городу %s."  % (color, speed, city)
print(Robot.vor('eq',21,'dq'))
