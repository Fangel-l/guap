import sqlite3

connect = sqlite3.connect("users_bot.db", check_same_thread=False)
cursor = connect.cursor()

def add_db(info_user, name_group):
    cursor.execute(f"""      
        CREATE TABLE IF NOT EXISTS {name_group}(
        user_id INTEGER PRIMARY KEY,
        user_name TEXT, 
        tg_id INTEGER,
        nikname TEXT
    );
    """)

    cursor.execute(f"SELECT user_id, tg_id FROM {name_group};")
    check_id = cursor.fetchall()
    connect.commit()

    if len(check_id) == 0:
        info_user[0] = 1
        cursor.execute(f"INSERT INTO {name_group} VALUES (?, ?, ?, ?);", info_user)
        connect.commit()
    else:
        flag = True
        for i in range(len(check_id)):
            if info_user[2] == check_id[i][1]:
                flag = False
                break

        if flag:
            info_user[0] = check_id[-1][0] + 1
            cursor.execute(f"INSERT INTO {name_group} VALUES (?, ?, ?, ?);", info_user)
            connect.commit()


def db_get(name_group):
    cursor.execute(f"SELECT user_name, tg_id, nikname FROM {name_group}")
    all_users = cursor.fetchall()
    connect.commit()
    return all_users

def update_username(name_group, username, tg_id):
    cursor.execute(f"""UPDATE {name_group} SET nikname = '{username}' WHERE tg_id = {tg_id}""")
    connect.commit()



def del_user_db(id_tg, name_group):
    cursor.execute(f"""DELETE from {name_group} WHERE tg_id ={id_tg};""")
    connect.commit()
