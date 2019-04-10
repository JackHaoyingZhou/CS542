import numpy as np

''' read the files'''
def getlist(filename):
	read_list = []
	with open(filename) as f:
		for line in f:
			line_data = line.strip()
			line_data = line.split(',')
			read_list.append(line_data)
	return read_list

'''median letter of letters'''
def midletter(lst):
	sortedlst = sorted(lst)
	index = (len(lst)-1)//2
	return sortedlst[index]

'''get rid of '?'''
def dequestion(lst):
	outlst = [[] for _ in range(len(lst))]
	for i in range(len(lst)):
		for j in range(len(lst[i])):
			if lst[i][j] == '?':
				continue
			else:
				outlst[i].append(lst[i][j])
	return outlst

'''change str into int or float if possible'''
def mknum(lst):
	outlst = [[] for _ in range(len(lst))]
	for i in range(len(lst)):
		for j in range(len(lst[i])):
			try:
				outlst[i].append(int(lst[i][j]))
			except:
				try:
					outlst[i].append(float(lst[i][j]))
				except:
					outlst[i].append(lst[i][j])
	return outlst

'''backup digit  eg.  a = '1', s = a.zfill(5)'''

'''find the replace element'''
def findr(lst):
	outlst = []
	for i in range(len(lst)):
		if (type(lst[i][1]) == int) or (type(lst[i][1]) == float) :
			outlst.append(np.mean(lst[i]))
		else:
			outlst.append(midletter(lst[i]))
	return outlst

'''modify the results of replacement element'''
def modfr(lst):
	outlst = []
	outlst.append(lst[0])
	outlst.append(str(round(lst[1],2)))
	outlst.append(str(round(lst[2],2)))
	outlst.append(lst[3])
	outlst.append(lst[4])
	outlst.append(lst[5])
	outlst.append(lst[6])
	outlst.append(str(round(lst[7],3)))
	outlst.append(lst[8])
	outlst.append(lst[9])
	a = str(int(lst[10]))
	outlst.append(a.zfill(2))
	outlst.append(lst[11])
	outlst.append(lst[12])
	b = str(int(lst[13]))
	outlst.append(b.zfill(5))
	outlst.append(str(int(lst[14])))
	return outlst


'''main function'''
def process(filename):
	#use entire dataset as source
	sourcefl = 'crx.data'
	source_list = getlist(sourcefl)
	# read the data first
	read_list = getlist(filename)
	# generate output list
	out_list = [[] for _ in range(len(read_list))]
	# initialize lists
	# source lists
	n = len(source_list[15])
	sflsts = [[] for _ in range(n)]
	sflsts_p = [[] for _ in range(n-1)]
	sflsts_n = [[] for _ in range(n-1)]
	resflsts_p = []
	resflsts_n = []
	results_p = []
	results_n = []
	# loaded lists
	rflsts = [[] for _ in range(n)]
	# input loaded data into empty lists
	for i in range(len(read_list)):
		for j in range(n):
			rflsts[j].append(read_list[i][j])
	# input source data into empty lists
	for i in range(len(source_list)):
		for j in range(n):
			sflsts[j].append(source_list[i][j])
	# get data for positive and negative sign
	for i in range(len(source_list)):
		for j in range(n-1):
			if source_list[i][15] == '+\n':
				sflsts_p[j].append(source_list[i][j])
			else:
				sflsts_n[j].append(source_list[i][j])

	# get rid of '?'
	sflsts_p = dequestion(sflsts_p)
	sflsts_n = dequestion(sflsts_n)
	# change into int or float if possible
	sflsts_p = mknum(sflsts_p)
	sflsts_n = mknum(sflsts_n)
	# find replace elements
	resflsts_p = findr(sflsts_p)
	resflsts_n = findr(sflsts_n)
	# modify the form
	results_p = modfr(resflsts_p)
	results_n = modfr(resflsts_n)


	'''main part'''
	for i in range(len(rflsts)):
		for j in range(len(rflsts[i])):
			if rflsts[i][15] == '+\n':
				if rflsts[i][j] == '?':
					out_list[j].append(results_p[i])
				else:
					out_list[j].append(rflsts[i][j])
			else:
				if rflsts[i][j] == '?':
					out_list[j].append(results_n[i])
				else:
					out_list[j].append(rflsts[i][j])

	# ready for writing
	outlst = []
	for i in range(len(out_list)):
		for j in range(len(out_list[i])):
			if j == 15:
				outlst.append(out_list[i][j])
			else:
				outlst.append(out_list[i][j] + ',')

	# write into file
	newfile = open(filename[0:3] + filename[8:] + '.processed','w')
	for k in range(len(outlst)):
		newfile.write(outlst[k])
	newfile.close()

# actions when running the python file
if __name__ == '__main__':
	process('crx.data.training')
	process('crx.data.testing')