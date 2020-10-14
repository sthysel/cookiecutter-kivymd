from kivymd.app import MDApp

class {{cookiecutter.app_name}}App(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"



if __name__ == "__main__":
    {{cookiecutter.app_name}}App().run()

