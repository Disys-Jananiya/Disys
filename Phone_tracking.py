photos={"camera":20,"watsapp images":35,"canva":1,"screenshots":100}
photos["snapspeed"]=10
photos["picsart"]=7
photos["photoLab"]=5       
photos["FaceApp"]=9
photos["EPIK"]=5
print(photos)
if isinstance(photos,dict)==True:
    print("entry is correct")
else :
    raise TypeError("entered datatype is wrong")
for i in photos.items():
    print(i)
