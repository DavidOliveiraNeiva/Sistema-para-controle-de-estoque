from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
import sys

app = QApplication(sys.argv)

# Abrir o arquivo .ui
ui_file = QFile("projeto_ui.ui")
ui_file.open(QFile.ReadOnly)

# Carregar a interface
loader = QUiLoader()
janela = loader.load(ui_file)
ui_file.close()

janela.show()
sys.exit(app.exec_())

#git status
#git add .
#git commit -m "teste" #adicionar uma descrição da alteração
#it push origin main