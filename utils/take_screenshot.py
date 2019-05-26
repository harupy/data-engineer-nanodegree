import os
import sys
import time
from PIL import ImageGrab

from PyQt5 import QtWidgets, QtCore, QtGui


class Screenshot(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()
    screen_width, screen_height = ImageGrab.grab().size
    self.setGeometry(0, 0, screen_width, screen_height)
    self.setWindowTitle(' ')
    self.begin = QtCore.QPoint()
    self.end = QtCore.QPoint()
    self.setWindowOpacity(0.3)
    QtWidgets.QApplication.setOverrideCursor(
      QtGui.QCursor(QtCore.Qt.CrossCursor)
    )
    self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    self.show()

  def paintEvent(self, event):
    qp = QtGui.QPainter(self)
    qp.setPen(QtGui.QPen(QtGui.QColor('black'), 1))
    qp.setBrush(QtGui.QColor(128, 128, 255, 128))
    qp.drawRect(QtCore.QRect(self.begin, self.end))

  def mousePressEvent(self, event):
    self.begin = event.pos()
    self.end = self.begin
    self.update()

  def mouseMoveEvent(self, event):
    self.end = event.pos()
    self.update()

  def mouseReleaseEvent(self, event):
    self.close()

  def get_captured_area(self):
    x1 = min(self.begin.x(), self.end.x())
    y1 = min(self.begin.y(), self.end.y())
    x2 = max(self.begin.x(), self.end.x())
    y2 = max(self.begin.y(), self.end.y())
    return x1, y1, x2, y2


if __name__ == '__main__':
  print('Waiting for 2 seconds')
  time.sleep(2)
  app = QtWidgets.QApplication(sys.argv)
  ss = Screenshot()
  ss.show()
  app.exec_()
  app.quit()
  x1, y1, x2, y2 = ss.get_captured_area()
  img = ImageGrab.grab(bbox=(2 * x1, 2 * y1, 2 * x2, 2 * y2))

  save_dir = 'notes/images'
  img_name = input('Save as: ')
  img_name = img_name if img_name else 'screenshot'
  img_name = img_name if img_name.endswith('.png') else img_name + '.png'
  save_path = os.path.join(save_dir, img_name)
  img.save(save_path)
  print('Done')
