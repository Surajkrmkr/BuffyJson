import json

path0 = "data/"
path = "data/brands/"

def choices():
    print(" 1 . Android      2 . Apple     3 . Asus     4 . Google")
    print(" 5 . HTC          6 . Huawei    7 . MIUI     8 . Motorola")
    print(" 9 . OnePlus      10 . Oppo    11 . Realme  12 . Samsung")
    print("13 . Sony         14 . Vivo    15 . Xiaomi  16 . ZTE")
    print("-------------------------Any other number to exit---------------------------")

    return int(input("\nEnter a number to add data in Brands\n"))

def switch(choice):
    switcher = {
        1: "Android",
        2: "Apple",
        3: "Asus",
        4: "Google",
        5: "HTC",
        6: "Huawei",
        7: "MIUI",
        8: "Motorola",
        9: "OnePlus",
        10: "Oppo",
        11: "Realme",
        12: "Samsung",
        13: "Sony",
        14: "Vivo",
        15: "Xiaomi",
        16: "ZTE"
    }
    if(switcher.get(choice, '0')=='0'):
        exit() 
    return switcher.get(choice)

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


def addData(name):
    imageData = {}
    with open(path+name+".json","r") as f:
        temp = json.load(f)

    imageData["id"] = len(temp[name]['Images'])+1
    imageData["heroID"] = name+str(len(temp[name]['Images'])+1)
    imageData["downloads"] = 0
    # imageData["name"] = input("name : ")
    imageData["name"] = 'Galaxy Z Flip'
    imageData["designer"] = name
    # imageData["category"] = input("category : ")
    imageData["size"] = input("size : ")
    imageData["imageUrl"] = input("imageUrl : ").replace('www','dl').replace('dropbox','dropboxusercontent').replace('/blob/','/raw/')
    imageData["compressUrl"] = input("compressUrl : ").replace('www','dl').replace('dropbox','dropboxusercontent').replace('/blob/','/raw/')
    
    temp[name]['Images'].insert(0,imageData)
    with open(path+name+".json","w") as f:
        json.dump(temp,f,indent=4);  

    print("\n------------------Data added to "+name+"-------------------")
    add = input("want to add this to popular enter y/n : ") 
    if add == 'y':
        addToPopular(
            imageName=imageData["name"],
            designer=name,
            category=name,
            size=imageData["size"],
            imageUrl=imageData["imageUrl"],
            compressUrl=imageData["compressUrl"]
            )

while True:
    choice = choices()
    name = switch(choice)
    addData(name)
    