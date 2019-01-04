import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
import minecart
from collections import deque


class App(QWidget):

    """

    For App class, it will pop up the filepicker window for users to select the files they want to separate

    For version 1.0.0, it can slice the pdf file and separate them based on basic shapes' color.

    """

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # self.openFileNameDialog()
        # self.openFileNamesDialog()
        self.saveFileDialog()
        self.show()

    def saveFileDialog(self):
        """
        Two modules are used to create and detect the pdfs
        Minecraft module: detect the color on each pdf page. more info can be foudn on Pypi.
        Warning: Minecraft didn't pass the unit test. High risk
        Pypdf2: PDF generator tools--more mature and developed
        """
        # return a tuple
        fileName, _filter = QFileDialog.getOpenFileName(self, "Open File")
        pdffile = PdfFileReader(open(fileName, "rb"))
        document = minecart.Document(open(fileName, "rb"))
        # Algorithm longest substring, use a queue to keep track of the same type of pages and store their indices. When the next page is not
        # the same type, queue will be emptied and pdf file will be created based on their indices
        queue = deque()
        for i in range(pdffile.getNumPages()):
            page = document.get_page(i)
            currentcolors = 0
            for shape in page.shapes:
                if shape.fill:
                    print(shape.fill.color.as_rgb())
                    if shape.fill.color.as_rgb() not in [(0, 0, 0), (1, 1, 1), [0, 0, 0], [1, 1, 1]]:
                        currentcolors = 1
            if i == 0:
                previouscolors = currentcolors
                queue.append(i)
            else:
                print(currentcolors, previouscolors)
                if previouscolors == currentcolors and i != pdffile.getNumPages()-1:
                    queue.append(i)
                else:
                    output = PdfFileWriter()
                    while(queue):
                        output.addPage(pdffile.getPage(queue.popleft()))
                    if previouscolors == 1:
                        with open("ColorDocument%s.pdf" % i, "wb") as outputStream:
                            output.write(outputStream)
                    else:
                        with open("blackwhitedocument%s.pdf" % i, "wb") as outputStream:
                            output.write(outputStream)
                    previouscolors = currentcolors
                    queue.append(i)
        while(queue):
            output.addPage(pdffile.getPage(queue.popleft()))
            with open("Document_last.pdf", "wb") as outputStream:
                output.write(outputStream)

        """
        pdffile = PdfFileReader(open(fileName, "rb"))
        for i in range(pdffile.numPages):
            output = PdfFileWriter()
            output.addPage(pdffile.getPage(i))
            with open("document-page%s.pdf" % i, "wb") as outputStream:
                output.write(outputStream)
"""
