
from PyQt5.QtWidgets import *
import sys
import numpy as np
from sıfır import Ui_MainWindow
from PyQt5 import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import random
from itertools import count
from  matplotlib import animation

count = 0
x = []
y_deg = []


class MiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)

        self.grafica = grafik()
        self.grafica1 = grafik()
        self.grafica2 = grafik()
        self.grafica3 = grafik()

        self.ui.grafica_bir.addWidget(self.grafica)
        self.ui.grafica_iki.addWidget(self.grafica1)
        self.ui.grafica_uc.addWidget(self.grafica2)
        self.ui.grafica_dort.addWidget(self.grafica3)

        self.ui.label.setText(str(y_deg))
        self.ui.label_2.setText(str(y_deg))
        self.ui.label_3.setText(str(y_deg))
        self.ui.label_4.setText(str(y_deg))



class grafik(QMainWindow):
    
    def draw_graph(i):
        global count
        count +=1
        x.append(count)
        y_deg.append(random.randint(0,84))

        plt.cla()
        plt.scatter(x,y_deg)
        plt.plot(x,y_deg)

    anima = animation.FuncAnimation(plt.gcf(),draw_graph,interval=1000)

    plt.show()
        

class grafik(QMainWindow):
    
    def draw_graph(i):
        global count
        count +=1
        x.append(count)
        y_deg.append(random.randint(0,84))

        plt.cla()
        plt.scatter(x,y_deg)
        plt.plot(x,y_deg)

    anima = animation.FuncAnimation(plt.gcf(),draw_graph,interval=1000)

    plt.show()
            



class grafik(QMainWindow):
    
    def draw_graph(i):
        global count
        count +=1
        x.append(count)
        y_deg.append(random.randint(0,84))

        plt.cla()
        plt.scatter(x,y_deg)
        plt.plot(x,y_deg)

    anima = animation.FuncAnimation(plt.gcf(),draw_graph,interval=1000)

    plt.show()


class grafik(QMainWindow):
    
    def draw_graph(i):
        global count
        count +=1
        x.append(count)
        y_deg.append(random.randint(0,84))

        plt.cla()
        plt.scatter(x,y_deg)
        plt.plot(x,y_deg)

    anima = animation.FuncAnimation(plt.gcf(),draw_graph,interval=1000)

    plt.show()

if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = MiApp()
     mi_app.show()
     sys.exit(app.exec_())  
