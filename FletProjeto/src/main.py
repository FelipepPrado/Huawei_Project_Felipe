import flet as ft

class Ongs:
    def __init__(self,titulo, texto1, image2):
        self.titulo=titulo
        self.texto1=texto1
        self.content=ft.Row(
            ft.Container(
                image2,
                content=ft.Column(
                    [
                        ft.Text(titulo, size=20),
                        ft.Text(texto1, size=14)
                    ]
                )
            )
        )

def main(page: ft.Page):
    Brown = "#4A3928"
    page.title = "Planting The Future"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def button_clicked(e):
        page.clean()
        page.update()
        page.vertical_alignment=ft.MainAxisAlignment.CENTER
        page.add(
            ft.Column(
                [
                    ft.Container(
                        bgcolor=ft.colors.BROWN,
                        content=ft.Column(
                            [
                                ft.Row([
                                    image1,
                                    ft.Icon(name = ft.Icons.PERSON_OUTLINED, color="#50EA3B")
                                ]
                                ),
                                ft.Text("Procurar ong", color="#50EA3B"),
                                search_button
                            ]
                        ),
                        #alignment=ft.alignment.top_center #Não ta funcionando
                    ),
                    ft.Container(
                        bgcolor=ft.colors.BROWN,
                        content=ft.Column(
                            tome1 = Ongs("SOS Mata Atlântica", "Reflorestamento da Mata Atlântica", image2),
                            tome2 = Ongs("SOS Mata Atlântica", "Reflorestamento da Mata Atlântica", image2),
                            tome3 = Ongs("SOS Mata Atlântica", "Reflorestamento da Mata Atlântica", image2),
                            tome4 = Ongs("SOS Mata Atlântica", "Reflorestamento da Mata Atlântica", image2)
                        )
                    )
                ]
            )
        )


    image1 = ft.Image(
        src="C:Users/user.geral/Downloads/image1.png",
        width=90,
        height=90,
        fit=ft.ImageFit.COVER, 
    )

    image2 = ft.Image(
        src="C:/Users/user.geral/Downloads/image2.png",
        width=430,
        height=480,
        #border_radius= ft.border_radius.only(top_left, top_right),
        fit=ft.ImageFit.COVER,
    )

    email_user = ft.TextField(
        hint_text= "Email",
        width=360,
        height=38,
        bgcolor = ft.colors.WHITE,
        color = "#000000",
        border_color = Brown,
        border_radius=8,
        border_width=2,
        hint_style=ft.TextStyle(color="#000000", size=14)
    )
    
    senha_user = ft.TextField(
        hint_text="Senha",
        password=True,
        can_reveal_password=True,
        width=360,
        height=38,
        bgcolor = ft.colors.WHITE,
        color = "#000000",
        border_color = Brown,
        border_radius=8,
        border_width=2,
        hint_style=ft.TextStyle(color="#000000", size=14)
    )

    search_button = ft.TextField(
        prefix_icon = ft.Icon(name=ft.Icons.SEARCH, color = "#000000"),
        hint_text= "Pesquisar",
        width=360,
        height=38,
        bgcolor = ft.colors.WHITE,
        color = "#000000",
        border_color = Brown,
        border_radius=8,
        border_width=2,
        hint_style=ft.TextStyle(color="#000000", size=14)
    )

    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.END

    page.padding=10

    page.add(
        #page.padding=0,
        ft.Column(
            [
                image2,
                ft.Container(
                    width=430,
                    height=380,
                    bgcolor = "#E7E1E1",
                    border_radius=15,
                    content=ft.Column(
                        [
                            ft.Column(
                                [
                                    image1,
                                    ft.Text("Planting the Future", size=28, color = Brown, weight=ft.FontWeight.BOLD)
                                ],
                                spacing=0,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            email_user,
                            senha_user,
                            ft.TextButton(text = "Esqueceu sua senha?", style = ft.ButtonStyle(color = "#000000")),
                            ft.Container(
                                ft.ElevatedButton(
                                    bgcolor = "#50EA3B",
                                    color = ft.Colors.BLACK,
                                    style = ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=7), text_style=ft.TextStyle(size=18)),
                                    content=ft.Row([
                                            ft.Icon(name=ft.icons.LOGOUT, color=ft.Colors.BLACK),
                                            ft.Text("Entrar")
                                        ],
                                        width=340,
                                        height=28,
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                    on_click=button_clicked
                                ),
                                border=ft.border.all(color="#000000", width=2),
                                border_radius=8,
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        #alignment=ft.MainAxisAlignment.END
                    )
                )
            ],
            spacing=0
        )
    )


ft.app(main)
