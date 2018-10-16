// Explicit allocate
#include <stdio.h>
#include <stdlib.h>
void foo(int n) {
    int i, *p;

    /* Allocate a block of n ints */
    p = (int *) malloc(n * sizeof(int));
    if (p == NULL) {
        perror("malloc");
        exit(0);
    }

    /* Initialize allocated block */
    for (i=0; i<n; i++)
        p[i] = i;
    /* Return allocated block to the heap */
    free(p);
}


// GC
void foo() {
    int *p = malloc(128);
    return; /* p block is now garbage*/
}


// Memory Trick
// Dereferencing Bad Pointers
int val;
...
scanf("%d", val);

// Reading Uninitialized Memory
/* return y = Ax */
int *matvec(int **A, int *x) {
    int *y = malloc(N * sizeof(int));
    int i, j;

    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            y[i] += A[i][j] * x[j];
    return y;
}

// Overwriting Memory
int **p;
p = malloc(N * sizeof(int));
for (i = 0; i < N; i++)
    p[i] = malloc(M * sizeof(int));
//
int **p;
p = malloc(N * sizeof (int *));
for (i = 0; i <= N; i++)
    p[i] = malloc(M * sizeof(int));
//
char s[8];
int i;
gets(s); /* reads "123456789" from stdin */
//
int *search(int *p, int val) {
    while (*p && *p != null)
        p += sizeof(int);

    return p;
}
//
int *BinheapDelete(int **binheap, int *size) {
    int *packet;
    packet = binheap[0];
    binheap[0] = binheap[*size - 1];
    *size--;
    Heapify(binheap, *size, 0);
    return (packet);
}
