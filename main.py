import customtkinter as ctk

window_size = "800x600"

# main class
class MainMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        # vaariables to be used on the app
        self.button_sizes_main_menu_x = 480
        self.button_sizes_main_menu_y = 80

        # setting up window
        self.geometry(window_size)
        self.title("Coffee Shop App")
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure((0, 2), weight = 1)
        self.resizable(False, False)

        # widgets to be used
        self.adding_menu_item = ctk.CTkButton(self, width = self.button_sizes_main_menu_x, height = self.button_sizes_main_menu_y, text = "Adding Menu Item", font = ("Arial", 40), command = self.adding_menu_function)
        self.adding_menu_item.grid(row = 0, column = 0)

        self.checking_menu_prices = ctk.CTkButton(self, width = self.button_sizes_main_menu_x, height = self.button_sizes_main_menu_y, text = "Check the menu prices" , font = ("Arial", 40), command = self.check_menu_function)
        self.checking_menu_prices.grid(row = 1, column = 0)

        self.checkout_customer = ctk.CTkButton(self, width = self.button_sizes_main_menu_x, height = self.button_sizes_main_menu_y, text = "Checkout", font = ("Arial", 40), command = self.checkout_menu)
        self.checkout_customer.grid(row = 2, column = 0)
    
    # button functions
    def adding_menu_function(self):
       # Setting up new window
       menu_for_adding_items = ctk.CTkToplevel(self)
       menu_for_adding_items.geometry(window_size)
       menu_for_adding_items.grid_columnconfigure((0, 2), weight = 1)
       menu_for_adding_items.grid_rowconfigure(0, weight = 2)
       menu_for_adding_items.resizable(False, False)
       menu_for_adding_items.wm_transient(self)

       # widgets for adding items
       enter_menu_item = ctk.CTkEntry(menu_for_adding_items, width = 300, height = 70, placeholder_text=" ", font = ("Arial", 30))
       enter_menu_item.grid(row = 0, column = 0)

       enter_item_price = ctk.CTkEntry(menu_for_adding_items, width = 300, height = 70, placeholder_text = " ", font = ("Arial", 30))
       enter_item_price.grid(row = 0, column = 1)

       add_item = ctk.CTkButton(menu_for_adding_items, width = 70, height = 70, text = "+", font = ("Arial", 40))
       add_item.grid(row = 0, column = 2)

       enter_menu_text = ctk.CTkLabel(menu_for_adding_items, text = "Add menu item", font = ("Arial", 36),  text_color = "White")
       enter_menu_text.place(x = 60, y = 190)

       enter_price_text = ctk.CTkLabel(menu_for_adding_items, text = "Set item price(Php)", font = ("Arial", 36),  text_color = "White")
       enter_price_text.place(x = 360, y = 190)

    def check_menu_function(self):
        print("You picked checking menu prices!")

    def checkout_menu(self):
        print("You will checkout a customer!")

if __name__ == "__main__":
    main_menu = MainMenu()
    # mainloop to keep window running
    main_menu.mainloop()