#include <stdio.h>
#include <math.h>

/*
int soma_pot (int x, int n)
{
    int i, j, s=0, pot;
    for ( i = 0; i < n; i++)
    {
        pot=1;
        for (j=i; j>0; j--)
        {
            pot=pot*x;
        }
        s=s+pot;
    }
    return s;
}
*/

int soma_pot (int x, int n)
{
    int i, s=0;
    for (i=0; i<n; i++)
    {
        s=s+pow(x, i);
    }
    return s;
}

int main(void)
{
    int n;
    printf("Digite o número de termos que deve-se somar as de potências de 2: \n");
    scanf("%d", &n);
    printf("O valor da soma é %d\n", soma_pot(2, n));
    return 0;
}