from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from random import randint as rr

from kivy.core.window import Window

Window.size = (600, 400)
Window.clearcolor = (100/255, 180/255, 150/255, 1)
Window.title = "Konvertor"

class Ilova(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text='Konvertor dasturi\nSonlarni kiriting!')
        self.tb = Label(text='Terabayt')
        self.gb = Label(text='Gigabayt')
        self.kb = Label(text='Kilobayt')
        self.input_data = TextInput(hint_text='qiymatni kiriting(mb)', multiline=False)
        self.input_data.bind(text=self.on_text)

    def on_text(self, *args):
        data = self.input_data.text
        if data.isnumeric():
            self.gb.text = 'Gigabayt: ' + str(float(data) / 1024)
            self.tb.text = 'Terabayt: ' + str(float(data) / (1024 * 1024))
            self.kb.text = 'Kilobayt: ' + str(float(data) * 1024)
        else:
            self.input_data = ''

    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.input_data)
        box.add_widget(self.kb)
        box.add_widget(self.gb)
        box.add_widget(self.tb)

        return box

if __name__ == "__main__":
    Ilova().run()