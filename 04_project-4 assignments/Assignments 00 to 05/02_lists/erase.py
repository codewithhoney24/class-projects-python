import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(event):
    """Erases objects in contact with the eraser by changing their color to white."""
    x, y = event.x, event.y

    # Get all items overlapping the eraser
    overlapping_objects = canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)
    
    for obj in overlapping_objects:
        if obj != eraser:
            canvas.itemconfig(obj, fill='white')

def move_eraser(event):
    """Moves the eraser with the mouse."""
    canvas.coords(eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
    erase_objects(event)

root = tk.Tk()
root.title("Eraser Tool")

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

# Create a grid of blue squares
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")

# Create the eraser
eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")

# Bind mouse movement to eraser
canvas.bind("<Motion>", move_eraser)

root.mainloop()
