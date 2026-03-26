import flet as ft

from components.card import content_card

def home(page: ft.Page):

    async def to_register(e):
        await page.push_route("/register")

    async def to_overview(e):
        await page.push_route("/overview")

    home_page = ft.Container(
        content=ft.Row(
            controls=[
                content_card("Register","Register a new employee", to_register),
                content_card("Overview","Overview of all registered employees", to_overview),
            ]
        )
    )
    return home_page