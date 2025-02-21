import tkinter as tk
from datetime import datetime

task_counter = 1

def add_task():
    global task_counter
    task_text = task_entry.get().strip()
    if task_text:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        task_list.insert(tk.END, f"{task_counter}. {task_text}  [{timestamp}]")
        task_counter += 1
        task_entry.delete(0, tk.END)

def mark_done():
    selected_task = task_list.curselection()
    if selected_task:
        index = selected_task[0]
        task_list.itemconfig(index, {'fg': 'gray', 'font': ('Arial', 10, 'italic')})
        task_list.selection_clear(index)

def delete_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_list.delete(selected_task[0])

# GUI Setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("450x500")
root.configure(bg='#f0f0f0')

frame = tk.Frame(root, bg='#f0f0f0')
frame.pack(pady=20)

task_entry = tk.Entry(frame, width=40, font=('Arial', 12))
task_entry.pack(pady=5, padx=10)

button_frame = tk.Frame(frame, bg='#f0f0f0')
button_frame.pack()

add_button = tk.Button(button_frame, text="Add Task", command=add_task, font=('Arial', 10, 'bold'), bg='#4CAF50', fg='white', padx=10)
add_button.grid(row=0, column=0, padx=5, pady=5)

mark_done_button = tk.Button(button_frame, text="Mark as Done", command=mark_done, font=('Arial', 10, 'bold'), bg='#2196F3', fg='white', padx=10)
mark_done_button.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, font=('Arial', 10, 'bold'), bg='#f44336', fg='white', padx=10)
delete_button.grid(row=0, column=2, padx=5, pady=5)

task_list = tk.Listbox(frame, width=50, height=15, font=('Arial', 12), bg='white', fg='black', selectbackground='#d3d3d3')
task_list.pack(pady=10, padx=10)

root.mainloop()
