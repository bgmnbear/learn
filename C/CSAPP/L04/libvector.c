// 静态库
// 文件 main.c
#include <stdio.h>
#include "vector.h"
int x[2] = {1, 2};
int y[2] = {3, 4};
int z[2];
int main()
{
    addvec(x, y, z, 2);
    printf("z = [%d %d]\n", z[0], z[1]);
    return 0;
}
// -----------------------------------------
// 文件 addvec.c
void addvec(int *x, int *y, int *z, int n)
{
    int i;
    for (i = 0; i < n; i++)
        z[i] = x[i] + y[i];
}
// -----------------------------------------
// 文件 multvec.c
void multvec(int *x, int *y, int *z, int n)
{
    int i;
    for (i = 0; i < n; i++)
        z[i] = x[i] * y[i];
}


// 编译链接的时候，把静态库放到编译命令的后面
unix> gcc -L. libtest.o -lmine
# 上面这句不会出错，但是下面的会
unix> gcc -L. -lmine libtest.o
libtest.o: In function `main`:
libtest.o(.text+0x4): Undefined reference to `libfun`
