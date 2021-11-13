from UI.App import App
"""
class Main(tk.Frame):
    def __init__(self, root, db):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='add.gif')
        button_open_dialog = tk.Button(toolbar, text='Добавить', command=self.open_dialod, bg='#d7d8e0',
                                       bd=0, compound=tk.TOP, image=self.add_img)
        button_open_dialog.pack(side=tk.LEFT)

        button_edit_dialog = tk.Button(toolbar, text='Редактировать', command=self.open_update_dialog, bg='#d7d8e0',
                                       bd=0, compound=tk.TOP, image=self.add_img)
        button_edit_dialog.pack(side=tk.LEFT)

        button_delete = tk.Button(toolbar, text='Удалить', command=self.delete_records, bg='#d7d8e0',
                                       bd=0, compound=tk.TOP, image=self.add_img)
        button_delete.pack(side=tk.LEFT)

        self.three = ttk.Treeview(self, columns=('ID', 'description', 'cost', 'total'), height=15, show='headings')

        self.three.column('ID', width=30, anchor=tk.CENTER)
        self.three.column('description', width=365, anchor=tk.CENTER)
        self.three.column('cost', width=150, anchor=tk.CENTER)
        self.three.column('total', width=100, anchor=tk.CENTER)

        self.three.heading('ID', text='ID')
        self.three.heading('description', text='Наименование')
        self.three.heading('cost', text='Статья дохода\\расхода')
        self.three.heading('total', text='Сумма')

        self.three.pack()

    def records(self, description, cost, total):
        self.db.insert_data(description, cost, total)
        self.view_records()

    def update_record(self, description, cost, total):
        self.db.cursor.execute('''UPDATE finance SET description=?, costs=?, total=? WHERE ID=?''',
                               (description, cost, total, self.three.set(self.three.selection()[0], '#1')))
        self.db.connect.commit()
        self.view_records()

    def view_records(self):
        self.db.cursor.execute('''SELECT * FROM finance''')
        [self.three.delete(i) for i in self.three.get_children()]
        [self.three.insert('', 'end', values=row) for row in self.db.cursor.fetchall()]

    def delete_records(self):
        for selection_item in self.three.selection():
            self.db.cursor.execute('''DELETE FROM finance WHERE ID=?''', (self.three.set(selection_item, '#1')))
        self.db.connect.commit()
        self.view_records()

    def open_dialod(self):
        Child()

    def open_update_dialog(self):
        Update()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить что-то')
        self.geometry("400x220+400+300")
        self.resizable(False, False)

        label_description = tk.Label(self, text='Наименование')
        label_description.place(x=50, y=50)

        label_selection = tk.Label(self, text='Статья дохода\\расхода')
        label_selection.place(x=50, y=80)

        label_sum = tk.Label(self, text='Сумма')
        label_sum.place(x=50, y=110)

        self.entry_desctiption = ttk.Entry(self)
        self.entry_desctiption.place(x=200, y=50)

        self.combobx = ttk.Combobox(self, values=[u'Доход', u'Расход'])
        self.combobx.current(0)
        self.combobx.place(x=200, y=80)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=110)

        button_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        button_cancel.place(x=300, y=170)

        self.button_add = ttk.Button(self, text='Добавить')
        self.button_add.place(x=220, y=170)
        self.button_add.bind('<Button-1>', lambda event: self.add_record)

        self.grab_set()
        self.focus_set()

    def add_record(self):
        self.view.records(self.entry_desctiption.get(),
                          self.combobx.get(),
                          self.entry_money.get())
        self.destroy()


class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()

    def init_edit(self):
        self.title('Редактирвоать')

        button_edit = ttk.Button(self, text='Редактировать')
        button_edit.place(x=205, y=170)
        button_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_desctiption.get(),
                                                                             self.combobx.get(),
                                                                             self.entry_money.get()))
        self.button_add.destroy()

class DB:
    def __init__(self):
        self.connect = sqlite3.connect('finance.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS finance (id integer primary key, description text, costs text, total real)''')
        self.connect.commit()

    def insert_data(self, description, cost, total):
        self.cursor.execute('''INSERT INTO finance (description, costs, total) VALUES (?, ?, ?)''',
                            (description, cost, total))
        self.connect.commit()

"""
if __name__ == "__main__":
    app = App()
    """
    db = DB()
    root = tk.Tk()
    app = Main(root, db)
    app.pack()
    root.title("Evm")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()"""
