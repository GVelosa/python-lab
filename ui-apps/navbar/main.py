import flet as ft

from components.navbar import create_navbar
from components.appbar import create_appbar
from pages.home import home_page
from pages.user import user_page

def main(page: ft.Page):
    page.navigation_bar = create_navbar()
    page.appbar = create_appbar("Main")
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    home = home_page()
    user = user_page()
    content = ft.Container(content = home)

    def change_page(e):
        if page.navigation_bar.selected_index == 0:
            content.content = home
        elif page.navigation_bar.selected_index == 1:
            content.content = user

        page.update()

    page.navigation_bar.on_change = change_page

    page.add(
        content
        )

if __name__ == "__main__":
    ft.run(main)
