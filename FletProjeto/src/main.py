import time
import flet as ft

#Forma de criar um botão personalizado, vou precisar pra um botão do login, então é bom
class MyButton(ft.ElevatedButton):
    def __init__(self):
        super().__init__()
        self.bgcolor = ft.Colors.GREEN
        self.color = ft.Colors.BLACK
        self.content=ft.Row([
                            ft.Icon(name=ft.icons.LOGOUT, color=ft.Colors.BLACK),
                            ft.Text("Entrar")
                        ],
                        width=285,
                        alignment=ft.MainAxisAlignment.CENTER
                    )

def main(page: ft.Page):
    Brown = "#4A3928"
    page.title = "Planting The Future"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    email_user = ft.TextField(
        hint_text= "Email",
        width=360,
        height=48,
        bgcolor = ft.colors.WHITE,
        border_radius=8,
        border_width=0,
        hint_style=ft.TextStyle(color="#000000")
        )
    
    senha_user = ft.TextField(
        hint_text="Senha", 
        password=True,
        can_reveal_password=True,
        width=360,
        height=48,
        bgcolor = ft.colors.WHITE,
        border_radius=8,
        border_width=0,
        hint_style=ft.TextStyle(color="#000000")
        )

    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Card(
            content = ft.Container(
                ft.Card(
                    content = ft.Container(
                        content=ft.Column( 
                            [
                                ft.Text("Planting the Future", size=32, color = Brown),
                                ft.Container(email_user, border=ft.border.all(color=Brown, width=2), border_radius=10),
                                ft.Container(senha_user, border=ft.border.all(color=Brown, width=2), border_radius=10),
                                ft.Text("Esqueceu sua senha", size=16, color = "#000000"),
                                ft.Container(MyButton(), border=ft.border.all(color="#000000", width=2), border_radius=40)
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ),
                    width=430,
                    height=320,
                    color = ft.colors.WHITE
                ),
                alignment=ft.alignment.bottom_center
            ),
            width=430,
            height=720,
            color = ft.colors.BROWN
            
        )
    )


ft.app(main)
