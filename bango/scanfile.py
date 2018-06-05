import os

def scanfile(path):
	"""扫描路径下的包括子文件夹下所有的文件"""
	#存文件名
	filenames = []
	#存路径
	filepaths = []
	#存临时子文件夹路径列表
	subfolders = []
	#得出文件夹的子文件夹和文件
	for x in os.listdir(path):
		abs_path_dir = os.path.join(path, x)
		# 如果是文件，存名字和路径
		if not os.path.isdir(abs_path_dir):
			filenames.append(x)
			filepaths.append(abs_path_dir)
		# 如果是文件夹就暂时存路径，待后面递归调用函数
		else:
			subfolders.append(abs_path_dir)
		
	for x in subfolders:
		fns, fps = scanfile(x)
		filenames.extend(fns)
		filepaths.extend(fps)
	return filenames, filepaths
	
	
def fileswithin(path):
	"""扫描路径下的文件，不包括子文件夹的文件"""
	filenames = []
	for x in os.listdir(path):
		abs_path_dir = os.path.join(path, x)
		# 如果是文件，存名字
		if not os.path.isdir(abs_path_dir):
			filenames.append(x)
	return filenames
	
	
def main():
	path = input("输入绝对路径：")
	fns, fps = scanfile(path)
	# print(fns)
	# print(fps)
	with open('./scanfiles.txt', 'w') as f:
		for x in fns:
			f.write(x)
			f.write('\n')
	
if __name__ == "__main__":
	main()
