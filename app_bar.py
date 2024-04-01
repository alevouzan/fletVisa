import flet as ft
from State import global_state

def app_bar(page: ft.Page):
    return ft.AppBar(
        title=ft.Text("Koumanias Visa"),
        center_title=True,  # Optional: Center the title
        actions=[
            ft.IconButton(icon=ft.icons.LOGOUT, on_click=lambda e: logout(page))
        ]
    )


def logout(page: ft.Page):
    # Reset the username state (if you want)
    username_state = global_state.get_state_by_key("username")
    if username_state:
        username_state.set_state(None)  # Or whatever logic you want to clear the state

    # Navigate back to the login page 
    page.go("/")






