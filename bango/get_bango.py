def is_alphabet(uchar):
	if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
		return True
	else:
		return False


with open('./scanfiles.txt', 'r') as f:
	filenames = f.read()
#用换行符隔开的名字转为列表	
filenames = filenames.split('\n')
# print(filenames)
for i in range(len(filenames)):
	#去掉扩展名
	filenames[i] = filenames[i].split('.')[0]
	#只保留英文
	filenames[i] = ''.join([x for x in filenames[i] if is_alphabet(x)])
# print(filenames)	
finalnames = []
#把名字列表去重
for x in filenames:
	if x not in finalnames and x:
		finalnames.append(x)
finalnames.sort()
# print(finalnames)
out = input("输入输出文件名：")
with open(out, 'w') as f:
	for x in finalnames:
		f.write(x)
		f.write('\n')
	
