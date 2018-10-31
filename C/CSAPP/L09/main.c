// Process based
void sigchld_handler(int sig){
    while (waitpid(-1, 0, WNOHANG) > 0)
        ;
    return;
    // Reap all zombie children
}
int main(int argc, char **argv) {
    int listenfd, connfd;
    socklen_t clientlen;
    struct sockaddr_storage clientaddr;

    Signal(SIGCHLD, sigchld_handler);
    listenfd = Open_listenfd(argv[1]);
    while (1) {
        clientlen = sizeof(struct sockaddr_storage);
        connfd = Accept(listenfd, (SA *) &clientaddr, &clientlen);
        if (Fork() == 0) {
            Close(listenfd); // Child closes its listening socket
            echo(connfd); // Child services client
            Close(connfd); // Child closes connection with client
            exit(0); // Child exits
        }
        Close(connfd); // Parent closes connected socket (important!)
    }
}

// Thread routine
void *thread(void *vargp){
    int connf = *((int *)vargp);
    // detach 之后不用显式 join，会在执行完毕后自动回收
    Pthread_detach(pthread_self());
    Free(vargp);
    echo(connfd);
    // 一定要记得关闭！
    Close(connfd);
    return NULL;
}
int main(int argc, char **argv) {
    int listenfd, *connfdp;
    socklen_t clientlen;
    struct sockaddr_storage clientaddr;
    pthread_t tid;

    listenfd = Open_listenfd(argv[1]);
    while (1) {
        clientlen = sizeof(struct sockaddr_storage);
        // 这里使用新分配的 connected descriptor 来避免竞争条件
        connfdp = Malloc(sizeof(int));
        *connfdp = Accept(listenfd, (SA *) & clientaddr, &clientlen);
        Pthread_create(&tid, NULL, thread, connfdp);
    }
}

// Shared variables
char **ptr; // 全局变量
int main()
{
    long i;
    pthread_t tid;
    char *msgs[2] = {
        "Good Day!",
        "Bad Day!"
    };
}
ptr = msgs;
for (i = 0; i < 2; i++)
    Pthread_create(&tid, NULL, thread, (void *)i);
Pthread_exit(NULL);
}
void *thread(void *vargp)
{
    long myid = (long)vargp;
    static int cnt = 0;

    // 这里每个线程都可以访问 ptr 这个全局变量
    printf("[%ld]: %s (cnt=%d)\n", myid, ptr[myid], ++cnt);
    return NULL;
}

// Critical Sections
// 全局共享变量
volatile long cnt = 0; // 计数器
int main(int argc, char **argv)
{
    long niters;
    pthread_t tid1, tid2;

    niter2 = atoi(argv[1]);
    Pthread_create(&tid1, NULL, thread, &niters);
    Pthread_create(&tid2, NULL, thread, &niters);
    Pthread_join(tid1, NULL);
    Pthread_join(tid2, NULL);

    // 检查结果
    if (cnt != (2 * niters))
        printf("Wrong! cnt=%ld\n", cnt);
    else
        printf("Correct! cnt=%ld\n", cnt);
    exit(0);
}

// Signal
// 先定义信号量
volatile long cnt = 0;
sem_t mutex;
Sem_init(&mutex, 0, 1);
// 在线程中用 P 和 V 包围关键操作
for (i = 0; i < niters; i++)
{
    P(&mutex);
    cnt++;
    V(&mutex);
}


// sbuf.c
// Create an empty, bounded, shared FIFO buffer with n slots
void sbuf_init(sbuf_t *sp, int n) {
    sp->buf = Calloc(n, sizeof(int));
    sp->n = n;                  // Buffer holds max of n items
    sp->front = sp->rear = 0;   // Empty buffer iff front == rear
    Sem_init(&sp->mutex, 0, 1); // Binary semaphore for locking
    Sem_init(&sp->slots, 0, n); // Initially, buf has n empty slots
    Sem_init(&sp->items, 0, 0); // Initially, buf has 0 items
}
// Clean up buffer sp
void sbuf_deinit(sbuf_t *sp){
    Free(sp->buf);
}
// Insert item onto the rear of shared buffer sp
void sbuf_insert(sbuf_t *sp, int item) {
    P(&sp->slots);                        // Wait for available slot
    P(&sp->mutext);                       // Lock the buffer
    sp->buf[(++sp->rear)%(sp->n)] = item; // Insert the item
    V(&sp->mutex);                        // Unlock the buffer
    V(&sp->items);                        // Announce available item
}
// Remove and return the first tiem from the buffer sp
int sbuf_remove(sbuf_f *sp) {
    int item;
    P(&sp->items);                         // Wait for available item
    P(&sp->mutex);                         // Lock the buffer
    item = sp->buf[(++sp->front)%(sp->n)]; // Remove the item
    V(&sp->mutex);                         // Unlock the buffer
    V(&sp->slots);                         // Announce available slot
    return item;
}
