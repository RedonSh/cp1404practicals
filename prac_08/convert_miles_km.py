from kivy.app import App
from kivy.lang import Builder

MILES = 0.621371


class MilesToKM(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate(self):
        result = self.get_miles()
        km = result * MILES
        self.root.ids.output_label.text = str(km)

    def add_on(self, change):
        result = self.get_miles() + change
        self.root.ids.input_miles.text = str(result)
        self.calculate()

    def get_miles(self):
        try:
            result = float(self.root.ids.input_miles.text)
            return result
        except ValueError:
            return 0


MilesToKM().run()
