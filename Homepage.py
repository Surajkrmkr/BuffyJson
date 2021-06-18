import json

path = "data/"

def choices():
    print("\nEnter a number to add data\n")
    print("1 for Popular")
    print("2 for Trending")
    print("0 for Exit")

def addData(choice):
    imageData = {}
    with open(path+choice+".json","r") as f:
        temp = json.load(f)

    imageData["id"] = len(temp[choice])+1
    imageData["heroID"] = choice+str(len(temp[choice])+1)
    imageData["downloads"] = 0
    imageData["name"] = input("name : ")
    imageData["designer"] = input("designer : ")
    imageData["category"] = input("category : ")
    imageData["size"] = input("size : ")
    imageData["imageUrl"] = input("imageUrl : ").replace('www','dl').replace('dropbox','dropboxusercontent')
    imageData["compressUrl"] = input("compressUrl : ").replace('www','dl').replace('dropbox','dropboxusercontent')
    
    temp[choice].insert(0,imageData)
    with open(path+choice+".json","w") as f:
        json.dump(temp,f,indent=4);  

    print("\n------------------Data added  to "+choice+"-------------------") 

while True:
    choices()
    choice = int(input("\n"))
    if choice == 1:
        addData("popular")
    elif choice == 2:
        addData("Trending")
    elif choice == 0:
        exit()
    else:
        print("\n Sorry you did wrong choice")



