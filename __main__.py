#__main__
#inclem.net/pages/kivy-crash-course
#pythonprogramming.net/kivy-application-development-tutorial
#Variables which start with b are buttons
#Variables which start with l are labels
#Variables which start with box are boxes
#Variables which start with g are Grids
#IMPORTS
from datetime import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
#scraper imports
import requests
from bs4 import BeautifulSoup
#plot imports
import matplotlib.pyplot as plt
import numpy as np
from kivy.properties import StringProperty
from kivy.uix.image import Image


#CLASS
class Welcome(Screen):
    datestring = "Current Time: " + str(datetime.today())
    pass


class Menu(Screen):
    pass


class Scraper(Screen):
    page = requests.get("https://kivy.org/docs/contact.html")
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all('p')[0].get_text()

    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)
    plt.plot(t, s)

    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.savefig("test.png")
    source = StringProperty(None)
    myimage = Image(source = 'text.png')

    pass



class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("WeFidget.kv")


class MainApp(App):
    def build(self):
        return presentation


MainApp().run()


if __name__ == '__main__':
    MainApp().run()