#include<stdio.h>
#include<stdlib.h>

#define MAX_LENGTH 100

#define GET_ROW(_sm,_i) ((_sm)->entries[(_i)].row)
#define GET_COL(_sm,_i) ((_sm)->entries[(_i)].col)
#define GET_VALUE(_sm,_i) ((_sm)->entries[(_i)].value)

typedef struct entry
{
    int row,col;
    int value;
}entry;

typedef struct spmatrix
{
    int row,col;
    int length;
    entry entries[MAX_LENGTH];
}spmatrix;

void transpose(spmatrix *s,spmatrix *d)
{
    int len = s->length; 
    int *spos = (int*)malloc(sizeof(int)*s->col);
    int *coll = (int*)malloc(sizeof(int)*s->col);
    
    int i,t;
    //init
    for(i=0;i<s->col;++i)
        coll[i] = 0;

    //count 
    for(i=0;i<len;++i)
        coll[s->entries[i].col]++;

    
    //calcuate 
    spos[0] = 0;
    for(i=1;i<s->col;++i)
        spos[i] = spos[i-1]+coll[i-1];


    for(i=0;i<len;++i)
    {
        t = spos[s->entries[i].col]++;
        d->entries[t].col = s->entries[i].row;  
        d->entries[t].row = s->entries[i].col;  
        d->entries[t].value = s->entries[i].value;  
    }
    d->row = s->col;
    d->col = s->row;
    d->length = len;
}

void add(spmatrix *a,spmatrix *b,spmatrix *c)
{
    int la = a->length;
    int lb = b->length;
    int lc = 0;

    int i,j;

    for(i=0,j=0;i<la&&j<lb;)
    {
        if(GET_ROW(a,i) == GET_ROW(b,j))
        {
            if(GET_COL(a,i) == GET_COL(b,j))
            {
                GET_ROW(c,lc) = GET_ROW(a,i);
                GET_COL(c,lc) = GET_COL(a,i);
                GET_VALUE(c,lc) = GET_VALUE(a,i)+GET_VALUE(b,j);
                ++lc;
                ++i;
                ++j;
            }
            else if(GET_COL(a,i) > GET_COL(b,j))
            {
                GET_ROW(c,lc) = GET_ROW(b,j);
                GET_COL(c,lc) = GET_COL(b,j);
                GET_VALUE(c,lc) = GET_VALUE(b,j);
                ++lc;
                ++j;
            }
            else if(GET_COL(a,i) < GET_COL(b,j))
            {
                GET_ROW(c,lc) = GET_ROW(a,i);
                GET_COL(c,lc) = GET_COL(a,i);
                GET_VALUE(c,lc) = GET_VALUE(a,i);
                ++lc;
                ++i;
            }
        }
        else if(GET_ROW(a,i) > GET_ROW(b,j))
        {
            GET_ROW(c,lc) = GET_ROW(b,j);
            GET_COL(c,lc) = GET_COL(b,j);
            GET_VALUE(c,lc) = GET_VALUE(b,j);
            ++lc;
            ++j;
        }
        else
        {
            GET_ROW(c,lc) = GET_ROW(b,j);
            GET_COL(c,lc) = GET_COL(b,j);
            GET_VALUE(c,lc) = GET_VALUE(b,j);
            ++lc;
            ++j;
        }
    }

    for(;i<la;++i)
    {
        GET_ROW(c,lc) = GET_ROW(a,i);
        GET_COL(c,lc) = GET_COL(a,i);
        GET_VALUE(c,lc) = GET_VALUE(a,i);
        ++lc;
    }

    for(;j<lb;++j)
    {
        GET_ROW(c,lc) = GET_ROW(b,j);
        GET_COL(c,lc) = GET_COL(b,j);
        GET_VALUE(c,lc) = GET_VALUE(b,j);
        ++lc;
    }

    c->length = lc;
    c->row = a->row;
    c->col = a->col;
}

void spmatrix2matrix(spmatrix *s,int *m,int *r,int *c)
{
    int row = s->row;
    int col = s->col;
    
    int i,j;
    for(i=0;i<row;++i)
        for(j=0;j<col;++j)
            *(m+i*col+j) = 0;

    for(i=0;i<s->length;++i)
        *(m+s->entries[i].row*col+s->entries[i].col) = s->entries[i].value;

    *r = row;
    *c = col;
}
void matrix2spmatrix(int *m,int r,int c,spmatrix *sm)
{
    int i,j;
    int t = 0;
    for(i=0;i<r;++i)
    {
        for(j=0;j<c;++j)
        {
            if(*(m+i*c+j)!=0)
            {
                sm->entries[t].value = *(m+i*c+j);
                sm->entries[t].row = i;
                sm->entries[t].col = j;
                ++t;
            }
        }
    }
    sm->length = t;
    sm->row = r;
    sm->col = c;
}

void print_matrix(int *m,int r,int c)
{
    int i,j;
    for(i=0;i<r;++i)
    {
        for(j=0;j<c;++j)
            printf("%d ",*(m+i*c+j));
        printf("\n");
    }
}

void print_spmatrix(spmatrix *sm)
{
    int i;
    for(i=0;i<sm->length;++i)
        printf("(%d %d) %d\n",sm->entries[i].row,sm->entries[i].col,sm->entries[i].value);
}

int main()
{
    spmatrix sm,sm2,sm3;

    int m[100];
    int r,c;
    int i,j;
    
    scanf("%d %d",&r,&c);
    for(i=0;i<r;++i)
        for(j=0;j<c;++j)
            scanf("%d",m+i*c+j);

    matrix2spmatrix(m,r,c,&sm);
    print_spmatrix(&sm);
    puts("=============");
    transpose(&sm,&sm2);
    print_spmatrix(&sm2);

    spmatrix2matrix(&sm2,m,&r,&c);
    print_matrix(m,r,c);

    scanf("%d %d",&r,&c);
    for(i=0;i<r;++i)
        for(j=0;j<c;++j)
            scanf("%d",m+i*c+j);

    matrix2spmatrix(m,r,c,&sm);
    print_spmatrix(&sm);
    puts("=============");
    scanf("%d %d",&r,&c);
    for(i=0;i<r;++i)
        for(j=0;j<c;++j)
            scanf("%d",m+i*c+j);

    matrix2spmatrix(m,r,c,&sm2);
    print_spmatrix(&sm2);
    puts("=============");

    add(&sm,&sm2,&sm3);    
    spmatrix2matrix(&sm3,m,&r,&c);
    print_matrix(m,r,c);
    return 0;
}
