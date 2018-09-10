// Page Fault
int a[1000];
main()
{
    a[500] = 13;
}

// Page Fault -> Segmentation Fault
int a[1000];
main()
{
    a[5000] = 13;
}


// Process Control
// fork
if ((pid = fork()) < 0) {
    fprintf(stderr, "fork error: %s\n", strerror(errno));
    exit(0);
}
// helper function
void unix_error(char *msg) /* Unix-style error */
{
    fprintf(stderr, "%s: %s\n", msg, strerror(errno));
    exit(0);
}
// 上面的片段可以写为
if ((pid = fork()) < 0)
    unix_error("fork error");
// 将 fork() 包装
pid_t Fork(void)
{
    pid_t pid;
    if ((pid = fork()) < 0)
        unix_error("Fork error");
    return pid;
}


// Create Process
int main()
{
    pid_t pid;
    int x = 1;

    pid = Fork();
    if (pid == 0)
    {   // Child
        printf("I'm the child!  x = %d\n", ++x);
        exit(0);
    }

    // Parent
    printf("I'm the parent! x = %d\n", --x);
    exit(0);
}


// Signal
void forkandkill()
{
    pid_t pid[N];
    int i;
    int child_status;

    for (i = 0; i < N; i++)
        if ((pid[i] = fork()) == 0)
            while(1) ;  // 死循环

    for (i = 0; i < N; i++)
    {
        printf("Killing process %d\n", pid[i]);
        kill(pid[i], SIGINT);
    }

    for (i = 0; i < N; i++)
    {
        pid_t wpid = wait(&child_status);
        if (WIFEXITED(child_status))
            printf("Child %d terminated with exit status %d\n",
                    wpid, WEXITSTATUS(child_status));
        else
            printf("Child %d terminated abnormally\n", wpid);
    }
}

void sigint_handler(int sig) // SIGINT 处理器
{
    printf("想通过 ctrl+c 来关闭我？\n");
    sleep(2);
    fflush(stdout);
    sleep(1);
    printf("OK. :-)\n");
    exit(0);
}
int main()
{
    // 设定 SIGINT 处理器
    if (signal(SIGINT, sigint_handler) == SIG_ERR)
        unix_error("signal error");

    // 等待接收信号
    pause();
    return 0;
}


// 临时阻塞特定的信号
sigset_t mask, prev_mask;
Sigemptyset(&mask); // 创建空集
Sigaddset(&mask, SIGINT); // 把 SIGINT 信号加入屏蔽列表中
// 阻塞对应信号，并保存之前的集合作为备份
Sigprocmask(SIG_BLOCK, &mask, &prev_mask);
...
... // 这部分代码不会被 SIGINT 中断
...
// 取消阻塞信号，恢复原来的状态
Sigprocmask(SIG_SETMASK, &prev_mask, NULL);


// None Local Jump
jmp_buf env;
P1()
{
    if (setjmp(env))
    {
        // 跳转到这里
    } else
    {
        P2();
    }

}
P2()
{
    ...
    P2();
    ...
    P3();
}
P3()
{
    longjmp(env, 1);
}
