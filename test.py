import numpy as np
import torch

aten = torch.Tensor([[11, 12, 13, 14],
                     [21, 22, 23, 24],
                     [31, 32, 33, 34],
                     [41, 42, 43, 44]])

print(torch.einsum('ab -> ', aten))