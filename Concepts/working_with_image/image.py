from PIL import Image

img_open = Image.open("Pollock_to_Hussey.jpg")

#img_open.show()
#print(img_open.format_description)

#crop the image
x = 0
y = 0

w = 600 / 3
h = 500
crop_img = img_open.crop((x,y,w,h))
print(crop_img.size)
#crop_img.show()


#paste the crop image in another image

# img_open.paste(im=crop_img, box=((0,0)))
# img_open.show()

#set resize the the image
# img_resize = img_open.resize((3000,500))
# img_resize.show()


