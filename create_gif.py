import imageio.v3 as iio

filenames = ['Screenshot from 2025-07-11 17-42-55.png', 'Screenshot from 2025-07-11 17-43-04.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('sasuke.gif', images, duration = 200, loop = 0)