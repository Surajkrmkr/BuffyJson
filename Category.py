import json

path = "data/Category/"

def choices():
    print(" 1 . Abstract      2 . Amoled     3 . Animal                 4 . Anime")
    print(" 5 . Cars & Bike   6 . Cartoon    7 . Flower                 8 . Games")
    print(" 9 . Horror       10 . Love      11 . Minimal Illustration  12 . Minimal")
    print("13 . Movies       14 . Music     15 . Nature                16 . Night Life")
    print("17 . Pathways     18 . People    19 . Piyush KPV            20 . Sci-Fi")
    print("21 . Series       22 . Sports    23 . Sunview               24 . Super Heroes")
    print("-------------------------Any other number to exit---------------------------")

    return int(input("\nEnter a number to add data in Category\n"))

def switch(choice):
    switcher = {
        1: "Abstract",
        2: "Amoled",
        3: "Animal",
        4: "Anime",
        5: "Cars & Bike",
        6: "Cartoon",
        7: "Flower",
        8: "Games",
        9: "Horror",
        10: "Love",
        11: "Minimal Illustration",
        12: "Minimal",
        13: "Movies",
        14: "Music",
        15: "Nature",
        16: "Night Life",
        17: "Pathways",
        18: "People",
        19: "Piyush KPV",
        20: "Sci-Fi",
        21: "Series",
        22: "Sports",
        23: "Sunview",
        24: "Super Heroes"
    }
    if(switcher.get(choice, '0')=='0'):
        exit() 
    return switcher.get(choice)

def addData(name):
    imageData = {}
    with open(path+name+".json","r") as f:
        temp = json.load(f)

    imageData["id"] = len(temp[name]['Images'])+1
    imageData["heroID"] = name+str(len(temp[name]['Images'])+1)
    imageData["downloads"] = 0
    imageData["name"] = input("name : ")
    imageData["designer"] = input("designer : ")
    # imageData["category"] = input("category : ")
    imageData["size"] = input("size : ")
    imageData["imageUrl"] = input("imageUrl : ").replace('www','dl').replace('dropbox','dropboxusercontent')
    imageData["compressUrl"] = input("compressUrl : ").replace('www','dl').replace('dropbox','dropboxusercontent')
    
    temp[name]['Images'].insert(0,imageData)
    with open(path+name+".json","w") as f:
        json.dump(temp,f,indent=4);  

    print("\n------------------Data added to "+name+"-------------------") 

while True:
    choice = choices()
    name = switch(choice)
    addData(name)
    