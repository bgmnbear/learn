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
