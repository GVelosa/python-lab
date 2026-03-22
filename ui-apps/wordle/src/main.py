import flet as ft

def main(page: ft.Page):
    page.title = "Wordle Clone"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    async def next_field(e, next_control):
        if len(e.control.value) == 1:
            await next_control.focus()

    game_title = ft.Text(
        "Wordle Clone",
        theme_style=ft.TextThemeStyle.HEADLINE_LARGE
    )

    letter_1 = ft.TextField(capitalization=ft.TextCapitalization.WORDS, max_length=1, width=50)
    letter_2 = ft.TextField(capitalization=ft.TextCapitalization.WORDS, max_length=1, width=50)
    letter_3 = ft.TextField(capitalization=ft.TextCapitalization.WORDS, max_length=1, width=50)
    letter_4 = ft.TextField(capitalization=ft.TextCapitalization.WORDS, max_length=1, width=50)
    letter_5 = ft.TextField(capitalization=ft.TextCapitalization.WORDS, max_length=1, width=50)

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

    page.add(
        game_title,
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[letter_1, letter_2, letter_3, letter_4, letter_5]
        )
    )

ft.run(main)