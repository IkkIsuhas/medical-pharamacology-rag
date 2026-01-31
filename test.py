import torch

if torch.cuda.is_available:
    print(torch.device)
else:
    print("not found")