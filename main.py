import PySimpleGUI as sg

sg.theme("DarkAmber")

layout = [
    [sg.Text("Password : "), sg.InputText("")],
    [name('Image'), sg.Image(sg.EMOJI_BASE64_HAPPY_THUMBS_UP)],
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