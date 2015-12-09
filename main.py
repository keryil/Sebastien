from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label
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


class SebastienApp(App):
    def build(self):
        drawer = NavigationDrawer()

        # Add the navigation panel
        sidepanel = BoxLayout(orientation="vertical")
        sidepanel.add_widget(Label(text="Navigation"))
        drawer.add_widget(sidepanel)

        # Create all screens
        screens = [ListsScreen(name='lists'),
                   ProductsScreen(name='products'),
                   HistoryScreen(name='history'),
                   SettingsScreen(name='settings')]

        sm = ScreenManager()
        map(sm.add_widget, screens)
        drawer.add_widget(sm)

        # Create corresponding buttons
        # for navigation
        def go_to_screen(button):
            sm.current = button.text.lower()
        buttons = []

        for screen in screens:
            button = Button(text=screen.name.capitalize())
            button.bind(on_release=go_to_screen)
            buttons.append(button)

        map(sidepanel.add_widget, buttons)

        return drawer


if __name__ == '__main__':
    SebastienApp().run()
