from matplotlib import pyplot as plt



class corrAnalysis:
    def __init__(self, valList, otherData, xlab, ylab):
        self.values = valList
        self.data = otherData
        self.xlabel = xlab
        self.ylabel = ylab

    def mean(self):
        s1 = 0
        f = 0
        s2 = 0
        e = 0
        for i in self.values:
           s1 = s1 + i
           f = f + 1
        for i in self.data:
            s2 = s2 + i
            e = e + 1
        return s1/f, s2/e

    def correlationCoefficient(self):
        xMean, yMean = self.mean()
        numer = 0
        summation2 = 0
        summation3 = 0
        if len(self.values) == len(self.data):
            f = 0
            for i in self.values:
                numer = numer + ((i-xMean)*(self.data[f]-yMean))
                summation2 = summation2 + ((i-xMean)**2)
                summation3 = summation3 + ((self.data[f]-yMean)**2)
                f = f + 1
            denom = (summation3*summation2)**(0.5)
            if denom != 0:
                return numer/denom
            else:
                return 0
        else:
            raise Exception("Index bounof lists do not match")

    def chart(self):
        r = round(self.correlationCoefficient(),2)
        
        plt.xlabel(str(self.xlabel) + " r = "+str(r))
        plt.ylabel(str(self.ylabel))

        plt.plot(self.values,self.data)
        plt.show()
