import flet as ft

from components.genericButton import genericButton 
from database.operations import create_user

def signup_view(page: ft.Page):
    
    async def to_login(e):
        await page.push_route("/")

    
    def user_create(e):
        name = user_name.value
        email = user_email.value
        password = user_pass.value

        if not all([
            user_name.value,
            user_email.value,
            user_pass.value,
            confirm_pass.value
        ]):
            confirm_text.value = "Missing information!"
            return
        if user_pass.value != confirm_pass.value:
            confirm_text.value = "Passwords do not match!"
            return
        if "@" not in user_email.value:
            confirm_text.value = "Invalid email!"
            return
        
        create_user(name, email, password)
        confirm_text.value = "Account Created! You Can Now Login!"
        confirm_text.color=ft.Colors.GREEN
        user_name.value = ""
        user_email.value = ""
        user_pass.value = ""
        confirm_pass.value = ""
        page.update()

    user_name = ft.TextField(label="Enter Username")
    user_email = ft.TextField(label="Enter Email")
    user_pass = ft.TextField(label="Create Password", password=True, can_reveal_password=True)
    confirm_pass = ft.TextField(label="Confirm Password", password=True, can_reveal_password=True)
    signup_button = genericButton("SignUp", user_create)
    login_button = genericButton("Alredy has an acconut?", to_login)
    confirm_text = ft.Text(value="", color=ft.Colors.RED)
    buttons_row = ft.Row(
                    alignment = ft.MainAxisAlignment.CENTER,
                    controls=[
                        signup_button, login_button
                    ]
                )

    signup_page = ft.Container(
        border_radius=10,
        padding=16,
        bgcolor=ft.Colors.AMBER_800,
        content= ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                user_name, user_email, user_pass, confirm_pass, ft.Divider(), buttons_row, confirm_text
                
            ]
        )
    )
    
    
    return signup_page