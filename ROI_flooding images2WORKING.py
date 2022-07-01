import cv2
import numpy as np
import glob
import os

#sorting a list of paths
frame = glob.glob(f".\\Python flooding images\\*")
limit = len(frame)
String_List = []
for i in range(limit):
    String_List.append(0)
    


#print(limit)
   # List.append(i)

#List.sort()
#print(List)

##digits.sort()
#print(digits)
for i in range(limit): #for every number up to 20,000
    str = frame[i] #call the file in the position of i in the frame's list
    value = str.replace('.\\Python flooding images\\','') 
    value = value.replace('.jpg','')
    value = int(value)      #change called file's string-number name to an integer
    String_List[value] = str #saying the file called should be placed in the position of the 0 in String_List that has the same index position as the file's number name
    
    
#print(String_List)

#for i in frame:
#    i.replace('P', 'j')
#    i.replace('F','a')
#    List.append(i)
    
#List.sort()
#print(List)
#print(str)
#frame = sorted(frame)

#print(frame)
# Read image
image = cv2.imread("C:\\Users\\Naomi\\Documents\\Scholarships and Internships\\Python flooding images\\1.jpg")

# ROI
r = cv2.selectROI("select the area", image)
r = list(r)
# perform conversion from strings in list to int
#for i in range(0, len(r)):
    #r[i] = int(r[i])
frameNr = 0

#print(r)   


#frame_2 = sorted(frame, key=lambda i: os.path.splitext(os.path.basename(i))[0])

for infile in String_List:
    read_image = cv2.imread(infile)
#     # Crop image
    cropped_image = read_image[int(r[1]):int(r[1]+r[3]), 
                            int(r[0]):int(r[0]+r[2])]
    cv2.imwrite(f'C:\\Users\\Naomi\\Desktop\\Psychology\\Frames Output\\{frameNr}.jpg', cropped_image)
    
    frameNr = frameNr+1

    #print(infile)

# keeping image up
cv2.waitKey(0)
