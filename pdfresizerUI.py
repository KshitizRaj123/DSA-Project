import customtkinter as ctk
from PIL import Image, ImageTk
from pdfmergerlogic import merge_pdfs  # Import the function from pdfmergerlogic.py
from pdfresizerlogic import *  # Keep your other logic as required
#yes

# Set Dark Mode
ctk.set_appearance_mode("Dark")

# Initialize main window
root = ctk.CTk()
root.title("PDF Merger & Resizer")
#12
# Set window size
window_width = 1300
window_height = 850

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position for centering
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Frame Setup 
main_frame = ctk.CTkFrame(root, fg_color="transparent")  # Transparent frame
merge_frame = ctk.CTkFrame(root, fg_color="transparent")
resize_frame = ctk.CTkFrame(root, fg_color="transparent")

def show_frame(frame):
    """Switch to the given frame without removing background"""
    frame.tkraise()

# Set frames to fill the window
for frame in (main_frame, merge_frame, resize_frame):
    frame.place(relwidth=1, relheight=1)

# Main Screen UI 
# Textbox (Non-Editable)
textbox = ctk.CTkTextbox(main_frame, width=500, height=50, text_color='White', fg_color='brown', font=('Arial', 30))
textbox.insert("0.5", "Welcome to PDF Merger & Resizer")
textbox.configure(state="disabled")  # Make it non-editable
textbox.place(relx=0.2, rely=0.1)

# Merge PDF Image
image1 = ctk.CTkImage(light_image=Image.open("image1.png"), size=(300, 300))
label1 = ctk.CTkLabel(main_frame, image=image1, text="")
label1.place(relx=0.15, rely=0.3)

# Resize PDF Image
image2 = ctk.CTkImage(light_image=Image.open("image2.png"), size=(300, 300))
label2 = ctk.CTkLabel(main_frame, image=image2, text="")
label2.place(relx=0.68, rely=0.3)

# Buttons
button1 = ctk.CTkButton(main_frame, text="Merge PDF", fg_color="#210201", corner_radius=20,
                        hover_color='#E1C321', text_color='green', font=("Arial", 18),
                        command=lambda: show_frame(merge_frame))

button2 = ctk.CTkButton(main_frame, text="Resize PDF", fg_color='#210201', corner_radius=20,
                        hover_color='#E1C321', text_color='green', font=("Arial", 18),
                        command=lambda: show_frame(resize_frame))

button3 = ctk.CTkButton(main_frame, text="Exit", fg_color='#210201', corner_radius=20,
                        hover_color='#E1C321', text_color='green', font=("Arial", 18),
                        command=root.destroy)

# Place buttons
button1.place(relx=0.2, rely=0.8)
button2.place(relx=0.75, rely=0.8)
button3.place(relx=0.45, rely=0.9)

# ========== Merge PDF Screen ========== 
merge_label = ctk.CTkLabel(merge_frame, text="Merge PDFs Here", font=("Arial", 24))
merge_label.pack(pady=20)

# Number Selector (Dropdown)
selector_value = ctk.StringVar(value="0")  # Default value

number_selector = ctk.CTkComboBox(merge_frame, values=["1", "2", "3"], 
                                  variable=selector_value, 
                                  font=("Arial", 16))
number_selector.pack(pady=10, padx=20)

# Label to show selected number
selected_label = ctk.CTkLabel(merge_frame, text=f"Selected: {selector_value.get()}", font=("Arial", 16))
selected_label.pack(pady=10)

# Frame to hold dynamically generated buttons
button_frame = ctk.CTkFrame(merge_frame, fg_color="transparent")
button_frame.pack(pady=10)

# Function to confirm selection and create buttons
confirmed_value = 0  # Store confirmed value

def confirm_selection():
    global confirmed_value
    confirmed_value = int(selector_value.get())  # Convert to integer
    selected_label.configure(text=f"Confirmed: {confirmed_value}")  # Update label

    # Clear previous buttons
    for widget in button_frame.winfo_children():
        widget.destroy()

    # Create new buttons
    for i in range(1, confirmed_value + 1):
        pdf_button = ctk.CTkButton(button_frame, text=f"PDF {i}", command=lambda i=i: merge_pdfs(i))  # Trigger function with dynamic argument
        pdf_button.pack(pady=5)

# Confirm Button
confirm_button = ctk.CTkButton(merge_frame, text="Confirm", command=confirm_selection)
confirm_button.pack(pady=10)

# Back Button
merge_back_button = ctk.CTkButton(merge_frame, text="Back to Main", command=lambda: show_frame(main_frame))
merge_back_button.pack(pady=20)

# Initially, show the main screen
show_frame(main_frame)

# Function to handle keypress events
def key_press(event):
    if event.keysym == "Escape":
        root.destroy()
    elif event.keysym.lower() == "m":
        show_frame(merge_frame)
    elif event.keysym.lower() == "r":
        show_frame(resize_frame)

# Bind Escape key
root.bind("<KeyPress>", key_press)

# Start main loop
root.mainloop()
