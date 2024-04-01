import flet as ft
from views.home_view import HomeView
from views.login_view import LoginView
from app_bar import app_bar


class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.routes = {
            "/": LoginView(), 
            "/home": HomeView(), 
        }
        self.page.add(self.routes["/"])

    def route_change(self, route):
        #print("1")
        #print(self.page.controls)
        #print(self.routes[route.route])
        #print(self.routes)
        #print("2")
        self.page.controls.pop()
        self.page.add(self.routes[route.route])
        self.page.update()

        update_appbar(self.page)




def update_appbar(page: ft.Page):  
    if page.route != "/": 
        page.appbar = app_bar(page)
    else:
        page.appbar = None 
    page.update()