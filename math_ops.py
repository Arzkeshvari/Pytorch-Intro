# ================================================================== #
#                                   Math Ops                         #
# ================================================================== #

import torch

a = torch.rand(4,5)
b = torch.rand(4,5)

add = a + b
sub = a - b
mul = a * b
div = a / b
print(div)

c = 1.5
print(a + 1.5)
print(torch.add(a, 1.5))
print(torch.sub(a, 1.5))
print(torch.mul(a, 1.5))
print(torch.div(a, 1.5))

d = torch.rand(5,2)
print(torch.mm(a,d))

print(torch.sin(a))
print(torch.cos(a))
print(torch.tan(a))
print(torch.asin(a))
print(torch.acos(a))
c = torch.tensor([1.5])
print(torch.atan(c))
print(torch.sinh(a))
print(torch.cosh(a))
print(torch.tanh(a))

print(a)
print(torch.round(a))
print(torch.floor(a))
print(torch.ceil(a))

print(torch.pow(a,b))
print(a**b)
print(torch.exp(a))
print(torch.log(a))
print(torch.log1p(a)) # log(1+a)

#       | min, if x_i < min
# y_i = | x_i, if min <= x_i <= max
#       | max, if x_i > max
print(a)
print(torch.clamp(a, 0.3, 0.6))