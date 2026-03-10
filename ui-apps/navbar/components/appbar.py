import flet as ft

def create_appbar(page_name: str):

    # def handle_checked_item_click(e: ft.Event[ft.PopupMenuItem]):
    #     e.control.checked = not e.control.checked

    appbar = ft.AppBar(
        # leading=ft.Icon(ft.Icons.PALETTE),
        # leading_width=40,
        title=ft.Text(page_name, color="#bbc3cd"),
        center_title=True,
        bgcolor="#14151c",
        actions=[
            ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
            # ft.PopupMenuButton(
            #     items=[
            #         ft.PopupMenuItem(content="Item 1"),
            #         ft.PopupMenuItem(),  # divider
            #         ft.PopupMenuItem(
            #             content="Checked item",
            #             checked=False,
            #             on_click=handle_checked_item_click,
            #         ),
            #     ]
            # ),
        ],
    )

    return appbar