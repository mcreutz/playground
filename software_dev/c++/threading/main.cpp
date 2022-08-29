// #include <stdio.h>
#include <iostream>
#include <cstdlib>
#include <thread>

void myThread(int ident)
{
    for (unsigned long long int i = 0; i < 5000000000; i++)
    {
        int x = 9 / 8;
    }
    ident += 1;
    std::cout << "Done";
}

int main()
{
    std::thread th1(myThread, 1);
    th1.join();
    return 0;
}