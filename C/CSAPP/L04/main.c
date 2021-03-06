// Symbol resolution
// 文件 main.c
int sum(int *a, int n);
int array[2] = {1, 2}; // 变量 array 在此定义
int main() // 定义了一个全局函数
{
    int val = sum(array, 2);
    // val 是局部变量，链接器并不知道
    // sum 函数是一个全局引用
    // array 变量是一个全局引用
    return val;
}
// 文件 sum.c
int sum(int *a, int n) // 定义了一个全局函数
{
    int i, s = 0;
    // i 和 s 是局部变量，链接器并不知道
    for (i = 0; i < n; i++)
        s += a[i];

    return s;
}

// 两个函数中定义了同名的静态变量
int f()
{
    static int x = 0;
    return x;
}

int g()
{
    static int x = 1;
    return x;
}


// 两个文件中定义了同名的全局变量
// 文件 p1.c
int foo = 5; // 强符号，已初始化
p1() { ... } // 强符号，函数
// -----------------------------------------
// 文件 p2.c
int foo;     // 弱符号，未初始化
p2() { ... } // 强符号，函数


// 同时声明了两个同名函数并且都是强符号，会出现链接错误
// 文件 p1.c
int x;
p1() { ... }
// -----------------------------------------
// 文件 p2.c
p1() { ... }


// 对 p2 中的 x 进行写入时，会影响到 p1 中的 y
// 因为 x 实际上引用的是同一个地址，而 double 的字节数是 int 的两倍
// 文件 p1.c
int x;
int y;
p1() { ... }
// -----------------------------------------
// 文件 p2.c
double x;
p2() { ... }


// p1 中变量为强符号（因为初始化），p2 中的变量为弱符号
// 对 p2 的 x 进行改动，会同时影响 p1 中的 x 和 y
// 文件 p1.c
int x = 7;
int y = 4;
p1() { ... }
// -----------------------------------------
// 文件 p2.c
double x;
p2() { ... }




// Relocation
int sum(int *a, int n);
int array[2] = {1, 2};
int main()
{
    int val = sum(array, 2);
    return val;
}
