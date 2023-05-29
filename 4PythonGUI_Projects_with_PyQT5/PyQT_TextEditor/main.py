from PyQt5.QtWidgets import QApplication
from text_editor import TextEditor
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = TextEditor()
    ui.show()
    sys.exit(app.exec_())
