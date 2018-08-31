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
    
