import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# interesante cambiar los corchetes para ver los efectos
window = sg.Window("My To-DO App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box,edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica',20))

# con .read para la ejecución hasta que se hace algo
# interesante imprimir el evente

while True:
    event, values = window.read()
    print(1, event) # titulo button
    print(2, values) # key del input box y lo escrito en la caja
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index]= new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()
