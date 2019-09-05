from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QLineEdit, QMessageBox, QDesktopWidget, QSizePolicy, QDateEdit, QTimeEdit, QWidget
from functools import partial
from datetime import date, time, datetime

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import random
import os

import pandas as pd

integer_reg = QRegExp('[0-9]*')
float_reg = QRegExp('[0-9]+.?[0-9]{,2}')
base_dir = os.path.abspath(os.path.dirname(__file__))


def dateUpdate(w: QDateEdit, var_name: str, m):
    if not isinstance(w, QDateEdit):
        raise TypeError
    if not isinstance(var_name, str):
        raise TypeError
    try:
        if var_name not in m.__dict__:
            raise ValueError
    except AttributeError:
        raise
    m.__dict__[var_name] = date(
        year=w.date().year(),
        month=w.date().month(),
        day=w.date().day(),
    )
    print(m.__dict__[var_name])


def timeUpdate(w: QTimeEdit, var_name: str, m):
    if not isinstance(w, QTimeEdit):
        raise TypeError
    if not isinstance(var_name, str):
        raise TypeError
    try:
        if var_name not in m.__dict__:
            raise ValueError
    except AttributeError:
        raise
    m.__dict__[var_name] = time(
        hour=w.time().hour(),
        minute=w.time().minute(),
        second=w.time().second(),
    )
    print(m.__dict__[var_name])


class AbstractWithSpecialFunctions:

    def validate_int_input(self, w: QLineEdit):
        if not isinstance(w, QLineEdit):
            raise TypeError
        validator = QRegExpValidator(integer_reg, w)
        w.setValidator(validator)

    def validate_float_input(self, w: QLineEdit):
        if not isinstance(w, QLineEdit):
            raise TypeError
        validator = QRegExpValidator(float_reg, w)
        w.setValidator(validator)

    def batch_set_int_validator(self, ls: [QLineEdit,]):
        for w in ls:
            self.validate_int_input(w)

    def batch_set_float_validator(self, ls: [QLineEdit,]):
        for w in ls:
            self.validate_float_input(w)

    def move_to_center(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def bind_edit_to_var(self, e: QLineEdit, v: str, f):
        '''bind line_edit to a variable'''
        if f not in [int, float, str, dateUpdate, timeUpdate]:
            raise TypeError('only float/int/str is allowed')
        # if not isinstance(e, (QLineEdit, QDateEdit, QTimeEdit)):
        #     raise TypeError('only QLineEdit object allowed')
        if not isinstance(v, str):
            raise TypeError
        if v in self.__dict__:
            pass
        else:
            self.__dict__[v] = None
        if isinstance(e, QLineEdit):
            e.textChanged.connect(partial(self.__update_var, e, v, f))
        elif isinstance(e, QDateEdit):
            e.dateChanged.connect(partial(self.__update_var, e, v, f))
        elif isinstance(e, QTimeEdit):
            e.timeChanged.connect(partial(self.__update_var, e, v, f))
        else:
            raise TypeError('Not Supported {} Object'.format(e.__class__.__name__))

    def __update_var(self, e: QLineEdit, v, f):
        print('Editing', e, v, f.__name__, e.text())
        if not isinstance(e, QLineEdit):
            if isinstance(e, (QDateEdit, QTimeEdit)):
                return f(e, v, self)
            else:
                return
        if f not in [str, int, float]:
            return
        if v not in self.__dict__:
            return
        if f == int:
            try:
                self.__dict__[v] = int(e.text())
            except (TypeError, ValueError):
                self.__dict__[v] = None
        elif f == float:
            try:
                self.__dict__[v] = float(e.text())
            except (ValueError, TypeError):
                self.__dict__[v] = None
        elif f == str:
            self.__dict__[v] = e.text().strip()
            if not self.__dict__[v]:
                self.__dict__[v] = None

    def check_values(self, data_to_check: dict = None):
        '''check and find out those None Values
        parameters = {
            '日期': "tab3_var_date",
            '时间': "tab3_var_time",

        }

        '''
        if data_to_check is None:
            return
        results = []
        for k, v in data_to_check.items():

            if v not in self.__dict__:
                raise KeyError('{} is not attribute of {}'.format(k, self.__class__.__name__))
            if self.__dict__[v] is None:
                results.append(k)
        return results

    def show_warn_message(self, message: str, title='警告', parent=None):
        return warn_message(parent=parent, message=message, title=title)


def warn_message(parent, message, title='警告'):
    reply = QMessageBox.warning(parent, title, message, QMessageBox.Yes|QMessageBox.No)
    if reply == QMessageBox.Yes:
        return True
    else:
        return False


# # support chinese
# font_common = FontProperties(
#     fname=os.path.join(base_dir, 'fonts', 'STHeiti-Light-3.ttc'), size=12
# )
# font_title = FontProperties(
#     fname=os.path.join(base_dir, 'fonts', 'STHeiti-Medium-4.ttc'), size=14
# )
#
# font_small = FontProperties(
#     fname=os.path.join(base_dir, 'fonts', 'STHeiti-Light-3.ttc'), size=8
# )

plt.rcParams['axes.unicode_minus'] = False


class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi, tight_layout=True)
        self.ax = self.fig.add_subplot(111)

        super().__init__(figure=self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(
            self,
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        FigureCanvas.updateGeometry(self)

    def plot(self, data: pd.DataFrame, title=None, x_label=None, y_label=None, small=None):
        if not isinstance(data, pd.DataFrame):
            raise TypeError

        self.ax.cla()

        self.ax.scatter(data['x'], data['y'], alpha=0.5)

        # if small:
        #     font_cap = font_small
        #     font_content = font_small
        # else:
        #     font_cap = font_title
        #     font_content = font_common

        if title:
            self.ax.set_title(title, ) # fontproperties=font_cap

        if x_label:
            self.ax.set_xlabel(x_label, ) # fontproperties=font_content
        if y_label:
            self.ax.set_ylabel(y_label, ) # fontproperties=font_content
        try:
            self.draw()
        except IndexError:
            pass

    def clear(self):
        self.ax.cla()

        self.draw()


