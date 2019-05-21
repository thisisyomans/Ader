from PIL import Image, ImageFilter
import webbrowser

filename = 'tests/car1/bmw1.jpeg'

img = Image.open(filename)
#webbrowser.open(filename)
#img.show()
if img.width < 1080 and img.height < 1080:
	print("This image will not work on Instagram, which requires a square image of at least 1080x1080 pixels.")
if img.width > img.height:
	size = (img.height, img.height)
#	img = img.resize(size, Image.ANTIALIAS)
#	img.save('tests/avocadoimage/instaedit.jpg')
	area = (img.width/2 - img.height/2, img.height/2 - img.height/2, img.width/2 + img.height/2, img.height/2 + img.height/2)
	cropped = img.crop(area)
	cropped.save('tests/car1/instaedit.jpg')
elif img.height > img.width:
	size = (img.width, img.width)
#	img = img.resize(size, Image.ANTIALIAS)
#	img.save('tests/avocadoimage/instaedit.jpg')
	area = (img.width/2 - img.width/2, img.height/2 - img.width/2, img.width/2 + img.width/2, img.height/2 + img.width/2)
	cropped = img.crop(area)
	cropped.save('tests/car1/instaedit.jpg')
