from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.navigationdrawer import NavigationDrawer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from product import Product

class ListsScreen(Screen, BoxLayout):
    pass


class ProductsScreen(Screen, BoxLayout):
    pass


class HistoryScreen(Screen, BoxLayout):
    pass


class SettingsScreen(Screen, BoxLayout):
    pass


class MenuWidget(BoxLayout):
    manager = ObjectProperty(None)


class SebastienApp(App):
    def init_database(self):
        self.db_engine = create_engine('sqlite:///:memory:', echo=True)
        self.db_session = sessionmaker(bind=self.db_engine)

        product = Product(name="Bread", units="Weight")
        self.db_session.add(product)

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

        return drawer


if __name__ == '__main__':
    SebastienApp().run()
