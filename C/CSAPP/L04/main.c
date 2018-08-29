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
