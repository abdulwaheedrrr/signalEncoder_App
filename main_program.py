# main_program.py

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout # type: ignore
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color, Rectangle
from kivy.properties import ListProperty
from kivy.metrics import dp
from kivy.lang import Builder # <--- ADD THIS IMPORT

# Import all your encoding functions
# This import looks correct given your file name 'encoding_scheme_logic'
from encoding_scheme_logic import (
    nrz_l,
    nrz_i,
    rz,
    manchester,
    differential_manchester
)

class SignalDrawer(Widget):
    signal_data = ListProperty([]) # List of signal levels

    def on_size(self, *args): self.draw_signal()
    def on_pos(self, *args): self.draw_signal()
    def on_signal_data(self, instance, value): self.draw_signal()

    def draw_signal(self):
        self.canvas.clear()
        with self.canvas:
            Color(0, 0, 0, 1) # Background
            Rectangle(pos=self.pos, size=self.size)

            if not self.signal_data: return

            padding_x = self.width * 0.05
            padding_y = self.height * 0.15
            drawable_width = self.width - 2 * padding_x
            drawable_height = self.height - 2 * padding_y

            y_levels = {
                -1: self.y + padding_y,
                0: self.y + self.height / 2,
                1: self.y + self.height - padding_y
            }

            num_time_units = len(self.signal_data)
            x_step = drawable_width / num_time_units if num_time_units > 0 else 0

            # X-axis (0V line)
            Color(0.5, 0.5, 0.5, 1)
            Line(points=[self.x + padding_x, y_levels[0], self.x + self.width - padding_x, y_levels[0]], width=dp(1))

            # Signal lines
            Color(0, 0.7, 1, 1) # Blue
            points = []
            current_x = self.x + padding_x

            for i, level in enumerate(self.signal_data):
                y_coord = y_levels.get(level, y_levels[0])

                if i == 0:
                    points.extend([current_x, y_coord])
                else:
                    points.extend([current_x, points[-1]]) # Horizontal segment
                    points.extend([current_x, y_coord])    # Vertical transition

                current_x += x_step
                points.extend([current_x, y_coord]) # End of horizontal segment

            Line(points=points, width=dp(2.5))


class MainAppLayout(BoxLayout):
    def encode_and_draw(self, scheme_name):
        binary_input_str = self.ids.binary_input.text.strip()
        signal_display_widget = self.ids.signal_display

        if not binary_input_str:
            signal_display_widget.signal_data = []
            return

        try:
            signal = []
            # Call respective encoding function
            if scheme_name == 'nrz_l': signal = nrz_l(binary_input_str)
            elif scheme_name == 'nrz_i': signal = nrz_i(binary_input_str, initial_level=1)
            elif scheme_name == 'rz': signal = rz(binary_input_str)
            elif scheme_name == 'manchester': signal = manchester(binary_input_str)
            elif scheme_name == 'differential_manchester': signal = differential_manchester(binary_input_str, initial_transition_is_lh=True)
            else: signal_display_widget.signal_data = []; return

            if signal is not None:
                signal_display_widget.signal_data = signal
            else: # Encoding function returned invalid data (e.g., due to bad input)
                signal_display_widget.signal_data = []

        except Exception as e:
            print(f"Error: {e}") # Log error for debugging
            signal_display_widget.signal_data = []

    def clear_signal(self):
        self.ids.signal_display.signal_data = []
        self.ids.binary_input.text = ""


class EncodingApp(App):
    def build(self):
        Builder.load_file('kivy_main.kv')
        return MainAppLayout()

if __name__ == '__main__':
    EncodingApp().run()