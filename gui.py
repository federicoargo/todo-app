import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

# interesante cambiar los corchetes para ver los efectos
window = sg.Window("My To-DO App", layout=[[label], [input_box, add_button]])
# con .read para la ejecución hasta que se hace algo
window.read()
print("hello")
window.close()
