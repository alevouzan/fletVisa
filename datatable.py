import flet as ft


class ApplicantDataTable(ft.DataTable):
    def __init__(self):
        super().__init__(
            columns=[
                ft.DataColumn(ft.Text('Name')),
                ft.DataColumn(ft.Text('Surname')),
                ft.DataColumn(ft.Text('Date')),
                ft.DataColumn(ft.Text('Actions')),  # Placeholder for actions
            ],
            rows=[]  # Initially empty rows
        )

    def update_data(self, applicants):
        self.rows = [
            fr.DataRow([
                ft.DataCell(ft.Text(applicant[1])),  # Name
                ft.DataCell(ft.Text(applicant[2])),  # Surname
                ft.DataCell(ft.Text(applicant[5].strftime("%Y-%m-%d"))),  # Formatted date
                ft.DataCell(ft.Text(''))  # Placeholder for actions
            ]) for applicant in applicants
        ]
        self.update()
