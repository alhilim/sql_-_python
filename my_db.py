import mysql.connector
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

class My_db:
    def __init__(self,db_name,table_name):
        self.database_name=db_name
        self.table_name=table_name
        self.main_window=Tk()
        self.main_window.geometry('1650x1000')


        self.dp_frame=Frame(self.main_window)
        self.dp_frame.pack(fill='both',expand=1)

        self.edit_frame=Frame(self.main_window)
        self.edit_frame.pack(fill='both',expand=1,anchor='e')

        self.btn=Button(self.dp_frame,text='EDIT TABLE',font=("HELVATICA",15),background='yellow',foreground='black',command=self.edit_my_db)
        self.btn.grid(row=0,column=0,sticky='ne')

    def command(self,command):

        database_name=self.database_name

        # الاتصال بقاعدة البيانات
        conn = mysql.connector.connect(host='localhost',user='root'
                                    ,password='',database=database_name)
        mycur = conn.cursor()

        # تنفيذ الاستعلام
        mycur.execute(command)

        conn.commit()
        conn.close()

    def displayBig1(self,command):
         
        dp_frame=self.dp_frame

        database_name=self.database_name

        # الاتصال بقاعدة البيانات
        conn = mysql.connector.connect(host='localhost',user='root'
                                    ,password='',database=database_name)
        mycur = conn.cursor()

        # تنفيذ الاستعلام
        mycur.execute(command)

        # طباعة أسماء الحقول
        data_heading = [desc[0] for desc in mycur.description]
        print(data_heading)  # ['my_name']

        rows = mycur.fetchall()

        # Create Frame for Treeview
        tf=Frame(dp_frame,width=1500,height=300)
        tf.grid(padx=10,column=0,row=1,pady=20)
        tf.pack_propagate(False)


        # ADD STYLE 
        style=ttk.Style()

        # Pick A Theme
        style.theme_use("default")

        # Configure the Treeview Colors
        style.configure("stylebig1.Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=30,
                fieldbackground="#D3D3D3"  )

        # Treeview Scrollbar
        ts=Scrollbar(tf)
        ts.pack(side=RIGHT,fill=Y)

        ts2=Scrollbar(tf,orient='horizontal')
        ts2.pack(side=BOTTOM,fill=X)

        # CREATE THE TREEVIEW
        myt2=ttk.Treeview(tf,style='stylebig1.Treeview',yscrollcommand=ts.set,xscrollcommand=ts2.set, selectmode="extended")
        myt2.pack(fill=BOTH,expand=TRUE)

        # conf the scrollbar
        ts.config(command=myt2.yview)
        ts2.config(command=myt2.xview)

        for head in data_heading:
            like=0

            for head_2 in data_heading:
                if head ==head_2:
                    like+=1
                    if like>1:
                        index=data_heading.index(head)
                        data_heading[index]=head+" "



        # Define The Columns for The Treeview
        myt2['columns']=[record for record in data_heading]

        # Format columns for the size of the column 
        myt2.column("#0",width=0,stretch=NO)
        for record in data_heading:
            if 'ID' in record.upper():
                myt2.column(record,width=100,anchor=CENTER)
            else:
                myt2.column(record,width=150,anchor=CENTER)


        myt2.heading('#0',text='')

        for record in data_heading:
            myt2.heading(record,text=record)

        # ADD COLORS TO THE ROWS 
        myt2.tag_configure("oddrow",background="white") 
        myt2.tag_configure("evenrow",background="lightblue") 

        for record in myt2.get_children():
            myt2.delete(record)

        mycur.execute(command)
        records=mycur.fetchall()

        for row,record in enumerate(records):
            if row%2==0:
                myt2.insert(parent='',index='end',iid=None,values=record,tags='oddrow',)
            else:
                myt2.insert(parent='',index='end',iid=None,values=record,tags='evenrow',)

        conn.commit()
        conn.close()
        # root.mainloop()

    def displayBig2(self,command):
         
        dp_frame=self.dp_frame

        database_name=self.database_name

        # الاتصال بقاعدة البيانات
        conn = mysql.connector.connect(host='localhost',user='root'
                                    ,password='',database=database_name)
        mycur = conn.cursor()

        # تنفيذ الاستعلام
        mycur.execute(command)

        # طباعة أسماء الحقول
        data_heading = [desc[0] for desc in mycur.description]
        print(data_heading)  # ['my_name']

        rows = mycur.fetchall()

        # Create Frame for Treeview
        tf=Frame(dp_frame,width=1500,height=300)
        tf.grid(padx=10,column=0,row=2,pady=20)
        tf.pack_propagate(False)


        # ADD STYLE 
        style=ttk.Style()

        # Pick A Theme
        style.theme_use("default")

        # Configure the Treeview Colors
        style.configure("stylebig.Treeview",
                background="red",
                foreground="black",
                rowheight=30,
                fieldbackground="lightgray"  )
        # Treeview Scrollbar
        ts=Scrollbar(tf)
        ts.pack(side=RIGHT,fill=Y)

        ts2=Scrollbar(tf,orient='horizontal')
        ts2.pack(side=BOTTOM,fill=X)

        # CREATE THE TREEVIEW
        myt2=ttk.Treeview(tf,style='stylebig.Treeview',yscrollcommand=ts.set,xscrollcommand=ts2.set, selectmode="extended")
        myt2.pack(fill=BOTH,expand=TRUE)

        # conf the scrollbar
        ts.config(command=myt2.yview)
        ts2.config(command=myt2.xview)

        for head in data_heading:
            like=0

            for head_2 in data_heading:
                if head ==head_2:
                    like+=1
                    if like>1:
                        index=data_heading.index(head)
                        data_heading[index]=head+" "



        # Define The Columns for The Treeview
        myt2['columns']=[record for record in data_heading]

        # Format columns for the size of the column 
        myt2.column("#0",width=0,stretch=NO)
        for record in data_heading:
            if 'ID' in record.upper():
                myt2.column(record,width=100,anchor=CENTER)
            else:
                myt2.column(record,width=150,anchor=CENTER)


        myt2.heading('#0',text='')

        for record in data_heading:
            myt2.heading(record,text=record)

        # ADD COLORS TO THE ROWS 
        myt2.tag_configure("oddrow",background="white") 
        myt2.tag_configure("evenrow",background="lightblue") 

        for record in myt2.get_children():
            myt2.delete(record)

        mycur.execute(command)
        records=mycur.fetchall()

        for row,record in enumerate(records):
            if row%2==0:
                myt2.insert(parent='',index='end',iid=None,values=record,tags='oddrow',)
            else:
                myt2.insert(parent='',index='end',iid=None,values=record,tags='evenrow',)

        conn.commit()
        conn.close()
        # root.mainloop()

    def display1(self,command):
         
        dp_frame=self.dp_frame

        database_name=self.database_name

        # الاتصال بقاعدة البيانات
        conn = mysql.connector.connect(host='localhost',user='root'
                                    ,password='',database=database_name)
        mycur = conn.cursor()

        # تنفيذ الاستعلام
        mycur.execute(command)

        # طباعة أسماء الحقول
        data_heading = [desc[0] for desc in mycur.description]
        print(data_heading)  # ['my_name']

        rows = mycur.fetchall()

        # Create Frame for Treeview
        tf=Frame(dp_frame,width=750,height=300)
        tf.grid(padx=10,column=0,row=1,pady=20)
        tf.pack_propagate(False)


        # ADD STYLE 
        style=ttk.Style()

        # Pick A Theme
        style.theme_use("default")

        # Configure the Treeview Colors
        style.configure("style1.Treeview",
                background="red",
                foreground="blue",
                rowheight=25,
                fieldbackground="blue"  )
        # Treeview Scrollbar
        ts=Scrollbar(tf)
        ts.pack(side=RIGHT,fill=Y)

        ts2=Scrollbar(tf,orient='horizontal')
        ts2.pack(side=BOTTOM,fill=X)

        # CREATE THE TREEVIEW
        myt2=ttk.Treeview(tf,style='style1.Treeview',yscrollcommand=ts.set,xscrollcommand=ts2.set, selectmode="extended")
        myt2.pack(fill=BOTH,expand=TRUE)

        # conf the scrollbar
        ts.config(command=myt2.yview)
        ts2.config(command=myt2.xview)

        for head in data_heading:
            like=0

            for head_2 in data_heading:
                if head ==head_2:
                    like+=1
                    if like>1:
                        index=data_heading.index(head)
                        data_heading[index]=head+" "


        # Define The Columns for The Treeview
        myt2['columns']=[record for record in data_heading]

        # Format columns for the size of the column 
        myt2.column("#0",width=0,stretch=NO)
        for record in data_heading:
            if 'ID' in record.upper():
                myt2.column(record,width=100,anchor=CENTER)
            else:
                myt2.column(record,width=150,anchor=CENTER)


        myt2.heading('#0',text='')

        for record in data_heading:
            myt2.heading(record,text=record)

        # ADD COLORS TO THE ROWS 
        myt2.tag_configure("oddrow",background="white") 
        myt2.tag_configure("evenrow",background="lightblue") 

        for record in myt2.get_children():
            myt2.delete(record)

        mycur.execute(command)
        records=mycur.fetchall()

        for row,record in enumerate(records):
            if row%2==0:
                myt2.insert(parent='',index='end',iid=None,values=record,tags='oddrow',)
            else:
                myt2.insert(parent='',index='end',iid=None,values=record,tags='evenrow',)

        conn.commit()
        conn.close()
        # root.mainloop()

    def display2(self,command):
            
        dp_frame=self.dp_frame


        database_name=self.database_name
        # الاتصال بقاعدة البيانات
        conn = mysql.connector.connect(host='localhost',user='root'
                                    ,password='',database=database_name)
        mycur = conn.cursor()

        # تنفيذ الاستعلام
        mycur.execute(command)

        # طباعة أسماء الحقول
        data_heading = [desc[0] for desc in mycur.description]
        print(data_heading)  # ['my_name']

        rows = mycur.fetchall()

        # Create Frame for Treeview
        tf=Frame(dp_frame,width=750,height=300)
        tf.grid(column=1,row=1)
        tf.pack_propagate(False)

        # Treeview Scrollbar

        # ADD STYLE 
        style=ttk.Style()

        # Pick A Theme
        style.theme_use("default")

        # Configure the Treeview Colors
        style.configure("style2.Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="black"  )
        ts=Scrollbar(tf)
        ts.pack(side=RIGHT,fill=Y)

        ts2=Scrollbar(tf,orient='horizontal')
        ts2.pack(side=BOTTOM,fill=X)

        # CREATE THE TREEVIEW
        myt=ttk.Treeview(tf,style='style2.Treeview',yscrollcommand=ts.set,xscrollcommand=ts2.set, selectmode="extended")
        myt.pack(fill=BOTH,expand=TRUE)

        # conf the scrollbar
        ts.config(command=myt.yview)
        ts2.config(command=myt.xview)
        for head in data_heading:
            like=0

            for head_2 in data_heading:
                if head ==head_2:
                    like+=1
                    if like>1:
                        index=data_heading.index(head)
                        data_heading[index]=head+" "



        # Define The Columns for The Treeview
        myt['columns']=[record for record in data_heading]

        # Format columns for the size of the column 
        myt.column("#0",width=0,stretch=NO)
        for record in data_heading:
            if 'ID' in record.upper():
                myt.column(record,width=100,anchor=CENTER)
            else:
                myt.column(record,width=150,anchor=CENTER)


        myt.heading('#0',text='')

        for record in data_heading:
            myt.heading(record,text=record)

        # ADD COLORS TO THE ROWS 
        myt.tag_configure("oddrow",background="white") 
        myt.tag_configure("evenrow",background="lightblue") 

        for record in myt.get_children():
            myt.delete(record)

        mycur.execute(command)
        records=mycur.fetchall()

        for row,record in enumerate(records):
            if row%2==0:
                myt.insert(parent='',index='end',iid=None,values=record,tags='oddrow',)
            else:
                myt.insert(parent='',index='end',iid=None,values=record,tags='evenrow',)

        conn.commit()
        conn.close()

    def display3(self,command):
        
        dp_frame=self.dp_frame

        database_name=self.database_name
        # الاتصال بقاعدة البيانات
        conn = mysql.connector.connect(host='localhost',user='root'
                                    ,password='',database=database_name)
        mycur = conn.cursor()

        # تنفيذ الاستعلام
        mycur.execute(command)

        # طباعة أسماء الحقول
        data_heading = [desc[0] for desc in mycur.description]
        print(data_heading)  # ['my_name']

        rows = mycur.fetchall()

        # ADD STYLE 
        style=ttk.Style()

        # Pick A Theme
        style.theme_use("default")

        # Configure the Treeview Colors
        style.configure("style3.Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3"  )

        # Create Frame for Treeview
        tf=Frame(dp_frame,width=750,height=300)
        tf.grid(padx=10,column=0,row=2)
        tf.pack_propagate(False)

        # Treeview Scrollbar
        ts=Scrollbar(tf)
        ts.pack(side=RIGHT,fill=Y)

        ts2=Scrollbar(tf,orient='horizontal')
        ts2.pack(side=BOTTOM,fill=X)

        # CREATE THE TREEVIEW
        myt=ttk.Treeview(tf,style='style3.Treeview',yscrollcommand=ts.set,xscrollcommand=ts2.set, selectmode="extended")
        myt.pack(fill=BOTH,expand=TRUE)

        # conf the scrollbar
        ts.config(command=myt.yview)
        ts2.config(command=myt.xview)

        for head in data_heading:
            like=0

            for head_2 in data_heading:
                if head ==head_2:
                    like+=1
                    if like>1:
                        index=data_heading.index(head)
                        data_heading[index]=head+" "


        # Define The Columns for The Treeview
        myt['columns']=[record for record in data_heading]

        # Format columns for the size of the column 
        myt.column("#0",width=0,stretch=NO)
        for record in data_heading:
            if 'ID' in record.upper():
                myt.column(record,width=100,anchor=CENTER)
            else:
                myt.column(record,width=150,anchor=CENTER)


        myt.heading('#0',text='')

        for record in data_heading:
            myt.heading(record,text=record)

        # ADD COLORS TO THE ROWS 
        myt.tag_configure("oddrow",background="white") 
        myt.tag_configure("evenrow",background="lightblue") 

        for record in myt.get_children():
            myt.delete(record)

        mycur.execute(command)
        records=mycur.fetchall()

        for row,record in enumerate(records):
            if row%2==0:
                myt.insert(parent='',index='end',iid=None,values=record,tags='oddrow',)
            else:
                myt.insert(parent='',index='end',iid=None,values=record,tags='evenrow',)

        conn.commit()

    def display4(self,command):
    
        dp_frame=self.dp_frame

        database_name=self.database_name
        # الاتصال بقاعدة البيانات
        conn = mysql.connector.connect(host='localhost',user='root'
                                    ,password='',database=database_name)
        mycur = conn.cursor()

        # تنفيذ الاستعلام
        mycur.execute(command)

        # طباعة أسماء الحقول
        data_heading = [desc[0] for desc in mycur.description]
        print(data_heading)  # ['my_name']

        rows = mycur.fetchall()

        # ADD STYLE 
        style=ttk.Style()

        # Pick A Theme
        style.theme_use("default")

        # Configure the Treeview Colors
        style.configure("style4.Treeview",
                background="green",
                foreground="purple",
                rowheight=25,
                fieldbackground="purple"  )

        # Create Frame for Treeview
        tf=Frame(dp_frame,width=750,height=300)
        tf.grid(column=1,row=2)
        tf.pack_propagate(False)

        # Treeview Scrollbar
        ts=Scrollbar(tf)
        ts.pack(side=RIGHT,fill=Y)

        ts2=Scrollbar(tf,orient='horizontal')
        ts2.pack(side=BOTTOM,fill=X)

        # CREATE THE TREEVIEW
        myt=ttk.Treeview(tf,style='style4.Treeview',yscrollcommand=ts.set,xscrollcommand=ts2.set, selectmode="extended")
        myt.pack(fill=BOTH,expand=TRUE)

        # conf the scrollbar
        ts.config(command=myt.yview)
        ts2.config(command=myt.xview)

        for head in data_heading:
            like=0

            for head_2 in data_heading:
                if head ==head_2:
                    like+=1
                    if like>1:
                        index=data_heading.index(head)
                        data_heading[index]=head+" "



        # Define The Columns for The Treeview
        myt['columns']=[record for record in data_heading]

        # Format columns for the size of the column 
        myt.column("#0",width=0,stretch=NO)
        for record in data_heading:
            if 'ID' in record.upper():
                myt.column(record,width=100,anchor=CENTER)
            else:
                myt.column(record,width=150,anchor=CENTER)


        myt.heading('#0',text='')

        for record in data_heading:
            myt.heading(record,text=record)

        # ADD COLORS TO THE ROWS 
        myt.tag_configure("oddrow",background="white") 
        myt.tag_configure("evenrow",background="lightblue") 

        for record in myt.get_children():
            myt.delete(record)

        mycur.execute(command)
        records=mycur.fetchall()

        for row,record in enumerate(records):
            if row%2==0:
                myt.insert(parent='',index='end',iid=None,values=record,tags='oddrow',)
            else:
                myt.insert(parent='',index='end',iid=None,values=record,tags='evenrow',)

        conn.commit()
       
    def edit_my_db(self):
        dp_frame=self.dp_frame
        for widget in dp_frame.winfo_children():
            widget.destroy()
        dp_frame.forget()

        global edit_f

        data_base_name=self.database_name
        table_name=self.table_name

        conn=mysql.connector.connect(host='localhost',user='root',
                                password='',database=data_base_name)

        mycur=conn.cursor()


        mycur.execute(f"DESCRIBE {table_name}")

        data_heading=[head[0] for head in mycur.fetchall()]

        root=self.edit_frame

        def search_record():
            conn=mysql.connector.connect(host='localhost',user='root',
                                        password='',
                                        database=data_base_name)

            mycur=conn.cursor()
            for record in myt.get_children():
                myt.delete(record)
            mycur.execute(f"SELECT* FROM {table_name} WHERE {search_drop.get()} LIKE '__{search_box.get()}%'")
            records=mycur.fetchall()
            for row,record in enumerate(records):
                if row%2==0:
                    myt.insert(parent='',index='end',iid=None,values=record,tags='oddrow',)
                else:
                    myt.insert(parent='',index='end',iid=None,values=record,tags='evenrow',)
            conn.commit()
            conn.close()
            search_box.delete(0,'end')
            clear_box()
    
        def delete_all_records():
            response= messagebox.askyesno("WOOH!!!!!","Are You Sure You Want To Delete Record?!")
            if response==1:
                conn=mysql.connector.connect(host='localhost',user='root',
                                            password='',
                                            database=data_base_name)

                mycur=conn.cursor()

                mycur.execute(f"TRUNCATE {table_name}")

                conn.commit()
                conn.close()
                quary_data()

        def delete_record():
            global edit_f
            conn=mysql.connector.connect(host='localhost',user='root',
                                    password='',database=data_base_name)

            mycur=conn.cursor()

            mycur.execute(F"""
                        SELECT COLUMN_NAME
                        FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
                        WHERE TABLE_SCHEMA = %s AND TABLE_NAME=%s AND CONSTRAINT_NAME='PRIMARY'
                            """,(data_base_name,table_name))
            primarykey=[row[0] for row in mycur.fetchall()]


            
            for widget in edit_f.winfo_children():
                widget.destroy()
            edit_f.pack_forget()
            
            
            def combo_selected(e):
                edit_box.delete(0,'end')
                selected=drop.get()
                edit_box.insert(0,var_box_lbl[f'box_{selected}'].get())
            
            def confir_delete():
                response= messagebox.askyesno("WOOH!!!!!","Are You Sure You Want To Delete Record?!")

                if response==1:

                    selected=myt.selection()

                    # conn.commit()
                    for select in selected:
                        myt.delete(select) 

                    conn=mysql.connector.connect(host='localhost',user='root',
                                                password='',
                                                database=data_base_name)

                    mycur=conn.cursor()

                    value_update=""

                    if edit_box.get().isdigit():
                        value_update+=f"{edit_box.get()}"
                    else:
                        value_update+=f"'{edit_box.get()}'"
                    
                    data=f"DELETE FROM {table_name}  "

                    data+=f" WHERE {drop.get()} = {value_update}"

                    print(data)

                    mycur.execute(data)

                    conn.commit()
                    conn.close()

                    for widget in edit_f.winfo_children():
                        widget.destroy()
                    
                    edit_f.pack_forget()

                    quary_data()

                
            edit_f=LabelFrame(root,text="DELETE RECORD!",width=1400,height=100,font=("helvatica",15))
            edit_f.pack()
            edit_f.grid_propagate(False)

            info_lbl=Label(edit_f,text="DELETE WHERE COLUMN.....",font=("helvatica",20))
            info_lbl.grid(row=1,column=0)

            # # Drop Down Box
            drop = ttk.Combobox(edit_f,style="CustomCombobox.TCombobox", values=data_heading,font=("Helvetica",20),justify='center')
            drop.set(primarykey[0])
            drop.grid(row=1,column=1,padx=5)
            drop.bind("<<ComboboxSelected>>",combo_selected)

            lbl=Label(edit_f,text=' = ',font=('helvetica',30))
            lbl.grid(row=1,column=2)

            edit_box=Entry(edit_f,font=('helvetica',20),width=25)
            edit_box.grid(row=1,column=3)
            edit_box.insert(0,var_box_lbl[f'box_{primarykey[0]}'].get())

            update_btn=Button(edit_f,text='Delete',background='red',fg='white',font=('helvetica',20),command=confir_delete)
            update_btn.grid(row=1,column=4,padx=65)


        def quary_data():
            clear_box()
            conn=mysql.connector.connect(host='localhost',user='root',
                                        password='',
                                        database=data_base_name)

            mycur=conn.cursor()
            for record in myt.get_children():
                myt.delete(record)
            mycur.execute(f"SELECT* FROM {table_name}")
            records=mycur.fetchall()
            for row,record in enumerate(records):
                if row%2==0:
                    myt.insert(parent='',index='end',iid=None,values=record,tags='oddrow',)
                else:
                    myt.insert(parent='',index='end',iid=None,values=record,tags='evenrow',)
            conn.commit()
            conn.close()

        def insert_record():  
            conn=mysql.connector.connect(host='localhost',user='root',
                                        password='',
                                        database=data_base_name)

            mycur=conn.cursor()

            sql_head_name=' , '.join(data_heading)

            for_vlue='%s,'*len(data_heading)
            for_vlue=for_vlue.rstrip(',')

            sql_cmnd=f"INSERT INTO {table_name} ({sql_head_name}) VALUES({for_vlue})"
            data=[]


            for record in var_box:
                if record.get().isdigit():
                    data.append(int(record.get()))
                else:
                    data.append(record.get())

            mycur.execute(sql_cmnd,data)
            conn.commit()
            conn.close()

            quary_data()

        def edit_record():

            conn=mysql.connector.connect(host='localhost',user='root',
                                    password='',database=data_base_name)

            mycur=conn.cursor()
                    
            global edit_f
            for widget in edit_f.winfo_children():
                widget.destroy()
            edit_f.pack_forget()
            

            def combo_selected(e):
                edit_box.delete(0,'end')
                selected=drop.get()
                edit_box.insert(0,var_box_lbl[f'box_{selected}'].get())


            def update_record():

                conn=mysql.connector.connect(host='localhost',user='root',
                                            password='',
                                            database=data_base_name)

                mycur=conn.cursor()
                value_update=""
                if edit_box.get().isdigit():
                    value_update+=f"{edit_box.get()}"
                else:
                    value_update+=f"'{edit_box.get()}'"
                data=f"UPDATE {table_name} SET "

                for index,box in enumerate (var_box):
                    boxy=box.get()
                    if boxy.isdigit():

                        data+=f" {data_heading[index]} = {boxy} , "
                    else:
                        data+=f" {data_heading[index]} ='{boxy}' , "
                data=data.rstrip(', ')
                data+=f" WHERE {drop.get()} = {value_update}"

                print(data)

                mycur.execute(data)

                conn.commit()
                conn.close()
                
                for widget in edit_f.winfo_children():
                    widget.destroy()
                edit_f.pack_forget()
                
                quary_data()

            
            edit_f=LabelFrame(root,text="UPDATE RECORD",width=1400,height=100,font=("helvatica",15))
            edit_f.pack()
            edit_f.grid_propagate(False)

            info_lbl=Label(edit_f,text="UPDATE WHERE COLUMN.....",font=("helvatica",20))
            info_lbl.grid(row=1,column=0)

            mycur.execute(f"""
                        SELECT COLUMN_NAME 
                        FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
                        WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s AND CONSTRAINT_NAME = 'PRIMARY'
                            """,(data_base_name,table_name))
            primarykey=[row[0] for row in mycur.fetchall()]

            # # Drop Down Box
            drop = ttk.Combobox(edit_f, values=data_heading,font=("Helvetica",20),foreground='purple',justify='center')
            drop.set(primarykey[0])
            drop.grid(row=1,column=1,padx=5)
            drop.bind("<<ComboboxSelected>>",combo_selected)

            lbl=Label(edit_f,text=' = ',font=('helvetica',30))
            lbl.grid(row=1,column=2)

            edit_box=Entry(edit_f,font=('helvetica',20),width=25)
            edit_box.grid(row=1,column=3)
            edit_box.insert(0,var_box_lbl[f'box_{primarykey[0]}'].get())

            update_btn=Button(edit_f,text='UPDATE',fg='purple',font=('helvetica',20),command=update_record)
            update_btn.grid(row=1,column=4,padx=65)

        def clear_box():
            for box in var_box:
                box.delete(0,'end')
        
        def select_record(e):
            clear_box()
            y=myt.focus()
            x=myt.selection()
            values=myt.item(y,'values')
        
            for index,box in enumerate(var_box):
                box.insert(0,values[index])

        # ADD STYLE 
        style=ttk.Style()

        # Pick A Theme
        style.theme_use("default")

        # Configure the Treeview Colors
        style.configure("edit_style.Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3"  )

        # Configure the Treeview Colors
        style.configure("CustomCombobox.TCombobox",
                background="red",
                foreground="lightgray",
                font=('Arial',25),
                fieldbackground="black"  )

        # Create Frame for Treeview
        tf=Frame(root,width=1200,height=300)
        tf.pack(pady=10)
        tf.pack_propagate(False)

        # Treeview Scrollbar
        ts=Scrollbar(tf)
        ts.pack(side=RIGHT,fill=Y)

        ts2=Scrollbar(tf,orient='horizontal')
        ts2.pack(side=BOTTOM,fill=X)
        # CREATE THE TREEVIEW
        myt=ttk.Treeview(tf,style="edit_style.Treeview",yscrollcommand=ts.set,xscrollcommand=ts2.set, selectmode="extended")
        myt.pack(fill='both',expand=1)

        # conf the scrollbar
        ts.config(command=myt.yview)
        ts2.config(command=myt.xview)

        for head in data_heading:
            like=0

            for head_2 in data_heading:
                if head ==head_2:
                    like+=1
                    if like>1:
                        index=data_heading.index(head)
                        data_heading[index]=head+" "



        # Define The Columns for The Treeview
        myt['columns']=[record for record in data_heading]

        # Format columns for the size of the column 
        myt.column("#0",width=0,stretch=NO)
        for record in data_heading:
            if 'ID' in record.upper():
                myt.column(record,width=100,anchor=CENTER)
            else:
                myt.column(record,width=150,anchor=CENTER)


        myt.heading('#0',text='')

        for record in data_heading:
            myt.heading(record,text=record.title())

        # ADD COLORS TO THE ROWS 
        myt.tag_configure("oddrow",background="white") 
        myt.tag_configure("evenrow",background="lightblue") 


        edit_frame=Frame(root,width=1400,height=300,background='gray')
        edit_frame.pack()
        edit_frame.grid_propagate(False)

        rf=LabelFrame(edit_frame,text='RECORDS',width=900,height=285,background='gray')
        rf.grid(row=1,column=0,pady=10,sticky='n')
        rf.grid_propagate(False)

        var_box_lbl={}
        var_box=[]

        row=0
        column=0
        for head in data_heading:
            if row<6:
                var_box_lbl['lbl_'+head]=Label(rf,text=head.title(),font=('helvetica',10))
                var_box_lbl['lbl_'+head].grid(row=row,column=column,padx=10,pady=10)

                var_box_lbl['box_'+head]=Entry(rf)
                var_box_lbl['box_'+head].grid(row=row,column=column+1,padx=10)
                var_box.append(var_box_lbl['box_'+head])
            else:
                if row==6:
                    row=0
                    column+=2
                var_box_lbl['lbl_'+head]=Label(rf,text=head.title(),font=('helvetica',10))
                var_box_lbl['lbl_'+head].grid(row=row,column=column,padx=10,pady=10)

                var_box_lbl['box_'+head]=Entry(rf)
                var_box_lbl['box_'+head].grid(row=row,column=column+1,padx=10)
                var_box.append(var_box_lbl['box_'+head])
            row+=1

        command_frame=LabelFrame(edit_frame,text="COMMANDS",width=500,height=146,background='gray')
        command_frame.grid(sticky=N,row=0,column=1,columnspan=100,rowspan=100)
        command_frame.grid_propagate(False)

        btn_add=Button(command_frame,text="Insert Record",command=insert_record)
        btn_add.grid(row=0,column=0,padx=10,pady=20)

        btn_delet=Button(command_frame,text="Delete Record",command=delete_record)
        btn_delet.grid(row=0,column=1,padx=10,pady=20)

        btn_delet_sel=Button(command_frame,text="Delete All Records",command=delete_all_records)
        btn_delet_sel.grid(row=0,column=2,padx=10,pady=20)

        btn_edit=Button(command_frame,text="Update Record",command=edit_record)
        btn_edit.grid(row=1,column=0,padx=10,pady=20)
        

        btn_quary_data=Button(command_frame,text="Restart Data",command=quary_data)
        btn_quary_data.grid(row=1,column=1,padx=10,pady=20)
        
        # ==============================================================================================================================


        # Search Records===================================================================================================================
        search_frame=LabelFrame(edit_frame,text='SEARCH RECORDS',background='gray',width=485,height=150)
        search_frame.grid(row=1,column=2,sticky=S)
        search_frame.grid_propagate(False)

        lbl=Label(search_frame,text='Search By.....',background='gray',foreground='black',font=('helvetica',12))
        lbl.grid(row=1,column=0,pady=45)
    
        # # Drop Down Box
        search_drop = ttk.Combobox(search_frame, values=data_heading,justify='center')
        search_drop.set(data_heading[-1])
        search_drop.grid(row=1,column=1,padx=5)

        lbl=Label(search_frame,text=' = ',background='gray',font=('helvetica',10))
        lbl.grid(row=1,column=2)

        search_box=Entry(search_frame,font=('helvetica',10),width=20)
        search_box.grid(row=1,column=3)

        search_btn=Button(search_frame,text='Search',background='green',fg='white',font=('helvetica',10),command=search_record)
        search_btn.grid(row=1,column=4,padx=15)
        # ====================================================================================================================================



        # Edit Records===========================================================================================================================
        myt.bind("<ButtonRelease-1>",select_record)

        edit_f=LabelFrame(root,text="",width=1400,height=100,font=("helvatica",15))
        edit_f.pack()
        edit_f.grid_propagate(False)
        # ======================================================================================================================================

        quary_data()

        conn.close()

    def run(self):
        self.main_window.mainloop()
