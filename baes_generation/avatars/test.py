# import cv2
# import glob
# import os
# import random
# import numpy as np


# # Загрузка списка файлов
# img_path = 'avatars'
# full_pathes = glob.glob( os.path.join( img_path, '*png' ) )

# # Определяем необходимый размер изображений, основываясь на первом изображении в директории
# img0 = cv2.imread(full_pathes[0], cv2.IMREAD_COLOR)
# height, width, channels = img0.shape

# print('\nRequired image size is ', img0.shape)
# print('Required image type is ', type(img0))
# print('Required image data type (Numpy) is ', img0.dtype)

# # Проверка одинакового размера всех изображений
# for i in range(1, len(full_pathes)):
#     img = cv2.imread(full_pathes[i], cv2.IMREAD_COLOR)
#     if img.shape != (height, width, channels):
#         raise ValueError('Image sizes do not match')

# # Представление изображений в директории в виде массива
# print('\nPrinting an array representation of an image')
# print(img)

# # Проходим по изображениям
# pixel_colors = []

# for filename in os.listdir(img_path):
#     img = cv2.imread(os.path.join(img_path, filename))
#     height, width, channels = img.shape
#     for y in range(height):
#         for x in range(width):
#             for z in range(channels):
#                 pixel = img[y, x]
#                 if pixel[0] == pixel[1] == pixel[2]:
#                     color = pixel[0]
#                 else:
#                     color = random.choice(pixel)
#                 pixel_colors.append(color)


# # Создаём матрицу нашего нового изображения и заполняем её нулями
# new_avatar = np.zeros((560, 528, 3), dtype='uint8')
# height, width, channels = new_avatar.shape


# for y in range(height):
#     for x in range(width):
#         for z in range(channels):
#             color = random.choice(pixel_colors)
#             if isinstance(color, tuple):
#                 color = tuple(int(x) for x in color)
#             new_avatar[y, x, z] = color


# # Просмаотриваем наше сгенерированное изображение
# cv2.imshow('New Avatar', new_avatar)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Сохраняем изображение на диск
# cv2.imwrite('new avatar.png', new_avatar)
