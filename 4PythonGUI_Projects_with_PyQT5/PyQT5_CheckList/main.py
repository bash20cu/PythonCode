from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem
from PyQt5.uic import loadUi
import sys



# Creacion de la clase principal

class Main(QMainWindow):
  def __init__(self):
    super(Main,self).__init__()
    loadUi("main.ui",self)
    todos = ["walk dog", "buy groceries"]
    for todo in todos:
      item = QListWidgetItem(todo)
      self.todo_listWidget.addItem(todo)
    
    
    
if __name__ == '__main__':
  app = QApplication(sys.argv)
  window = Main()
  window.show()
  app.exec_()