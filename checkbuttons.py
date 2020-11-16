import kivy

from kivy.config import Config
Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '450')
Config.write()

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton


def on_text1(instance, value):
    print('The widget', instance, 'have:', value)

def on_text2(instance, value):
    print('The widget', instance, 'have:', value)
 
# Boxlayout is the App class
class BoxLayoutDemo(App):

    def build(self):
        self.title = 'Calculadora'
        
        superBox= BoxLayout(orientation='vertical', size_hint_x= None,padding=( 10, 0, 0, 10))
        caja1 = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        caja2 = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        caja3 = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        caja4 = GridLayout(cols=2, row_force_default=True, row_default_height=40)
        l1 = Label(text='Valor uno',halign='left', size_hint=(None,None),size= (75, 40))
        l1.bind(size=l1.setter('texture_size'))    
        
        self.textinput1 = TextInput(size_hint=(None,None),size= (175, 50))
        self.textinput1.bind(text=on_text1)
        
        l2 = Label(text='Valor dos',halign='left', size_hint=(None,None),size= (75, 40))
        l2.bind(size=l2.setter('texture_size')) 
        
        self.etiqueta1=Label(text='Sumar',size_hint=(None,None),size= (75, 40))
        self.check1 = CheckBox(size_hint=(None,None),size= (75, 40))
        
        self.etiqueta2=Label(text='Restar',size_hint=(None,None),size= (75, 40))
        self.check2 = CheckBox(size_hint=(None,None),size= (75, 40))

        self.etiqueta3=Label(text='Multiplicar',size_hint=(None,None),size= (75, 40))
        self.check3 = CheckBox(size_hint=(None,None),size= (75, 40))

        self.etiqueta4=Label(text='Dividir',size_hint=(None,None),size= (75, 40))
        self.check4 = CheckBox(size_hint=(None,None),size= (75, 40))

        self.textinput2 = TextInput(size_hint=(None,None),size= (175, 50))
        self.textinput2.bind(text=on_text2)


        button1= Button(text="Ejecutar",size_hint=(None,None),size= (75, 50))
        button1.bind(on_press=self.buttonClicked)
        

        self.l3 = Label(text='Resultado',halign='left', size_hint=(None,None),size= (280, 80))
        self.l3.bind(size=self.l3.setter('texture_size'))

        superBox.add_widget(l1)
        superBox.add_widget(self.textinput1)
        superBox.add_widget(l2)
        superBox.add_widget(self.textinput2)

        caja1.add_widget(self.etiqueta1)
        caja1.add_widget(self.check1)
        caja2.add_widget(self.etiqueta2)
        caja2.add_widget(self.check2)
        caja3.add_widget(self.etiqueta3)
        caja3.add_widget(self.check3)
        caja4.add_widget(self.etiqueta4)
        caja4.add_widget(self.check4)

        superBox.add_widget(caja1)
        superBox.add_widget(caja2)
        superBox.add_widget(caja3)
        superBox.add_widget(caja4)

        superBox.add_widget(button1)
        
        superBox.add_widget(self.l3)
     

        return superBox

    def buttonClicked(self,btn):
        try:
         s=""   
         valor1=float(self.textinput1.text)
         valor2=float(self.textinput2.text)
         if self.check1.active:
          valor3=valor1+valor2
          s="{}{}+{}={}\n".format(s,valor1,valor2,valor3)
         if self.check2.active:
          valor3=valor1-valor2
          s="{}{}-{}={}\n".format(s,valor1,valor2,valor3)
         if self.check3.active:
          valor3=valor1*valor2
          s="{}{}x{}={}\n".format(s,valor1,valor2,valor3)
         if self.check2.active:
          valor3=valor1/valor2
          s="{}{}÷{}={}".format(s,valor1,valor2,valor3)

         self.l3.text=s 
        except:
         self.l3.text="Se introducioeron datos erroneos!!";   

    
   

 

# Instantiate and run the kivy app

if __name__ == '__main__':

    BoxLayoutDemo().run()