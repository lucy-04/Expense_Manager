import sqlite3 as db
from datetime import date
def init():
    conn = db.connect('spent.db')
    cur = conn.cursor()

    sql = '''
    create table if not exists expenses(
    amount number,
    category string,
    date string
    )
    '''
    cur.execute(sql)
    conn.commit()
    




def log (amount,category):
    global date
    date = date.today()
    conn = db.connect('spent.db')
    cur = conn.cursor()

    sql = '''
    insert into expenses values(
         {},
        '{}',
        '{}'
    )
    '''.format(amount,category,date)


    cur.execute(sql)
    conn.commit()


def view(category = ''):
    conn = db.connect('spent.db')
    cur = conn.cursor()

    if len(category) < 1:
        sql = ''' select * from expenses'''
        total_amount ='''select sum(amount) from expenses'''
    else:
        sql = '''
        select * from expenses where category = '{}' '''.format(category)
        total_amount ='''select sum(amount) from expenses where category = '{}' '''.format(category)
    cur.execute(sql)

    results = cur.fetchall()
    cur.execute(total_amount)

    total = cur.fetchone()
    return total,results


def create_budget_table(tablename):
    conn = db.connect('spent.db')
    cur = conn.cursor()

    sql = '''
    create table '{}'(
    amount number,
    category string,
    message string,
    date string
    )
    '''.format(tablename)
    
    cur.execute(sql)
    conn.commit()
    
def log_budgettable(tablename,amount,category,message =''):
    global date
    date = date.today()
    conn = db.connect('spent.db')
    cur = conn.cursor()

    sql = '''
    insert into '{}' values(
         {},
        '{}',
        '{}',
        '{}'
    )
    '''.format(tablename,amount,category,message,date)


    cur.execute(sql)
    conn.commit()
def existing_tables():

    single_table = []
    conn = db.connect('spent.db')
    cur = conn.cursor()
    show_table ='''SELECT name FROM sqlite_master WHERE type='table' '''
    cur.execute(show_table)
    conn.commit()
    tables = cur.fetchall()  
    for i in tables:
        single_table.append(i[0])
    return single_table

    

def drop():
    conn = db.connect('spent.db')
    cur = conn.cursor()

    sql = '''
    delete from expenses
    '''
    cur.execute(sql)
    conn.commit()

def delete_budget_table(i):

    conn = db.connect('spent.db')
    cur = conn.cursor()

    sql = '''
    drop table '{}'
    '''.format(i)
    cur.execute(sql)   
    conn.commit()

print(existing_tables())