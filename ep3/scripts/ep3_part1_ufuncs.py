import numpy as np

try:
    from scipy import special
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False

np.random.seed(0)

print("=" * 80)
print("EP3 Part 1: Universal Functions")
print("=" * 80)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output

values = np.random.randint(1, 10, size=5)
print("\n1) Loop vs Vectorization")
print("values =", values)
print("reciprocal by loop  =", compute_reciprocals(values))
print("reciprocal by NumPy =", 1.0 / values)

print("\n2) Array with Array")
a = np.arange(5)
b = np.arange(1, 6)
print("a =", a)
print("b =", b)
print("a / b =", a / b)

print("\n3) Multi-dimensional array")
x = np.arange(9).reshape((3, 3))
print("x =")
print(x)
print("2 ** x =")
print(2 ** x)

print("\n4) Array Arithmetic")
x = np.arange(4)
print("x      =", x)
print("x + 5  =", x + 5)
print("x - 5  =", x - 5)
print("x * 2  =", x * 2)
print("x / 2  =", x / 2)
print("x // 2 =", x // 2)
print("-x     =", -x)
print("x ** 2 =", x ** 2)
print("x % 2  =", x % 2)
print("expression =", -(0.5 * x + 1) ** 2)

print("\n5) UFunc Functions")
print("np.add(x, 2)      =", np.add(x, 2))
print("np.subtract(x, 2) =", np.subtract(x, 2))
print("np.multiply(x, 2) =", np.multiply(x, 2))
print("np.divide(x, 2)   =", np.divide(x, 2))
print("np.power(x, 2)    =", np.power(x, 2))
print("np.mod(x, 2)      =", np.mod(x, 2))

print("\n6) Absolute Value")
x_abs = np.array([-2, -1, 0, 1, 2])
print("x_abs =", x_abs)
print("np.abs(x_abs) =", np.abs(x_abs))

x_complex = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])
print("complex =", x_complex)
print("np.abs(complex) =", np.abs(x_complex))

print("\n7) Trigonometric Functions")
theta = np.linspace(0, np.pi, 3)
print("theta      =", theta)
print("sin(theta) =", np.sin(theta))
print("cos(theta) =", np.cos(theta))
print("tan(theta) =", np.tan(theta))

x_inv = [-1, 0, 1]
print("arcsin =", np.arcsin(x_inv))
print("arccos =", np.arccos(x_inv))
print("arctan =", np.arctan(x_inv))

print("\n8) Exponential and Logarithm")
x_exp = [1, 2, 3]
print("exp(x)  =", np.exp(x_exp))
print("exp2(x) =", np.exp2(x_exp))
print("3^x     =", np.power(3, x_exp))

x_log = [1, 2, 4, 10]
print("ln(x)    =", np.log(x_log))
print("log2(x)  =", np.log2(x_log))
print("log10(x) =", np.log10(x_log))

x_small = [0, 0.001, 0.01, 0.1]
print("expm1(x) =", np.expm1(x_small))
print("log1p(x) =", np.log1p(x_small))

print("\n9) scipy.special")
if SCIPY_AVAILABLE:
    x_special = [1, 5, 10]
    print("gamma(x)   =", special.gamma(x_special))
    print("gammaln(x) =", special.gammaln(x_special))
    print("beta(x, 2) =", special.beta(x_special, 2))

    x_erf = np.array([0, 0.3, 0.7, 1.0])
    print("erf(x)    =", special.erf(x_erf))
    print("erfc(x)   =", special.erfc(x_erf))
    print("erfinv(x) =", special.erfinv(x_erf))
else:
    print("SciPy not installed. Run: pip install scipy")

print("\n10) Advanced UFunc Features")
x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
print("out= y =", y)

y = np.zeros(10)
np.power(2, x, out=y[::2])
print("power with view output =", y)

x = np.arange(1, 6)
print("np.add.reduce(x) =", np.add.reduce(x))
print("np.multiply.reduce(x) =", np.multiply.reduce(x))
print("np.add.accumulate(x) =", np.add.accumulate(x))
print("np.multiply.accumulate(x) =", np.multiply.accumulate(x))
print("np.multiply.outer(x, x) =")
print(np.multiply.outer(x, x))
