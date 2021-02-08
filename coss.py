import numpy as np
from matplotlib import pyplot as plt
n=np.arange(1,500)
n.shape;
F=250;
Fs=10000;
F2=20000;
s=0.5*np.cos(2*np.pi*F/Fs*n+np.pi/2)
s.shape;
from matplotlib import pyplot as plt
plt.subplot(3,5,1)
plt.plot(n,s);
plt.title("coswave")
s1=0.5*np.cos(2*np.pi*F/Fs*n+np.pi/4)
plt.subplot(3,5,2)
plt.plot(n,s1)
plt.title("coswave with frequency varing")
s2=1*np.cos(2*np.pi*F/F2*n+np.pi/2)
plt.subplot(3,5,3)
plt.plot(n,s2)
plt.title("coswave with sampling frequency varing")
s3=1*np.cos(2*np.pi*F/Fs*n+np.pi/2)
plt.subplot(3,5,4)
plt.plot(n,s3)
plt.title("coswave")
s4=s1+s2
plt.subplot(3,5,5)
plt.plot(n,s4)
plt.title("coswave addition")
s5=s1-s2
plt.subplot(3,5,6)
plt.plot(n,s5)
plt.title("coswave subtraction")
s6=s1*s2
plt.subplot(3,5,7)
plt.plot(n,s6)
plt.title("coswave multiplication")
s7=s1/s2
plt.subplot(3,5,8)
plt.plot(n,s7)
plt.title("coswave division")
plt.show()

