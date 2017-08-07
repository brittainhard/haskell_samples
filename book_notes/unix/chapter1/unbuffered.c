/**
 * <unistd.h> is the header that contains the read, write, etc functions. Apue
 * is importing that header.
 */
#include "../apue.h"


#define BUFFSIZE 4096


int main(int argc, char *argv[])
{
    int n;
    char buf[BUFFSIZE];

    while((n = read(STDIN_FILENO, buf, BUFFSIZE)) > 0){
        if(write(STDOUT_FILENO, buf, n) != n){
            err_sys("Write error.");
        }
    }

    if(n > 0){
        err_sys("Read error.");
    }

    return 0;
}
