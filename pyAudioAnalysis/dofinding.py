import audioTrainTest as aT
import sys
from PySide6.QtWidgets import QWidget, QApplication, QLineEdit, QMainWindow, QTextBrowser, QPushButton, QMenu
import os
import configparser

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.text = ""  # ==> 默认文本内容
        self.setWindowTitle('Drag in wav plz')  # ==> 窗口标题
        self.resize(500, 400)  # ==> 定义窗口大小
        self.textBrowser = QTextBrowser()
        self.setCentralWidget(self.textBrowser)  # ==> 定义窗口主题内容为textBrowser
        self.setAcceptDrops(True)  # ==> 设置窗口支持拖动（必须设置）
        self.config=configparser.ConfigParser()
        self.cfgpath=os.path.join(os.path.dirname(os.path.abspath(__file__)),'SearchingCFG.ini')
        self.config.read(self.cfgpath)
        self.ModelName = 'svm'
        self.ModelFile = 'svmModel'
        self.Modelnum = int(self.config.get('Model','num'))
        self.ModelNameList = []
        self.ModelFileList = []
        self.curModelIndex = 0
        self.displayNum = int(self.config.get('Model','DisplayNum'))
        for i in range(int(self.Modelnum)):
            self.ModelNameList.append(self.config.get('Model','ModelName'+str(i)))
            self.ModelFileList.append(self.config.get('Model','ModelFile'+str(i)))
        self.textBrowser.setText('using model file: '+self.ModelFile+'\n'+'show first '+str(self.displayNum)+' results.\n'+'press to change model and num of results')
        self.initUI()

    # 鼠标拖入事件
    def dragEnterEvent(self, event):
        file = event.mimeData().urls()[0].toLocalFile()
        if file.endswith('.wav'):
            event.accept()
        else:
            self.textBrowser.setText('drag in wav file please!!!')
            event.ignore()
    # 鼠标放开
    def dropEvent(self, event):
        self.setWindowTitle('FindingSimilarAudio')
        file = event.mimeData().urls()[0].toLocalFile()  # ==> 获取文件路径
        #print("拖拽的文件 ==> {}".format(file))
        #self.text += file + "\n"
        #self.textBrowser.setText(self.text)
        if file.endswith('.wav'):
            self.text = ''
            class_id, probability, classes = aT.file_classification(file, self.ModelFile,self.ModelName)
            top_n_idx=probability.argsort()[::-1][0:self.displayNum]
            for i in top_n_idx:
                self.text += classes[i][2:] + "\n"
        else:
            self.text = 'drag in wav file please!!!'
        self.textBrowser.setText(self.text)
        event.accept()#事件处理完毕,不向上转发,ignore()则向上转发
    def initUI(self):
        CModelBtn = QPushButton('Change Model', self)
        CModelBtn.setCheckable(True)
        CModelBtn.move(10, 350)
        PlusBtn = QPushButton('+', self)
        PlusBtn.setCheckable(True)
        PlusBtn.move(110, 350)
        MinusBtn = QPushButton('-', self)
        MinusBtn.setCheckable(True)
        MinusBtn.move(210, 350)
        CModelBtn.clicked[bool].connect(self.changeModel)
        PlusBtn.clicked[bool].connect(self.PlusNum)
        MinusBtn.clicked[bool].connect(self.MinusNum)
        #self.setGeometry(300, 300, 280, 170)
        #self.setWindowTitle('切换按钮') 
        #self.show()
        
    def changeModel(self, pressed):
        if self.curModelIndex < self.Modelnum-1:
            self.curModelIndex += 1
        else:
            self.curModelIndex = 0
        self.ModelFile = self.ModelFileList[self.curModelIndex]
        self.ModelName = self.ModelNameList[self.curModelIndex]
        self.textBrowser.setText('using model file: '+self.ModelFile)

    def PlusNum(self, pressed):
        self.displayNum += 1
        self.textBrowser.setText('show first '+str(self.displayNum)+' results.')

    def MinusNum(self, pressed):
        if self.displayNum > 1:
            self.displayNum -= 1
        else:
            self.displayNum = 1
        self.textBrowser.setText('show first '+str(self.displayNum)+' results.')
    
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())

#traininglist = listdir('../../../SFXClassified/')
#print(traininglist)
#aT.extract_features_and_train(traininglist, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)
class_id, probability, classes = aT.file_classification("G:\SimilaritySearchingTool\\testsource\\testResult\MACK Drone Synth Descending.wav", "svmSMtemp","svm")
#print(class_id,probability,classes)
top_n=3
top_n_idx=probability.argsort()[::-1][0:top_n]
for i in top_n_idx:
    print(classes[i])