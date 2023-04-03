import PySimpleGUI as sg
import qrcode

layout = [
    [sg.Input(key="Text")],
    [sg.Button("Create")],
    [sg.Image(key="QR")],
]

window = sg.Window("QR Code Generator", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Create":
        text = values["Text"]
        img = qrcode.make(text)
        img.save("qr.png")
        window["QR"].update(filename="qr.png")

window.close()
 
