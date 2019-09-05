# -*- coding:utf-8 -*-
'''
Umap_Dimension_Reduction
'''
__author__ = 'Xiuxian Li'

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.figure import Figure
import numpy as np
import UmapGUI

import numpy as np
from sklearn.datasets import load_iris, load_digits
from sklearn.model_selection import train_test_split
import seaborn as sns
import pandas as pd
import umap


class Umapx(QMainWindow):
    def __init__(self, parent=None):
        super(Umapx, self).__init__(parent)
        self.ui = UmapGUI.Ui_Umap()
        self.ui.setupUi(self)

        self._static_ax0 = self.ui.GV.figure.subplots()
        self._static_ax11 = self.ui.GV11.figure.subplots()
        self._static_ax12 = self.ui.GV12.figure.subplots()
        self._static_ax13 = self.ui.GV13.figure.subplots()
        self._static_ax21 = self.ui.GV21.figure.subplots()
        self._static_ax22 = self.ui.GV22.figure.subplots()
        self._static_ax23 = self.ui.GV23.figure.subplots()
        self._static_ax31 = self.ui.GV31.figure.subplots()
        self._static_ax32 = self.ui.GV32.figure.subplots()
        self._static_ax33 = self.ui.GV33.figure.subplots()

        self.ui.MD1.valueChanged.connect(self.MD1Fun)
        self.ui.MD2.valueChanged.connect(self.MD2Fun)
        self.ui.MD3.valueChanged.connect(self.MD3Fun)
        self.ui.NN1.valueChanged.connect(self.NN1Fun)
        self.ui.NN2.valueChanged.connect(self.NN2Fun)
        self.ui.NN3.valueChanged.connect(self.NN3Fun)

        self.ui.GV11.figure.canvas.mpl_connect('button_press_event', self.M11)
        self.ui.GV12.figure.canvas.mpl_connect('button_press_event', self.M12)
        self.ui.GV13.figure.canvas.mpl_connect('button_press_event', self.M13)
        self.ui.GV21.figure.canvas.mpl_connect('button_press_event', self.M21)
        self.ui.GV22.figure.canvas.mpl_connect('button_press_event', self.M22)
        self.ui.GV23.figure.canvas.mpl_connect('button_press_event', self.M23)
        self.ui.GV31.figure.canvas.mpl_connect('button_press_event', self.M31)
        self.ui.GV32.figure.canvas.mpl_connect('button_press_event', self.M32)
        self.ui.GV33.figure.canvas.mpl_connect('button_press_event', self.M33)

        iris = load_iris()

        reducer = umap.UMAP(n_neighbors=self.ui.NN1.value(), min_dist=self.ui.MD1.value())
        embedding11 = reducer.fit_transform(iris.data)
        self._static_ax11.scatter(embedding11[:, 0], embedding11[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN1.value(), min_dist=self.ui.MD2.value())
        embedding12 = reducer.fit_transform(iris.data)
        self._static_ax12.scatter(embedding12[:, 0], embedding12[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN1.value(), min_dist=self.ui.MD3.value())
        embedding13 = reducer.fit_transform(iris.data)
        self._static_ax13.scatter(embedding13[:, 0], embedding13[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)
        reducer = umap.UMAP(n_neighbors=self.ui.NN2.value(), min_dist=self.ui.MD1.value())
        embedding21 = reducer.fit_transform(iris.data)
        self._static_ax21.scatter(embedding21[:, 0], embedding21[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN2.value(), min_dist=self.ui.MD2.value())
        embedding22 = reducer.fit_transform(iris.data)
        self._static_ax22.scatter(embedding22[:, 0], embedding22[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN2.value(), min_dist=self.ui.MD3.value())
        embedding23 = reducer.fit_transform(iris.data)
        self._static_ax23.scatter(embedding23[:, 0], embedding23[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)
        reducer = umap.UMAP(n_neighbors=self.ui.NN3.value(), min_dist=self.ui.MD1.value())
        embedding31 = reducer.fit_transform(iris.data)
        self._static_ax31.scatter(embedding31[:, 0], embedding31[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN3.value(), min_dist=self.ui.MD2.value())
        embedding32 = reducer.fit_transform(iris.data)
        self._static_ax32.scatter(embedding32[:, 0], embedding32[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN3.value(), min_dist=self.ui.MD3.value())
        embedding33 = reducer.fit_transform(iris.data)
        self._static_ax33.scatter(embedding33[:, 0], embedding33[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

    def MD1Fun(self):
        iris = load_iris()
        self._static_ax11.clear()
        self._static_ax21.clear()
        self._static_ax31.clear()

        reducer = umap.UMAP(n_neighbors=self.ui.NN1.value(), min_dist=self.ui.MD1.value())
        embedding11 = reducer.fit_transform(iris.data)
        self._static_ax11.scatter(embedding11[:, 0], embedding11[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN2.value(), min_dist=self.ui.MD1.value())
        embedding21 = reducer.fit_transform(iris.data)
        self._static_ax21.scatter(embedding21[:, 0], embedding21[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN3.value(), min_dist=self.ui.MD1.value())
        embedding31 = reducer.fit_transform(iris.data)
        self._static_ax31.scatter(embedding31[:, 0], embedding31[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

    def MD2Fun(self):
        iris = load_iris()
        self._static_ax12.clear()
        self._static_ax22.clear()
        self._static_ax32.clear()

        reducer = umap.UMAP(n_neighbors=self.ui.NN1.value(), min_dist=self.ui.MD2.value())
        embedding12 = reducer.fit_transform(iris.data)
        self._static_ax12.scatter(embedding12[:, 0], embedding12[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN2.value(), min_dist=self.ui.MD2.value())
        embedding22 = reducer.fit_transform(iris.data)
        self._static_ax22.scatter(embedding22[:, 0], embedding22[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN3.value(), min_dist=self.ui.MD2.value())
        embedding23 = reducer.fit_transform(iris.data)
        self._static_ax32.scatter(embedding23[:, 0], embedding23[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

    def MD3Fun(self):
        iris = load_iris()
        self._static_ax31.clear()
        self._static_ax32.clear()
        self._static_ax33.clear()

        reducer = umap.UMAP(n_neighbors=self.ui.NN1.value(), min_dist=self.ui.MD3.value())
        embedding31 = reducer.fit_transform(iris.data)
        self._static_ax31.scatter(embedding31[:, 0], embedding31[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN2.value(), min_dist=self.ui.MD3.value())
        embedding32 = reducer.fit_transform(iris.data)
        self._static_ax32.scatter(embedding32[:, 0], embedding32[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN3.value(), min_dist=self.ui.MD3.value())
        embedding33 = reducer.fit_transform(iris.data)
        self._static_ax33.scatter(embedding33[:, 0], embedding33[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

    def NN1Fun(self):
        iris = load_iris()
        self._static_ax11.clear()
        self._static_ax12.clear()
        self._static_ax13.clear()

        reducer = umap.UMAP(n_neighbors=self.ui.NN1.value(), min_dist=self.ui.MD1.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax11.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN1.value(), min_dist=self.ui.MD2.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax12.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN1.value(), min_dist=self.ui.MD3.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax13.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

    def NN2Fun(self):
        iris = load_iris()
        self._static_ax21.clear()
        self._static_ax22.clear()
        self._static_ax23.clear()

        reducer = umap.UMAP(n_neighbors=self.ui.NN2.value(), min_dist=self.ui.MD1.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax21.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN2.value(), min_dist=self.ui.MD2.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax22.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN2.value(), min_dist=self.ui.MD3.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax23.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

    def NN3Fun(self):
        iris = load_iris()
        self._static_ax31.clear()
        self._static_ax32.clear()
        self._static_ax33.clear()

        reducer = umap.UMAP(n_neighbors=self.ui.NN3.value(), min_dist=self.ui.MD1.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax31.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN2.value(), min_dist=self.ui.MD2.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax32.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

        reducer = umap.UMAP(n_neighbors=self.ui.NN3.value(), min_dist=self.ui.MD3.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax33.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                  s=0.1)

    def M11(self, event):
        iris = load_iris()
        self._static_ax0.clear()
        self._static_ax11.clear()

        reducer = umap.UMAP(n_neighbors=self.ui.NN1.value(), min_dist=self.ui.MD1.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax0.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=1)
        self._static_ax11.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=0.3)

    def M12(self, event):
        iris = load_iris()
        self._static_ax0.clear()
        self._static_ax12.clear()

        reducer = umap.UMAP(n_neighbors=self.ui.NN1.value(), min_dist=self.ui.MD2.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax0.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=1)
        self._static_ax12.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=0.3)

    def M13(self, event):
        iris = load_iris()
        self._static_ax0.clear()
        self._static_ax13.clear()

        reducer = umap.UMAP(n_neighbors=self.ui.NN1.value(), min_dist=self.ui.MD3.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax0.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=1)
        self._static_ax13.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=0.3)

    def M21(self, event):
        iris = load_iris()
        self._static_ax0.clear()
        self._static_ax21.clear()

        reducer = umap.UMAP(n_neighbors=self.ui.NN2.value(), min_dist=self.ui.MD1.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax0.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=1)
        self._static_ax21.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=0.3)

    def M22(self, event):
        iris = load_iris()
        self._static_ax0.clear()
        self._static_ax22.clear()
        reducer = umap.UMAP(n_neighbors=self.ui.NN1.value(), min_dist=self.ui.MD2.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax0.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=1)
        self._static_ax22.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=0.3)

    def M23(self, event):
        iris = load_iris()
        self._static_ax0.clear()
        self._static_ax23.clear()
        reducer = umap.UMAP(n_neighbors=self.ui.NN2.value(), min_dist=self.ui.MD3.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax0.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=1)
        self._static_ax23.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=0.3)

    def M31(self, event):
        iris = load_iris()
        self._static_ax0.clear()
        self._static_ax31.clear()

        reducer = umap.UMAP(n_neighbors=self.ui.NN3.value(), min_dist=self.ui.MD1.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax0.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=1)
        self._static_ax31.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=0.3)

    def M32(self, event):
        iris = load_iris()
        self._static_ax0.clear()
        self._static_ax32.clear()

        reducer = umap.UMAP(n_neighbors=self.ui.NN3.value(), min_dist=self.ui.MD2.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax0.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=1)
        self._static_ax32.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=0.3)

    def M33(self, event):
        iris = load_iris()
        self._static_ax0.clear()
        self._static_ax33.clear()

        reducer = umap.UMAP(n_neighbors=self.ui.NN3.value(), min_dist=self.ui.MD3.value())
        embedding = reducer.fit_transform(iris.data)
        self._static_ax0.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=1)
        self._static_ax33.scatter(embedding[:, 0], embedding[:, 1], c=[sns.color_palette()[x] for x in iris.target],
                                 s=0.3)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    form = Umapx()
    form.show()
    sys.exit(app.exec_())