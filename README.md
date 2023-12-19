# Lab 4

1. The implementation for multithreaded is located in multithread.py and the implementation for single thread is located in single_thread.py

2. The multithreaded implementation appears to take more time in general, although it follows a similar time complexity curve. I believe this is due to the overhead required to create different threads, especially in python. Additionally, I wasn't able to test this with large enough arrays as my computer would run out of memory, so it is possible that there are advantages that I am just not able to see to to memory constraints.

3. For the reason described above, I believe that it would be beneficial to stop creating threads at some defined length of the list and solve it single threaded from there. This would limit the number of threads created, saving some memory, and would remove a lot of the overhead. The optimal number of threads is likely to depends on the processor being used. Additionally, it might be interesting to see if a GPU implementation would perform better on much larger datasets. If the length of the list is short enough for the single-threaded part, this may be viable.

