from my_db import My_db
db_name='codemy'
table_name1='program_langs'
table_name2='program_user'
db=My_db(db_name,table_name2)


"""
-----------------SYNTAX OF JOIN------------------------
        (SELECT * or COLUMN , COLUMN ,COLUMN

                FROM table1 JOIN table2

                WHERE table1.ID = table2.ID)
"""
db.display1(f"""
                SELECT * FROM {table_name1} , {table_name2}
            """)


db.display2(f"""
                SELECT * 
                FROM {table_name2} l JOIN {table_name1} u
                WHERE u.lang_id = l.lang_id
            """)


db.display3(f"""
                SELECT * FROM {table_name1}, {table_name2} 
                WHERE program_user.lang_id = program_langs.lang_id
            """)











db.command(f"""
        CREATE TABLE IF NOT EXISTS program_langs(lang_name VARCHAR(255) , lang_id INT AUTO_INCREMENT  , PRIMARY KEY(lang_id))
        """)

db.command(f"""
        CREATE TABLE IF NOT EXISTS program_user(progra_name VARCHAR(255) , 
        program_id INT AUTO_INCREMENT ,
        lang_id INT NOT NULL , 
        PRIMARY KEY(program_id) ,
        FOREIGN KEY(lang_id) REFERENCES program_langs(lang_id))
        """)




db.run()