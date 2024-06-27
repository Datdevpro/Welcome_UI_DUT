import tkinter as tk
import time
from datetime import datetime
import math
 
# Height and width of Analog clock window
# Create a Tkinter window
root = tk.Tk()
root.title("Analog Clock")
root.geometry("600x600")
# Constants for clock size
CLOCK_WIDTH = 400
CLOCK_HEIGHT = 400
CLOCK_CENTER_X = CLOCK_WIDTH // 2
CLOCK_CENTER_Y = CLOCK_HEIGHT // 2
CLOCK_RADIUS = min(CLOCK_WIDTH, CLOCK_HEIGHT) // 2 - 20

# Function to draw the clock
def draw_clock():
    current_time = datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second
    
    # Clear canvas
    canvas.delete("all")
    
    # Draw clock outline
    canvas.create_oval(CLOCK_CENTER_X - CLOCK_RADIUS, CLOCK_CENTER_Y - CLOCK_RADIUS,
                       CLOCK_CENTER_X + CLOCK_RADIUS, CLOCK_CENTER_Y + CLOCK_RADIUS, width=5, outline="black")
    
    # Draw hour hand
    hour_angle = math.radians((hour % 12) * 30 - 90)
    hour_x = CLOCK_CENTER_X + 0.6 * CLOCK_RADIUS * math.cos(hour_angle)
    hour_y = CLOCK_CENTER_Y + 0.6 * CLOCK_RADIUS * math.sin(hour_angle)
    canvas.create_line(CLOCK_CENTER_X, CLOCK_CENTER_Y, hour_x, hour_y, width=4)
    
    # Draw minute hand
    minute_angle = math.radians(minute * 6 - 90)
    minute_x = CLOCK_CENTER_X + 0.8 * CLOCK_RADIUS * math.cos(minute_angle)
    minute_y = CLOCK_CENTER_Y + 0.8 * CLOCK_RADIUS * math.sin(minute_angle)
    canvas.create_line(CLOCK_CENTER_X, CLOCK_CENTER_Y, minute_x, minute_y, width=3)
    
    # Draw second hand
    second_angle = math.radians(second * 6 - 90)
    second_x = CLOCK_CENTER_X + 0.9 * CLOCK_RADIUS * math.cos(second_angle)
    second_y = CLOCK_CENTER_Y + 0.9 * CLOCK_RADIUS * math.sin(second_angle)
    canvas.create_line(CLOCK_CENTER_X, CLOCK_CENTER_Y, second_x, second_y, fill="red", width=2)
    
    # Draw clock center
    canvas.create_oval(CLOCK_CENTER_X - 5, CLOCK_CENTER_Y - 5, CLOCK_CENTER_X + 5, CLOCK_CENTER_Y + 5, fill="black")

    # Schedule next clock update after 1000 milliseconds (1 second)
    root.after(1000, draw_clock)

# Create a canvas to draw the clock
canvas = tk.Canvas(root, width=CLOCK_WIDTH, height=CLOCK_HEIGHT, bg="white")
canvas.pack()

# Start drawing the clock
draw_clock()

# Run the Tkinter event loop
root.mainloop()