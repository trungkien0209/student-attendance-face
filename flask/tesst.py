import cv2
import os
import glob


folder = glob.glob("D:/DATN/Data_Face/Bui Quoc Dung_212110_assignsubmission_file_/image/*.jpg")

var = 2                 # Second Example
while True:              
   print ('Current variable value :', var)
   var = var -1
   if var > 0:
      for file in folder:
        print(file)
        img = cv2.imread(file , cv2.IMREAD_UNCHANGED)
        resized = cv2.resize(img,  (550, 600))
        cv2.imshow("Sheep", resized)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()
   else:
        break

