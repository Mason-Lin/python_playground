from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.orientation = "vertical"
        for i in range(5):
            self.btn = Button(
                text="Button " + str(i), on_press=self.remove_filter_btn
            )
            self.add_widget(self.btn)

        self.btn = Button(
            text="hello",
            size_hint=(None, None),
            halign="center",
            size=(128, 128),
            text_size=(118, None),
        )
        self.add_widget(self.btn)

    def load(self, path, selection):
        print(path, selection)

    def remove_filter_btn(self, instance):
        # self.remove_widget(instance)
        print(instance)


class MyApp(App):
    def build(self):
        return MainWindow()


if __name__ == "__main__":
    MyApp().run()
