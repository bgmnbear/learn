#include <stdio.h>
#include <stdlib.h>

int thirdBits(void) {
  int a = 0x49;
  int b = (a << 9);
  int c = b + a;
  return (c << 18) + c; // Steps 4 and 5
}

int isTmin(int x) {
   return !(x+x)&!!(x);
}

int isNotEqual(int x, int y)
{
	return(!!(x ^ y));
}

int anyOddBit(int x) {
    return !!((x | (x >> 8) | (x >> 16) | (x >> 24)) & 0xaa);
}

int negate(int x) {
  return ~x + 1;
}

int conditional(int x, int y, int z) {
    /*
     *if x!=0,mask=0x00000000,so y&~mask==y and z&mask==0
     *if x==0,mask=0xffffffff,so y&~mask = y&0 =0; z&mask=z
     */
    int mask= ~!x+1;
    return (y & ~mask)|(z & mask);
}

int subOK(int x, int y) {
    int res = ~y + 1 + x;
    int sameSign = (x ^ y) >> 31;
    int resSign = (res ^ x) >> 31;
    return !(sameSign & resSign);
}

int isGreater(int x, int y) {
    int sign_x = x >> 31;
    int sign_y = y >> 31;

    int sameSign = !(sign_x ^ sign_y);
    int diffSign = !sameSign;

    int resSign = (~y + x) >> 31;

    return (sameSign & !resSign) | (diffSign & !sign_x);
}

int main(int argc, char const *argv[]) {
    int a = isGreater(-3, 4);
    int b = isGreater(-5, -3);
    int c = isGreater(5, -5);
    printf("%d%d%d", a, b, c);
    return 0;
}
