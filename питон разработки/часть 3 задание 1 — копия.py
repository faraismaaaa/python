class TabMen(object):
    def __init__(self,atomicmass,electrons,valent,simvol):
        self.atomicmass=atomicmass
        self.electrons=electrons
        self.valent=valent
        self.simvol=simvol
    def atom(self):
        return "атомная масса этого элемента равна %s" % self.atomicmass
    def elect(self):
        return "количество электронов атома этого элемента равно %s" % self.electrons
    def val(self):
        return "валентность аома этого элемента равна %s" % self.valent
    def sim(self):
        return "в периодической таблице этот элемент обозначается символом %s" % self.simvol
if __name__=="__main__":
    водород=TabMen("1.00797",1,1,"H")
    барий=TabMen("137.34",56,2,"Ва")
    технеций=TabMen("[99]",43,7,"Tc")
    борий=TabMen("[262]",107,3,"Bh")
    титан=TabMen("47.90",22,2,"Ti")
