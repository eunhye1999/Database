from random import *
import mysql.connector
import requests
import os
import time

cnx = mysql.connector.connect(user='root', password='tt054202249',host='localhost',database='university')

def insertTranscripts(data):
	# try:
	cursor = cnx.cursor()
	cursor.execute('INSERT INTO university.transcrip(std_id,tr_year,tr_semester,sub_id,grade_char) VALUES (%s,%s,%s,%s,%s)',data)
	# except Exception as e:
	# 	print (data)
	# 	print (e)
	
def insert(data):
	xx = mysql.connector.connect(user='root', password='tt054202249',host='localhost',database='kmutnbdb')
	try:
		cursor = xx.cursor()
		cursor.execute('INSERT INTO kmutnbdb.main_transcrip VALUES (%s,%s,%s,%s,%s)',data)
	except Exception as e:
		print (data)
		print (e)
	xx.commit()
	xx.close()

sql = '''
SELECT std.std_id, std.std_fname, std.std_lname, SUM(sub.credit* g.grade_id)/ SUM(sub.credit)
FROM main_transcrip m
INNER JOIN student std ON m.std_id = std.std_id
INNER JOIN subject sub ON m.sub_id = sub.sub_id
INNER JOIN grade g ON m.grade_char = g.grade_char
where std.std_id = "5801012620020"
'''
sql2 = '''
SELECT MAX(id) AS max_id
FROM group3.transcripts_table;
'''



grade = ['A','B+','B','C+','C','D+','D','F']
std_id = ['5801012610091','5801012620020','5801012620046','5801012620071','5801012630050']
sub_id = ['010123101','010123102','040203111','040313005','040313006','080103001','080203901','080303505',
'010113010','010113011','010123103','040203112','040313007','040313008','080103002','080303501','010123104','010123106',
'010123107','010123108','010123109','040503001','010123110','010123111','010123112','010123113','010123114','040203100',
'010123115','010123116','010123117','010123118','010123119','040313017','080103016','010123105','040313016']
start = time.time()
for i in range(0,100):
	insert([choice(std_id),randint(2012,2017),randint(1,2),choice(sub_id),choice(grade)])

# for i in range(0,100):
# 	insertTranscripts([choice(std_id),randint(2012,2017),randint(1,2),choice(sub_id),choice(grade)])

cnx.commit()
cnx.close()
end = time.time()
print(end - start ,'s')
# insertTranscripts([choice(std_id),randint(2012,2017),randint(1,2),choice(sub_id),choice(grade)])