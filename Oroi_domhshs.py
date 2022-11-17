from helpers.fek import fek
import re

class Xwros:
    xwroi = {}
    def __init__(self, name, calcString, xwros=None):
        self.name = name
        self.calcString = calcString
        self.xwros = xwros
        self.emvado = None
        self.canCalculate = False
        self.dependancies = []
        Xwros.xwroi[self.name] = self

        # Vriskei xwrous - metavlhtes
        self.regexPattern = r"[A-zΑ-ω]+[\d.Α-ω]+"
        matches = re.findall(self.regexPattern, self.calcString)
        self.dependancies = matches

    
    def findCalculationDependancies(self):
        if self.canCalculate:
            return True
        if not self.dependancies:
            self.canCalculate = True
            self.calculate()
            return True
        else: 
            self.dependanciesValues = []
            for i in self.dependancies:
                # an dependency iparxei stous xwrous kai exei timh tote pare thnn timh
                if not Xwros.xwroi[i]:
                    print(f"Dependancy {i} does not exist yet!!")
                    return False
                else:
                    dependancy = Xwros.xwroi[i]
                    print(dependancy)
                    dependancy.findCalculationDependancies()
                    if dependancy.canCalculate:
                        self.dependanciesValues.append(dependancy.emvado)
                    else:
                        return False
            self.canCalculate = True
            self.calculate()

    def calculate(self):
        # replace dependancies with their values
        editedString = self.calcString

        if self.dependancies:
            for i in range(len(self.dependancies)):
                print(self.dependancies[i],self.dependanciesValues[i])
                editedString = re.sub(self.regexPattern, self.dependanciesValues[i], editedString)
        self.calcString = editedString
        self.emvado = eval(self.calcString)

    def prettyPrintCalc(self):
        pass

    def printCalc(self):
        print(self.calcString)
    
    def printFek(self, nomos="NOK 4067/12"):
        dom = fek[self.xwros]["dom"]
        print(f"{nomos}, Άρ.{dom[0]} παρ.{dom[1]}, περ.{dom[2]}")

## Ktirio
class Ktirio:
    def __init__(self, name, xwroiArray, orofoi):
        self.xwroi = xwroiArray
    def domhsh(self):
        pass
    def kalipsi(self):
        pass
    def listAllXwroi(self):
        for xwros in self.xwroi:
            print(f"{xwros.name} , {xwros.xwros}, {xwros.emvado}")
    


## Pinakida
class Pinakida:
    def __init__(self, ktirio):
        self.ktirio = ktirio
    def emvadaOla(self):

        # self.epimerousEmvada(eArray)
        # self.domhsh(dArray)
        pass
    def epimerousEmvada(self, eArray):
        # vriskw tous xwrous pou den einai D
        pass
    def domhsh(self, dArray):
        #vriskw tous xwrous pou einai D
        pass

    def logizomeni_domhsh(self):
        # copy twn xwrwn
        # gia kathe mia timh vriskw array me poia einai se afti kai tous kanw pop
        # mexri na min exw alles times
        # kathe epanalipsi einai mia grammi sto output
        # meta kanw sort me vash poio thelw na fainetai panw-panw
        pass


x = Xwros("e12", "9.2", xwros="yp")
a = Xwros("e13", "9,5 + e12")
b = Xwros("e14", "10*e13")

b.findCalculationDependancies()
