import customtkinter as ctk

# vaariables to be used on the app
window_size = "800x600"

# setting up window
window = ctk.CTk()
window.geometry(window_size)
window.grid_columnconfigure(0, weight = 1)
window.grid_rowconfigure(0, weight = 1)

# frame to put options on
main_frame = ctk.CTkFrame(window)

# mainloop to keep window running
window.mainloop()