#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include "omp.h"
void inicializar(double *xP,double *uP, double delta_xP,double L);
double *Lax(double *uP, double t_max, double delta_t, double delta_x);

int N;

int main(int argc, char **argv)
{
	

	double delta_x,L,t_max,delta_t;
	double *x, *u_init, *u_final;

	if(argv[1]!=0)
	{
		t_max =atof(argv[1]);
	}
	else
	{
		t_max =4.0;
	}
		
	L=4.0;
	delta_x=0.05;
	delta_t=0.5*delta_x;	

	int i;	
	N=(int) L/delta_x+1;

	u_init=malloc(sizeof(double)*N);
	x=malloc(sizeof(double)*N);
	omp_set_dynamic(0);
	omp_set_num_threads(4); 

	#pragma omp parallel for 
	for(i=0;i<N;i++)
	{
			x[i]=i*delta_x;
			if(x[i]<2.0)
			{
				u_init[i] =1.0;
			}
			else
			{
				u_init[i]=0.0;
			}
	
	}

	u_final= Lax(u_init, t_max,  delta_t, delta_x);

	FILE *f1 = fopen("inicial.txt", "w");
	char buffer[80];
	sprintf(buffer,"final_%.1fomp.txt",t_max);
	FILE *f2 = fopen(buffer, "w");

	for(i=0;i<N;i++)
	{
		fprintf(f1,"%lf,%lf\n",x[i],u_init[i]);
		fprintf(f2,"%lf,%lf\n",x[i],u_final[i]);

	}

	fclose(f1);
	fclose(f2);

	return 0;
}



double *flux(double *uP)
{	
	int i;
	double *fx=malloc(sizeof(double)*N);

	for(i=0;i<N;i++)
	{
		fx[i]=0.5*uP[i]*uP[i];
		
	}

	return fx;

}

double *Lax(double *uP, double t_max, double delta_t, double delta_x)
{
	int N_t,i,j;
	N_t= t_max/delta_t;
	double *u_final=malloc(sizeof(double)*N);
	double *F;
	#pragma omp parallel for 
	for(i=0;i<N;i++)
	{
			u_final[i]=uP[i];

	}
	for(i=0;i<N_t;i++)
	{

		F= flux(u_final);
		#pragma omp parallel for 
		for(j=1;j<N-1;j++)
		{	
			u_final[j]=0.5*(u_final[j+1] + u_final[j-1])-(0.5*delta_t/delta_x)*(F[j+1]-F[j-1]);
		}
	}


	return u_final;

}
