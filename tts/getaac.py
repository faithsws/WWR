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
import os
text=u"你好"
FLITE=False
MP3=False


dbpath = os.path.split(__file__)[0]
dbfile = os.path.join(dbpath, "pinyin7.db")
print(dbpath)
def GetAac(text):
	salt = ''.join(random.sample(string.ascii_letters + string.digits, 16))
	if FLITE:
		db = sqlite3.connect(dbfile)
		cur = db.cursor()
		print(len(text))
		word = ""
		for zifu in [text[i] for i in range(0,len(text),1) ]:
			print(repr(zifu))
			sql = 'select pinyin from duizhaobiao where hanzi="%s" ' % (zifu)
			pinyin = cur.execute(sql).fetchone()
			if None == pinyin:continue
			pinyin = pinyin[0]
			print(pinyin)

			word = word +  pinyin + " "
			
		print(word)
		p = subprocess.Popen(["flite","-t", word, "-o",os.path.join(dbpath,salt+".wav")])
		p.wait()
		cur.close()
		db.close()
	else:
		p = subprocess.Popen(["espeak","-vzh",'"'+ text+'"', "-w",os.path.join(dbpath,salt+".wav")])
		p.wait()

	ext = ".mp3"
	if MP3:
		ext = ".mp3"
		p1 = subprocess.Popen(["lame",os.path.join(dbpath,salt+".wav"), os.path.join(dbpath,salt+ext)])
		p1.wait()
	else:
		ext = ".aac"
		p1 = subprocess.Popen(["faac",os.path.join(dbpath,salt+".wav"), "-o", os.path.join(dbpath,salt+ext)])
		p1.wait()
	subprocess.Popen(["rm",os.path.join(dbpath,salt+".wav"), "-rf" ])

	return salt+ext
if __name__ == "__main__":
	print(GetAac(text))

