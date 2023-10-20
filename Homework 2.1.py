import numpy as np
import matplotlib.pyplot as plt

lena_path = 'img/lenabin.bin'
pepper_path = 'img/peppersbin.bin'
lena = np.fromfile(lena_path, dtype= np.uint8).reshape(256,256)
pepper = np.fromfile(pepper_path,dtype= np.uint8).reshape(256,256)

plt.figure()
plt.subplot(121)
plt.imshow(lena, cmap='gray')
plt.title('Lena Image')

plt.figure()
plt.subplot(122)
plt.imshow(pepper, cmap='gray')
plt.title('Pepper Image')



J = np.zeros((256, 256), dtype=np.uint8)
J[:, :128] = lena[:, :128]
J[:, 128:] = pepper[:, 128:]

plt.figure()
plt.imshow(J, cmap='gray')
plt.title('Image J')

K = np.zeros((256, 256), dtype=np.uint8)
K[:, :128] = J[:, 128:]
K[:, 128:] = J[:, :128]

plt.figure()
plt.imshow(K, cmap='gray')
plt.title('Image K')

plt.show()