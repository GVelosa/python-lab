import flet as ft

from database.operations import create_department, consult_manager

managers_infos = consult_manager()

def create_departments(page: ft.Page):
    
    def manager_options():
        if managers_infos:
            return [ft.DropdownOption(key=managers) for managers in managers_infos[0]]
        else:
            return None

    # def manager_name_to_id():
    #     if manager.value

    def on_click():
        create_department(title.value, manager.value)

    title = ft.TextField(label="Dapartment Name")
    manager = ft.Dropdown(label="Department Manager", options=manager_options())
    create_button = ft.Button("Create New Department", on_click=on_click)
    create_departments = ft.Column(
        controls=[
            title, manager, create_button
        ]
    )
    return create_departments