import sympy as sy
from sympy.physics import mechanics as mc
import numpy as np
from sympy import sympify, nsimplify

def forward() :
	# assigning variables to sympi
	R, theta, alpha, a, d, theta1, theta2, theta3, theta4, theta5, d1, d2, d3, d4, d5 = sy.symbols('R, theta, alpha, a, d, theta1, theta2, theta3, theta4, theta5, d1, d2, d3, d4, d5')


	# Calculating Transformation Matrix with variables
	A = sy.Matrix([[sy.cos(theta), -sy.sin(theta)*sy.cos(alpha), sy.sin(theta)*sy.sin(alpha), a*sy.cos(theta)], 
									 [sy.sin(theta), sy.cos(theta)*sy.cos(alpha), -sy.cos(theta)*sy.sin(alpha), a*sy.sin(theta)],
									 [0, sy.sin(alpha), sy.cos(alpha),d],
									 [0, 0, 0, 1]])
	pi=np.pi


	A0_1= A.subs({alpha:pi/2, d:d1, theta:theta1, a:0})

	A1_2= A.subs({alpha:0, d:d2, theta:theta2, a:0})
	A1_2=nsimplify(A1_2,tolerance=1e-3,rational=True)

	A2_3= A.subs({alpha:-pi/2, d:d3, theta:theta3, a:0})
	A2_3=nsimplify(A2_3,tolerance=1e-3,rational=True)

	A3_4= A.subs({alpha:pi/2, d:d4, theta:theta4, a:0})
	A3_4=nsimplify(A3_4,tolerance=1e-3,rational=True)

	A4_5= A.subs({alpha:pi/2, d:d5, theta:theta5, a:0})
	A4_5= nsimplify(A4_5,tolerance=1e-3,rational=True)

	# Transformations
	T0_1=A0_1
	T0_1=nsimplify(T0_1,tolerance=1e-3,rational=True)

	T0_2=(T0_1*A1_2)
	T0_2=nsimplify(T0_2,tolerance=1e-3,rational=True)

	T0_3=(T0_2*A2_3)
	T0_3=nsimplify(T0_3,tolerance=1e-3,rational=True)

	T0_4=(T0_3*A3_4)
	T0_4=nsimplify(T0_4,tolerance=1e-3,rational=True)

	# T0_5=(T0_4*A4_5)
	# T0_5=nsimplify(T0_5,tolerance=1e-3,rational=True)

	# T0_f=T0_5.subs({theta1:0,theta2:pi/2,theta3:0,theta4:pi/2,theta5:pi/2, d1:150, d2:0, d3:0, d4:100, d5:100})
	# return T0_5
	return T0_4, T0_3, T0_2, T0_1


if __name__ == "__main__" :
	T0_4, T0_3, T0_2, T0_1 = forward()
    T0_f=T0_4.subs({theta1:X_sub[0],theta2:X_sub[1],theta3:X_sub[2],theta4:X_sub[3], d1:150, d2:0, d3:0, d4:400})
    f_x, f_y, f_z = T0_f[0,3], T0_f[1,3], T0_f[2,3]
    print(f'Locations : {f_x}, {f_y}, {f_z}')
