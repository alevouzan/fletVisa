import flet as ft
from State import State


class LoginView(ft.UserControl):
    def __init__(self):
        super().__init__() 
        self.username_input = ft.TextField(label="Username")
        self.password_input = ft.TextField(label="Password",  password=True, can_reveal_password=True) 
        self.error_text = ft.Text("")  # For error messages

    def build(self):
        return ft.Column([
            ft.Text("Login Page"),
            self.username_input,
            self.password_input,
            ft.ElevatedButton("Login", on_click=self.handle_login),
            self.error_text  # Display the error if any
        ])

    def handle_login(self, e):
        username = self.username_input.value
        password = self.password_input.value

        if self.authenticate(username, password):
            print(f"Username to be passed: {username}") # Add this line
            username_state = State("username",username)
            self.page.go("/home")
        else:
            self.error_text.value = "Invalid username or password"
            self.page.update() 

    def authenticate(self, username, password):
        with open('users.txt', 'r') as file:
            for line in file:
                stored_username, stored_password = line.strip().split(':')
                if username == stored_username and password == stored_password:
                    return True  
        return False 
