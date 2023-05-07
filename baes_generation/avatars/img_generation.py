from PIL import Image
import numpy as np


img1 = Image.open('avatar1.png')
width, height = img1.size


def polynomical_pixel(numbers):
    n = len(numbers)
    x = np.arange(1, n+1)
    y = np.array(numbers)
    p = np.polyfit(x, y, 2)
    return int(np.polyval(p, n+1))


new_avatar = Image.new('RGB', (width, height), color='white')

images = []
for i in range(1, 12):
    img_path = f'avatar{i}.png'
    img = np.array(Image.open(img_path))
    images.append(img)
    print(images[i-1])

r_total = [0]*12
g_total = [0]*12
b_total = [0]*12

for x in range(width):
    for y in range(height):
        for i in range(1, 12):
            pixel = images[i-1][y][x]
            r, g, b = pixel[0],pixel[1],pixel[2]
            r_total[i] = r
            g_total[i] = g
            b_total[i] = b

        r_avg = polynomical_pixel(r_total)
        g_avg = polynomical_pixel(g_total)
        b_avg = polynomical_pixel(b_total)
        for j in range (1,12):
            r_total[j] = 0
            g_total[j] = 0
            b_total[j] = 0

        new_avatar.putpixel((x, y), (r_avg, g_avg, b_avg))


new_avatar.save('new avatar.png')
