import flet as ft
import random

# from database.operations import consult_user

employee_code = random.randint(10000, 99999)
manager_id = random.randint(100, 999)
# userenames = consult_user()

def create_employee_view(page: ft.Page):


    def on_click():
        print(employment_type.value)
    #     create_employee(
    #         employee_name.value,
    #         employee_code,
    #         int(job_title_id.value),
    #         int(department_id.value),
    #         is_manager.value,
    #         manager_id if is_manager else None,
    #         float(salary.value),
    #         hire_date.value,
    #         float(performance_score.value) if performance_score.value else None,
    #         status.value,
    #         employment_type.value
    #     )

    employee_name = ft.TextField(label="Name")
    # employee_code = ft.TextField(label="Employee Code")
    job_title_id = ft.TextField(label="Job Title ID")
    department_id = ft.TextField(label="Department ID")
    is_manager = ft.Switch(label="Is Manager?")
    # manager_id = ft.TextField(label="Manager ID (optional)")
    salary = ft.TextField(label="Salary")
    hire_date = ft.TextField(label="Hire Date (YYYY-MM-DD)")
    performance_score = ft.TextField(label="Performance Score (optional)")
    status = ft.Dropdown(label="Employee Status")
    employment_type = ft.Dropdown(label="Employment Type", options=[])

    create_button = ft.ElevatedButton("Create Employee", on_click=on_click)

    create_employee = ft.Column(
        controls=[
            employee_name,
            job_title_id,
            department_id,
            is_manager,
            salary,
            hire_date,
            performance_score,
            status,
            employment_type,
            create_button
        ]
    )

    return create_employee