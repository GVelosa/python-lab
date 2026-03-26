import flet as ft

from components.genericButton import genericButton 

def register(page: ft.Page):
    
    async def to_home(e):
        await page.push_route("/home")

    register_page = ft.Column(
        controls=[
            ft.Text("Página de Registro"),
            ft.Button("Home", on_click=to_home)
        ]
    )
    
    return register_page