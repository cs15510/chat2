#讀取檔案
def read_file(filename):
	chat2 = []
	with open(filename,"r", encoding = "utf-8-sig") as f:
		for line in f:
			chat2.append(line.strip().split(" "))
	return chat2


#計數
def word_count(chat2):
	allen_word_count = 0
	allen_stick_count = 0
	allen_pic_count = 0
	viki_word_count = 0
	viki_stick_count = 0
	viki_pic_count = 0
	for i in chat2:
		time = i[0]
		name = i[1]
		content = i[2:]
		if name == "Allen":
			if content == ["貼圖"]:
				allen_stick_count += 1
			elif content == ["圖片"]:
				allen_pic_count += 1
			else:
				for w in content:
					allen_word_count += len(w)
		if name == "Viki":
			if content == ["貼圖"]:
				viki_stick_count += 1
			elif content == ["圖片"]:
				viki_pic_count += 1
			else:
				for w in content:
					viki_word_count += len(w)
	print("Allen講了", allen_word_count, "個字")
	print("Allen用了", allen_pic_count, "個圖片")
	print("Allen用了", allen_stick_count, "個貼圖")
	print("Viki講了", viki_word_count, "個字")
	print("Viki用了", viki_pic_count, "個圖片")
	print("Viki用了", viki_stick_count, "個貼圖")



chat2 = read_file("LINE-Viki.txt")
word_count(chat2)