from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.navigationdrawer import NavigationDrawer


class ListsScreen(Screen):
    pass


class ProductsScreen(Screen):
    pass


class HistoryScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class MenuWidget(BoxLayout):
    manager = ObjectProperty(None)


class SebastienApp(App):
    def build(self):
        drawer = NavigationDrawer()

        # Add the navigation panel
        sm = ScreenManager()
        sidepanel = MenuWidget()
        sidepanel.manager = sm

        drawer.add_widget(sidepanel)

        # Create all screens
        screens = [ListsScreen(name='lists'),
                   ProductsScreen(name='products'),
                   HistoryScreen(name='history'),
                   SettingsScreen(name='settings')]

        map(sm.add_widget, screens)
        drawer.add_widget(sm)

        # Create corresponding buttons
        # for navigation
        def go_to_screen(button):
            sm.current = button.text.lower()

        def setup_button(screen):
            button = Button(text=screen.name.capitalize())
            button.bind(on_release=go_to_screen)
            return button

        buttons = map(setup_button, screens)
        # map(sidepanel.add_widget, buttons)

        return drawer


if __name__ == '__main__':
    SebastienApp().run()
