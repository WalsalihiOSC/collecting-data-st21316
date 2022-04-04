from tkinter import *


class Collect:
    def __init__(self, parent):
        f1 = Frame(parent, bg="#FFC0CB")
        self.show_all_btn = Button(f1, text="Show All",
                                   command=self.show_all, bd=1, padx=20)
        self.enter_data_btn = Button(
            parent, text="Enter data", padx=5, pady=5, command=self.enter_data)

        self.label_collect_data = Label(
            f1, text="Collecting Person Data", bg="#FFC0CB")
        self.first_name_label = Label(
            parent, text="First name:", padx=15, pady=10)
        self.age_label = Label(parent, text="Age:", padx=15, pady=10)
        self.question_label = Label(
            parent, text="Do you have a mobile phone?", padx=15, pady=10)

        self.first_name_entry = Entry(parent, width=20)
        self.age_entry = Entry(parent, width=20)

        self.v = StringVar()
        self.v.set("0")
        self.no_rb = Radiobutton(
            parent, value="No", text="No", variable=self.v, padx=15, pady=5)
        self.yes_rb = Radiobutton(
            parent, value="Yes", text="Yes", variable=self.v, padx=15, pady=5)

# positioning label and entry
        self.label_collect_data.grid(row=1, column=1, padx=15, pady=10)
        self.show_all_btn.grid(row=1, column=2, padx=45, pady=10)
        f1.grid(row=1, column=1, columnspan=2, sticky=W)
        self.first_name_label.grid(row=2, column=1, sticky=W)
        self.age_label.grid(row=3, column=1, sticky=W)
        self.question_label.grid(row=4, column=1, sticky=W)
        self.first_name_entry.grid(row=2, column=2, padx=5, pady=10, sticky=W)
        self.age_entry.grid(row=3, column=2, padx=5, pady=10, sticky=W)
        self.no_rb.grid(row=4, column=2, sticky=W)
        self.yes_rb.grid(row=5, column=2, sticky=W)
        self.enter_data_btn.grid(row=6, column=2, sticky=W)

# Creating a list for each person
        person_list = []

    def show_all(self):
        pass

    def enter_data(self):
        pass


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Collecting Data")
    root.geometry("340x250")
    show = Collect(root)
    root.mainloop()
