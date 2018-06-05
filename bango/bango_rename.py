from scanfile import fileswithin

def list_lower(list_str):
	for i in range(len(list_str)):
		list_str[i] = list_str[i].lower()
		
		
def read_list_txt(filepath):
	with open(filepath) as f:
		items = f.readlines()
	for i in range(len(items)):
		items[i] = items[i].strip()
	return items

def main():
	# path = input('请输入路径：')
	path = 'I:\\'
	filenames = fileswithin(path)
	list_lower(filenames)	
	# print(filenames)
	
	bangos = read_list_txt('./c_bango.txt')
	list_lower(bangos)
	print(bangos)
		
if __name__ == '__main__':
	main()
