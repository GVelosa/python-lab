import flet as ft

from components.genericButton import genericButton 

def signup(page: ft.Page):
    
    async def to_login(e):
        await page.push_route("/")

    
    async def to_home(e):
        user_infos = {
            "name": user_name.value,
            "email": user_email.value,
            "pass" : user_pass.value,
            "confirm_pass": confirm_pass.value 
        }
        if not all([
            user_name.value,
            user_email.value,
            user_pass.value,
            confirm_pass.value
        ]):
            print("Missing information")
            return
        if user_pass.value != confirm_pass.value:
            print("Passwords do not match")
            return
        await page.push_route("/home")
        print(user_infos)


    user_name = ft.TextField(label="Enter Username")
    user_email = ft.TextField(label="Enter Email")
    user_pass = ft.TextField(label="Create Password")
    confirm_pass = ft.TextField(label="Confirm Password")
    signup_button = genericButton("SignUp", to_home)
    login_button = genericButton("Alredy has an acconut?", to_login)
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
                user_name, user_email, user_pass, confirm_pass, ft.Divider(), buttons_row
                
            ]
        )
    )
    
    
    return signup_page