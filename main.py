import PySimpleGUI as sg
import yaml
import pyperclip
import json

def get_options(file_path):
    with open(file_path, 'r') as file:
        options = yaml.load(file, Loader=yaml.FullLoader)
    return options

options = get_options('options.yaml')
#fields: Option, Detail level, Output style, Photo adjust, Camera adjusts 
#Styles = options.Styles
menuOptions = list(options.keys())
print(menuOptions)
styleOptions = options["Style"]
artistOptions = options["Artist"]
optionOptions = options["Option"]
detailLevelOptions = options["Detail level"]
outputStyleOptions = options["Output style"]
cameraAdjustsOptions = options["Camera adjusts"]

layout = [[sg.Text('Choose the values of your prompt below:')]]
# First the window layout in 2 columns

outputStyle_block = [
    [sg.Text('Output style')],
    [sg.InputText(size=(20, 1), enable_events=True, key='-INPUT-OUTPUT-STYLE-')],
    [sg.Listbox(outputStyleOptions, size=(20, 4), enable_events=True, key='-LIST-OUTPUT-STYLE-')],
    [sg.HorizontalSeparator()]
]

style_block = [
    [sg.Text('Style')],
    [sg.InputText(size=(20, 1), enable_events=True, key='-INPUT-STYLE-')],
    [sg.Listbox(styleOptions, size=(20, 4), enable_events=True, key='-LIST-STYLE-')],
    [sg.HorizontalSeparator()]
]

camera_block = [
    [sg.Text('Camera adjust')],
    [sg.InputText(size=(20, 1), enable_events=True, key='-INPUT-CAMERA-ADJUST-')],
    [sg.Listbox(cameraAdjustsOptions, size=(20, 4), enable_events=True, key='-LIST-CAMERA-ADJUST-')],
    [sg.HorizontalSeparator()]
]
artist_block = [
    [sg.Text('Artist')],
    [sg.InputText(size=(20, 1), enable_events=True, key='-INPUT-ARTIST-')],
    [sg.Listbox(artistOptions, size=(20, 4), enable_events=True, key='-LIST-ARTIST-')],
    [sg.HorizontalSeparator()]
]

option_block = [
    [sg.Text('Option')],
    [sg.InputText(size=(20, 1), enable_events=True, key='-INPUT-OPTION-')],
    [sg.Listbox(optionOptions, size=(20, 4), enable_events=True, key='-LIST-OPTION-')],
    [sg.HorizontalSeparator()]
]

detail_level_block = [
    [sg.Text('Detail level:')],
    [sg.InputText(size=(20, 1), enable_events=True, key='-INPUT-DETAIL-LEVEL-')],
    [sg.Listbox(detailLevelOptions, size=(20, 4), enable_events=True, key='-LIST-DETAIL-LEVEL-')],
    [sg.HorizontalSeparator()]
]

# ----- Full layout -----
layout = [
    [[sg.Column(style_block),
     sg.VSeperator(),
     sg.Column(artist_block),
     sg.VSeperator(),
     sg.Column(option_block)
     ],
     [sg.Column(detail_level_block),
     sg.VSeperator(),
     sg.Column(outputStyle_block),
     sg.VSeperator(),
     sg.Column(camera_block)
],     
     ],
]

layout.append([sg.Text('Enter image topic:'), sg.InputText(key='TOPIC')])
layout.append([sg.Button('Submit'), sg.Button('Exit')])
layout.append([sg.Text('Output: '), sg.InputText(key='output', size=(40,1))])
layout.append([sg.Button('Copy to clipboard', key='copy', visible=False)])

    
window = sg.Window('Image Prompt Generator', layout)

#function to fetch my world in data and retrieve info about brazil violence
while True:
    event, values = window.read()

    if event == 'Submit':
        output = values["TOPIC"]+ ', '  + values['-INPUT-STYLE-']+ ', '  + values['-INPUT-ARTIST-'] + ', '  + values['-INPUT-OPTION-']+ ', '  + values['-INPUT-DETAIL-LEVEL-']+ ', '  + values['-INPUT-OUTPUT-STYLE-']+ ', '  + values['-INPUT-CAMERA-ADJUST-']
        window['output'].update(output)
        window['copy'].update(visible=True)
    if event == 'copy':
        pyperclip.copy(values['output'])    # display in the listbox
    if values['-INPUT-STYLE-']  is not None:
        if values['-INPUT-STYLE-'] != '':                         # if a keystroke entered in search field
            search = values['-INPUT-STYLE-']
            new_values = [x for x in styleOptions if search in x]  # do the filtering
            window['-LIST-STYLE-'].update(new_values)     # display in the listbox
        else:
            # display original unfiltered list
            window['-LIST-STYLE-'].update(styleOptions)
            # if a list item is chosen
        if event == '-LIST-STYLE-' and len(values['-LIST-STYLE-']):
            selected_option = values['-LIST-STYLE-'][0]  # Get the first selected option
            window['-INPUT-STYLE-'].update(selected_option)  # Update the input field with the selected option
    if values['-INPUT-ARTIST-']  is not None:
        if values['-INPUT-ARTIST-'] != '':                         # if a keystroke entered in search field
            search = values['-INPUT-ARTIST-']
            new_values = [x for x in artistOptions if search in x]  # do the filtering
            window['-LIST-ARTIST-'].update(new_values)     # display in the listbox
        else:
                # display original unfiltered list
            window['-LIST-ARTIST-'].update(artistOptions)
                # if a list item is chosen
        if event == '-LIST-ARTIST-' and len(values['-LIST-ARTIST-']):
            selected_option = values['-LIST-ARTIST-'][0]  # Get the first selected option
            window['-INPUT-ARTIST-'].update(selected_option)  # Update the input field with the selected option
        if values['-INPUT-OPTION-']  is not None:
            if values['-INPUT-OPTION-'] != '':                         # if a keystroke entered in search field
                search = values['-INPUT-OPTION-']
                new_values = [x for x in optionOptions if search in x]  # do the filtering
                window['-LIST-OPTION-'].update(new_values)     # display in the listbox
            else:
                    # display original unfiltered list
                window['-LIST-OPTION-'].update(optionOptions)
                    # if a list item is chosen
            if event == '-LIST-OPTION-' and len(values['-LIST-OPTION-']):
                selected_option = values['-LIST-OPTION-'][0]  # Get the first selected option
                window['-INPUT-OPTION-'].update(selected_option)  # Update the input field with the selected option
        if values['-INPUT-DETAIL-LEVEL-']  is not None:
            if values['-INPUT-DETAIL-LEVEL-'] != '':                         # if a keystroke entered in search field
                search = values['-INPUT-DETAIL-LEVEL-']
                new_values = [x for x in detailLevelOptions if search in x]  # do the filtering
                window['-LIST-DETAIL-LEVEL-'].update(new_values)     # display in the listbox
            else:
                    # display original unfiltered list
                window['-LIST-DETAIL-LEVEL-'].update(detailLevelOptions)
                    # if a list item is chosen
            if event == '-LIST-DETAIL-LEVEL-' and len(values['-LIST-DETAIL-LEVEL-']):
                selected_option = values['-LIST-DETAIL-LEVEL-'][0]  # Get the first selected option
                window['-INPUT-DETAIL-LEVEL-'].update(selected_option)  # Update the input field with the selected option 
        if values['-INPUT-OUTPUT-STYLE-']  is not None:
            if values['-INPUT-OUTPUT-STYLE-'] != '':                         # if a keystroke entered in search field
                search = values['-INPUT-OUTPUT-STYLE-']
                new_values = [x for x in outputStyleOptions if search in x]  # do the filtering
                window['-LIST-OUTPUT-STYLE-'].update(new_values)     # display in the listbox
            else:
                    # display original unfiltered list
                window['-LIST-OUTPUT-STYLE-'].update(outputStyleOptions)
                    # if a list item is chosen
            if event == '-LIST-OUTPUT-STYLE-' and len(values['-LIST-OUTPUT-STYLE-']):
                selected_option = values['-LIST-OUTPUT-STYLE-'][0]  # Get the first selected option
                window['-INPUT-OUTPUT-STYLE-'].update(selected_option)  # Update the input field with the selected option 
        if values['-INPUT-CAMERA-ADJUST-']  is not None:
            if values['-INPUT-CAMERA-ADJUST-'] != '':                         # if a keystroke entered in search field
                search = values['-INPUT-CAMERA-ADJUST-']
                new_values = [x for x in cameraAdjustsOptions if search in x]  # do the filtering
                window['-LIST-CAMERA-ADJUST-'].update(new_values)     # display in the listbox
            else:
                    # display original unfiltered list
                window['-LIST-CAMERA-ADJUST-'].update(cameraAdjustsOptions)
                    # if a list item is chosen
            if event == '-LIST-CAMERA-ADJUST-' and len(values['-LIST-CAMERA-ADJUST-']):
                selected_option = values['-LIST-CAMERA-ADJUST-'][0]  # Get the first selected option
                window['-INPUT-CAMERA-ADJUST-'].update(selected_option)  # Update the input field with the selected option 
    if event in (None, 'Exit'):
        break

window.close()
