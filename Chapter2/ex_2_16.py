""" 为了能够现实下列代码的执行效果，请在安装PyTorch之后，在Python交互命令行界面，
    即在系统命令行下输入python这个命令回车后，在>>>提示符后执行下列代码
    （#号及其后面内容为注释，可以忽略）
"""

import torch

t1 = torch.randn(3,4) # 随机产生四个张量
t2 = torch.randn(3,4)
t3 = torch.randn(3,4)
t4 = torch.randn(3,2) # 沿着最后一个维度做堆叠，返回大小为3×4×3的张量
torch.stack([t1,t2,t3], -1).shape
torch.cat([t1,t2,t3,t4], -1).shape # 沿着最后一个维度做拼接，返回大小为3×14的张量
t = torch.randn(3, 6) # 随机产生一个3×6的张量
t.split([1,2,3], -1) # 把张量沿着最后一个维度分割为三个张量
t.split(3, -1) # 把张量沿着最后一个维度分割，分割大小为3，输出的张量大小均为3×3
t.chunk(3, -1) # 把张量沿着最后一个维度分割为三个张量，大小均为3×2
