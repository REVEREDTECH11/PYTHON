import numpy as np
import math
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

Rcg2 = 4 #a
Rcg3 = 12 #b
offset = 0 #c
theta2 = 45 #degrees
omega2 = 10 #rads / s
alpha2 = 20 #rads / s^2
m2 = 0.002
m3 = 0.020
m4 = 0.060
friction : 0 #u

I2 = 0.10
I3 = 0.2
Rg2mag = 2
Rg3mag = 5
T3 = 20

theta3 = 166.40 #degrees
alpha3 = -2.40 #rads / s^2

ag2mag = 203.96 
ag2ang = 213.69	#degree

ag3mag = 371.08 
ag3ang = 200.84 #degree

ag4mag = 357.17 
ag4ang = 180 #degree

Rp3 = 0 #in
SRp3 = 0 #degrees

#Force and Torque
Fp3 = 0 #ibf
SFp3 = 0 #degrees
T3 = 20 #ibfin

print("x and y components of the position vectors")
R12x = (Rg2mag*(math.cos(math.radians(theta2) + math.radians(180))))
print(f"R12x = {R12x:.3f} in")
R12y = (Rg2mag*(math.sin(math.radians(theta2) + math.radians(180))))
print(f"R12y = {R12y:.3f} in")
R32x = Rg2mag*(math.cos(math.radians(theta2)))
print(f"R32x = {R32x:.3f} in")
R32y = Rg2mag*(math.cos(math.radians(theta2)))
print(f"R32y = {R32y:.3f} in")
R23x = Rg3mag*(math.cos(math.radians(theta3)))
print(f"R23x = {R23x:.3f} in")
R23y = Rg3mag*(math.sin(math.radians(theta3)))
print(f"R23y = {R23y:.3f} in")
R43x = (Rcg3 - Rg3mag)*math.cos(math.radians(theta3+180))
print(f"R43x = {R43x:.3f} in")
R43y = (Rcg3 - Rg3mag)*math.sin(math.radians(theta3+180))
print(f"R43y = {R43y:.3f} in")
Rp3x = Rp3*math.cos(math.radians(theta3 + 180 + SRp3))
print(f"Rp3x = {Rp3x:.3f} in")
Rp3y = Rp3*math.sin(math.radians(theta3 + 180 + SRp3))
print(f"Rp3y = {Rp3y:.3f} in")
print()

print("x and y components of the accelerations of all moving links")
aG2x = ag2mag*math.cos(math.radians(ag2ang))
print(f"aG2x = {aG2x:.3f} insec^-2")
aG2y = ag2mag*math.sin(math.radians(ag2ang))
print(f"aG2y = {aG2y:.3f} insec^-2")
aG3x = ag3mag*math.cos(math.radians(ag3ang))
print(f"aG3x = {aG3x:.3f} insec^-2")
aG3y = ag3mag*math.sin(math.radians(ag3ang))
print(f"aG3y = {aG3y:.3f} insec^-2")
aG4x = ag4mag*math.cos(math.radians(ag4ang))
print(f"aG4x = {aG4x:.3f} insec^-2")
print()

print("x any y components of the external force at P on Link 3")
Fp3x = Fp3*math.cos(math.radians(SFp3))
print(f"Fp3x = {Fp3x:.3f} ibf")
Fp3y = Fp3*math.sin(math.radians(SFp3))
print(f"Fp3y = {Fp3y:.3f} ibf")
print()

#Substitute value into the matrix equation
matrixC = np.array([[1,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,0],[-R12y,R12x,-R32y,R32x,0,0,0,1],[0,0,-1,0,1,0,0,0],[0,0,0,-1,0,1,0,0],[0,0,R23y,R23y,-R43y,R43x,0,0],[0,0,0,0,-1,0,0,0],[0,0,0,0,0,-1,1,0]])
matrixF = np.array([[m2*aG2x],[m2*aG2y],[I2*alpha2],[m3*aG3x],[m3*aG3y],[I3*alpha3-Rp3y*Fp3x-T3],[m4*aG4x],[0]])

#print(matrixF)
#for row in matrixC:
#    print(row)
C_inv = np.linalg.inv(matrixC)
#print(C_inv)
R = np.matmul(C_inv, matrixF)
#num = 1
#for row in R:
#    print(f"R{num} = {row}")
#    num+=1
F12x = R[0]
print(f"R1 = F12x = {F12x} ibf")
F12y = R[1]
print(f"R2 = F12y = {F12y} ibf")
F32x = R[2]
print(f"R3 = F32x = {F32x} ibf")
F32y = R[3]
print(f"R4 = F32y = {F32y} ibf")
F43x = R[4]
print(f"R5 = F43x = {F43x} ibf")
F43y = R[5]
print(f"R6 = F43y = {F43y} ibf")
F14y = R[6]
print(f"R7 = F14y = {F14y} ibf")
T12 = R[7]
print(f"T12 = {T12} ibf")
print()


print("Calculate the force and torque")
F21x = -F12x
F21y = (-F12y)
print(f"F1{F21x} + j{F21y}")
F41 = -F14y
Fsy = F21y + F41 
Fs = (f"Fs = {F21x} + j{Fsy}")
print(Fs)
MagFs = math.sqrt((math.pow(F21x,2)+math.pow(Fsy,2)))
print(f"Fs = {MagFs}")
Anglefs = math.degrees(math.atan((Fsy/F21x)))
print(f"ThetaFs = {Anglefs}")
T = -T12
print(f"T = {T} ibf")