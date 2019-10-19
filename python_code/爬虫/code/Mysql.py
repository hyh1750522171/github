import pymysql


def connectdb():
    print('连接到mysql服务器...')
    # 打开数据库连接
    # 用户名:hp, 密码:Hp12345.,用户名和密码需要改成你自己的mysql用户名和密码，并且要创建数据库TESTDB，并在TESTDB数据库中创建好表Student
    db = pymysql.connect("localhost","hp","Hp12345.","TESTDB")
    print('连接上了!')
    return db


def createtable(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 如果存在表Sutdent先删除
    cursor.execute("DROP TABLE IF EXISTS Student")
    sql = """CREATE TABLE Student (
            ID CHAR(10) NOT NULL,
            Name CHAR(8),
            Grade INT )"""

    # 创建Sutdent表
    cursor.execute(sql)


def insertdb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = """INSERT INTO Student
         VALUES ('001', 'CZQ', 70),
                ('002', 'LHQ', 80),
                ('003', 'MQ', 90),
                ('004', 'WH', 80),
                ('005', 'HP', 70),
                ('006', 'YF', 66),
                ('007', 'TEST', 100)"""

    #sql = "INSERT INTO Student(ID, Name, Grade) \
    #    VALUES ('%s', '%s', '%d')" % \
    #    ('001', 'HP', 60)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        print ('插入数据失败!')
        db.rollback()


def querydb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    #sql = "SELECT * FROM Student \
    #    WHERE Grade > '%d'" % (80)
    sql = "SELECT * FROM Student"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            ID = row[0]
            Name = row[1]
            Grade = row[2]
            # 打印结果
            print ("ID: %s, Name: %s, Grade: %d" % \
                (ID, Name, Grade))
    except:
        print ("Error: unable to fecth data")


def deletedb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 删除语句
    sql = "DELETE FROM Student WHERE Grade = '%d'" % (100)

    try:
       # 执行SQL语句
       cursor.execute(sql)
       # 提交修改
       db.commit()
    except:
        print ('删除数据失败!')
        # 发生错误时回滚
        db.rollback()


def updatedb(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 更新语句
    sql = "UPDATE Student SET Grade = Grade + 3 WHERE ID = '%s'" % ('003')

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        print ('更新数据失败!')
        # 发生错误时回滚
        db.rollback()


def closedb(db):
    db.close()


def main():
    db = connectdb()    # 连接MySQL数据库

    createtable(db)     # 创建表
    insertdb(db)        # 插入数据
    print ('\n插入数据后:')
    querydb(db)
    deletedb(db)        # 删除数据
    print ('\n删除数据后:')
    querydb(db)
    updatedb(db)        # 更新数据
    print('\n更新数据后:')
    querydb(db)

    closedb(db)         # 关闭数据库


class MysqlHelper(object):

    def __init__(self, host='localhost', port=3306, db='test01', user='root', passwd='wangbo123', charset='utf8'):
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)

    def insert(self, sql, params):
        return self.__cud(sql, params)

    def update(self, sql, params):
        return self.__cud(sql, params)

    def delete(self, sql, params):
        return self.__cud(sql, params)

    def __cud(self, sql, params=[]):
        try:
            # 用来获得python执行Mysql命令的方法,也就是我们所说的操作游标
            # cursor 方法将我们引入另外一个主题：游标对象。通过游标扫行SQL 查询并检查结果。
            # 游标连接支持更多的方法，而且可能在程序中更好用。
            cs1 = self.conn.cursor()
            # 真正执行MySQL语句
            rows = cs1.execute(sql, params)
            self.conn.commit()
            # 完成插入并且做出某些更改后确保已经进行了提交，这样才可以将这些修改真正地保存到文件中。
            cs1.close()
            self.conn.close()
            return rows  # 影响到了哪行
        except Exception as e:
            print(e)
            self.conn.rollback()

    def fetchone(self, sql, params=[]):
        # 一次只返回一行查询到的数据
        try:
            cs1 = self.conn.cursor()
            cs1.execute(sql, params)
            row = cs1.fetchone()
            # 把查询的结果集中的下一行保存为序列
            # rint(row)
            # row是查询的值
            cs1.close()
            self.conn.close()
            return row
        except Exception as e:
            print("None", e)

    def fetchall(self,sql,params):
        # 接收全部的返回结果行
        # 返回查询到的全部结果值
        try:
            cs1 = self.conn.cursor()
            cs1.execute(sql, params)
            rows = cs1.fetchall()
            cs1.close()
            self.conn.close()

            return rows
        except Exception as e:
            print("None", e)


if __name__ == '__main__':
    main()
