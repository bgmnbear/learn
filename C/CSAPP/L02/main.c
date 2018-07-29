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
