import audioTrainTest as aT
import os

def listdir(path):
    dirlist = []
    file_list=os.listdir(path)
    for temp in file_list:
        path_now = os.path.join(path, temp)
        if os.path.isdir(path_now)==True:
            dirlist.append(path_now)
    return dirlist

traininglist = listdir('../../../SFXClassified/')
#print(traininglist)
aT.extract_features_and_train(traininglist, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)
#class_id, probability, classes = aT.file_classification("../testsource/testResult/testMagic.wav", "svmSMtemp","svm")
#print(class_id,probability,classes)