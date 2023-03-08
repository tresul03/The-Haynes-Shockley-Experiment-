#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define PI 3.14159265358979323846
#define BOLTZMANN_CONST 1.38e-23
#define TEMPEATURE 300
#define ELECTRONCHARGE 1.6e-19
#define MOBILITY 1e-1
#define DIFFUSION_CONSTANT (MOBILITY*BOLTZMANN_CONST*TEMPEATURE)/ELECTRONCHARGE
#define CARRIER_LIFETIME 10e-6


long double normaliser(float time);
long double decay(float time);
long double probabilityDensity(long double x, long double time);

int main(void){



    return 0;
}


long double normaliser(float time){ //A(t) = 1/sqrt(4*pi*Dt)
    return pow(sqrt(4*PI*DIFFUSION_CONSTANT*time) , -1);
}


long double decay(float time){
    return expl(- time / CARRIER_LIFETIME);
}


long double probabilityDensity(long double x, long double time){
    return normaliser(time) * exp(- pow(x, 2) / (4*DIFFUSION_CONSTANT*time));
}

//todo: write the random-walk algorithm
//todo: write an output file (idk how to word this better atm)