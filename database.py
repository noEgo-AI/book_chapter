import pymysql

connection = pymysql.connect(host='', user='', password='', db='', charset='')
cursor = connection.cursor(pymysql.cursors.DictCursor)
print(2)

# cursor2 = connection.cursor()


# sql = "select * from information"
# cursor.execute(sql)
# rows = cursor.fetchall()
#
#
# print(list(rows[0].keys()))
# for i in rows:
#     print(f'딕셔너리:{i}')
#
# print('------------------------------------')
# # sql = "insert into lsy.information (access_id, password, name) values('e','e','eansoup')"
# # cursor.execute(sql)
# # connection.commit()   # update, create, delete 시에 이걸 기입해야 바뀐다.
#
# sql = "select * from information"
# cursor2.execute(sql)
# rows = cursor2.fetchall()
# # print(rows[0]['local_id'])
#
# for i in rows:
#     print(f'튜플형식 {i}')
#
# print('------------------------------------')
#
# cursor.close()
# cursor2.close()
# connection.close()
#
# # sql = "select * from information"
# # cursor.execute(sql)
# # rows = cursor.fetchall()
# #
# # for i in rows:
# #     print(f'아직 안 닫힌 건가?{i}')

