import PySimpleGUI as sg

sg.theme("DarkAmber")

layout = [
    [sg.Text("Password : "), sg.InputText("")],
    [sg.Text("Username : "), sg.InputText("")],
    [sg.Button("Login"), sg.Button("Exit")]
]

window = sg.Window('Login Screen', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "Login":
        print("Login")
    print(values[0])

window.close()