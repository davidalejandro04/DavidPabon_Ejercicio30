gcc walk.c -fopenmp -o walk
./walk >> datosWalk.txt



#Corre la version paralela
gcc omp_non_linear_advection.c -fopenmp -o nla
./nla 0.5
./nla 1.0
./nla 2.0
./nla 4.0
./nla 10.0

#Corre la version serial
gcc non_linear_advection.c -lm -o nla2
./nla2 0.5
./nla2 1.0
./nla2 2.0
./nla2 4.0
./nla2 10.0


python3 grafica.py
rm *.txt nla nla2 walk



