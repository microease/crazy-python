# coding:utf-8
# File Name：     exec_dll.py
# Description :
# Author :       micro
# Date：          2019/12/18
import sqlite3

conn = sqlite3.connect('first.db')
c = conn.cursor()
c.execute("""
    create table user_tb(
    _id integer primary key autoincrement,
    name text,
    pass text,
    gender text
    )
""")
c.execute("""
create table order_db(
    _id integer primary key autoincrement,
    item_name text,
    item_number real,
    user_id inteter,
    foreign key(user_id) references user_tb(_id)
)
""")
c.close()
conn.close()