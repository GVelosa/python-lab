import flet as ft

def guess_field():
    return ft.TextField(
        capitalization=ft.TextCapitalization.WORDS,
        max_length=1,
        width=50
    )