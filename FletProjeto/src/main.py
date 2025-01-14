import time
import flet as ft

#Forma de criar um botão personalizado, vou precisar pra um botão do login, então é bom
class MyButton(ft.ElevatedButton):
    def __init__(self):
        super().__init__()
        self.bgcolor = ft.Colors.GREEN
        self.color = ft.Colors.BLACK
        self.content= ft.Row([
                            ft.Icon(name=ft.icons.LOGOUT, color=ft.Colors.BLACK),
                            ft.Text("Entrar"),
                        ],
                        width=285,
                        alignment=ft.MainAxisAlignment.CENTER
                    )

def main(page: ft.Page):
    page.title = "Planting The Future"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    email_user = ft.TextField(
        label = "Email",
        width=300,
        bgcolor = ft.colors.WHITE,
        border_radius=8,
        border_width=0
        )
    
    senha_user = ft.TextField(
        label="Senha", password=True,
        can_reveal_password=True,
        width=300,
        bgcolor = ft.colors.WHITE,
        border_radius=8,
        border_width=0
        )
    
    page.add(
        ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column( 
                [
                    ft.Container(email_user, border=ft.border.all(color="#4A3928", width=2), border_radius=10),
                    ft.Container(senha_user, border=ft.border.all(color="#4A3928", width=2), border_radius=10),
                    ft.Container(MyButton(), border=ft.border.all(color="#000000", width=2), border_radius=40)
                ]
            )
                
        )
    )


ft.app(main)
