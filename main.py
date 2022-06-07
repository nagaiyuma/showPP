import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import numpy as np
import csv
import pprint

ttfontname = "./fonts/RictyDiminished-Regular.ttf"
fontsize = 36

# 画像サイズ，背景色，フォントの色を設定
canvasSize    = (2700, 150)
backgroundRGB = (255, 255, 255)
textRGB       = (0, 0, 0)

a = np.zeros((61, 55))
with open('./data/新宿駅フィールドワーク - シート1.csv') as f:
	reader = csv.reader(f)
	for i in reader:
		start = int(i[1])
		end = int(i[2])
		locate = int(i[3])
		n = int(i[4])
		for j in range(start, end + 1):
			a[j][locate] = n

images = []
for i in a:
	text = ""
	for j in i:
		if j == 0:
			text += "◯"
		if j == 1:
			text += "❶"
		if j == 2:
			text += "❷"
		img  = PIL.Image.new('RGB', canvasSize, backgroundRGB)
		draw = PIL.ImageDraw.Draw(img)
		font = PIL.ImageFont.truetype(ttfontname, fontsize)
		textWidth, textHeight = draw.textsize(text,font=font)
		textTopLeft = (canvasSize[0]//6, canvasSize[1]//2-textHeight//2) # 前から1/6，上下中央に配置
		draw.text(textTopLeft, text, fill=textRGB, font=font)
	images.append(img)

images[0].save('pic/pillow_imagedraw.gif',save_all=True, append_images=images[1:], optimize=False, duration=80, loop=0)
# 用意した画像に文字列を描く


