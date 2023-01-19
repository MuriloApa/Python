#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct cel{
    char chave[46];
    struct cel *prox;
};

typedef struct cel pizza;

/*A função abaixo é responsável por alocar uma nova célula para a lista que contém as palavras*/
pizza *aloca_cc (char *word)
{
    pizza *nova;
    nova=(pizza*) malloc(sizeof(pizza));
    if (nova==NULL)
    {
        fprintf(stderr, "Erro ao alocar nova célula\n");
        return NULL;
    }
    else
    {
        strcpy(nova->chave, word);
        nova->prox=NULL;
        return nova;
    } 
}

/*Função para mostrar a lista das palavras lidas*/
void imprime_lista_cc (pizza *lista, FILE *ptsaida)
{
    pizza *pt;
    pt=lista->prox;
    if (pt!=NULL)
    {
        while (pt->prox!=NULL)
        {
            fprintf(ptsaida,"%s\n", pt->chave);
            pt=pt->prox;
        }
        fprintf(ptsaida,"%s", pt->chave);
    }
}

int main(void)
{   
    FILE *ptentrada, *ptsaida;
    return 0;
}