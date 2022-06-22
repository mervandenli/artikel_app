import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.QtGui import QIcon
import pandas as pd

df = pd.read_csv("words.csv")

class artikelApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(artikelApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.input_box.returnPressed.connect(self.search_word)
        self.ui.search_btn.clicked.connect(self.search_word)
        

    def search_word(self):
        sender = self.sender().text()

        searching_word = self.ui.input_box.text().capitalize()
        
        df.dropna(inplace = True)
        def word_find(lemma):
            if searching_word == lemma:
                return True
            return False
        
        finding_word = df[df["lemma"].apply(word_find)].head(11)
        typ = finding_word["Typ"].to_list()
        wort_form = finding_word["Wortform"].to_list()
        wort_dict = dict(zip(typ, wort_form))

        for i in wort_dict:
            if i == "nominativ singular":
                raw_word = wort_dict["nominativ singular"]
                if wort_dict["genus"] == "f":
                    artikel_type = "die"
                elif wort_dict["genus"] == "m":
                    artikel_type = "der"
                elif wort_dict["genus"] == "n":
                    artikel_type = "das"
                self.ui.nominativ_singular.setText(artikel_type +' '+ raw_word)
            elif i == "nominativ plural":
                raw_word = wort_dict["nominativ plural"]
                if wort_dict["genus"] == "f":
                    artikel_type = "die"
                elif wort_dict["genus"] == "m":
                    artikel_type = "die"
                elif wort_dict["genus"] == "n":
                    artikel_type = "die"
                self.ui.nominativ_plural.setText(artikel_type +' '+ raw_word)
            elif i == "genitiv singular":
                raw_word = wort_dict["genitiv singular"]
                if wort_dict["genus"] == "f":
                    artikel_type = "der"
                elif wort_dict["genus"] == "m":
                    artikel_type = "des"
                elif wort_dict["genus"] == "n":
                    artikel_type = "des"
                self.ui.genitiv_singular.setText(artikel_type +' '+ raw_word)
            elif i == "genitiv plural":
                raw_word = wort_dict["genitiv plural"]
                if wort_dict["genus"] == "f":
                    artikel_type = "der"
                elif wort_dict["genus"] == "m":
                    artikel_type = "der"
                elif wort_dict["genus"] == "n":
                    artikel_type = "der"
                self.ui.genitiv_plural.setText(artikel_type +' '+ raw_word)
            elif i == "dativ singular":
                raw_word = wort_dict["dativ singular"]
                if wort_dict["genus"] == "f":
                    artikel_type = "der"
                elif wort_dict["genus"] == "m":
                    artikel_type = "dem"
                elif wort_dict["genus"] == "n":
                    artikel_type = "dem"
                self.ui.dativ_singular.setText(artikel_type +' '+ raw_word)
            elif i == "dativ plural":
                raw_word = wort_dict["dativ plural"]
                if wort_dict["genus"] == "f":
                    artikel_type = "den"
                elif wort_dict["genus"] == "m":
                    artikel_type = "den"
                elif wort_dict["genus"] == "n":
                    artikel_type = "den"
                self.ui.dativ_plural.setText(artikel_type +' '+ raw_word)
            elif i == "akkusativ singular":
                raw_word = wort_dict["akkusativ singular"]
                if wort_dict["genus"] == "f":
                    artikel_type = "die"
                elif wort_dict["genus"] == "m":
                    artikel_type = "den"
                elif wort_dict["genus"] == "n":
                    artikel_type = "das"
                self.ui.akkusativ_singular.setText(artikel_type +' '+ raw_word)
            elif i == "akkusativ plural":
                raw_word = wort_dict["akkusativ plural"]
                if wort_dict["genus"] == "f":
                    artikel_type = "die"
                elif wort_dict["genus"] == "m":
                    artikel_type = "die"
                elif wort_dict["genus"] == "n":
                    artikel_type = "die"
                self.ui.akkusativ_plural.setText(artikel_type +' '+ raw_word)
            
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = artikelApp()
    win.show()
    sys.exit(app.exec_())


app()
