import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
add_button = sg.Button("Add")

# interesante cambiar los corchetes para ver los efectos
window = sg.Window("My To-DO App",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica',20))

# con .read para la ejecución hasta que se hace algo
# interesante imprimir el evente

while True:
    event, values = window.read()
    print(event) # titulo button
    print(values) # key del input box y lo escrito en la caja
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close()
