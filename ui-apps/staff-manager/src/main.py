import flet as ft

from pages.signup import signup
from pages.login import login
from pages.home import home
from pages.register import register
from pages.overview import overview

def main(page: ft.Page):
    page.title = "Staff Manager"

    def route_change():
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                bgcolor=ft.Colors.WHITE,
                controls=[
                    login(page)
                ],
            )
        )

        if page.route == "/signup":
            page.views.append(
                ft.View(
                    route="/signup",
                    bgcolor=ft.Colors.WHITE,
                    controls=[
                        signup(page)
                    ],
                )
            )
        if page.route == "/home":
            page.views.append(
                ft.View(
                    route="/home",
                    bgcolor=ft.Colors.WHITE,
                    controls=[
                        home(page)
                    ],
                )
            )
        if page.route == "/register":
            page.views.append(
                ft.View(
                    route="/register",
                    bgcolor=ft.Colors.WHITE,
                    controls=[
                        register(page)
                    ],
                )
            )
        if page.route == "/overview":
            page.views.append(
                ft.View(
                    route="/overview",
                    bgcolor=ft.Colors.WHITE,
                    controls=[
                        overview(page)
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
