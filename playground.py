from __future__ import print_function

import argparse

import torch
import GPUtil

a = torch.Tensor([1,2,3,4])
a.cuda()
GPUtil.showUtilization()
# result = torch.cuda.memory_snapshot()
# print(result)
#
# b = a