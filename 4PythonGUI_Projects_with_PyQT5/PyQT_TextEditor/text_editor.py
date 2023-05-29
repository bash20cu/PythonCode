from PyQt5.QtWidgets import QMainWindow,QFileDialog
from PyQt5.uic import loadUi
import os

class TextEditor(QMainWindow):
    def __init__(self):
        super(TextEditor, self).__init__()
        loadUi("main.ui", self)
        self.current_path = None
        
        self.actionNew.triggered.connect(self.newFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_As.triggered.connect(self.saveFileAs)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionCut.triggered.connect(self.cut)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)

    def newFile(self):
        self.textEdit.clear()
        self.setWindowTitle("Untitled")
        self.current_path = None

    def saveFileAs(self):
        root_path = os.path.dirname(os.path.abspath(__file__))
        default_path = os.path.join(root_path, "output.txt")
        
        pathname, _ = QFileDialog.getSaveFileName(self, 'Save file', default_path, 'Text files (*.txt)')
        if pathname:
            filetext = self.textEdit.toPlainText()
            with open(pathname[0], 'w') as f:
                f.write(filetext)
            self.current_path = pathname[0]
            self.setWindowTitle(pathname[0])

    def saveFile(self):
        if self.current_path:
            filetext = self.textEdit.toPlainText()
            with open(self.current_path, 'w') as f:
                f.write(filetext)
        else:
            self.saveFileAs()

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'D:\codefirst.io\PyQt5 Text Editor', 'Text files (*.txt)')
        self.setWindowTitle(fname[0])
        with open(fname[0], 'r') as f:
            filetext = f.read()
            self.textEdit.setText(filetext)
        self.current_path = fname[0]

    def undo(self):
        self.textEdit.undo()

    def redo(self):
        self.textEdit.redo()

    def copy(self):
        self.textEdit.copy()

    def cut(self):
        self.textEdit.cut()

    def paste(self):
        self.textEdit.paste()