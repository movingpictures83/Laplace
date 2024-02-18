from scipy import ndimage

class LaplacePlugin:
    def input(self, inputfile):
        infile = open(inputfile, 'r')
        self.vector = []
        for line in infile:
           self.vector.append(float(line.strip()))
    def run(self):
        self.result = ndimage.laplace(self.vector)
    def output(self, outputfile):
        print(self.result)

#result = ndimage.laplace([4,5,2])
#print(result)
