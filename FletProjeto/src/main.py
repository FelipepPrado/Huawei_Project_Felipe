import time
import flet as ft

#Forma de criar um botão personalizado, vou precisar pra um botão do login, então é bom
class MyButton(ft.ElevatedButton):
    def __init__(self):
        super().__init__()
        self.bgcolor = ft.Colors.GREEN
        self.color = ft.Colors.BLACK
        self.text = "Entrar"

def main(page: ft.Page):
    page.title = "Planting The Future"

    email_user = ft.TextField(label = "Email", width=300)
    senha_user = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=300)
    page.add(
        email_user,
        senha_user,
        MyButton()
    )


ft.app(main)
