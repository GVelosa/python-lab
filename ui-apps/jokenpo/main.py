import flet as ft
import random

def main(page: ft.Page):
    #Configs
    page.title = "Jo-Ken-Po"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    Ico_Size = 50
    Ico_Color = "04283D"
    Ico_Bg = ft.Colors.BLUE_GREY_100

    #Funções
    def player_selection(selected: int):
        bot = random.randint(1,3)
        bot_selection(bot, bot_choice)
        bot_choice.update()
        game(selected, bot)
    
    def bot_selection(selection: int, bot_choice: ft.Icon):
        match selection:
            case 1:
                bot_choice.icon = ft.Icons.DIAMOND
            case 2:
                bot_choice.icon = ft.Icons.CONTENT_CUT
            case 3:
                bot_choice.icon = ft.Icons.ARTICLE_SHARP
            case _:
                pass
    
    def game(selected: int, bot: int):
        if selected == 1 and bot == 2 or selected == 2 and bot == 3 or selected == 3 and bot == 1:
            result.value = "Você ganhou"
            result.color = ft.Colors.GREEN
            player_score.value+=1
            player_score.update()
        elif selected == bot:
            result.value = "Empatou"
            result.color = ft.Colors.YELLOW
        else:
            result.value = "Você perdeu"
            result.color = ft.Colors.RED
            bot_score.value+=1
            bot_score.update()
        result.update()

    #Itens
    ##Text
    title = ft.Text("Jo-Ken-Po", theme_style=ft.TextThemeStyle.HEADLINE_LARGE)
    title2 = ft.Text("Select a option to play the game:",
    theme_style=ft.TextThemeStyle.TITLE_LARGE)
    bot_text = ft.Text("Seleção do Bot:")
    result = ft.Text(value="")
    player_score = ft.Text(value=0, color=ft.Colors.BLACK, size=40)
    bot_score = ft.Text(value=0, color=ft.Colors.BLACK, size=40)

    ##Buttons
    rock = ft.FilledIconButton(ft.Icons.DIAMOND, on_click=lambda e: player_selection(1), icon_size=Ico_Size, icon_color=Ico_Color, bgcolor=Ico_Bg)
    scissors = ft.FilledIconButton(ft.Icons.CONTENT_CUT, on_click=lambda e: player_selection(2), icon_size=Ico_Size, icon_color=Ico_Color, bgcolor=Ico_Bg)
    paper = ft.FilledIconButton(ft.Icons.ARTICLE_SHARP, on_click=lambda e: player_selection(3), icon_size=Ico_Size, icon_color=Ico_Color, bgcolor=Ico_Bg)

    ##Icons
    bot_choice = ft.Icon(icon=None, size=Ico_Size)
    player_icon  = ft.Icon(ft.Icons.FACE_6, size=30, color=ft.Colors.BLACK)
    bot_icon = ft.Icon(ft.Icons.SMART_TOY, size=30, color=ft.Colors.BLACK)
    
    ##Box
    player_box = ft.Container(
    content=ft.Row([player_icon, player_score], alignment=ft.MainAxisAlignment.CENTER),
    bgcolor=ft.Colors.BLUE_50,
    border_radius=10,
    border=ft.Border.all(3, ft.Colors.BLUE_400),
    width=100,
    )
    
    bot_box = ft.Container(
        content=ft.Row([bot_icon, bot_score], alignment=ft.MainAxisAlignment.CENTER),
        bgcolor=ft.Colors.RED_50,
        border_radius=10,
        border=ft.Border.all(3, ft.Colors.RED_400),
        width=100,
    )

    #add
    page.add(
         ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                player_box, bot_box
            ]
        ),
        title, title2,
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                rock,paper,scissors
            ]
        ),
        bot_text, bot_choice, ft.Text("Resultado:"),result
    )

ft.run(main)