#aplicaccion procesar
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image



class analisisTexto (App):
    def build(self):
        self.grid = GridLayout()
        self.grid.cols = 1
        self.grid.pos_hint={'center_x':0.5,'center_y':0.5}
        self.grid.size_hint=(0.8 , 0.8)
        self.grid.add_widget(Image(source='python.png'))
        self.texto=Label(
                        text='Introduce un texto para procesar ',
                        font_size=22,
                        color='#4d8cf5'
                        )
        self.grid.add_widget(self.texto)
        self.cajadetexto=TextInput()
        self.grid.add_widget(self.cajadetexto)
        self.boton=Button(text='Procesar',color='#4d8cf5',font_size=18,bold=True,size_hint=(0.5,0.7))
        self.boton.bind(on_press=self.procesar)
        self.grid.add_widget(self.boton)
        self.texto1=Label(
                        text='Introduce un texto para procesar ',
                        font_size=22,
                        color='#4d8cf5'
                        )
        self.grid.add_widget(self.texto1)
        self.texto2=Label(
                        text='Introduce un texto para procesar ',
                        font_size=22,
                        color='#4d8cf5'
                        )
        self.grid.add_widget(self.texto2)
        self.texto3=Label(
                        text='Introduce un texto para procesar ',
                        font_size=22,
                        color='#4d8cf5'
                        )
        self.grid.add_widget(self.texto3)
        return self.grid
    def procesar(self,instancia):
        cantidad_gerundio = 0
        lista_repetidas = []
        diccionario={}
        lista = self.cajadetexto.text
        lista =lista.split()
        for llave in lista:
            diccionario[llave]= diccionario.get(llave,0)+1
        #print(diccionario)

        for k,v in diccionario.items():
            if v >=5:
                lista_repetidas.append(k)
        #print(lista_repetidas)
        for palabra in lista:
            if palabra.endswith('ando') or palabra.endswith('iendo'):
                cantidad_gerundio =cantidad_gerundio +1
        #print(cantidad_gerundio)
        self.texto1.text = 'Este texto tiene ' + str(len(lista))+ ' palabras'
        self.texto2.text = 'Las mas repetidas son ' + str(lista_repetidas)
        self.texto3.text = 'la cantidad de gerundios usados son  ' + str(cantidad_gerundio)
if __name__=='__main__':
    analisisTexto().run()