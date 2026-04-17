import flet as ft

from components.guess_field import guess_field

def single_game_view(page: ft.Page):

    async def next_field(e, next_control):
        if len(e.control.value) == 1:
            await next_control.focus()

    game_title = ft.Text(
        "Wordle Clone",
        theme_style=ft.TextThemeStyle.HEADLINE_LARGE
    )

    letter_1 = guess_field()
    letter_2 = guess_field()
    letter_3 = guess_field()
    letter_4 = guess_field()
    letter_5 = guess_field()

    async def l1(e):
        await next_field(e, letter_2)

    async def l2(e):
        await next_field(e, letter_3)

    async def l3(e):
        await next_field(e, letter_4)

    async def l4(e):
        await next_field(e, letter_5)

    letter_1.on_change = l1
    letter_2.on_change = l2
    letter_3.on_change = l3
    letter_4.on_change = l4

    single_game = ft.Column(
        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        controls=[
            game_title,
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[letter_1, letter_2, letter_3, letter_4, letter_5]
            )
        ]
    )

    return single_game