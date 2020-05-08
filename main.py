from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.navigationdrawer import MDNavigationDrawer, NavigationLayout

from kivymd.theming import ThemableBehavior

from kivymd.uix.list import OneLineIconListItem, MDList

from kivymd.app import MDApp
from kivy.lang import Builder


from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty

from kivy.factory import Factory
from kivymd.uix.toolbar import MDToolbar



class LoginWindow(Screen):
    pass
    # v_login = ObjectProperty(None)
    # v_id_password = ObjectProperty(None)
    # v_btn_connection = ObjectProperty(None)
    # v_cb_keepInfo = ObjectProperty(None)


class MainWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


class SmartConnect(MDApp):
    def build(self):

        # screen_manager = WindowManager()
        #
        # # List of the screen to add
        # screens = [LoginWindow(name='LoginWindow'), MainWindow(name='MainWindow')]
        # for screen in screens:
        #     screen_manager.add_widget(screen)
        # screen_manager.current = 'LoginWindow'
        # kv = Builder.load_file('smart.kv')

        self.theme_cls.theme_style = 'Dark'
        return Builder.load_file('smart.kv')

# def on_start(self):
    #     # pass
    #     self.root.ids.id_login.text = 'iuoy'


if __name__== '__main__':
    SmartConnect().run()
