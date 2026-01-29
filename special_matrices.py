# ================================================================== #
#                          Special Matrices                          #
# ================================================================== #

import torch

z1 = torch.zeros(4)
z2 = torch.zeros(4,3)
z3 = torch.zeros(4,3,2)
print(z3)

o1 = torch.ones(2,3) + 5
o2 = torch.ones(2,3) * 5
o3 = torch.ones(2,3)
print(o1)

e1 = torch.eye(5)
e2 = torch.eye(5,3)
print(e1)

r1 = torch.rand(4)
r2 = torch.rand(5,2)
print(r2)

rn1 = torch.randn(5)
rn2 = torch.randn(5,4)
print(rn2)

rp1 = torch.randperm(10)
print(rp1)

ra1 = torch.range(10, 100)
ra2 = torch.range(10, 100, 0.5)
print(ra2)

l1 = torch.linspace(0, 5) #s = 100
l2 = torch.linspace(0, 5, 10)
print(l2)

lg1 = torch.logspace(-10, 10, 50)
print(lg1)


print(z3.size())

print(r2.size(0)*r2.size(1))
print(r2.numel())

print(r2.dtype)

r3 = r2.type(torch.DoubleTensor)
print(r3)