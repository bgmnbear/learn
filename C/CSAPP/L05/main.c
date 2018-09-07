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
