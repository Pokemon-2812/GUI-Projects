import os
path="C:\\Users\\Ishan\\Downloads\\"
files=os.listdir(path)
index=1
for file in files:
	if file.endswith(".jpg"):
		os.rename(path+"\\"+file,f"{path}\\{index}.jpg")
		index+=1