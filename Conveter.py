"""
The SimpleConverter might convert complex numbers from algebraic form
to exponential form and back.
It's useful for students studying power engineering for counting alternating currents and voltage.

"""
import math, cmath

from kivy.uix.floatlayout import FloatLayout

from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp


from kivy.core.window import Window

Window.size = (375, 812)

Kv = Builder.load_file("Converter.kv")


class Converter(FloatLayout):
    """Simple complex converter which converts number
        from algebraic form to exponential form and back
    """

    first_digit = ObjectProperty(None)
    second_digit = ObjectProperty(None)
    third_digit = ObjectProperty(None)
    fourth_digit = ObjectProperty(None)
    result = ObjectProperty(None)

    def alg_exp(self):
        """Converts from algebraic form to exponential

        Parameters
        ----------
        first_digit: str
        second_digit: str

        Returns
        -------
        str
            a complex number representing the exponential form
        """

        if self.first_digit.text != '' or self.second_digit.text != '':

            self.resulting = complex(float(self.first_digit.text),
                                     float(self.second_digit.text)
                                     )
            self.angle_deg = round(math.degrees(cmath.phase(self.resulting)), 4)
            self.modulus = round(abs(self.resulting), 4)
            self.resulting = '%s e %s' % (str(self.modulus), str(self.angle_deg))
            self.result.text = self.resulting
        else:

            self.result.text = "Enter the number"

    def exp_alg(self):
        """Converts from exponential form to algebraic

       Parameters
       ----------
       thirt_digit: str
       fourth_digit: str

       Returns
       -------
       str
           a complex number representing the algebraic form
       """

        if self.third_digit.text != '' or self.fourth_digit.text != '':

            self.real_part = round(float(self.third_digit.text) * math.cos(math.radians(float(self.fourth_digit.text))), 4)
            self.imag_part = round(
                float(self.third_digit.text) * math.sin(float(math.radians(float(self.fourth_digit.text)))), 4)

            if self.imag_part < 0:
                self.imag_part = str(self.imag_part).replace('-', '-j')
                self.resulting = "%s %s" % (str(self.real_part), str(self.imag_part))
            else:
                self.resulting = "%s +j%s" % (str(self.real_part), str(self.imag_part))
            self.result.text = self.resulting

        else:

            self.result.text = "Enter the number"


class MyApp(MDApp):

    def build(self):
        return Converter()


plApp = MyApp()

plApp.run()

