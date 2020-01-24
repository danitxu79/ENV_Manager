import sys

import PyQt5.QtCore
from PyQt5.QtWidgets import (QApplication, QFileIconProvider, QFileSystemModel,
                             QTreeView)

app = QApplication(sys.argv)

PyQt5.QtCore.QCoreApplication.setApplicationVersion(PyQt5.QtCore.QT_VERSION_STR)
parser = PyQt5.QtCore.QCommandLineParser()
parser.setApplicationDescription("Qt Dir View Example")
parser.addHelpOption()
parser.addVersionOption()

dontUseCustomDirectoryIconsOption = PyQt5.QtCore.QCommandLineOption('c',
                                                                    "Set QFileIconProvider.DontUseCustomDirectoryIcons")
parser.addOption(dontUseCustomDirectoryIconsOption)
parser.addPositionalArgument('directory', "The directory to start in.")
parser.process(app)
try:
    rootPath = parser.positionalArguments().pop(0)
except IndexError:
    rootPath = None

model = QFileSystemModel()
model.setRootPath('')
if parser.isSet(dontUseCustomDirectoryIconsOption):
    model.iconProvider().setOptions(
        QFileIconProvider.DontUseCustomDirectoryIcons)
tree = QTreeView()
tree.setModel(model)
if rootPath is not None:
    rootIndex = model.index(PyQt5.QtCore.QDir.cleanPath(rootPath))
    if rootIndex.isValid():
        tree.setRootIndex(rootIndex)

# Demonstrating look and feel features.
tree.setAnimated(True)
tree.setIndentation(20)
tree.setSortingEnabled(True)

availableSize = QApplication.desktop().availableGeometry(tree).size()
tree.resize(availableSize / 2)
tree.setColumnWidth(0, tree.width() / 3)

tree.setWindowTitle("Dir View")
tree.show()

sys.exit(app.exec_())
