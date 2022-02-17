import json
import os
import shutil
import math

rootPath = r"E:\Buffywalls"
dstPath = "D:\BuffyJson\BuffyData\Trending"
path0 = "data/"
path = "data/Category/"
pickedWallspaths = os.listdir(rootPath)


date = "Feb 17"

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
    shutil.copytree(rootPath,dstPath+'\{}'.format(date),dirs_exist_ok=True)


def addData():
    imageData = {}
    with open(path0+"Trending.json","r") as f:
        temp = json.load(f)

    imageData["id"] = len(temp['Trending'])+1
    imageData["heroID"] = 'Trending'+str(len(temp['Trending'])+1)
    imageData["downloads"] = 0
    imageData["name"] = img_name
    imageData["designer"] = 'Buffy'
    imageData["category"] = 'Trending'
    imageData["size"] = img_size
    imageData["imageUrl"] = image_url
    imageData["compressUrl"] = image_compress_url
    
    temp['Trending'].insert(0,imageData)
    with open(path0+"Trending.json","w") as f:
        json.dump(temp,f,indent=4); 
    print("-----Added Succesfully-----") 

for i in range(1,len(pickedWallspaths),2):
    img_path = os.path.join(rootPath,pickedWallspaths[i])
    img_name = pickedWallspaths[i][0:-4]
    image_url = 'https://github.com/Surajkrmkr/BuffyData/raw/main/Trending/{}/{}'.format(date,pickedWallspaths[i]).replace(" ",'%20')
    image_compress_url = 'https://github.com/Surajkrmkr/BuffyData/raw/main/Trending/{}/{}'.format(date,pickedWallspaths[i-1]).replace(" ",'%20')
    img_size = convert_size(os.stat(img_path).st_size)
    
    addData()
    copy_images()
    




