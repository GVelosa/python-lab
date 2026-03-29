import flet as ft

from pages.signup import signup_view
from pages.login import login_view
from pages.home import home_view
from pages.register_employees import create_employee_view
from pages.create_job_title import create_job_title_view
from pages.overview import overview_view
from pages.create_departments import create_departments
from database.db import init_db

init_db()

def main(page: ft.Page):
    page.title = "Staff Manager"
    
    def route_change():
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                bgcolor=ft.Colors.WHITE,
                controls=[
                    login_view(page)
                ],
            )
        )

        if page.route == "/signup":
            page.views.append(
                ft.View(
                    route="/signup",
                    bgcolor=ft.Colors.WHITE,
                    controls=[
                        signup_view(page)
                    ],
                )
            )
        if page.route == "/home":
            page.views.append(
                ft.View(
                    route="/home",
                    bgcolor=ft.Colors.WHITE,
                    controls=[
                        home_view(page)
                    ],
                )
            )
        if page.route == "/create_employee":
            page.views.append(
                ft.View(
                    route="/create_employee",
                    bgcolor=ft.Colors.WHITE,
                    controls=[
                        create_employee_view(page)
                    ],
                )
            )
        if page.route == "/overview":
            page.views.append(
                ft.View(
                    route="/overview",
                    bgcolor=ft.Colors.WHITE,
                    controls=[
                        overview_view(page)
                    ],
                )
            )

        if page.route == "/create_departments":
            page.views.append(
                ft.View(
                    route="/create_departments",
                    bgcolor=ft.Colors.WHITE,
                    controls=[
                        create_departments(page)
                    ],
                )
            )

        if page.route == "/create_job_title":
            page.views.append(
                ft.View(
                    route="/create_job_title",
                    bgcolor=ft.Colors.WHITE,
                    controls=[
                        create_job_title_view(page)
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
