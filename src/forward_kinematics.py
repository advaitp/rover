import sympy as sy
from sympy.physics import mechanics as mc
import numpy as np
from sympy import sympify, nsimplify

<<<<<<< HEAD

if __name__ == "__main__" :
	# assigning variables to sympi
	R, theta, alpha, a, d = sy.symbols('R, theta, alpha, a, d')
=======
def forward_values(Q,T0_4):
    #caluclates Endfecttor values (x,y,z) by forward kinematics
    T0_w=T0_4.subs({theta1:Q[0],theta2:Q[1],theta3:Q[2],theta4:Q[3],theta5:Q[4],d1:150,d2:420,d3:201+198.5,d4:105.5,d5:100,a1:,a2:,a3:,a4:, a5:})
    return T0_w 

def inverse_kin(Q, T0_4, loc):
    #Calculates  inverse kinematics and gives qdot
    f=T0_7[:3,3]

    X=[theta1,theta2,theta3,theta4]
    J_half=f.jacobian(X)

    J_otherhalf=T0_1[:3,2].row_join(T0_2[:3,2].row_join(T0_3[:3,2].row_join(T0_4[:3,2])))
    J=J_half.col_join(J_otherhalf)
    J=J.subs({d1:360,d2:420,d3:201+198.5,d4:105.5,theta1:Q[0],theta2:Q[1],theta3:0,theta4:Q[2]})
    J=nsimplify(J,tolerance=1e-3,rational=True)

    J=np.array(J,dtype=float)
    J_inv=np.linalg.pinv(J)
    
    # Calculating Transformation Matrix with variables
    X_e= sy.Matrix([[loc[0],loc[1], loc[2]]])

    X_e=np.array(X_e,dtype='float')
    X_f=np.zeros((X_e.shape[0],2*X_e.shape[1]))
    X_f[:,:3]=X_e
    Q=J_inv@X_f.T
    
    return Q

if __name__ == "__main__" :
	# assigning variables to sympi
	R, theta, alpha, a, d,theta1, theta2, theta3, theta4, theta5, theta6, a1, a2, a3, a4, a5, d1, d2, d3, d4, d5 = sy.symbols('R, theta, alpha, a, d,theta1, theta2, theta3, theta4, theta5, theta6, a1, a2, a3, a4, d1, d2, d3, d4, d5')
>>>>>>> 84afa75ac9c06bdfcb22b3980484986799ece04d


	# Calculating Transformation Matrix with variables
	A = sy.Matrix([[sy.cos(theta), -sy.sin(theta)*sy.cos(alpha), sy.sin(theta)*sy.sin(alpha), a*sy.cos(theta)], 
<<<<<<< HEAD
									 [sy.sin(theta), sy.cos(theta)*sy.cos(alpha), -sy.cos(theta)*sy.sin(alpha), a*sy.sin(theta)],
									 [0, sy.sin(alpha), sy.cos(alpha),d],
									 [0, 0, 0, 1]])
	pi=np.pi


	A0_1= A.subs({alpha:-pi/2, d:150, theta:0, a:0})

	A1_2= A.subs({alpha:0, d:0, theta:pi/2, a:0})
	A1_2=nsimplify(A1_2,tolerance=1e-3,rational=True)

	A2_3= A.subs({alpha:pi/2, d:0, theta:0, a:0})
	A2_3=nsimplify(A2_3,tolerance=1e-3,rational=True)

	A3_4= A.subs({alpha:-pi/2, d:100, theta:pi/2, a:0})
=======
	                 [sy.sin(theta), sy.cos(theta)*sy.cos(alpha), -sy.cos(theta)*sy.sin(alpha), a*sy.sin(theta)],
	                 [0, sy.sin(alpha), sy.cos(alpha),d],
	                 [0, 0, 0, 1]])
	pi=np.pi

	# Calculating for  origin o frame to A1
	# angles are in radian
	A0_1= A.subs({alpha:-pi/2, d:d1, theta:theta1, a:a1})

	A1_2= A.subs({alpha:0, d:d2, theta:theta2, a:a2})
	A1_2=nsimplify(A1_2,tolerance=1e-3,rational=True)

	A2_3= A.subs({alpha:pi/2, d:d3, theta:theta3, a:a3})
	A2_3=nsimplify(A2_3,tolerance=1e-3,rational=True)

	A3_4= A.subs({alpha:-pi/2, d:d4, theta:theta4, a:a4})
>>>>>>> 84afa75ac9c06bdfcb22b3980484986799ece04d
	A3_4=nsimplify(A3_4,tolerance=1e-3,rational=True)

	# Transformations
	T0_1=A0_1
	T0_2=(A0_1*A1_2)
	T0_3=(T0_2*A2_3)
	T0_4=(T0_3*A3_4)
<<<<<<< HEAD
	
	f_x, f_y, f_z = T0_4[3,0], T0_4[3,1], T0_4[3,2]

=======

	x = input("Enter your x coordinate")
	y = input("Enter your y coordinate")
	z = input("Enter your z coordinate")
	loc = (x, y, z)

	Q = inverse_kin(Q, T0_4, loc)
	print(f"Joint Angles are {Q[0]}, {Q[1]}, {Q[2]}, {Q[3]}")

	f_T0_4 = forward_values(Q, T0_4)
	f_x, f_y, f_z = f_T0_4[3,0], f_T0_4[3,1], f_T0_4[3,2]
	print(f"Locations through forward kinematics {f_x}, {f_y}, {f_z}")
>>>>>>> 84afa75ac9c06bdfcb22b3980484986799ece04d
