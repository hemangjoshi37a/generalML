from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import os

class MainScreen(Screen):
    pass

class HowManyEx(Screen):
    pass

class GetMoreData(Screen):
    pass

class PredictCat(Screen):
    pass

class PredQuant(Screen):
    pass

class LabelData(Screen):
    pass

class NumCatK(Screen):
    pass

class Sample10K(Screen):
    pass

class Sample10K2(Screen):
    pass

class Sample10K3(Screen):
    pass

class Sample100K(Screen):
    pass

class Sample100K2(Screen):
    pass

class MShiftVBGMM(Screen):
    pass

class Error(Screen):
    pass

class LSVC(Screen):
    pass

class SGDC(Screen):
    pass

class TextData(Screen):
    pass

class KernelApprox(Screen):
    pass

class KNC(Screen):
    pass

class NaiveBayes(Screen):
    pass

class SVCEC(Screen):
    pass

class LLE(Screen):
    pass

class MiniBKM(Screen):
    pass

class KMean(Screen):
    pass

class SpectralClust(Screen):
    pass

class Visual(Screen):
    pass

class PredStrct(Screen):
    pass

class RandPCA(Screen):
    pass

class IsoSpectralEmbed(Screen):
    pass

class FewFeatIMP(Screen):
    pass

class LoadDialog(Screen):
        load = ObjectProperty(None)
        cancel = ObjectProperty(None)
    

class SGDR(Screen):
    pass

class RRSVR(Screen):
    pass

class SVRER(Screen):
    pass

class ElasticNetLasso(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass


presentation = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return presentation

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)
    

class MyWidget(BoxLayout):
    def open(self, path, filename):
        with open(os.path.join(path, filename[0])) as f:
            print (f.read())

    def selected(self, filename):
        print ("selected: %s" % filename[0])

#class LoadDialog(FloatLayout):
#    load = ObjectProperty(None)
#    cancel = ObjectProperty(None)
#    
class MyApp(App):
    def build(self):
        return MyWidget()
    


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            self.text_input.text = stream.read()
            return(self.text_input.text)

        self.dismiss_popup()

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()

class Editor(App):
    pass

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)

if __name__=="__main__":
    MainApp().run()
    

#hj=MainApp()
#hj.run()
        
#--------------------------Part : 4 : python file-----------------
#from kivy.app import App
#from kivy.uix.widget import Widget
#
#class Widgets(Widget):
#    pass
#
#class widgetssdx(App):
#    def build(self):
#        return Widgets()
#    
#
#hj=widgetssdx()
#hj.run()

#---------------------------Part : 4 : kv file-------------------
#<Widgets>
#	
#	Label:
#    	text : "How many training examples do you have??"
#    		
#	Button :
#		size : 190,35
#		pos : 0,0
#		text : "less than 50"
#		color : 0,1,0,1
#		font_size : 20
#		
#	Button :
#		size : 190,35
#		pos : 200,0
#		text : "more than 50"
#		color : 1,0,0,1
#		font_size : 20


#--------------------------Part : 5 : python file-----------------
#from kivy.app import App
#from kivy.uix.widget import Widget
#
#class Widgets(Widget):
#    pass
#
#class widgetssdx(App):
#    def build(self):
#        return Widgets()
#    
#
#hj=widgetssdx()
#hj.run()

#---------------------------Part : 5 : kv file-------------------
#<Button>:
#    font_size : 20    
#    size : 190,35
#    color : 0,1,0,1
#
#<Widgets>:	
#    Label:
#        text : "How many training examples do you have??"
#        pos : root.x+100 , root.top-self.height
#    		
#    Button :
#        pos : 0,0
#        text : "less than 50"
#		
#    Button :
#        pos : 250,0
#        text : "more than 50"
#


#--------------------------Part : 6 : python file-----------------
#from kivy.app import App
#from kivy.uix.widget import Widget
#from kivy.uix.floatlayout import FloatLayout
#
#
#class Widgets(Widget):
#    pass
#
#class widgetssdx(App):
#    def build(self):
#        return FloatLayout()
#
#hj=widgetssdx()
#hj.run()


#---------------------------Part : 6 : kv file-------------------
#<Button>:
#    font_size : 20    
#    color : 0,1,0,1
#    size_hint: 0.3,0.1
#
#<FloatLayout>:	
#    Label:
#        text : "How many training examples do you have??"
#        pos : root.x+100 , root.top-self.height
#    		
#    Button :
#        pos_hint : {"left":0 , 'top':1}
#        text : "less than 50"
#		
#    Button :
#        pos_hint : {"right":1 , 'top':1}
#        text : "more than 50"



#--------------------------Part : 7 : python file-----------------
#from kivy.app import App
#from kivy.uix.widget import Widget
#
#class TouchInput(Widget):
#    def on_touch_down(self,touch):
#        print(touch)    
#    def on_touch_move(self,touch):
#        print(touch)
#    def on_touch_up(self,touch):
#        print(touch)
#
#class widgetssdx(App):
#    def build(self):
#        return TouchInput()
#
#hj=widgetssdx()
#hj.run()
#---------------------------Part : 7 : kv file-------------------
#<Button>:
#    font_size : 20    
#    color : 0,1,0,1
#    size_hint: 0.3,0.1
#
#<FloatLayout>:	
#    Label:
#        text : "How many training examples do you have??"
#        pos : root.x+100 , root.top-self.height
#    		
#    Button :
#        pos_hint : {"left":0 , 'top':1}
#        text : "less than 50"
#		
#    Button :
#        pos_hint : {"right":1 , 'top':1}
#        text : "more than 50"

#------------------------------------
#<Button>:
#    font_size : 20    
#    color : 1,0,0,1
#    size_hint: 0.3,0.1
#    
#<Label>:
#    font_size : 25
#    color : 1,0,0,1
#    size_hint: 0.3,0.1