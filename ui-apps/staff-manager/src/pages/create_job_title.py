import flet as ft

from database.operations import create_jobs_title

def create_job_title_view(page: ft.Page):
    
    def on_click():
        create_jobs_title(title.value)

    title = ft.TextField(label="Job Title")
    create_button = ft.Button("Create New Job Title", on_click=on_click)
    create_departments = ft.Column(
        controls=[
            title, create_button
        ]
    )
    return create_departments