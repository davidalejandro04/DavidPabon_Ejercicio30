rm *.png 
module load anaconda/python3

#cd $PBS_O_WORKDIR

gcc non_linear_advection.c -lm -o nlaserial
./nlaserial 0.5
./nlaserial 1.0
./nlaserial 2.0
./nlaserial 4.0
./nlaserial 10.0

#Corre la version paralela
gcc omp_non_linear_advection.c -fopenmp -o nla
./nla 0.5
./nla 1.0
./nla 2.0
./nla 4.0
./nla 10.0

gcc ompwalk.c -fopenmp -o ompwalk
./ompwalk >> datosWalkomp.txt

gcc walk.c -fopenmp -o walk
./walk >> datosWalk.txt

python3 grafica.py
rm *.txt nla nlaserial ompwalk



