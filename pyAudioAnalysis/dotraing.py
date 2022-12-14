import audioTrainTest as aT
#aT.extract_features_and_train(["../testsource/test1","../testsource/test2","../testsource/test3","../testsource/test4","../testsource/test5","../testsource/test6","../testsource/test7","../testsource/test8"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)
class_id, probability, classes = aT.file_classification("../testsource/testResult/testMagic.wav", "svmSMtemp","svm")
print(class_id,probability,classes)