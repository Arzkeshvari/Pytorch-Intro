# ================================================================== #
#                          Create Tensors                            #
# ================================================================== #

import torch

scalar = torch.tensor(1)
print(scalar)


vector = torch.tensor([1, 2, 3, 4, -1, 5.5])
print(vector)


matrix = torch.tensor([[1,   2,  -1,   3],
                       [5,   8,   9,   0],
                       [1.5, 1.2, 5.3, 6.3]])
print(matrix)


tensor3d = torch.tensor([
                         [[1, 2, 3],
                          [4, 5, 6]],

                         [[5, 1, -1],
                          [8, 2, 3]]
                         ])
print(tensor3d)


# tensor4d (2*3*4*2)


x = torch.CharTensor([[[1, 2,  3],
                       [4, 5,  6]],
                      [[5, 1, -10],
                       [8, 2,  3]]])
print(x)
print(x[0][1][2])
print(x[0, 1, 2])
print(x[1])
print(x[1, 1])
print(x[1, :, 1:])
print(x[:, :, 1:])
print(x[1, :, :2])

x[1, :, :2] = torch.CharTensor([[0, 1],
                                [2, 3]])
print(x)