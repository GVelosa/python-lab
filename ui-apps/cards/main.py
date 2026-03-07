import flet as ft
from components.card import create_card

def main(page: ft.Page):
    #Config Page
    page.title = "Navigations"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    card_QRCode = create_card(
        "assets/QRCodeGenerator.png",
        "QR-Code Generator",
        "A simple QR Code generator built in Python.")
    card_jokenpo = create_card(
        "assets/JoKenPoGame.png",
        "JoKenPo Game",
        "A classic Rock-Paper-Scissors(Jo-Ken-Po) game built in Python.")

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                card_QRCode, card_jokenpo
            ]
        )
    )   

if __name__ == "__main__":
    ft.run(main)
