import math

class complex:
    def __init__(self, re, im, out_format):
        self._re = re
        self._im = im
        self._format = out_format

    def __str__(self):
        return self._format(self._re, self._im)
    
def format_as_algebraic(re, im):
    return f"{re}+i*{im}"

def format_as_trigonometric(re, im):
    mod = math.sqrt(re*re+im*im)
    arg = re/im
    return f"{mod:.2f}*(cos({arg:.2f})+i*sin({arg:.2f}))"

def format_as_exponent(re, im):
    mod = math.sqrt(re*re+im*im)
    arg = re/im
    return f"{mod:.2f}*exp(i{arg:.2f})"

c1 = complex(2, 3, format_as_algebraic)
print(c1)
c1._format = format_as_trigonometric
print(c1)
c1._format = format_as_exponent
print(c1)
