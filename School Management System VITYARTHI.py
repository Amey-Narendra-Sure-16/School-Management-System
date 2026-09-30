import sqlite3
users = {'Principal': 'Boss@123', 'Teacher': 'Staff@123', 'Student': 'guest2026'}
con = sqlite3.connect('school_data.db')
con.execute("""create table if not exists student (student_id int primary key,
    name varchar(30), class varchar(5), section varchar(5), phone_number varchar(15))""")

def get_text(msg):
    while not (v := input(msg).strip()):
        print("can't leave this blank")
    return v
def get_number(msg):
    while not (v := get_text(msg)).isdigit():
        print('numbers only please')
    return int(v)
def find(sid):
    return con.execute('select * from student where student_id=?', (sid,)).fetchone()
def show(rows):
    for r in rows: print(*r, sep=' | ')
def add_student():
    sid = get_number('enter student roll number : ')
    if find(sid): return print('that roll number is already taken')
    with con: con.execute('insert into student values (?,?,?,?,?)', (sid, get_text('name : '),
        get_text('class : '), get_text('section : '), get_text('guardian phone : ')))
    print('saved')
def search_student():
    data = find(get_number('enter student_id : '))
    show([data]) if data else print('no student with that id')
def show_all():
    rows = con.execute('select * from student order by student_id').fetchall()
    print('total records:', len(rows)); show(rows)
def update_student():
    sid = get_number('enter student_id to update : ')
    if not find(sid): return print('record not found')
    choice = get_number('change what? 1.name 2.class 3.section 4.phone : ')
    if not 1 <= choice <= 4: return print('not a valid option')
    column = ['name', 'class', 'section', 'phone_number'][choice - 1]
    with con: con.execute(f'update student set {column}=? where student_id=?', (get_text('new value : '), sid))
    print('updated')
def delete_student():
    sid = get_number('enter student id to delete : ')
    if not find(sid): return print('no such student_id')
    with con: con.execute('delete from student where student_id=?', (sid,))
    print('deleted')
def login():
    for i in range(3):
        if users.get(input('username : ')) == input('password : '):
            print('login successful'); return True
        print('wrong username/password,', 2 - i, 'tries left')
    return False

actions = {1: add_student, 2: search_student, 3: show_all, 4: update_student, 5: delete_student}
print('### SCHOOL MANAGEMENT SYSTEM ###')
if login():
    option = 0
    while option != 6:
        print('\n1. add  2. search  3. show all  4. update  5. delete  6. exit')
        option = get_number('pick an option : ')
        if option in actions: actions[option]()
        elif option != 6: print('not a valid choice')
con.close()
