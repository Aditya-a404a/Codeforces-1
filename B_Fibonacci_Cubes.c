#include <stdio.h>
#include <stdlib.h>

int main() {
    int T;
    if (scanf("%d", &T) != 1) return 0;
    
    while (T--) {
        int n, m;
        scanf("%d %d", &n, &m);
        
        // Precomputed Fibonacci as per your Python array
        int fib[] = {0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144};
        // Ensure n is within bounds [0..11]
        if (n < 0) n = 0;
        if (n > 11) n = 11;
        
        char *s = (char*)malloc((m + 1) * sizeof(char));
        s[m] = '\0';
        
        for (int i = 0; i < m; i++) {
            int x, y, z;
            scanf("%d %d %d", &x, &y, &z);
            
            int mi = x < y ? (x < z ? x : z) : (y < z ? y : z);
            int ma = x > y ? (x > z ? x : z) : (y > z ? y : z);
            
            if (mi < fib[n]) {
                s[i] = '0';
            } else if (fib[n] + fib[n - 1] <= ma) {
                s[i] = '1';
            } else {
                s[i] = '0';
            }
        }
        
        printf("%s\n", s);
        free(s);
    }
    
    return 0;
}
