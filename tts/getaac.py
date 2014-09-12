#!/usr/bin/python
# -*- coding: utf-8 -*-  
import subprocess
import sys
#text = sys.argv[1]
import sqlite3
import random
import string

#print(repr(text))
#print(text.decode('gbk'))
#text=text.decode("gb2312").encode("utf-8")
text=u"你好"
def GetAac(text):
	db = sqlite3.connect("pinyin7.db")
	cur = db.cursor()
	print(len(text))
	word = ""
	for zifu in [text[i] for i in range(0,len(text),1) ]:
		print(repr(zifu))
		sql = 'select pinyin from duizhaobiao where hanzi="%s" ' % (zifu)
		pinyin = cur.execute(sql).fetchone()[0]
		print(pinyin)

		word = word +  pinyin + " "
		
	print(word)
	salt = ''.join(random.sample(string.ascii_letters + string.digits, 16))
	subprocess.Popen(["flite","-t", word, "-o",salt+".wav"])
	subprocess.Popen(["faac",salt+".wav", "-o", salt+".aac"])
	subprocess.Popen(["rm",salt+".wav", "-rf" ])

	cur.close()
	db.close()
	return salt+".aac"
if __name__ == "__main__":
	print(GetAac(text))

