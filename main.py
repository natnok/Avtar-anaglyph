from PIL import Image

image = Image.open("monro.jpg")
red, green, blue = image.split()

image = Image.open = red
coordinates = (50, 0, image.width, image.height)
red_left = image.crop(coordinates)

image = Image.open = red
coordinates = (25, 0, 671, image.height)
red_middle = image.crop(coordinates)

monro_blend_red = Image.blend(red_middle, red_left, 0.5)

image = Image.open = blue
coordinates = (0, 0, 646, image.height)
blue_left = image.crop(coordinates)

image = Image.open = blue
coordinates = (25, 0, 671, image.height)
blue_middle = image.crop(coordinates)

monro_blend_blue = Image.blend(blue_middle, blue_left, 0.5)

green = Image.open = green
coordinates = (25, 0, 671, image.height)
green = green.crop(coordinates)

avatar = Image.merge("RGB", (monro_blend_red, green, monro_blend_blue))

avatar_80x80 = Image.open = avatar
avatar_80x80.thumbnail((80, 80))
avatar_80x80.save("avatar_80x80.jpg")
