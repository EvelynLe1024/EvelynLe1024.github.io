from PIL import Image, ImageFilter

img = Image.open('./scenery_images/beach.jpg')

filtered_img = img.convert('L')
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("grey.png", 'png')

