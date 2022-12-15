import audioTrainTest as aT
import sys
from PySide6.QtWidgets import QWidget, QApplication, QLineEdit, QMainWindow, QTextBrowser

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.paths = ""  # ==> 默认文本内容
        self.setWindowTitle('文件拖入')  # ==> 窗口标题
        self.resize(500, 400)  # ==> 定义窗口大小
        self.textBrowser = QTextBrowser()
        self.setCentralWidget(self.textBrowser)  # ==> 定义窗口主题内容为textBrowser
        self.setAcceptDrops(True)  # ==> 设置窗口支持拖动（必须设置）

    # 鼠标拖入事件
    def dragEnterEvent(self, event):
        self.setWindowTitle('dragEnterEvent')
        file = event.mimeData().urls()[0].toLocalFile()  # ==> 获取文件路径
        if file not in self.paths:  # ==> 去重显示
            print("拖拽的文件 ==> {}".format(file))
            #self.paths += file + "\n"
            #self.textBrowser.setText(self.paths)
            if file.endswith('.wav'):
                self.paths = ''
                class_id, probability, classes = aT.file_classification(file, "svmSMtemp","svm")
                top_n=3
                top_n_idx=probability.argsort()[::-1][0:top_n]
                for i in top_n_idx:
                    self.paths += classes[i] + "\n"
            else:
                self.paths = 'drag in wav file please!!!'
            self.textBrowser.setText(self.paths)
            # 鼠标放开函数事件
            event.accept()

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