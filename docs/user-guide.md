# User Guide — Student Task Manager

This guide walks through using the Student Task Manager from the terminal.

## Starting the app

```bash
python main.py
```

You will see the main menu:

```
===== Student Task Manager =====
1. Add task
2. Display tasks
3. Complete task
4. Delete task
5. Exit
```

Type the number of an option and press Enter.

## 1. Adding a task

Choose **1**, then type the task title:

```
Choose an option (1-5): 1
Enter task title: Revise DevOps notes
Task added with ID 1.
```

**Validation:** titles cannot be empty. If you press Enter without typing
anything (or type only spaces), the app refuses the task:

```
Enter task title:
Error: Task title cannot be empty.
```

## 2. Displaying tasks

Choose **2** to see all tasks. `[ ]` means pending, `[x]` means completed:

```
Your tasks:
[ ] 1. Revise DevOps notes
[x] 2. Submit CSC418 assignment
```

If there are no tasks yet, the app says: `No tasks yet. Add one to get started!`

## 3. Completing a task

Choose **3**, then enter the ID shown in the display list:

```
Enter the ID of the task to complete: 1
Task 1 marked as completed.
```

If the ID does not exist, nothing changes and you see
`No task found with ID 99.` — the same happens if you type something that
is not a number (`Error: task ID must be a number.`).

## 4. Deleting a task

Choose **4**, then enter the ID:

```
Enter the ID of the task to delete: 2
Task 2 deleted.
```

As with completing, an invalid ID deletes nothing and shows a message.

## 5. Exiting

Choose **5** to quit:

```
Goodbye!
```

## Tips

- IDs are assigned automatically in order and are shown in the display list —
  always check the ID there before completing or deleting.
- Tasks are held in memory for the session, so add, complete and delete within
  one run of the app.
