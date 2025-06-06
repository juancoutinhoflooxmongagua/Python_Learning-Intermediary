tasks = []        
undo_stack = []   
redo_stack = []   

while True:
    print("\nEstado atual:", tasks)
    entry = input('Digite uma tarefa ou um comando ("listar", "desfazer", "refazer", "sair"): ').strip().lower()

    if entry == 'sair':
        break
    elif entry == 'listar':
        print("\nTarefas atuais:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif entry == 'desfazer':
        if undo_stack:
            redo_stack.append(tasks.copy())  
            tasks = undo_stack.pop()       
            print("Última ação desfeita.")
        else:
            print("Nada para desfazer!")
    elif entry == 'refazer':
        if redo_stack:
            undo_stack.append(tasks.copy())  
            tasks = redo_stack.pop()      
            print("Última ação refeita.")
        else:
            print("Nada para refazer!")
    else:
        undo_stack.append(tasks.copy()) 
        tasks.append(entry)             
        redo_stack.clear()            
        print(f'Tarefa "{entry}" adicionada com sucesso.')