
import math
class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __eq__(self, other):
        if self.real == other.real and self.imaginary == other.imaginary:
            return True
        else:
            return False

    def __add__(self, other):
        if isinstance(other, ComplexNumber) == False:
                other = ComplexNumber(other, 0)
        return ComplexNumber((self.real + other.real),(self.imaginary + other.imaginary))
    def __radd__(self,other):
        if isinstance(other, ComplexNumber) == False:
                other = ComplexNumber(other, 0)
        return self+other

    def __mul__(self, other):
        if isinstance(other, ComplexNumber) == False:
                other = ComplexNumber(other, 0)
        a, b, c, d = self.real, self.imaginary, other.real, other.imaginary
        return ComplexNumber(a * c - b * d, b * c + a * d)
    def __rmul__(self, other):
        if isinstance(other, ComplexNumber) == False:
                other = ComplexNumber(other, 0)
        return self*other
    def __sub__(self, other):
        if isinstance(other, ComplexNumber) == False:
                other = ComplexNumber(other, 0)
        return  ComplexNumber((self.real - other.real),(self.imaginary - other.imaginary) )
    def __rsub__(self, other):
        if isinstance(other, ComplexNumber) == False:
                other = ComplexNumber(other, 0)
        return (self*-1)+other
    def __truediv__(self, other):
        if isinstance(other, ComplexNumber) == False:
                other = ComplexNumber(other, 0)
        a, b, c, d = self.real, self.imaginary, other.real, other.imaginary
        return ComplexNumber(float((a * c + b * d)/(c**2 + d**2)) , float((b * c - a * d)/(c**2 + d**2)))
    def __rtruediv__(self, other):
        if isinstance(other, ComplexNumber) == False:
                other = ComplexNumber(other, 0)
        return other/self
       

    def __abs__(self):
        
        return math.sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber(round(math.cos(self.imaginary), 8) * math.exp(self.real), round(math.sin(self.imaginary), 8) * math.exp(self.real))
        pass
