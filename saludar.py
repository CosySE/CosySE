from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

class Saludar (App):
    def build(self):
        self.ventana = GridLayout()
        self.ventana.cols = 1
        self.ventana.size_hint=(0.5 , 0.4)
        self.ventana.pos_hint ={'center_x':0.5,'center_y':0.5}
        #insertando imagen
        self.ventana.add_widget(Image(source='python.png'))
        #insertando el label
        self.saludo = Label(
                            text='Python te va a saludar Escribe tu Nombre',
                            color= '#4d8cf5',
                            font_size = 24
                            )
        self.ventana.add_widget(self.saludo)
        #insertando text input
        self.usuario = TextInput(
                                multiline=False,
                                padding_y = (10,10),
                                size_hint =(1,0.9)
                                )
        self.ventana.add_widget(self.usuario)
        #insertando boton
        self.boton = Button(
                        text='Saludate',
                        size_hint=(1,0.9),
                        bold = True,
                        background_color = '#4d8cf5'
                        )
        self.boton.bind(on_press = self.saludate)
        self.ventana.add_widget(self.boton)
        return self.ventana
    def saludate(self,instancia):
        self.saludo.text = 'Hola  ' + self.usuario.text + '  Python te saluda'

    
if __name__=='__main__':
    Saludar().run()