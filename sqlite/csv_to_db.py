import sqlite3 as db
import os
import csv
from random import *
class MainTable:
	def __init__(self, database):
		self.conn = db.connect(database)
		self.table = "Main"

	def sql_query(self,sql):
		con = self.conn
		with con:
			cur = con.cursor()
			try:
				cur.execute(sql)
				return cur.fetchall()
			except Exception as e:
				print (e)

	def select_all(self):
		con = self.conn
		with con:
			cur = con.cursor()
			cur.execute("SELECT * FROM MainSPK")
		return cur.fetchall()

	def insert(self, data):
		con = self.conn
		with con:
			cur = con.cursor()
			try:
				# cur.execute("PRAGMA foreign_keys = ON")
				cur.execute("INSERT INTO MainSPK VALUES (?,?,?,?,?,?)",data)
			except Exception as e:
				print (data)
				print (e)
			con.commit()

	def delete(self,data):
		con = self.conn
		with con:
			cur = con.cursor()
			cur.execute("DELETE FROM MainSPK WHERE student_id = ? AND year = ? AND semester = ? AND course_code = ?",data)

################
# read csv and insert to db here
################
# main_TB = MainTable("KMUTNBdb.db")
# file_list = []
# for (dirpath, dirnames, filenames) in os.walk('.'):
#         file_list.extend(filenames)
#         break
# csv_file_list = [file for file in file_list if file.endswith('.csv')]
# for file in csv_file_list:
#         print('reading file:', file)
#         with open(file, 'r') as csv_file:
#                 csv_reader = csv.reader(csv_file, delimiter=',')
#                 for row in csv_reader:
#                         main_TB.insert(row)

# i=0
# main_TB = MainTable("KMUTNBdb_v1.db")
# with open("csv/transaction/Fhox.csv", 'r') as csv_file:
# 	csv_reader = csv.reader(csv_file)
# 	for row in csv_reader:
# 		i += 1
# 		print(i)
# 		main_TB.insert(row)

top = MainTable("KMUTNBdb_v1.db")
grade = ['A','B+','B','C+','C','D+','D','F']
std_id = ['5801012610091','5801012620020','5801012620046','5801012620071','5801012630050']
sub_id = ['010123101','010123102','040203111','040313005','040313006','080103001','080203901','080303505',
'010113010','010113011','010123103','040203112','040313007','040313008','080103002','080303501','010123104','010123106',
'010123107','010123108','010123109','040503001','010123110','010123111','010123112','010123113','010123114','040203100',
'010123115','010123116','010123117','010123118','010123119','040313017','080103016','010123105','040313016']
count = 101
for i in range(0,100):
	count += 1
	# top.insert([count,choice(std_id),randint(2012,2017),randint(1,2),choice(sub_id),choice(grade)])
	top.insert([count,'5555','randint(2012,2017)','randint(1,2)','choice(sub_id)','choice(grade)'])

# top.insert(["5801012610091","",'3',"010123101","B+"])
# grade = top.sql_query('''
# 	SELECT std.student_id, std.firstname, std.lastname, SUM(sub.credit* g.grade_id)/ SUM(sub.credit)
# 	FROM MainSPK m
# 	INNER JOIN Student std ON m.student_id = std.student_id
# 	INNER JOIN Subject sub ON m.course_code = sub.course_code
# 	INNER JOIN Grade g ON m.grade_char = g.grade_char
# 	where std.student_id = '5801012610091' 
# 	''')
# print(grade)
