from math import sin
def f(x): return sin(x)
a=0
b=2
n=21
h= (b-a)/n
S=h*(f(a)+f(b))
for i in range(1,n):
    S = S+f(a+i*h)
Integral=h*S
print('Integral = %f' %Integral)