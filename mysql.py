
import pymysql as sq
#import sys
def loginsql(host,user,pa):  
#host='192.168.2.4'
#user='root'
#pa='Ed0911872587+'
    conn = sq.connect(host,user,pa)
    conn.select_db('mcpt')
    cur=conn.cursor()
    cur.execute("select * from pt;")
    res=cur.fetchall()
    return res
    if user and pa != None:
        for i in j:
            return j
            #if user in name and passwd in password:
                #return j
                #break
    #if password and name != None:
        #for uswd in res:
            #user = uswd[0]
            #passwd = uswd[1]
            #if name in user and password in passwd:
                #for j in res:
                    #print("{}\t{}".format(j[0],j[1]))
                    
                #break
        else:
            return error()
            #print('your user or password is Wrong!!!!')
    else:
        return error()
        #print('your user or password is None!!!!')    
    cur.close()
    conn.commit()
    conn.close()
def error():
    msg="wrong"
    return msg    
