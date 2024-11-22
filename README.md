# Avtar-anaglyph
## Create an anaglif avatar from a picture

Importing the ```PIL``` library
```
1    from PIL import Image
```
Open the picture from the root directory, and ```image.split``` the picture into channels (RGB) 
```
3    image = Image.open("monro.jpg")
4    red, green, blue = image.split()
```
Open the ```red``` channel and ```image.crop``` at the ```coordinates``` to the right
```
6    image = Image.open = red
7    coordinates = (50, 0, image.width, image.height)
8    red_left = image.crop(coordinates)
```
Open the ```red``` channel again and ```image.crop``` the image on the sides, by half the value set in the previous step
```
10    image = Image.open = red
11    coordinates = (25, 0, 671, image.height)
12    red_middle = image.crop(coordinates)
```
Make a ```image.blend``` of results, from the variables in which the trimming results lie
```
14    monro_blend_red = Image.blend(red_middle, red_left, 0.5)
```
Open the ```blue``` channel and ```image.crop``` at the ```coordinates``` to the right
```
16    image = Image.open = blue
17    coordinates = (0, 0, 646, image.height)
18    blue_left = image.crop(coordinates)
```
Open the ```blue``` channel again and ```image.crop``` the image on the sides, by half the value set in the previous step
```
20    image = Image.open = blue
21    coordinates = (25, 0, 671, image.height)
22    blue_middle = image.crop(coordinates)
```
Make a ```image.blend``` of results, from the variables in which the trimming results lie
```
24    monro_blend_blue = Image.blend(blue_middle, blue_left, 0.5)
```
Open the ```green``` channel, and ```image.crop``` on the sides, no blending is done
```
26    green = Image.open = green
27    coordinates = (25, 0, 671, image.height)
28    green = green.crop(coordinates)
```
Merge the ```red```, ```green```, ```blue``` channels into one, exactly in this order
```
30    avatar = Image.merge("RGB", (monro_blend_red, green, monro_blend_blue))
```
Using the ```thumbnail``` method, you can easily make a ```thumbnail``` of an image. A ```thumbnail``` is a smaller version of the image, with preserved proportions. A tuple with maximum width and height is taken as input. The ```thumbnail``` method itself will select new ````coordinates``` so that the picture fits into the specified area
```
32    avatar_80x80 = Image.open = avatar
33    avatar_80x80.thumbnail((80, 80))
34    avatar_80x80.save("avatar_80x80.jpg")
```


[Pillow](https://pillow.readthedocs.io/en/stable/#) is the friendly PIL fork by Jeffrey [A. Clark and contributors](https://github.com/python-pillow/Pillow/graphs/contributors). PIL is the Python Imaging Library by Fredrik Lundh and contributors :+1:
