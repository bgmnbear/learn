long plus(long x, long y);
void sumstore(long x, long y, long *dest)
{
    long t = plus(x, y);
    *dest = t;
}


long m12(long x)
{
    return x * 12;
}


long absdiff(long x, long y)
{
    long result;
    if (x > y)
        result = x-y;
    else
        result = y-x;
    return result;
}


long absdiff_goto(long x, long y)
{
    long result;
    int ntest = x <= y;
    if (ntest) goto Else;
    result = x-y;
    goto Done;
Else:
    result = y-x;
Done:
    return result;
}


// Do While 的 C 语言代码
long pcount_do(unsigned long x)
{
    long result = 0;
    do {
        result += x & 0x1;
        x >>= 1;
    } while (x);
    return result;
}
// Goto 版本
long pcount_goto(unsigned long x)
{
    long result = 0;
loop:
    result += x & 0x1;
    x >>= 1;
    if (x) goto loop;
    return result;
}

long switch_eg (long x, long y, long z){
	long w = 1;
	switch (x) {
		case 1:
			w = y*z;
			break;
		case 2:
			w = y/z;
			// fall through
		case 3:
			w += z;
			break;
		case 5:
		case 6:
			w -= z;
			break;
		default:
			w = 2;
	}
	return w;
}


// multstore 函数
void multstore (long x, long y, long *dest)
{
    long t = mult2(x, y);
    *dest = t;
}
// mult2 函数
long mult2(long a, long b)
{
    long s = a * b;
    return s;
}

long pcount_r(unsigned long x) {
	if (x == 0)
		return 0;
	else
		return (x & 1) + pcount_r(x >> 1);
}

int get_a_digit(int index, int dig)
{
    return A[index][dig];
}

struct rec
{
    int a[4];
    size_t i;
    struct rect *next;
};

struct S1
{
    char c;
    int i[2];
    double v;
} *p;

struct S2 {
	double v;
	int i[2];
	char c;
} *p;

struct S4 {
	char c;
	int i;
	char d;
} *p;

struct S5 {
	int i;
	char c;
	char d;
} *p;


typedef struct
{
    int a[2];
    double d;
} struct_t;

double fun(int i)
{
    volatile struct_t s;
    s.d = 3.14;
    s.a[i] = 1073741824; // 可能会越界
    return s.d;
}

// 从 stdin 中获取输入
char *gets(char *dest)
{
    int c = getchar();
    char *p = dest;
    while (c != EOF && c != '\n')
    {
        *p++ = c;
        c = getchar();
    }
    *p = '\0';
    return dest;
}
