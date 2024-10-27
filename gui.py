import functions
import FreeSimpleGUI as sg
import time

# para el tema del programa
# buscar pysimplegui themes en google
# sg.theme("DarkPurple4")
sg.theme("Black")

clock = sg.Text('',key='clock')
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
add_button = sg.Button("Add",size=10)
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45,10])
# el 45 es el número de filas, el 10 el de caracteres
# ver en Listbox, botón derecho, goto-> implementations
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# interesante cambiar los corchetes para ver los efectos
window = sg.Window("My To-DO App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box,edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica',20))

# con .read para la ejecución hasta que se hace algo
# interesante imprimir el evente

while True:
    # con timeout = 10 el ciclo se ejecuta cada 10 milisegundos,
    # mejor cada 200 milisegundos que sigue permitiendo ver los
    # segundos cambiar
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    """ print(1, event) # titulo button
    print(2, values) # key del input box y lo escrito en la caja
    print(3, values['todos'])"""
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index]= new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please, select an item first.", font=("Helvetica",20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please, select an item first.", font=("Helvetica",20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()
