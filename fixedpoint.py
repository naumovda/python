import numbers  # Numeric abstract base classes
import math

class FixedPoint(numbers.Rational):
    # limited number of slots to prevent the
    # adding of any additinal attributes
    __slots__ = ('value', 'scale', 'default_format')

    def __new__(cls, value, scale=100):
        # the initialization is for immutable object
        # so it overrides __new__ instead of __init__
        self = super().__new__(cls)
        if isinstance(value, FixedPoint):
            self.value = value.value
            self.scale = scale.scale
        elif isinstance(value, int):
            self.value = value
            self.scale = scale
        elif isinstance(value, float):
            self.value = int(scale*value+0.5)  # round half up
            self.scale = scale
        else:
            raise TypeError

        digits = int( math.log10(scale) )
        self.default_format='{{0:.{digits}f}}'.format(digits=digits)

        return self

    def __str__(self):
        return self.__format__(self.default_format)

    def __repr__(self):
        return '{__class__.__name:s}({value:d}, scale={scale:d})'.format(
            __class__=self.__class__, value=self.value, scale=self.scale
        )

    def __format__(self, format_spec):
        if format_spec == "": format_spec = self.default_format
        return format_spec.format(self.value/self.scale) # no rounding

    def numerator(self):
        return self.value

    def denominator(self):
        return self.scale

    def __add__(self, other):
        if not isinstance(other, FixedPoint):
            new_scale = self.scale
            new_value = self.value + other*self.scale
        else:
            new_scale = max(self.scale, other.scale)
            new_value = (self.value*(new_scale//self.scale)
            + other.value*(new_scale//other.scale))

        return FixedPoint(int(new_value), scale=new_scale)

    def __sub__(self, other):
        if not isinstance(other, FixedPoint):
            new_scale = self.scale
            new_value = self.value - other*self.scale
        else:
            new_scale = max(self.scale, other.scale)
            new_value = (self.value*(new_scale//self.scale)
            - other.value*(new_scale//other.scale))

        return FixedPoint(int(new_value), scale=new_scale)

    def __mul__(self, other):
        if not isinstance(other, FixedPoint):
            new_scale = self.scale
            new_value = self.value * other
        else:
            new_scale = self.scale * other.scale
            new_value = self.value * other.value

        return FixedPoint(int(new_value), scale=new_scale)

    def __truediv__(self, other):
        if not isinstance(other, FixedPoint):
            new_value = int(self.value/other)
        else:
            new_value = int(self.value / (other.value/other.scale))

        return FixedPoint(new_value, scale=self.scale)

    def __floordiv__(self, other):
        if not isinstance(other, FixedPoint):
            new_value = int(self.value // other)
        else:
            new_value = int(self.value // (other.value/other.scale))

        return FixedPoint(new_value, scale=self.scale)

    def __mod__(self, other):
        if not isinstance(other, FixedPoint):
            new_value = (self.value/self.scale) % other
        else:
            new_value = self.value % (other.value/other.scale)

        return FixedPoint(new_value, scale=self.scale)

    def __pow__(self, other):
        if not isinstance(other, FixedPoint):
            new_value = (self.value/self.scale) ** other
        else:
            new_value = (self.value/self.scale) ** (other.value/other.scale)

        return FixedPoint(int(new_value)*self.scale, scale=self.scale)

    # в этот момент я задолбалась, поэтому дальше так
    def __abs__(self):
        pass

    def __ceil__(self):
        pass

    def __eq__(self, other):
        pass

    def __floor__(self):
        pass

    def __le__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __neg__(self):
        pass

    def __pos__(self):
        pass

    def __radd__(self, other):
        pass

    def __rfloordiv__(self, other):
        pass

    def __rmod__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __round__(self, ndigits=None):
        pass

    def __rpow__(self, other):
        pass

    def __rtruediv__(self, other):
        pass

    def __trunc__(self):
        pass


fp1 = FixedPoint(2.36)
fp2 = FixedPoint(1.2)

# print('fp1:', fp1)
# print('fp1:', fp2)
# print(fp1 + fp2)
# print(fp1 - fp2)
# print(fp1 * fp2)
# print(fp1 / fp2)

fp3 = FixedPoint.__new__(FixedPoint, 300)
print(id(fp3))
# print(id(fp4))
fp4 = fp3
print(id(fp3))
print(id(fp4))
print(fp3)
print(fp4)

# fp1._text = '12345'