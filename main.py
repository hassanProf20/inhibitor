from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class AntiscalantApp(App):
    def build(self):
        # إنشاء واجهة المستخدم
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # إضافة عناصر واجهة المستخدم
        self.layout.add_widget(Label(text="معايرة الخزان", size_hint=(1, 0.1)))
        self.clicks_input = TextInput(hint_text="عدد الشرطات", multiline=False)
        self.liters_input = TextInput(hint_text="عدد اللترات", multiline=False)
        self.layout.add_widget(self.clicks_input)
        self.layout.add_widget(self.liters_input)

        self.layout.add_widget(Label(text="نسبة الخلط", size_hint=(1, 0.1)))
        self.water_input = TextInput(hint_text="كمية الماء باللتر", multiline=False)
        self.antiscalant_input = TextInput(hint_text="كمية مانع الترسيب باللتر", multiline=False)
        self.layout.add_widget(self.water_input)
        self.layout.add_widget(self.antiscalant_input)

        self.layout.add_widget(Label(text="حساب الاستهلاك", size_hint=(1, 0.1)))
        self.start_clicks_input = TextInput(hint_text="عدد الشرطات عند بداية الشهر", multiline=False)
        self.end_clicks_input = TextInput(hint_text="عدد الشرطات عند نهاية الشهر", multiline=False)
        self.preparations_input = TextInput(hint_text="عدد التحضيرات", multiline=False)
        self.preparation_amount_input = TextInput(hint_text="كمية التحضير باللتر", multiline=False)
        self.layout.add_widget(self.start_clicks_input)
        self.layout.add_widget(self.end_clicks_input)
        self.layout.add_widget(self.preparations_input)
        self.layout.add_widget(self.preparation_amount_input)

        # إضافة زر لحساب الاستهلاك
        self.calculate_button = Button(text="حساب الاستهلاك", size_hint=(1, 0.2))
        self.calculate_button.bind(on_press=self.calculate_consumption)
        self.layout.add_widget(self.calculate_button)

        return self.layout

    def calculate_consumption(self, instance):
        try:
            # قراءة القيم المدخلة
            clicks = float(self.clicks_input.text)
            liters = float(self.liters_input.text)
            antiscalant = float(self.antiscalant_input.text)
            start_clicks = float(self.start_clicks_input.text)
            end_clicks = float(self.end_clicks_input.text)
            preparations = float(self.preparations_input.text)
            preparation_amount = float(self.preparation_amount_input.text)

            # حساب ثابت الخلط (X)
            X = antiscalant / clicks

            # حساب قيمة بداية الشهر (Y)
            Y = X * start_clicks

            # حساب قيمة نهاية الشهر (Z)
            Z = X * end_clicks

            # حساب كمية التحضيرات (M)
            M = preparations * preparation_amount

            # حساب كمية الاستهلاك (A)
            A = M + Y - Z

            # عرض النتيجة في رسالة منبثقة
            self.show_popup(f"كمية الاستهلاك: {A:.2f} لتر")
        except Exception as e:
            self.show_popup("خطأ في المدخلات! تأكد من إدخال أرقام صحيحة.")

    def show_popup(self, message):
        # إنشاء رسالة منبثقة
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_label = Label(text=message)
        popup_button = Button(text="موافق", size_hint=(1, 0.2))

        # إضافة العناصر إلى الرسالة المنبثقة
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(popup_button)

        # إنشاء وعرض الرسالة المنبثقة
        popup = Popup(title="نتيجة الاستهلاك", content=popup_layout, size_hint=(0.8, 0.4))
        popup_button.bind(on_press=popup.dismiss)  # إغلاق الرسالة عند الضغط على "موافق"
        popup.open()

# تشغيل التطبيق
if __name__ == '__main__':
    AntiscalantApp().run()