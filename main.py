from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QTimer

import sys, os
from matplotlib.pyplot import title
import numpy as np
from mainwindow_ui import *
import EchartsUtils as echarts

# 主界面
def cvtPath(path):
    return path.replace(os.sep, "/")

class MainWindow(QMainWindow):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super(MainWindow, self).__init__(parent=parent, flags=flags)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        currentfolder = os.path.abspath(os.path.dirname(__file__))
        root = os.path.join(currentfolder, "html")

        htmlfile = os.path.join(root, "line.html")
        self.line1 = echarts.Line(cvtPath(htmlfile), self.ui.scrollArea, ["Series1 %", "Series2 %", "Series3 %", "Series4 %"], title="Line test")
        self.line2 = echarts.Line(cvtPath(htmlfile), self.ui.scrollArea_4, ["Series1 %", "Series2 %", "Series3 %", "Series4 %"], title="Line test")

        htmlfile = htmlfile = os.path.join(root, "bar.html")
        self.bar1 = echarts.Bar(cvtPath(htmlfile), self.ui.scrollArea_2, xAxis=["123"], legends=["Series1 %", "Series2 %", "Series3 %", "Series4 %"], title="Bar test1") 
        self.bar2 = echarts.Bar(cvtPath(htmlfile), self.ui.scrollArea_5, xAxis=["123"], legends=["Series1 %", "Series2 %", "Series3 %", "Series4 %"], title="Bar test2") 

        htmlfile = os.path.join(root, "pie.html")
        self.pie1 = echarts.Pie(cvtPath(htmlfile), self.ui.scrollArea_3, title="Pie test1/ms")
        self.pie2 = echarts.Pie(cvtPath(htmlfile), self.ui.scrollArea_7, title="Pie test2/ms")

        self.show()

        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.slotTimeout)
        self.count = 0
        self.timer.start()

    def slotTimeout(self):
        if self.line1.htmlLoadFinished:
            self.count += 1
            xValue = self.count
            yValue1 = np.random.randint(10,40)
            yValue2 = np.random.randint(20,40)
            yValue3 = np.random.randint(30,40)
            yValue4 = np.random.randint(20,40)            

            self.line1.update(xValue, [yValue1, yValue2, yValue3, yValue4])
            self.line2.update(xValue, [yValue1, yValue2, yValue3, yValue4])
            
            self.bar1.update([yValue1, yValue2, yValue3, yValue4])
            self.bar2.update([yValue1, yValue2, yValue3, yValue4])
            
            self.pie1.update({"test1": yValue1,"test2": yValue2,"test3": yValue3,"test4": yValue4})
            self.pie2.update({"test1": yValue1,"test2": yValue2,"test3": yValue3,"test4": yValue4})

            # if self.count > 20:
            #     self.timer.stop()
              

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())