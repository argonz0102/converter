import PySimpleGUI as sg

layout = [
    [sg.Input(key = '-Input-'),sg.Spin(['km til mil','kg til pound','sec til min'], key = '-Units-'), sg.Button('Konverter', key = '-Convert-')],
    [sg.Text('Output', key = '-Output-')]
]

window = sg.Window('Konverterer',layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-Convert-':
        input_value = values['-Input-']
        if input_value.isnumeric():
            match values['-Units-']:
                case 'km til mil':
                    output = round(float(input_value) * 0.6214,2)
                    output_string = f'{input_value} km er {output} engelske mil.'
                case 'kg til pound':
                    output = round(float(input_value) * 2.20462,2)
                    output_string = f'{input_value} kg er {output} pounds.'
                case 'sec til min':
                    output = round(float(input_value) / 60,2)
                    output_string = f'{input_value} sek er {output} min.'

            window['-Output-'].update(output_string)
        else:
            window['-Output-'].update('Skriv et tall')
window.close()

