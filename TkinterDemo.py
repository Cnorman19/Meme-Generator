from tkinter import *
from Pull_Image_From_Site import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Meme Generator (by Cameron Norman)")
        self.pack(fill=BOTH, expand=1)

        # buttons creation and configuration
        generate_meme_button = Button(self, text = "Generate Meme", fg = "white" , bg = "purple", command = Image_Generation.get_Images)
        generate_meme_button.place(relx = 0.5, rely = 0.3, anchor = CENTER)
        generate_meme_button.config(height = 4, width = 40)

        quit_Button = Button(self, text="QUIT", fg = "white" , bg = "pink", command = self.exit)
        quit_Button.place(relx=0.5, rely=0.6, anchor=CENTER)
        quit_Button.config(height = 4, width = 25)

    def exit(self):
        exit()

root = Tk()
root.geometry("600x400")

app = Window(root)
root.mainloop()
