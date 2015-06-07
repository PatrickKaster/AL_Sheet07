#!/usr/bin/env python
import numpy as np
import math
import pylab as P

""" author: Patrick Kaster (kaster@cs.uni-bonn.de) """



if __name__ == "__main__":
	
	N = 1000
	Z = 2000
	
	cube = np.random.rand(N,Z)

	distances = []
	angles = []

	for i in range(0, cube.shape[1]-1):
    		for j in range(i, cube.shape[1]-1):
        		v1 = cube[:,i]
			v2 = cube[:,j]
			v1Minusv2 = v1-v2
			distances.append(math.sqrt(np.dot(v1Minusv2, v1Minusv2)))
			v1 = v1 / np.linalg.norm(v1)
			v2 = v2 / np.linalg.norm(v2)		
			dotprod = np.dot(v1, v2)
			# fix precision problem			
			if (dotprod > 1.0):
				dotprod = 1.0
			angles.append(math.degrees(math.acos(dotprod)))

	avg = np.sum(distances)/len(distances)	
	print "avg. distance: ", avg
	fig1 = P.figure()
	n, bins, patches = P.hist(angles, 180, normed=1, histtype='bar')
	fig1.suptitle("angle distribution")
	P.xlabel("angles in degrees")
	fig2 = P.figure()	
	n, bins, patches = P.hist(distances, 32, normed=1, histtype='bar') # max hamming distance is sqrt(1000)~32
	fig2.suptitle("distance distribution")
	fig1.show()
	fig2.show()
	P.show()
	
	

