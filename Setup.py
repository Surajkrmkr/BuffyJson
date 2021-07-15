import json

path = "data/"

def choices():
    print("\nEnter a number to add data\n")
    print("1 for Setups")
    print("0 for Exit")

def addData(choice):
    imageData = {}
    with open(path+choice+".json","r") as f:
        temp = json.load(f)

    imageData["id"] = len(temp[choice])+1
    imageData["author"] = input("author : ")
    imageData["kwgt"] = input("kwgt : ")
    imageData["image"] = input("image : ")
    imageData["launcher"] = input("launcher : ")
    imageData["authorLink"] = input("authorLink : ")
    imageData["iconpackLink"] = input("iconpackLink : ")
    imageData["imageLink"] = input("imageLink : ")
    imageData["launcherLink"] = input("launcherLink : ")
    imageData["name"] = input("name : ")
    imageData["setupImageLink"] = input("setupImageLink : ").replace('www','dl').replace('dropbox','dropboxusercontent').replace('/blob/','/raw/')
    
    
    temp[choice].insert(0,imageData)
    with open(path+choice+".json","w") as f:
        json.dump(temp,f,indent=4);  

    print("\n------------------Data added  to "+choice+"-------------------") 

while True:
    choices()
    choice = int(input("\n"))
    if choice == 1:
        addData("setup")
    elif choice == 0:
        exit()
    else:
        print("\n Sorry you did wrong choice")



