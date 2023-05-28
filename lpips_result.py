import lpips
import os
from PIL import Image
import torch

device = torch.device('cuda:1' if torch.cuda.is_available() else 'cpu')
print(device)

loss_fn = lpips.LPIPS(net='alex', version='0.1').to(device)

# the total list of images
target_files = os.listdir('target_png/')
source_files = os.listdir('source_png/')

for file in target_files:
    img0 = lpips.im2tensor(lpips.load_image(os.path.join('target_png/'+file))).to(device)
    img0.unsqueeze(0)


# 画像と差分をまとめる
image_hash = {}

for file in source_files:
    img1 = lpips.im2tensor(lpips.load_image(os.path.join('source_png/'+file))).to(device)
    img1.unsqueeze(0)
    current_lpips_distance = loss_fn.forward(img0, img1)
    print('%s: %.3f'%(file, current_lpips_distance))
    image_hash[file] = current_lpips_distance

dic = sorted(image_hash.items(),key=lambda x:x[1],reverse=True)
print(dic)
