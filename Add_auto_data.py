import json
import os
import shutil
import math

rootPath = r"E:\Buffywalls"
dstPath = "D:\BuffyJson\BuffyData\Category"
path0 = "data/"
path = "data/Category/"
pickedWallspaths = os.listdir(rootPath)


name = 'Amoled'
date = "Oct 26"

# print(" 1 . Abstract      2 . Amoled     3 . Animals                 4 . Anime")
#     print(" 5 . Cars & Bike   6 . Cartoon    7 . Flower                 8 . Games")
#     print(" 9 . Horror       10 . Love      11 . Minimal Illustration  12 . Minimal")
#     print("13 . Movies       14 . Music     15 . Nature                16 . Night Life")
#     print("17 . Pathways     18 . People    19 . Piyush KPV            20 . Sci-Fi")
#     print("21 . Series       22 . Sports    23 . Sunview               24 . Super Heroes")
#     print("25 . Creative")


def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def copy_images():
    shutil.copytree(rootPath,dstPath+'\{}\{}'.format(name,date),dirs_exist_ok=True)


def addToPopular(imageName,designer,category,size,imageUrl,compressUrl):
    popularData = {}
    with open(path0+"popular.json","r") as f:
        temp = json.load(f)

    popularData["id"] = len(temp['popular'])+1
    popularData["heroID"] = 'popular'+str(len(temp['popular'])+1)
    popularData["downloads"] = 0
    popularData["name"] = imageName
    popularData["designer"] = designer
    popularData["category"] = category
    popularData["size"] = size
    popularData["imageUrl"] = imageUrl
    popularData["compressUrl"] = compressUrl
    
    temp['popular'].insert(0,popularData)
    with open(path0+"popular.json","w") as f:
        json.dump(temp,f,indent=4);  

    print("\n------------------Data also added to Popular-------------------") 


def addData():
    imageData = {}
    with open(path+name+".json","r") as f:
        temp = json.load(f)

    imageData["id"] = len(temp[name]['Images'])+1
    imageData["heroID"] = name+str(len(temp[name]['Images'])+1)
    imageData["downloads"] = 0
    imageData["name"] = img_name
    imageData["designer"] = 'Buffy'
    # imageData["category"] = input("category : ")
    imageData["size"] = img_size
    imageData["imageUrl"] = image_url
    imageData["compressUrl"] = image_compress_url
    
    temp[name]['Images'].insert(0,imageData)
    with open(path+name+".json","w") as f:
        json.dump(temp,f,indent=4);  

    # print("\n------------------Data added to "+name+"-------------------")
    add = input("{} ---- y/n : ".format(img_name)) 
    if add == 'y':
        addToPopular(
            imageName=imageData["name"],
            designer=imageData["designer"],
            category=name,
            size=imageData["size"],
            imageUrl=imageData["imageUrl"],
            compressUrl=imageData["compressUrl"]
            )

for i in range(1,len(pickedWallspaths),2):
    img_path = os.path.join(rootPath,pickedWallspaths[i])
    img_name = pickedWallspaths[i][0:-4]
    image_url = 'https://github.com/Surajkrmkr/BuffyData/raw/main/Category/{}/{}/{}'.format(name,date,pickedWallspaths[i]).replace(" ",'%20')
    image_compress_url = 'https://github.com/Surajkrmkr/BuffyData/raw/main/Category/{}/{}/{}'.format(name,date,pickedWallspaths[i-1]).replace(" ",'%20')
    img_size = convert_size(os.stat(img_path).st_size)
    
    addData()
    copy_images()
    




