#include <stdlib.h>

int main() {
    long long n, m;
    if (scanf("%lld %lld", &n, &m) != 2) return 1;
    
    long long **mat = (long long **)malloc(n * sizeof(long long *));
    for (int i = 0; i < n; i++) {
        mat[i] = (long long *)malloc(n * sizeof(long long));
        for (int j = 0; j < n; j++) {
            mat[i][j] = 0;
        }
    }
    
    int ans = 0;
    for (int i = 0; i < m; i++) {
        long long a, b;
        if (scanf("%lld %lld", &a, &b) != 2) return 1;

        
        if (a == b) {
            ans++;
            continue;
        }
        a -= 1;
        b -= 1;        
        if (mat[a][b] == 0 || mat[b][a] == 0) {
            mat[a][b] = 1;
            mat[b][a] = 1;
        } else {
            ans++;
        }
    }
    
    printf("%d\n", ans);
    
    for (int i = 0; i < n; i++) {
        free(mat[i]);
    }
    free(mat);
    
    return 0;
}