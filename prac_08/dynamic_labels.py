from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name, phone in self.name_to_phone.items():
            temp_label = Label(text=f"{name}: {phone}")
            temp_label.bind(on_press=self.press_label)
            self.root.ids.entries_label.add_widget(temp_label)

    def press_label(self, instance):
        name_and_number = instance.text
        name = name_and_number.split(":")[0].strip()
        self.status_text = f"{name}'s number is {self.name_to_phone[name]}"


DynamicWidgetsApp().run()
