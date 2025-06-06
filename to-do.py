import json
import os

FILE_NAME = "tasks_data.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"tasks": [], "undo_stack": [], "redo_stack": []}

def save_data(tasks, undo_stack, redo_stack):
    data = {
        "tasks": tasks,
        "undo_stack": undo_stack,
        "redo_stack": redo_stack
    }
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

data = load_data()
tasks = data["tasks"]
undo_stack = data["undo_stack"]
redo_stack = data["redo_stack"]

while True:
    print("\nEstado atual:", tasks)
    entry = input('Digite uma tarefa ou um comando ("listar", "desfazer", "refazer", "sair"): ').strip().lower()

    if entry == 'sair':
        save_data(tasks, undo_stack, redo_stack)
        break
    elif entry == 'listar':
        print("\nTarefas atuais:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif entry == 'desfazer':
        if undo_stack:
            redo_stack.append(tasks.copy())
            tasks = undo_stack.pop()
            save_data(tasks, undo_stack, redo_stack)
            print("Última ação desfeita.")
        else:
            print("Nada para desfazer!")
    elif entry == 'refazer':
        if redo_stack:
            undo_stack.append(tasks.copy())
            tasks = redo_stack.pop()
            save_data(tasks, undo_stack, redo_stack)
            print("Última ação refeita.")
        else:
            print("Nada para refazer!")
    else:
        undo_stack.append(tasks.copy())
        tasks.append(entry)
        redo_stack.clear()
        save_data(tasks, undo_stack, redo_stack)
        print(f'Tarefa "{entry}" adicionada com sucesso.')