from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivy.uix.screenmanager import ScreenManager

import phonenumbers
from phonenumbers import carrier,timezone,geocoder




class Phonefo(MDApp):

    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Cyan"

        self.manager=ScreenManager()

        self.mainscreen=MDScreen(name="MainScreen")
        self.infoscreen=MDScreen(name="InfoScreen")

        self.toolbar=MDToolbar(title="Phonefo App",pos_hint={"top":1})
        self.toolbar.right_action_items=[['arrow-right',self.go_right]]
        self.mainscreen.add_widget(self.toolbar)

        self.phone_number_input=MDTextField(pos_hint={"center_x":0.5,"top":0.6},size_hint=(0.75,1),halign="center",font_size=25)
        self.mainscreen.add_widget(self.phone_number_input)


        self.button=MDFillRoundFlatButton(text="Get Information",size_hint=(0.8,0.1),pos_hint={"center_x":0.5,"top":0.3},font_size=25,on_release=self.get_info)
        self.mainscreen.add_widget(self.button)

        # === Info Screen Design === #
        self.infotoolbar=MDToolbar(title="Phonefo App",pos_hint={"top":1})
        self.infotoolbar.right_action_items=[['arrow-left',self.go_left]]
        self.infoscreen.add_widget(self.infotoolbar)

        self.infogridlayout=MDGridLayout(cols=2,spacing=0,size_hint=(1,0.8),pos_hint={"top":0.8})
        self.infoscreen.add_widget(self.infogridlayout)

        self.country_code_label=MDLabel(text="Country Code:",pos_hint={"center_x":0.5},halign='center')
        self.infogridlayout.add_widget(self.country_code_label)

        self.country_code_answer_label=MDLabel(text="Country Code Answer:",pos_hint={"center_x":0.5},halign='center')
        self.infogridlayout.add_widget(self.country_code_answer_label)

        self.national_number_label=MDLabel(text="National Number:",pos_hint={"center_x":0.5},halign='center')
        self.infogridlayout.add_widget(self.national_number_label)

        self.national_number_answer_label=MDLabel(text="National Number Answer:",pos_hint={"center_x":0.5},halign='center')
        self.infogridlayout.add_widget(self.national_number_answer_label)

        self.timezone_label=MDLabel(text="TimeZone:",pos_hint={"center_x":0.5},halign='center')
        self.infogridlayout.add_widget(self.timezone_label)

        self.timezone_answer_label=MDLabel(text="Timezone Answer:",pos_hint={"center_x":0.5},halign='center')
        self.infogridlayout.add_widget(self.timezone_answer_label)

        self.country_label=MDLabel(text="Country:",pos_hint={"center_x":0.5},halign='center')
        self.infogridlayout.add_widget(self.country_label)

        self.country_answer_label=MDLabel(text="Country Answer:",pos_hint={"center_x":0.5},halign='center')
        self.infogridlayout.add_widget(self.country_answer_label)

        self.provider_label=MDLabel(text="Provider:",pos_hint={"center_x":0.5},halign='center')
        self.infogridlayout.add_widget(self.provider_label)

        self.provider_answer_label=MDLabel(text="Provider Answer:",pos_hint={"center_x":0.5},halign='center')
        self.infogridlayout.add_widget(self.provider_answer_label)

        self.isvalid_label=MDLabel(text="Valid:",pos_hint={"center_x":0.5},halign='center')
        self.infogridlayout.add_widget(self.isvalid_label)

        self.isvalid_answer_label=MDLabel(text="Valid Answer:",pos_hint={"center_x":0.5},halign='center')
        self.infogridlayout.add_widget(self.isvalid_answer_label)


        self.manager.add_widget(self.mainscreen)
        self.manager.add_widget(self.infoscreen)
        


        return self.manager

    def go_right(self,press):
        self.root.current="InfoScreen"
        self.root.transition.direction="left"

    def go_left(self,press):
        self.root.current="MainScreen"
        self.root.transition.direction="right"

    
    def get_info(self,press):
        number=self.phone_number_input.text
        pno=phonenumbers.parse(number)

        self.national_number_answer_label.text=""
        self.country_code_answer_label.text=""
        self.timezone_answer_label.text=""
        self.provider_answer_label.text=""
        self.country_answer_label.text=""
        self.isvalid_answer_label.text=""
        

        self.national_number_answer_label.text=str(pno.national_number)
        self.country_code_answer_label.text=str(pno.country_code)
        self.timezone_answer_label.text=str(timezone.time_zones_for_number(pno)[0])
        self.country_answer_label.text=str(geocoder.country_name_for_number(pno,'en'))
        self.provider_answer_label.text=str(carrier.name_for_number(pno, 'en'))
        self.isvalid_answer_label.text=str(phonenumbers.is_valid_number(pno))

        self.root.current="InfoScreen"
        self.root.transition.direction="left"

        
        


if __name__=="__main__":
    app=Phonefo()
    app.run()