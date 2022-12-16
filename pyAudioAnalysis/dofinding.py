import audioTrainTest as aT
import sys
from PySide6.QtWidgets import QWidget, QApplication, QLineEdit, QMainWindow, QTextBrowser, QPushButton, QMenu
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
        self.Modelfile = ''
        self.config=configparser.ConfigParser()
        self.cfgpath='./SearchingCFG.ini'
        self.config.read(self.cfgpath)
        self.Modelname = self.config.get('path','src')

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
            class_id, probability, classes = aT.file_classification(file, "svmSMtemp","svm")
            top_n=3
            top_n_idx=probability.argsort()[::-1][0:top_n]
            for i in top_n_idx:
                self.text += classes[i] + "\n"
        else:
            self.text = 'drag in wav file please!!!'
        self.textBrowser.setText(self.text)
        event.accept()#事件处理完毕,不向上转发,ignore()则向上转发
    def initUI(self):
        CModelBtn = QPushButton('Change Model', self)
        CModelBtn.setCheckable(True)
        CModelBtn.move(10, 10)
        
        CModelBtn.clicked[bool].connect(self.changeModel)
        #self.setGeometry(300, 300, 280, 170)
        #self.setWindowTitle('切换按钮') 
        #self.show()
        
    def changeModel(self, pressed):
        self.Modelname
    






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