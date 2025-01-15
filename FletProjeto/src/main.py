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
                        width=330,
                        height=28,
                        alignment=ft.MainAxisAlignment.CENTER
                    )

def main(page: ft.Page):
    Brown = "#4A3928"
    page.title = "Planting The Future"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    image1 = ft.Image(
        src="C:/Users/Felipe/Downloads/Floresta Urbana 1 (1).png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    image2 = ft.Image(
        src="C:/Users/Felipe/Downloads/image 1.png",
        width=430,
        height=320,
        fit=ft.ImageFit.CONTAIN,
    )

    email_user = ft.TextField(
        hint_text= "Email",
        width=360,
        height=48,
        bgcolor = ft.colors.WHITE,
        color = "#000000",
        border_color = Brown,
        border_radius=8,
        border_width=2,
        hint_style=ft.TextStyle(color="#000000")
        )
    
    senha_user = ft.TextField(
        hint_text="Senha", 
        password=True,
        can_reveal_password=True,
        width=360,
        height=48,
        bgcolor = ft.colors.WHITE,
        color = "#000000",
        border_color = Brown,
        border_radius=8,
        border_width=2,
        hint_style=ft.TextStyle(color="#000000")
        )

    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    
    page.add(
        ft.Container(
            width=430,
            height=720,
            bgcolor = ft.colors.BROWN,
            border_radius=15,
            content=ft.Column(
                [
                    image2,
                    ft.Container(
                        width=430,
                        height=400,
                        bgcolor = ft.colors.WHITE,
                        border_radius=15,
                        content=ft.Column(
                            [
                                image1,
                                ft.Text("Planting the Future", size=32, color = Brown, weight=ft.FontWeight.BOLD),
                                email_user,
                                senha_user,
                                ft.TextButton(text = "Esqueceu sua senha?", style = ft.ButtonStyle(color = "#000000")),
                                ft.Container(MyButton(), border=ft.border.all(color="#000000", width=2), border_radius=40)
                                    
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    )
                ],
                alignment=ft.alignment.bottom_center
            )
        )
    )


ft.app(main)
