import numpy as np
import sys
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import animation

from Random import Random

if __name__ == "__main__":

	#set default number of samples
	Nsample = 100

	# read the user-provided seed from the command line (if there)
	if '-Nsample' in sys.argv:
		p = sys.argv.index('-Nsample')
		Nsample = int(sys.argv[p+1])
	if '-h' in sys.argv or '--help' in sys.argv:
		print ("Usage: %s -Nsample [number]" % sys.argv[0])
		print
		sys.exit(1) 

	nAccept = 0
	nTotal = 0
	
	# accepted values
	Xaccept = []
	Yaccept = []
	Zaccept = []

	# reject values
	Xreject = []
	Yreject = []
	Zreject = []

	# sample number
	isample = []
	# calculated values of Pi (per sample)
	calcPi = []

	random = Random()

	idraw = max(1,int(Nsample)/100000)
	for i in range(0,Nsample):
		Z = random.rand()
		X = random.rand()
		Y = random.rand()

		nTotal += 1
		if(X*X + Y*Y + Z*Z <= 1): #accept if inside sphere
			nAccept += 1
			if(i % idraw == 0):
				Xaccept.append(X)
				Yaccept.append(Y)
				Zaccept.append(Y)
		else: # reject if outside
			if(i % idraw == 0):
				Xreject.append(X)
				Yreject.append(Y)
				Zreject.append(Y)
		if(i % idraw == 0):
			isample.append(nTotal)
			calcPi.append(6*nAccept/nTotal)



	#plot calculated pi vs sample number
	fig1 = plt.figure()
	plt.plot(isample,calcPi)
	plt.ylabel(r'Approximate $\pi$')
	plt.xlabel("Sample number")
	plt.xlim(0,isample[len(isample)-1])
	ax = plt.gca()
	ax.axhline(y=np.arccos(-1),color='green',label=r'true $\pi$')
	plt.title(r'Approximation of $\pi$ as a function of number of samples')
	plt.legend()

	fig1.savefig("calculatedPiPy.pdf")


	#plot accept/reject points
	fig2 = plt.figure()
	ax = plt.axes(projection='3d')
	ax.plot3D(Xaccept,Yaccept,Zaccept, marker='o',linestyle='',color='green',label='accept')
	ax.plot3D(Xreject,Yreject,Zreject, marker='p',linestyle='',color='red',label='reject')
	plt.ylabel("Y")
	plt.xlabel("X")
	plt.xlabel("Z")
	plt.legend()
    
    # draw sphere
	u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
	x = np.cos(u)*np.sin(v)
	y = np.sin(u)*np.sin(v)
	z = np.cos(v)
	ax.plot_wireframe(x, y, z, color="gray",label=r'$x^2 + y^2 + z^2= 1$')
    
	def rotate(angle):
		ax.view_init(120, azim=angle)

	plt.legend()
	plt.title('Sampled points')
	fig2.savefig("circleQuadPy.pdf")
	rot_animation = animation.FuncAnimation(fig2, rotate, frames=np.arange(0,362,40),interval=10000)