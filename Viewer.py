from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QWidget, QTabWidget
from PyQt5.QtWidgets import QLabel, QTextEdit, QScrollArea

class Console(QWidget):
    def __init__(self):
        super().__init__()
        vblConsole = QVBoxLayout()
        self.setLayout(vblConsole)
        self.teConsole = QTextEdit()
        vblConsole.addWidget(self.teConsole)
    
    def text(self):
        return self.teConsole.toPlainText()
        
    def setText(self, txt):
        self.teConsole.setText(txt)

class Viewer(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setMaximumWidth(600)
        self.teStdin = Console()
        self.teStdout = Console()

        twStd = QTabWidget()
        twStd.addTab(self.teStdin, "stdin")
        twStd.addTab(self.teStdout, "stdout")
        twStd.setMaximumSize(600, 300)

        lbLists = [QLabel("Double"), QLabel("Int"), QLabel("Char"), QLabel("Calculator")]
        self.glMemory = QGridLayout()
        for idx, label in enumerate(lbLists):
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("QLabel{ background-color : yellow;}")
            self.glMemory.addWidget(label, 0, idx)

        wgMemory = QWidget()
        wgMemory.setLayout(self.glMemory)

        saMemory = QScrollArea()
        saMemory.setWidget(wgMemory)
        saMemory.setWidgetResizable(True)
        saMemory.setAlignment(Qt.AlignTop)

        vblViewer = QVBoxLayout()
        vblViewer.addWidget(twStd)
        vblViewer.addWidget(saMemory)
        self.memoryLayouts = []
        self.beforeMemory = [[], [], [], []]

        self.setLayout(vblViewer)
    
    def consistMemoryDisplay(self, memory, pointer):
        for typePointer in range(len(self.beforeMemory)):
            for memoryPointer in range(len(self.beforeMemory[typePointer])):
                widget = self.glMemory.itemAtPosition(memoryPointer + 1, typePointer).widget()
                widget.setParent(None)
                widget.deleteLater()

        for typePointer in range(len(memory)):
            for memoryPointer in range(len(memory[typePointer])):
                lbData = QLabel(memory[typePointer][memoryPointer])
                lbData.setAlignment(Qt.AlignCenter)
                if pointer == (typePointer, memoryPointer):
                    lbData.setStyleSheet("QLabel{ background-color : red;}")
                else:
                    if (typePointer + memoryPointer) % 2:
                        lbData.setStyleSheet("QLabel{ background-color : gray;}")
                    else:
                        lbData.setStyleSheet("QLabel{ background-color : white;}")
                
                self.glMemory.addWidget(lbData, memoryPointer + 1, typePointer)
        
        self.beforeMemory = memory
