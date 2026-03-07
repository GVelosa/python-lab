import flet as ft
import random

def create_card(image_src, title_text, content_text):

    def color_change(e):
        colors = ["red","green","blue","yellow","orange","purple","pink"]
        card.bgcolor = random.choice(colors)
        card.update()

    image = ft.Image(src=image_src, border_radius=10)

    title = ft.Text(
        title_text,
        theme_style=ft.TextThemeStyle.TITLE_LARGE,
        weight=ft.FontWeight.BOLD
    )

    content = ft.Text(
        content_text,
        size=18,
        text_align=ft.TextAlign.CENTER
    )

    card = ft.Container(
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[image, title, content],
        ),
        bgcolor="blue",
        margin=10,
        padding=10,
        width=350,
        # height=350,
        border_radius=10,
        ink=True,
        on_click=color_change,
    )

    return card