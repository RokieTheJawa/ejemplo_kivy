import kivy

from kivy.config import Config
Config.set('graphics', 'height', '300')
Config.set('graphics', 'width', '300')
Config.write()

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


def on_text1(instance, value):
    print('The widget', instance, 'have:', value)

def on_text2(instance, value):
    print('The widget', instance, 'have:', value)
 
# Boxlayout is the App class
class BoxLayoutDemo(App):

    def build(self):
        self.title = 'Suma de dos numeros'
        
        superBox= BoxLayout(orientation='vertical', size_hint_x= None,padding=( 10, 0, 0, 10))
        l1 = Label(text='Valor uno',halign='left', size_hint=(None,None),size= (75, 40))
        l1.bind(size=l1.setter('texture_size'))    
        
        self.textinput1 = TextInput(size_hint=(None,None),size= (175, 50))
        self.textinput1.bind(text=on_text1)
        
        l2 = Label(text='Valor dos',halign='left', size_hint=(None,None),size= (75, 40))
        l2.bind(size=l2.setter('texture_size')) 
        
        self.textinput2 = TextInput(size_hint=(None,None),size= (175, 50))
        self.textinput2.bind(text=on_text2)

        button1= Button(text="Sumar",size_hint=(None,None),size= (75, 50))
        button1.bind(on_press=self.buttonClicked)
        

        self.l3 = Label(text='Resultado',halign='left', size_hint=(None,None),size= (280, 40))
        self.l3.bind(size=self.l3.setter('texture_size'))

        superBox.add_widget(l1)
        superBox.add_widget(self.textinput1)
        superBox.add_widget(l2)
        superBox.add_widget(self.textinput2)
        superBox.add_widget(button1)
        
        superBox.add_widget(self.l3)
     

        return superBox

    def buttonClicked(self,btn):
        try:
         valor1=float(self.textinput1.text)
         valor2=float(self.textinput2.text)
         valor3=valor1+valor2
         self.l3.text="{}+{}={}".format(valor1,valor2,valor3)
        except:
         self.l3.text="Se introdujeron datos erroneos!!"   

# Instantiate and run the kivy app

if __name__ == '__main__':

    BoxLayoutDemo().run()