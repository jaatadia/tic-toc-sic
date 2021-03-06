import csv
import matplotlib.pyplot as plt
import numpy as np

from typing import Iterable, Tuple, TypeVar
T = TypeVar("T")

def grouped(iterable: Iterable[T], n=2) -> Iterable[Tuple[T, ...]]:
	"""s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), ..."""
	return zip(*[iter(iterable)] * n)

ymin = 0
ymax = 0

with open('samples.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=';')
	first = True
	for row in plots:
		for i in row:
			if i!='':
				y = int(i)
				if(first):
					ymin = y
					ymax = y
					first = False
				if y<ymin:
					ymin = y
				if y>ymax:
					ymax = y 

nbins=600/20
bins=[]
increment = (ymax - ymin)/nbins
acum = ymin
while (acum<=ymax):
	bins = bins + [acum]
	acum = acum + increment

counter = 0
colors = ['green', 'red', 'blue']

with open('samples.csv','r') as csvfile:	
	plots = csv.reader(csvfile, delimiter=';')

	for (rowI, rowJ) in grouped(plots):
		plt.figure(counter) 
		plt.plot(range(0,600), [int(cell) for cell in rowI[1:]])
		#plt.plot(range(0,600), [np.nan if (cell == '') else int(cell) for cell in rowJ[1:]], 'o-')

		color=0
		position = 0
		for cell in rowJ[1:]:
			if(cell!=''):
				plt.axvline(position, color=colors[color], linestyle='dashed', label=cell)
				color+=1
			position += 1

		plt.title('Iteration ' + str(counter))
		plt.xlabel('Sample')
		plt.ylabel('Phi (MicroSeconds)')
		axes = plt.gca()
		axes.set_xlim([0,599])
		axes.set_ylim([ymin,ymax])
		plt.legend()
		plt.savefig('Iteration ' + str(counter) + '.png')
		plt.close()


		plt.figure(counter) 
		plt.hist([int(cell) for cell in rowI[1:]], bins=30)
		#plt.plot(range(0,600), [np.nan if (cell == '') else int(cell) for cell in rowJ[1:]], 'o-')


		color=0
		for cell in rowJ[1:]:
			if(cell!=''):
				plt.axvline(int(cell), color=colors[color], linestyle='dashed', label=cell)
				color+=1

		plt.xlabel('Phi (MicroSeconds)')
		plt.ylabel('Samples')
		plt.title('Iteration ' + str(counter))
		plt.legend()
		plt.savefig('Histogram Iteration ' + str(counter) + '.png')
		plt.close()

		

		counter += 1
