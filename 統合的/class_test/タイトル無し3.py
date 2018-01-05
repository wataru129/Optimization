import numpy as np
import math
import test
print(test.RBFN.val)
class RBFN:
    val = 100
    def ham(self):
        self.egg('call method')

    def egg(self,msg):
        print("{0}".format(msg))
        print(("{0}".format(self.val)))
