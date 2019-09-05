from ui.main import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
import sys
import time
import os
import pandas as pd
from utils import AbstractWithSpecialFunctions, PlotCanvas, base_dir
from functools import partial


class MainApp(QtWidgets.QMainWindow, Ui_MainWindow, AbstractWithSpecialFunctions):
    def __init__(self, df_ls, title=None):
        super().__init__()
        self.setupUi(self)
        self.move_to_center()

        if isinstance(title, str) and title:
            self.setWindowTitle(title)
            self.btn_detail.setEnabled(False)
        else:
            self.setWindowTitle('MultiPlot Main Window')

        self.thumbnails = []
        self.data = df_ls

        for i in range(12):
            i += 1
            label = self.__dict__['label_{}'.format(i)]
            grid_layout = self.__dict__['gridLayout_{}'.format(i+2)]
            label.hide()
            self.__dict__['canvas_{}'.format(i)] = PlotCanvas(
                parent=self.__dict__['mini_frame{}'.format(i)])
            grid_layout.addWidget(
                self.__dict__['canvas_{}'.format(i)], 0, 0, 1, 1)
            self.thumbnails.append(self.__dict__['canvas_{}'.format(i)])

        self.label_big.hide()
        self.canvas_big = PlotCanvas(parent=self.frame_figure)
        self.gridLayout_15.addWidget(self.canvas_big, 0, 0, 1, 1)

        self.current_index = None
        for index, canvas in enumerate(self.thumbnails):

            canvas.mouseDoubleClickEvent = partial(self.plot_big, index)
            canvas.plot(data=self.data[index], title='small pic {}'.format(index+1), small=True)

        self.btn_detail.clicked.connect(self.pop_new_window)

    def pop_new_window(self):
        '''在这里弹出窗口'''
        if self.current_index is None:
            return
        n = MainApp(df_ls=self.data, title='Pop Window {}'.format(self.current_index + 1))  # 传入新的 12 数据，这里暂时先传入旧的数据
        n.show()

    def plot_big(self, index, e):
        '''画大图'''
        self.current_index = index
        print('clicked', index)
        df = self.data[index]
        self.canvas_big.plot(data=df, title='big pic {}'.format(index+1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    df_ls = []
    # -------------------------------------------------
    # csv_ls = [os.path.join(base_dir, 'data', 'Data.csv') for i in range(12)]  # 12 个 csv 文件
    csv_ls = [
        os.path.join(base_dir, 'data', 'MINIST_01.csv'),
        os.path.join(base_dir, 'data', 'MINIST_02.csv'),
        os.path.join(base_dir, 'data', 'MINIST_03.csv'),
        os.path.join(base_dir, 'data', 'MINIST_04.csv'),
        os.path.join(base_dir, 'data', 'MINIST_05.csv'),
        os.path.join(base_dir, 'data', 'MINIST_06.csv'),
        os.path.join(base_dir, 'data', 'MINIST_01.csv'),
        os.path.join(base_dir, 'data', 'MINIST_01.csv'),
        os.path.join(base_dir, 'data', 'MINIST_01.csv'),
        os.path.join(base_dir, 'data', 'MINIST_01.csv'),
        os.path.join(base_dir, 'data', 'MINIST_01.csv'),
        os.path.join(base_dir, 'data', 'MINIST_01.csv'),
    ]
    # -------------------------------------------------
    for csv_file in csv_ls:
        df = pd.read_csv(csv_file, header=0, names=['x', 'y'])
        df_ls.append(df)
    m = MainApp(df_ls=df_ls)
    m.show()
    sys.exit(app.exec_())