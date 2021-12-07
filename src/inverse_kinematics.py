#!/usr/bin/env python
import numpy as np

th1 = 0, th2 = pi/2, th3 = 0, th4 = pi/2 

a1 = 0, a2 = 0, a3 = 0, a4 = 0

r11 = 1, r12 = 0, r13 = 0
r21 = 0, r22 = 1, r23 = 0
r31 = 0, r32 = 0, r33 = 1

dx = 30, dy = -20, dz = -50

th1 = np.arctan2(dy, dx)

s = dz - a1, r = np.sqrt(dx*dx + dy*dy - a2*a2)
D = (dx*dx + dy*dy - a2*a2 + s*s - a2*a2 - a3*a3)/(2*a2*a3)

th3 = np.arctan2(np.sqrt(1-D*D), D)

s1 = np.sin(th1), c1 = np.cos(th1), s3 = np.sin(th3), c3 = np.cos(th3)

th2 = np.arctan2(s, r) - np.tan(((a3*s3)/a2) + a3*c3)

s23 = np.sin(th2+th3), c23 = np.cos(th2+th3)

th4 = np.arctan2(-c1*s23*r13 - s1*s23*r33 + c23*r33,
	c1*c23*r13 + s1*c23*r23 + s23*r33)
