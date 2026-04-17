import flet as ft


def home_view(page: ft.Page):

    async def to_single_game():
        await page.push_route("/single_game")

    change_page = ft.Button(
        content="Mudar de Página",
        on_click=to_single_game
    )

    home = ft.Column(
        controls=[
            change_page
        ]
    )

    return home