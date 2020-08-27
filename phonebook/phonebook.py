import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import os


class Phone:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Phonebook')
        self.book = pd.DataFrame(columns=['name', 'last', 'num'])
        self.book['name'].astype('str')
        self.book['last'].astype('str')
        self.book['num'].astype('str')
        self.work_book = pd.DataFrame(columns=['name', 'last', 'num'])
        self.work_book['num'].astype('str')
        self.search_book = pd.DataFrame(columns=['name', 'last', 'num'])
        info_frame = ttk.Labelframe(self.root, text='Info')
        name_label = tk.Label(info_frame, text='Name')
        self.nameEntry = tk.Entry(info_frame)
        name_label.grid(row=0, column=0)
        self.nameEntry.grid(row=0, column=1)

        lastname_label = tk.Label(info_frame, text='Last Name')
        self.lastname_entry = tk.Entry(info_frame)
        lastname_label.grid(row=1, column=0)
        self.lastname_entry.grid(row=1, column=1)

        number_label = tk.Label(info_frame, text='Number')
        self.numberEntry = tk.Entry(info_frame)
        number_label.grid(row=2, column=0)
        self.numberEntry.grid(row=2, column=1)
        ttk.Button(info_frame, text='Add', command=self.add).grid(row=0, column=2, rowspan=3, columnspan=3)

        info_frame.grid(row=0, column=0)

        tools_frame = ttk.Labelframe(self.root, text='Tools')

        ttk.Button(tools_frame, text='Delete all', command=self.delete_all).grid(row=0, column=0)
        ttk.Button(tools_frame, text='Delete part', command=self.delete).grid(row=1, column=0)
        ttk.Button(tools_frame, text='Edit', command=None).grid(row=0, column=1)
        ttk.Button(tools_frame, text='Save', command=self.save_data).grid(row=1, column=1)
        ttk.Button(tools_frame, text='Import data', command=self.import_data).grid(row=2, column=0, rowspan=1,
                                                                                   columnspan=2)

        tools_frame.grid(row=0, column=1)

        treeview_frame = tk.Frame(self.root)
        self.tree = ttk.Treeview(treeview_frame, columns=('Name', 'Lastname', 'Number'), show='headings')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Lastname', text='Last Name')
        self.tree.heading('Number', text='Number')

        self.tree.grid(row=0, column=0)
        treeview_frame.grid(row=1, column=0, columnspan=2)

        search_frame = ttk.Labelframe(self.root, text='Search')
        self.search_text = ttk.Entry(search_frame)
        self.search_text.grid(row=0, column=0)
        self.r_var = tk.IntVar()
        ttk.Button(search_frame, text='Search', command=self.search).grid(row=0, column=1, padx=5)
        ttk.Radiobutton(search_frame, text='Name', variable=self.r_var, value=1).grid(row=0, column=2, padx=5)
        ttk.Radiobutton(search_frame, text='Last Name', variable=self.r_var, value=2).grid(row=0, column=3, padx=5)
        ttk.Radiobutton(search_frame, text='Number', variable=self.r_var, value=3).grid(row=0, column=4, padx=5)
        ttk.Button(search_frame, text='Clean', command=self.clean_search).grid(row=0, column=5, padx=5)
        search_frame.grid(row=2, column=0, columnspan=2)

        self.numbers = []

        # self.name = []
        # self.last = []
        # self.num = []
        self.root.mainloop()

    def add(self):

        self.work_book.loc[len(self.work_book)] = [self.nameEntry.get(), self.lastname_entry.get(),
                                                   (self.numberEntry.get())]
        print(type(self.nameEntry.get()))
        print(type(self.lastname_entry.get()))
        print(type(self.numberEntry.get()))
        print(self.work_book)
        print(self.book)
        self.tree.insert('', tk.END, value=(self.nameEntry.get(), self.lastname_entry.get(), str(self.numberEntry.get())))
        self.nameEntry.delete(0, tk.END)
        self.lastname_entry.delete(0, tk.END)
        self.numberEntry.delete(0, tk.END)

    def delete_all(self):
        self.tree.delete(*self.tree.get_children())
        self.work_book.drop(['name', 'last', 'num'], axis=1, inplace=True)
        self.work_book = pd.DataFrame(columns=['name', 'last', 'num'])
        print(self.work_book)

    def delete(self):
        print(self.work_book)
        for selected_item in self.tree.selection():
            # a=list(self.tree.item(selected_item).values())[2][2]'text'
            # print(a)
            print(selected_item)
            number = list(self.tree.item(selected_item).values())[2][2]
            print(number)
            print(type(number))
            self.numbers.append(number)
            print(self.numbers)
            self.tree.delete(selected_item)
        for item in self.numbers:
            self.work_book = self.work_book[self.work_book['num'] != item]
            print(self.work_book)
            self.numbers = []

    def save_data(self):
        df_path = os.path.join(os.getcwd(), 'phonebook.xlsx')
        self.book = self.work_book
        self.book.to_excel(df_path, index=False)
        print(self.book)

    def import_data(self):
        df_path = os.path.join(os.getcwd(), 'phonebook.xlsx')
        self.book = pd.read_excel(df_path, dtype=str)
        print(self.book)
        for i in range(0, len(self.book)):
            self.tree.insert('', tk.END,
                             value=(self.book.loc[i, 'name'], self.book.loc[i, 'last'], self.book.loc[i, 'num']))
            print(type(self.book.loc[i, 'name']))
            print(type(self.book.loc[i, 'last']))
            print(type(self.book.loc[i, 'num']))
        frames = [self.book, self.work_book]
        self.work_book = pd.concat(frames)

    def search(self):
        self.tree.delete(*self.tree.get_children())
        df_path = os.path.join(os.getcwd(), 'phonebook.xlsx')
        self.book = pd.read_excel(df_path, dtype=str)
        print(self.book)
        print(self.search_text.get())
        print(type(self.search_text.get()))
        if self.r_var.get() == 1:
            self.search_book = self.book[self.book['name'] == self.search_text.get()].reset_index()
            print(self.search_text.get())
            print(self.search_book)
            print(len(self.search_book))
            for i in range(0, len(self.search_book)):
                self.tree.insert('', tk.END, value=(self.search_book.loc[i, 'name'], self.search_book.loc[i, 'last'], self.search_book.loc[i, 'num']))
        elif self.r_var.get() == 2:
            self.search_book = self.book[self.book['last'] == self.search_text.get()].reset_index()
            print(self.search_text.get())
            print(self.search_book)
            print(len(self.search_book))
            for i in range(0, len(self.search_book)):
                self.tree.insert('', tk.END, value=(self.search_book.loc[i, 'name'], self.search_book.loc[i, 'last'], self.search_book.loc[i, 'num']))
        if self.r_var.get() == 3:
            self.search_book = self.book[self.book['num'] == str(self.search_text.get())].reset_index()
            print(self.search_text.get())
            print(self.search_book)
            print(len(self.search_book))
            for i in range(0, len(self.search_book)):
                self.tree.insert('', tk.END, value=(self.search_book.loc[i, 'name'], self.search_book.loc[i, 'last'], self.search_book.loc[i, 'num']))
        self.search_text.delete(0, tk.END)

    def clean_search(self):
        self.search_text.delete(0, tk.END)
        self.tree.delete(*self.tree.get_children())
        self.r_var.set(0)




Phone()
