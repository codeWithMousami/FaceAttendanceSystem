import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://faceattendancerealtime-e6fd6-default-rtdb.firebaseio.com/',
    'storageBucket':'faceattendancerealtime-e6fd6.appspot.com'
})




#Importing student images
folderPath ='images'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds =[]
for path  in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket =storage.bucket()
    blob= bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    #print(os.path.splitext(path)[0])
print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

print('Encoding started')
encodeListKnown = findEncodings(imgList)
encodeListKnowWithIds =[encodeListKnown,studentIds]
print('Encoding Complete')

#storing in pickle file
file =open('Encodefilee.p','wb')
pickle.dump(encodeListKnowWithIds,file)
file.close()
print('File saved')