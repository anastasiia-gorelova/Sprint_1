new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006'] 

for index_task in range(len(new_tasks)):
    if new_tasks[index_task] == 'task_005':
        completed_tasks.append(new_tasks.pop(index_task))
        break

new_tasks.remove('task_007')

last_task = new_tasks[-1]

print(last_task)