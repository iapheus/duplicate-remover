from PIL import Image
import imagehash
import os 

path = ""  # The location of the address where the pictures are located will be written here
hashList = []


for file in os.listdir(path): 
    if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"): 
        fileHash = imagehash.average_hash(Image.open(file)) 
        if fileHash not in hashList: # Checked hashes from inside the hashList so it can extract duplicate photos
            hashList.append(fileHash)
        else:
            os.remove(file)



