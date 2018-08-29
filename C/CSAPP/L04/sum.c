// 文件 sum.c
int sum(int *a, int n) // 定义了一个全局函数
{
    int i, s = 0;
    // i 和 s 是局部变量，链接器并不知道
    for (i = 0; i < n; i++)
        s += a[i];

    return s;
}
