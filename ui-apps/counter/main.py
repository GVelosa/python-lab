import asyncio

import flet as ft


def main(page: ft.Page):
    page.title = "Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    async def countdown(e):
        try:
            sec = int(seconds.value)
            while sec >= 0:
                warning_text.value = ""
                start.disabled = True
                count.value = str(sec)
                page.update()
                await asyncio.sleep(1)
                sec -= 1
            start.disabled = False
            start.update()
        except ValueError:
            warning_text.value = "Please enter a valid number."
            warning_text.update()
            return

    count = ft.Text(value="0", size=40)
    seconds = ft.TextField(label="Seconds", value = "", keyboard_type=ft.KeyboardType.NUMBER)
    start = ft.Button("Start Countdown", disabled=False,on_click=countdown)
    warning_text = ft.Text(value="", color=ft.Colors.RED)
    page.add(count, seconds, start, warning_text)

if __name__ == "__main__":
    ft.run(main)
