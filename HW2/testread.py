''' read the files'''
def getlist(filename):
	read_list = []
	with open(filename) as f:
		for line in f:
			line_data = line.strip()
			line_data = line.split(',')
			read_list.append(line_data)
	return read_list


p_list = getlist('crx.training.processed')
for i in range(len(p_list)):
	print(p_list[i])
print(len(p_list[1]))




#if __name__ == '__main__':
#	print_list(getlist('crx.data.testing.processed'))
