from PIL import Image, ImageDraw, ImageFont

for i in range(1, 10000):
	x = 0
	y = 0
	font_size = 0
	if i < 10:
		font_size = 225
		x = 50
	elif i < 100:
		font_size = 200
		x = 10
	elif i < 1000:
		font_size = 150
		x = 0
		y = 27
	else:
		font_size = 100
		x = 10
		y = 60
	img = Image.new('RGB', (250, 250), color = (31, 18, 30))
	fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', font_size)
	d = ImageDraw.Draw(img)
	d.text((x,y), f'{i}', font=fnt, fill=(0, 255, 255))

	img.save(f'./images/{i}.png')
