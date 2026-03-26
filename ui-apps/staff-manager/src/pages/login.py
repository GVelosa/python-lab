import flet as ft

from components.genericButton import genericButton 

def login(page: ft.Page):

    async def to_signup(e):
        await page.push_route("/signup")

    async def to_home(e):
        await page.push_route("/home")

    user_login = ft.TextField(label="Enter Username/Email")
    user_pass = ft.TextField(label="Password", password=True, can_reveal_password=True)
    login_button = genericButton("Login", to_home)
    signup_button = genericButton("Don't have an acconut?", to_signup)

    login_page = ft.Container(
        border_radius=10,
        padding=16,
        bgcolor=ft.Colors.AMBER_800,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                user_login, user_pass,
                ft.Row(
                    alignment = ft.MainAxisAlignment.CENTER, 
                    controls=[
                        login_button, signup_button
                    ]
                )
            ]
        )
    )
    
    return login_page