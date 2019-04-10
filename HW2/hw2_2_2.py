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

''' modify the last term'''
def mdflt(lst):
	outlst = [[] for _ in range(len(lst))]
	for i in range(len(lst)):
		for j in range(len(lst[i])):
			if j == len(lst[i])-1:
				outlst[i].append(lst[i][-1][0])
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

'''find the mean'''
def findm(lst):
	outlst = []
	for i in range(len(lst)):
		try:
			outlst.append(float(np.mean(lst[i])))
		except:
			outlst.append(0)
	return outlst

'''find the standard deviation'''
def findstd(lst):
	outlst = []
	for i in range(len(lst)):
		try:
			outlst.append(float(np.std(lst[i])))
		except:
			outlst.append(0)
	return outlst

'''normalize the data'''
def nmlz(means, stds, lst):
	outlst = [[] for _ in range(len(lst))]
	for i in range(len(lst)):
		for j in range(len(lst[i])):
			if type(lst[i][j]) == int or type(lst[i][j]) == float:
				outlst[i].append((lst[i][j]-means[j])/stds[j])
			else:
				outlst[i].append(lst[i][j])
	return outlst

''' add number as final list'''
def addo(lst):
	outlst = [[] for _ in range(len(lst[0]))]
	for j in range(len(lst[0])):
		for i in range(len(lst)+1):
			if i == len(lst):
				outlst[j].append(j)
			else:
				outlst[j].append(lst[i][j])
	return outlst

''' calculate the D2 distance'''
def caldis(slst,rlst):
	outlst = [[] for _ in range(len(rlst))]
	for i in range(len(rlst)):
		for j in range(len(slst)):
				if i == len(rlst)-1:
					#a = 0
					outlst[-1].append(slst[j][-1])
				elif type(rlst[i]) == str:
					if rlst[i] == slst[j][i]:
						outlst[i].append(0)
					else:
						outlst[i].append(1)
				else:
					outlst[i].append(rlst[i]-slst[j][i])
	return outlst

''' calculate sum'''
def calsum(lst):
	innerlst = [[],[]]
	outlst = []
	for i in range(len(lst[0])):
		nsum = 0
		for j in range(len(lst)-1):
			nsum += lst[j][i]*lst[j][i]
		innerlst[0].append(float(np.sqrt(nsum)))
		innerlst[1].append(lst[-1][i])
	outlst = addo(innerlst)
	return outlst

'''voting strategy'''
def votf(k, lst):
	ranklst = [[] for _ in range(len(lst[0]))]
	sortlst = []
	prelst = [[] for _ in range(len(lst))]
	outlst = []
	for i in range(len(lst[0])):
		for j in range(len(lst)):
			ranklst[i].append(lst[j][i])
	sortlst = sorted(ranklst[0])
	for n in range(len(sortlst)):
		for m in range(len(sortlst)):
			if n!=m:
				if sortlst[n] == sortlst[m]:
					print('have same sum')
			if sortlst[n] == ranklst[0][m]:
				prelst[n].append(ranklst[0][m])
				prelst[n].append(ranklst[1][m])
				prelst[n].append(ranklst[2][m])
	if k == 1:
		outlst.append(prelst[0][1])
	elif k <= 0:
		print('error')
	else:
		posno = 0
		negno = 0
		for i in range(k):
			if prelst[i][1] == '+':
				posno += 1
			else:
				negno += 1
		if posno > negno:
			outlst.append('+')
		elif posno < negno:
			outlst.append('-')
		else:
			outlst.append(prelst[0][1])
	outlst = str(outlst[0])
	return outlst

'''calculate the accuracy''' 
def acur(rlst,slst):
	if len(rlst) != len(slst):
		print('Input error!')
	outp = 0
	totalnum = len(rlst)
	right_value = 0
	for i in range(len(rlst)):
		if rlst[i] == slst[i][-1]:
			right_value += 1
	outp = (right_value/totalnum)*100
	return outp


'''main function: k is the k-NN's k, and sourcename as well as file name are as their names'''
def kNNC(k,sourcename,filename):
	# get source name
	source_list = getlist(sourcename)
	# read the data first
	read_list = getlist(filename)
	# get rid of '\n'
	source_list = mdflt(source_list)
	read_list = mdflt(read_list)

	# generate output list
	out_list = [[],[]]
	# initialize lists
	# source lists
	n = len(source_list[0])
	# source lists
	sflsts = [[] for _ in range(n)]
	nsflsts = []
	# other sources
	rmeans = []
	smeans = []
	rstds = []
	sstds = []
	numrl = []
	numsl = []
	results = []
	# loaded lists
	rflsts = [[] for _ in range(n)]
	nrflsts = []
	### make the data to be its transpose
	# input loaded data into empty lists
	for i in range(len(read_list)):
		for j in range(n):
			rflsts[j].append(read_list[i][j])
	# input source data into empty lists
	for i in range(len(source_list)):
		for j in range(n):
			sflsts[j].append(source_list[i][j])
	# modify lists
	rflsts = mknum(rflsts)
	sflsts = mknum(sflsts)
	numrl = mknum(read_list)
	numsl = mknum(source_list)
	# calculate means and stds
	rmeans = findm(rflsts)
	smeans = findm(sflsts)
	rstds = findstd(rflsts)
	sstds = findstd(sflsts)
	# normalize the data
	nrflsts = nmlz(rmeans, rstds, numrl)
	nsflsts = nmlz(smeans, sstds, numsl)
	# generate empty list for saving results
	showlst = []
	# kNN algorithm
	for i in range(len(nrflsts)):
		results = caldis(nsflsts, nrflsts[i])
		#results = modfstr(strno, results)
		results = calsum(results)
		results = votf(k, results)
		showlst.append(results)
	# calculate the accuracy
	accuracy = acur(showlst, read_list)
	# store the data into list
	out_list.append(showlst)
	out_list.append(accuracy)
	#####print out the results#####

	print('According to kNN algorithm, the labels in testing dataset should be:')
	for i in range(len(showlst)-1):
		print(showlst[i],end = ', ')
	print(showlst[-1])
	print('The accuracy of kNN algorithm is:', end = '   ')
	print(str(round(accuracy,4))+' %')
	return out_list


# actions when running .py file
if __name__ == '__main__':
	kNNC(20,'crx.training.processed','crx.testing.processed')