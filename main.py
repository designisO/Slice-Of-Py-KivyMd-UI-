from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.uix.image import Image
from kivymd.color_definitions import colors
from kivymd.uix.textfield import MDTextField


Window.size = (300, 600)


screen_helper = """
MDScreen:    
    MDBoxLayout:
        orientation: 'vertical'
        pos_hint: {'center_x': 0.5, 'center_y':0.9} 
    
        MDLabel:
            text:"SLICE OF PY"
            halign: "center"
            font_size: 28
            bold: True

    MDTextField:
        id: text_field
        hint_text: "Create Username"
        helper_text: "Hint: Username is your email address."
        helper_text_mode: "on_error"
        pos_hint: {'center_x': 0.5, 'center_y':0.7}
        size_hint_x:None
        width:250
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        on_text_validate: root.textInput(self)
    
    MDTextField:
        id: text_field
        hint_text: "Create Password"
        pos_hint: {'center_x': 0.5, 'center_y':0.6}
        size_hint_x:None
        width:250
        icon_right: "key"
        icon_right_color: app.theme_cls.primary_color
        on_text_validate: root.textInput(self)
    
    MDTextField:
        id: text_field
        hint_text: "Enter Full Name"
        helper_text_mode: "on_error"
        pos_hint: {'center_x': 0.5, 'center_y':0.5}
        size_hint_x:None
        width:250
        icon_right: "account-circle"
        icon_right_color: app.theme_cls.primary_color
        on_text_validate: root.textInput(self)
        
    MDTextField:
        id: text_field
        hint_text: "Github"
        helper_text_mode: "on_error"
        pos_hint: {'center_x': 0.5, 'center_y':0.4}
        size_hint_x:None
        width:250
        icon_right: "github"
        icon_right_color: app.theme_cls.primary_color
        on_text_validate: root.textInput(self)
    
    MDTextField:
        id: text_field
        hint_text: "Email Address"
        helper_text_mode: "on_error"
        pos_hint: {'center_x': 0.5, 'center_y':0.3}
        size_hint_x:None
        width:250
        icon_right: "mail"
        icon_right_color: app.theme_cls.primary_color
        on_text_validate: root.textInput(self)
        
    
    MDBottomAppBar:
        MDTopAppBar:
            icon: "send"
            type: "bottom"
            mode: "center"
            
            
            
    
"""



class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.theme_style = 'Dark'
        screen = Builder.load_string(screen_helper)

        return screen

    def textInput(self, widget):
        self.email = widget.text

    def onClick(self):
        self.textInput(self.ids.text_field)
        print(self.email)



MainApp().run()
