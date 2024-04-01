import flet as ft
from router import Router 
from app_bar import app_bar



def main(page: ft.Page):
    #page.theme_mode = "dark"
    router = Router(page)
    page.on_route_change = router.route_change
    router.page = page  

    def update_appbar():
        if page.route != "/":  # Show appbar on all routes except '/'
            page.appbar = app_bar(page)
        else:
            page.appbar = None  # Remove appbar for the login route
        page.update()

    update_appbar()

ft.app(target=main, assets_dir="assets")
