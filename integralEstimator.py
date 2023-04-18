import matplotlib.pyplot as plt

class approximateInt:
    
    
    def __init__(self, func):
        self.func = func # str

    def calcInt(self, a, b, method, n):
        # a - lower bounds, b - upper bounds, n - subintervals
        # method, right, left, trapezoidal, or simpsons
        changeX = (b-a)/n
        #x = ''
        #for y in func:
        #    if y.isalpha():
        #        x = y
        Sum = 0
        if method.lower() == "right":
            subInts = b   
            while subInts > a:
                x = subInts
                Sum += eval(self.func) # func must contain x
                subInts -= changeX
            Sum *= changeX
        elif method.lower() == "left":
            subInts = a  
            while subInts < b:
                x = subInts
                Sum += eval(self.func) # func must contain x
                subInts += changeX
            Sum *= changeX
        elif method.lower() == "midpoint":
            subInts = a
            while subInts < b:
                x = subInts
                Sum2 = eval(self.func) # func must contain x
                subInts += changeX
                x = subInts
                Sum2 += eval(self.func)
                Sum += Sum2/2
            Sum *= changeX
        elif method.lower() == "trapezoidal":
            subInts = a
            first = True
            while subInts <= b:
                x = subInts
                if first == True:
                    Sum += eval(self.func) # func must contain x
                    first = False
                else:
                    Sum += 2*eval(self.func)
                    if subInts + changeX >= b:
                        first = True
                subInts += changeX
            Sum *= (changeX/2)
        elif method.lower() == "simpsons":
            subInts = a
            first = True
            other = False
            while subInts <= b:
                x = subInts
                if first == True:
                    Sum += eval(self.func) # func must contain x
                    first = False
                else:
                    if other == False:
                       # print(eval(self.func))
                        Sum += (4*eval(self.func))
                        other = True
                    else:
                       # print(2*eval(self.func))
                        Sum += (2*eval(self.func))
                        #print(Sum)
                        other = False 
                    if subInts + changeX >= b:
                        first = True
                subInts += changeX
                #print(Sum)
                #print(subInts)
            Sum *= (changeX/3)




        return [method + " approximation is "+ str(round(Sum,2)), round(Sum,2)]

    def graph(self, lowBound, upBound):
        xArr = []
        yArr = []
        #print(func)
        for y in range(lowBound, upBound):
            x = y
            xArr.append(y)
            yArr.append(eval(self.func))
        plt.plot(xArr, yArr)
        plt.show()


    def graphInt(self, lowBound, upBound):
        xArr = []
        yArr = []
        for y in range(lowBound, upBound):
           # print("here")
            x = y
            xArr.append(y)
            inte = self.calcInt(0, y, "right", 4)[1]
            yArr.append(inte)
        plt.plot(xArr, yArr)
        plt.show()
        return


function = "4*(x**(1/2))+5*x+3"
func = approximateInt(function)
print(func.calcInt(1, 3, "right", 4))
print(func.calcInt(1, 3, "left", 4))
print(func.calcInt(1, 3, "midpoint", 4))
print(func.calcInt(1, 3, "trapezoidal", 4))
print(func.calcInt(1, 3, "simpsons", 4))
func.graph(0, 10)
func.graphInt(0, 10)
