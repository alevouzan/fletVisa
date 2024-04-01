import flet as ft
from flet import DataTable,DataColumn,DataRow,DataCell
from State import global_state
from dbconnector import connect_to_db,create_applicant,get_visa_applicants

from datatable import ApplicantDataTable  # Import your DataTable class 


def input_dialog(page: ft.Page):
    name_input = ft.TextField(label="Name", border_color=ft.colors.PRIMARY)
    surname_input = ft.TextField(label="Surname", border_color=ft.colors.PRIMARY)
    email_input = ft.TextField(label="Email", border_color=ft.colors.PRIMARY)
    country_input = ft.TextField(label="Country", border_color=ft.colors.PRIMARY)

    def close_dialog(e):
        name_input.border_color = ft.colors.PRIMARY
        surname_input.border_color = ft.colors.PRIMARY
        dlg.open = False
        page.update()


    def submit(e):
        name = name_input.value
        surname = surname_input.value
    

        # Validation
        if not name or not surname:
            name_input.border_color = ft.colors.RED
            surname_input.border_color = ft.colors.RED
            page.update() 
            return 
    
        # If validation passes
        name_input.border_color = ft.colors.PRIMARY
        surname_input.border_color = ft.colors.PRIMARY
        page.update()

    
        # Get other Input Values 
        email = email_input.value
        country = country_input.value
    
        # Do something with the submitted data
        print(f"Name: {name}, Surname: {surname}, Email: {email}, Country: {country}")
        
        # Save to database
        success = create_applicant(name, surname, email, country)
        if success:
            print("Applicant saved successfully!")
        else:   
            print("Error saving to database.")


        # Close the dialog
        dlg.open = False
        page.update()


    dlg = ft.AlertDialog(
        title=ft.Text("User Details"),
        content=ft.Column([name_input, surname_input, email_input, country_input]),
        actions=[
            ft.ElevatedButton("Submit", on_click=submit),
            ft.TextButton("Cancel", on_click=close_dialog),
        ],
        on_dismiss=lambda e: print("Dialog dismissed!"),
    )
    return dlg



class HomeView(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.greeting_text = ft.Text()
        self.open_dialog_button = ft.ElevatedButton("Open Dialog", on_click=self.show_dialog)
        self.dialog = None

        self.datatable = ApplicantDataTable()

    def did_mount(self):
        self.populate_datatable()


    def build(self):
        username_state = global_state.get_state_by_key("username")
        username = username_state.get_state() if username_state else "Guest"
        self.greeting_text.value = f"Welcome, {username}!" 

        # Create the Tabs control
        #self.tabs = ft.Tabs(  
        #    selected_index=0, 
        #    tabs=[
        #        ft.Tab(text="All Applicants", icon=ft.icons.VIEW_LIST),
        #        ft.Tab(text="Active", icon=ft.icons.CHECK_CIRCLE_OUTLINE),
        #        ft.Tab(text="Archive", icon=ft.icons.ARCHIVE_OUTLINED ),
        #        
        #    ],
        #    on_change=self.tabs_changed
        #)
       
        # Initial content assignment
        #self.current_tab_content = ft.Container(content=self.all_applicants_content) 

        return ft.Column([
            self.greeting_text,
            self.open_dialog_button,
            self.datatable,
            #self.tabs,
            #self.current_tab_content,
        ])

    #Dialog for Create New
    def show_dialog(self, e):
        if self.dialog is None:
            self.dialog = input_dialog(self.page) 
    
        # Add the dialog to the page, if we haven't already
        if self.dialog not in self.page.controls:
            self.page.add(self.dialog)
    
        self.dialog.open = True 
        self.page.update()


    # This method will be responsible for fetching and populating data
    def populate_datatable(self):
        all_applicants = get_visa_applicants()  
        print(f"All Applicants: {all_applicants}") 

        self.datatable.rows = [
            DataRow([
                DataCell(ft.Text(applicant[1])),  # Name
                DataCell(ft.Text(applicant[2])),  # Surname
                DataCell(ft.Text(applicant[5].strftime("%Y-%m-%d"))),  # Formatted date
                DataCell(ft.Text(''))  # Placeholder for actions
            ]) for applicant in all_applicants
        ]
        self.datatable.update()




#    def tabs_changed(self, e):
#        selected_index = e.control.selected_index
#        self.current_tab_content.content.controls.clear()  
#    
#        if selected_index == 0:
#            self.current_tab_content.content = self.all_applicants_content
#            print("Assigned All Applicants Content:", self.current_tab_content.content)
#        elif selected_index == 1:
#            self.current_tab_content.content = self.active_applicants_content
#            print("Assigned active Applicants Content:", self.current_tab_content.content)
#        elif selected_index == 2:
#            self.current_tab_content.content = self.archive_applicants_content
#            print("Assigned archive Applicants Content:", self.current_tab_content.content.content)
#        
#        # Force update before refreshing data
#        self.current_tab_content.content.update()
#    
#        self.refresh_tab_content() 
#
#
#
#    def populate_initial_tab(self):
#        self.refresh_tab_content() # Update the initial tab's data
#
#    def refresh_tab_content(self):
#        all_applicants = get_visa_applicants()
#        print(f"All Applicants: {all_applicants}")
#        active_applicants = [app for app in all_applicants if not app[6]] 
#        archive_applicants = [app for app in all_applicants if app[6]]
#
#        # Populate DataTables using applicants data 
#        self.all_datatable.update_data(all_applicants)
#        self.active_datatable.update_data(active_applicants)
#        self.archive_datatable.update_data(archive_applicants)