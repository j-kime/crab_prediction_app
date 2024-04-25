from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from predictor import predict_age
import pandas as pd

# Required to run the homescreen
class HomeScreen(Screen):
    pass

# Required to create buttons out of images
class ImageButton(ButtonBehavior, Image):
    pass

# Required for the settings screen, incomplete
class SettingsScreen(Screen):
    pass

# Required to run the input screen that predicts the age of the crab
class InputScreen(Screen):
    pass


#This always stays at the end
GUI = Builder.load_file("TheCrab.kv")
class MainApp(App):
    def build(self):
        return GUI
    
    #This method is used to change from one screen to another
    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name

    # Used to pull the function out of the predictor file, current prints the answer to the console 
    def predict_ages(self, pred_list):
        predict_age(pd.read_csv("./Cleaned_train_df.csv"), pred_list)

    
MainApp().run()