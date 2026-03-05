import customtkinter as ctk

# vaariables to be used on the app
window_size = "800x600"
button_sizes_main_menu_x = 480
button_sizes_main_menu_y = 80

# functions to be used
def option_picked(choice):
    print("You picked: ", choice)

# setting up window
window = ctk.CTk()
window.geometry(window_size)
window.grid_columnconfigure(0, weight = 1)
window.grid_rowconfigure((0, 2), weight = 1)
window.resizable(False, False)

# widgets to be used
adding_menu_item = ctk.CTkButton(window, width = 480, height = 80, text = "Adding Menu Item", font = ("Arial", 40))
adding_menu_item.grid(row = 0, column = 0)

checking_menu_prices = ctk.CTkButton(window, width = button_sizes_main_menu_x, height = button_sizes_main_menu_y, text = "Check the menu prices" , font = ("Arial", 40))
checking_menu_prices.grid(row = 1, column = 0)

checkout_customer = ctk.CTkButton(window, width = button_sizes_main_menu_x, height = button_sizes_main_menu_y, text = "Checkout", font = ("Arial", 40))
checkout_customer.grid(row = 2, column = 0)

# mainloop to keep window running
window.mainloop()