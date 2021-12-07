import sympy as sy
from sympy.physics import mechanics as mc
import numpy as np
from sympy import sympify, nsimplify


if __name__ == "__main__" :
	# assigning variables to sympi
	R, theta, alpha, a, d = sy.symbols('R, theta, alpha, a, d')


	# Calculating Transformation Matrix with variables
	A = sy.Matrix([[sy.cos(theta), -sy.sin(theta)*sy.cos(alpha), sy.sin(theta)*sy.sin(alpha), a*sy.cos(theta)], 
									 [sy.sin(theta), sy.cos(theta)*sy.cos(alpha), -sy.cos(theta)*sy.sin(alpha), a*sy.sin(theta)],
									 [0, sy.sin(alpha), sy.cos(alpha),d],
									 [0, 0, 0, 1]])
	pi=np.pi


	A0_1= A.subs({alpha:-pi/2, d:150, theta:0, a:0})

	A1_2= A.subs({alpha:0, d:0, theta:pi/2, a:0})
	A1_2=nsimplify(A1_2,tolerance=1e-3,rational=True)

	A2_3= A.subs({alpha:pi/2, d:0, theta:0, a:0})
	A2_3=nsimplify(A2_3,tolerance=1e-3,rational=True)

	A3_4= A.subs({alpha:-pi/2, d:150, theta:pi/2, a:0})
	A3_4=nsimplify(A3_4,tolerance=1e-3,rational=True)

	# Transformations
	T0_1=A0_1
	T0_2=(A0_1*A1_2)
	T0_3=(T0_2*A2_3)
	T0_4=(T0_3*A3_4)
	
	f_x, f_y, f_z = T0_4[3,0], T0_4[3,1], T0_4[3,2]
