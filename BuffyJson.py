# import json

# path = "data/"

# def choices():
#     print("\nEnter a number to add data\n")
#     # print("1 for Popular")
#     print("2 for Brands")
#     print("3 for Category")

# def addData(choice):
#     imageData = {}
#     with open(path+choice+".json","r") as f:
#         temp = json.load(f)
    

#     imageData["id"] = len(temp[choice])+1
#     imageData["heroID"] = choice+str(len(temp[choice])+1)
#     imageData["downloads"] = 0
#     imageData["name"] = input("name : ")
#     imageData["designer"] = input("designer : ")
#     imageData["category"] = input("category : ")
#     imageData["size"] = input("size : ")
#     imageData["imageUrl"] = input("imageUrl : ")
#     imageData["compressUrl"] = input("compressUrl : ")
    
#     temp[choice].append(imageData)
#     with open(path+choice+".json","w") as f:
#         json.dump(temp,f,indent=4);


# def printBrands():
#     print("1.Android    2.Apple"    )
    

# while True:
#     choices()
#     choice = int(input("\n"))
#     if choice == 1:
#         pass
#     elif choice == 2:
#         brandName = input("\nEnter brand name")
#         addData("popular")
#     else:
#         print("\n Sorry you did wrong choice")



