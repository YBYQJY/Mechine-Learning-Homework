from PIL import Image
	
if __name__ == '__main__':
	im_A = Image.open('PictureA.png')
	im_B = Image.open('PictureB.png')
	width, height = im_A.size
	im_ans = Image.new("RGB", (width, height), "white") 
	for i in range(0,width):
		for j in range(0,height):
			rgb_A = im_A.getpixel((i,j))
			rgb_B = im_B.getpixel((i,j))
			if rgb_A == rgb_B:
				im_ans.putpixel((i,j), (255,255,255))
			else:
				im_ans.putpixel((i,j), rgb_B)
	im_ans.save("PictureAns.png")
