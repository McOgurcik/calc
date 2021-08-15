import PySimpleGUI as sg
def otvet_layout():
    otvet_layout = [[sg.Multiline('   '+a+'   ')],[sg.Button('Exit')]]
    return otvet_layout
def otvet(otvet):
    global a
    a = otvet
    a = str(a)
    window_o = sg.Window('otvet',otvet_layout(),icon='name.ico')
    while True:
        event, values = window_o.read()
        # print(event, values)
        if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

           window_o.close()
           break
if __name__ == '__main__':
    print('Пожалуйста запустите исполнительный файл')
