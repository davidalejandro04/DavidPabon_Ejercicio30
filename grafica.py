import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt

inicial=np.genfromtxt("inicial.txt",delimiter=",");
final=np.genfromtxt("final_0.5.txt",delimiter=",");
final1=np.genfromtxt("final_1.0.txt",delimiter=",");
final2=np.genfromtxt("final_2.0.txt",delimiter=",");
final3=np.genfromtxt("final_4.0.txt",delimiter=",");
final4=np.genfromtxt("final_10.0.txt",delimiter=",");


plt.plot(inicial[:,0],inicial[:,1],label='Inicial')
plt.plot(final[:,0],final[:,1],label='t=0.5')
plt.plot(final1[:,0],final1[:,1],label='t=1.0')
plt.plot(final2[:,0],final2[:,1],label='t=2.0')
plt.plot(final3[:,0],final3[:,1],label='t=4.0')
plt.plot(final4[:,0],final4[:,1],label='t=10.0')
plt.ylabel(r'$f(x)')
plt.xlabel(r'$x')
plt.title('Solución a ecuación de advección: Paralelo')
plt.legend()
plt.savefig('graficaParalela.png')
plt.close()

inicial=np.genfromtxt("inicial.txt",delimiter=",");
final=np.genfromtxt("final_0.5omp.txt",delimiter=",");
final1=np.genfromtxt("final_1.0omp.txt",delimiter=",");
final2=np.genfromtxt("final_2.0omp.txt",delimiter=",");
final3=np.genfromtxt("final_4.0omp.txt",delimiter=",");
final4=np.genfromtxt("final_10.0omp.txt",delimiter=",");


plt.plot(inicial[:,0],inicial[:,1],label='Inicial')
plt.plot(final[:,0],final[:,1],label='t=0.5')
plt.plot(final1[:,0],final1[:,1],label='t=1.0')
plt.plot(final2[:,0],final2[:,1],label='t=2.0')
plt.plot(final3[:,0],final3[:,1],label='t=4.0')
plt.plot(final4[:,0],final4[:,1],label='t=10.0')
plt.ylabel(r'$f(x)')
plt.xlabel(r'$x')
plt.title('Solución a ecuación de advección: Serial')
plt.legend()
plt.savefig('graficaSerial.png')
plt.close()

datosWalk=np.genfromtxt('datosWalk.txt')
plt.hist(datosWalk)
plt.title('Caminata histograma')
plt.savefig('graficaWalk.png')

datosWalkomp=np.genfromtxt('datosWalkomp.txt')
plt.hist(datosWalkomp)
plt.title('Caminata histograma Paralela')
plt.savefig('graficaWalkomp.png')


