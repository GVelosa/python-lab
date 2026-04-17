import flet as ft

from pages.home.view import home_view
from pages.single_game.view import single_game_view

def main(page: ft.Page):
    page.title = "Wordle"

    def route_change():
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                controls=[
                    home_view(page)
                ]
            )
        )
        if page.route == "/single_game":
                page.views.append(
                ft.View(
                    route="/signup",
                    appbar= None,
                    controls=[
                        single_game_view(page)
                    ],
                )
            )

        page.update()
    async def view_pop(e):
        if e.view is not None:
            print("View pop:", e.view)
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    route_change()

if __name__ == "__main__":
    ft.run(main)