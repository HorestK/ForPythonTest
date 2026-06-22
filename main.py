from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

KV = '''
MDBoxLayout:
    orientation: 'vertical'

    MDTopAppBar:
        title: "Заказ пиццы"
        anchor_title: "left"
        elevation: 4
        right_action_items: [["exit-to-app", lambda x: app.stop_app()]]

    MDScrollView:
        MDGridLayout:
            cols: 1
            adaptive_height: True
            padding: "12dp"
            spacing: "12dp"

            # Карточка 1: Маргарита
            MDCard:
                orientation: "vertical"
                size_hint_y: None
                height: "120dp"
                padding: "8dp"
                ripple_behavior: True
                on_release: app.add_to_cart("Пицца Маргарита")

                MDBoxLayout:
                    orientation: "horizontal"
                    spacing: "12dp"
                    Image:
                        source: "images/margherita.jpg"
                        size_hint_x: None
                        width: "100dp"
                    MDBoxLayout:
                        orientation: "vertical"
                        MDLabel:
                            text: "Маргарита"
                            font_style: "H6"
                            bold: True
                        MDLabel:
                            text: "Томаты, моцарелла, базилик, соус"
                            font_style: "Body2"
                            theme_text_color: "Secondary"

            # Карточка 2: Пепперони
            MDCard:
                orientation: "vertical"
                size_hint_y: None
                height: "120dp"
                padding: "8dp"
                ripple_behavior: True
                on_release: app.add_to_cart("Пицца Пепперони")

                MDBoxLayout:
                    orientation: "horizontal"
                    spacing: "12dp"
                    Image:
                        source: "images/pepperoni.jpg"
                        size_hint_x: None
                        width: "100dp"
                    MDBoxLayout:
                        orientation: "vertical"
                        MDLabel:
                            text: "Пепперони"
                            font_style: "H6"
                            bold: True
                        MDLabel:
                            text: "Острые колбаски пепперони, моцарелла, соус"
                            font_style: "Body2"
                            theme_text_color: "Secondary"

            # Карточка 3: Четыре сыра
            MDCard:
                orientation: "vertical"
                size_hint_y: None
                height: "120dp"
                padding: "8dp"
                ripple_behavior: True
                on_release: app.add_to_cart("Пицца Четыре сыра")

                MDBoxLayout:
                    orientation: "horizontal"
                    spacing: "12dp"
                    Image:
                        source: "images/four_cheese.jpg"
                        size_hint_x: None
                        width: "100dp"
                    MDBoxLayout:
                        orientation: "vertical"
                        MDLabel:
                            text: "Четыре сыра"
                            font_style: "H6"
                            bold: True
                        MDLabel:
                            text: "Моцарелла, пармезан, чеддер, дорблю"
                            font_style: "Body2"
                            theme_text_color: "Secondary"

            # Карточка 4: Гавайская
            MDCard:
                orientation: "vertical"
                size_hint_y: None
                height: "120dp"
                padding: "8dp"
                ripple_behavior: True
                on_release: app.add_to_cart("Пицца Гавайская")

                MDBoxLayout:
                    orientation: "horizontal"
                    spacing: "12dp"
                    Image:
                        source: "images/hawaiian.jpg"
                        size_hint_x: None
                        width: "100dp"
                    MDBoxLayout:
                        orientation: "vertical"
                        MDLabel:
                            text: "Гавайская"
                            font_style: "H6"
                            bold: True
                        MDLabel:
                            text: "Сочная курица, ананасы, моцарелла, томатный соус"
                            font_style: "Body2"
                            theme_text_color: "Secondary"

            # Карточка 5: Мясная
            MDCard:
                orientation: "vertical"
                size_hint_y: None
                height: "120dp"
                padding: "8dp"
                ripple_behavior: True
                on_release: app.add_to_cart("Пицца Мясная")

                MDBoxLayout:
                    orientation: "horizontal"
                    spacing: "12dp"
                    Image:
                        source: "images/meat.jpg"
                        size_hint_x: None
                        width: "100dp"
                    MDBoxLayout:
                        orientation: "vertical"
                        MDLabel:
                            text: "Мясной микс"
                            font_style: "H6"
                            bold: True
                        MDLabel:
                            text: "Бекон, ветчина, фарш, охотничьи колбаски, соус"
                            font_style: "Body2"
                            theme_text_color: "Secondary"

            # Карточка 6: Вегетарианская
            MDCard:
                orientation: "vertical"
                size_hint_y: None
                height: "120dp"
                padding: "8dp"
                ripple_behavior: True
                on_release: app.add_to_cart("Пицца Вегетарианская")

                MDBoxLayout:
                    orientation: "horizontal"
                    spacing: "12dp"
                    Image:
                        source: "images/vegetarian.jpg"
                        size_hint_x: None
                        width: "100dp"
                    MDBoxLayout:
                        orientation: "vertical"
                        MDLabel:
                            text: "Вегетарианская"
                            font_style: "H6"
                            bold: True
                        MDLabel:
                            text: "Болгарский перец, грибы, маслины, томаты, кукуруза"
                            font_style: "Body2"
                            theme_text_color: "Secondary"

            # Карточка 7: Барбекю
            MDCard:
                orientation: "vertical"
                size_hint_y: None
                height: "120dp"
                padding: "8dp"
                ripple_behavior: True
                on_release: app.add_to_cart("Пицца Барбекю")

                MDBoxLayout:
                    orientation: "horizontal"
                    spacing: "12dp"
                    Image:
                        source: "images/barbecue.jpg"
                        size_hint_x: None
                        width: "100dp"
                    MDBoxLayout:
                        orientation: "vertical"
                        MDLabel:
                            text: "Цыпленок Барбекю"
                            font_style: "H6"
                            bold: True
                        MDLabel:
                            text: "Копченая куриная грудка, лук, соус барбекю"
                            font_style: "Body2"
                            theme_text_color: "Secondary"

    MDBottomAppBar:
        MDTopAppBar:
            icon: "cart-plus"
            type: "bottom"
            mode: "end"
            on_action_button: app.show_cart()
            left_action_items: [["menu", lambda x: app.show_stub_dialog()], ["email", lambda x: app.show_stub_dialog()], ["phone", lambda x: app.show_stub_dialog()]]
'''


class PizzaApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cart = []
        self.dialog = None

    def build(self):
        try:
            self.theme_cls.material_style = "M2"
        except AttributeError:
            pass

        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def add_to_cart(self, pizza_name):
        self.cart.append(pizza_name)
        self.dialog = MDDialog(
            text=f"Добавлено в корзину: {pizza_name}",
            buttons=[MDFlatButton(text="OK", on_release=self.close_dialog)]
        )
        self.dialog.open()

    def show_cart(self):
        if not self.cart:
            content_text = "Ваша корзина пуста."
        else:
            content_text = "Вы заказали:\n" + "\n".join(f"- {item}" for item in self.cart)

        self.dialog = MDDialog(
            title="Содержимое корзины",
            text=content_text,
            buttons=[MDFlatButton(text="Закрыть", on_release=self.close_dialog)]
        )
        self.dialog.open()

    def show_stub_dialog(self):
        self.dialog = MDDialog(
            text="Событие касания распознано и обработано.",
            buttons=[MDFlatButton(text="OK", on_release=self.close_dialog)]
        )
        self.dialog.open()

    def close_dialog(self, *args):
        if self.dialog:
            self.dialog.dismiss()

    def stop_app(self):
        self.stop()


if __name__ == '__main__':
    PizzaApp().run()

#exe:
#pip install PyInstaller
#pyinstaller --onefile [name]

#Buldozer
#linux нужен

#аналоги бульдозера есть на windows