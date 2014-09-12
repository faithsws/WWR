import sqlite3

db = sqlite3.connect("pinyin8.db")
db.text_factory=lambda x: unicode(x, "utf-8", "ignore") 
cur = db.cursor()
cur.execute('create table duizhaobiao (hanzi varchar(4) not null,pinyin varchar(10),fayin varchar(10))')
db.commit()
cnt = 0
with open("2.txt") as f:
    for line in f.readlines():
        token = line.split()
        if len(token) != 3: continue
        pinyin = token[1]
        fayin = token[1]
        for hanzi in [ token[2][i:i+2] for i in range(0,len(token[2]),2) ]:
            utf8 = hanzi.decode('gb2312')#.encode('utf-8')
            print(repr(utf8))
            cnt = cnt + 1
            sql = 'insert into duizhaobiao values("%s","%s","%s")' %(utf8,pinyin,fayin)
            cur.execute(sql)
db.commit()
cur.close()
db.close()
print(cnt)
