import numpy as np

#Tuning parameters
eps = 0.1 		#should be decreased over time
alpha = 0.4  	#should be decreased over time

#set up a table of states
states = np.full((3, 3), 0.5) #learned *value*


#Policy
V(s) = V(s) + alpha*( V(s_new) - V(s) )





#