import sympy as sy
from sympy.physics import mechanics as mc
import numpy as np
from sympy import sympify, nsimplify
from forward_kinematics import forward
from sympy import Integral, Matrix, pi, pprint

def Inverse_kin(T0_4, T0_3, T0_2, T0_1, X):
    #Calculates  inverse kinematics 
    f=T0_4[:3,3]
    J_half=f.jacobian(X)
    # J_otherhalf=T0_1[:3,2].row_join(T0_2[:3,2].row_join(T0_3[:3,2].row_join(T0_4[:3,2].row_join(T0_5[:3,2]))))
    J_otherhalf=T0_1[:3,2].row_join(T0_2[:3,2].row_join(T0_3[:3,2].row_join(T0_4[:3,2])))

    J=J_half.col_join(J_otherhalf)
    J=nsimplify(J,tolerance=1e-3,rational=True)
    # print(J)
    return J

if __name__ == "__main__" :

    R, theta, alpha, a, d, theta1, theta2, theta3, theta4, theta5, d1, d2, d3, d4, d5 = sy.symbols('R, theta, alpha, a, d, theta1, theta2, theta3, theta4, theta5, d1, d2, d3, d4, d5')
    pi=np.pi
    X = [theta1, theta2, theta3, theta4]

    # Solution 0 0 550 
    X_sub = [0,0,0,0]
    
    T0_4, T0_3, T0_2, T0_1 = forward()
    T0_f=T0_4.subs({theta1:X_sub[0],theta2:X_sub[1],theta3:X_sub[2],theta4:X_sub[3], d1:150, d2:0, d3:0, d4:400})
    f_x, f_y, f_z = T0_f[0,3], T0_f[1,3], T0_f[2,3]
    print(f'Locations : {f_x}, {f_y}, {f_z}')
    print('Location calculated from input theta value it is validated using thetas.Using location values we validate joint angles')

    J = Inverse_kin(T0_4, T0_3, T0_2, T0_1, X)
    J_val=J.subs({theta1:X_sub[0],theta2:X_sub[1],theta3:X_sub[2],theta4:X_sub[3], d1:150, d2:0, d3:0, d4:400})
    J_val= nsimplify(J_val,tolerance=1e-3,rational=True)
    J_val=np.array(J_val,dtype='float')
    # print(f'Jacobian for joint angles: {X_sub}')
    # pprint(J_val)
    
    J_inv=np.linalg.pinv(J_val)
    J_inv= nsimplify(J_inv,tolerance=1e-3,rational=True)

    print("Inverse kinematics Validation")
    print(f'Location of end effector {[f_x, f_y, f_z, 0, 0, 0]}')

    pos = np.matrix([f_x, f_y, f_z, 0, 0, 0])
    # pos = np.matrix([0, 0, -150, 0, 0, 0])
    j_a =(J_inv@pos.T)*pi
    print('Joint Angles')
    print(f'Theta1 : {j_a[0][0].flatten()}')
    print(f'Theta2 : {j_a[1][0].flatten()}')
    print(f'Theta3 : {j_a[2][0].flatten()}')
    print(f'Theta4 : {j_a[3][0].flatten()}')
    print(f'Theta5 : [[0]]')




