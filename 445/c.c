#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_N 200005

int main() {
    int n;
    scanf("%d", &n);
    
    int a[MAX_N];
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        a[i]--;  // 0-indexed
    }
    
    int ans[MAX_N];
    long long aaaaaa = 1;
    for (int i = 0; i < 100; i++) {
        aaaaaa *= 10;
    }
    
    for (int i = 0; i < n; i++) {
        int tmp = a[i];
        long long time = 0;
        bool sumi[MAX_N];
        memset(sumi, false, sizeof(sumi));
        
        // ループの開始点を見つける
        while (time <= n) {
            if (sumi[tmp]) {
                break;
            }
            sumi[tmp] = true;
            tmp = a[tmp];
            time++;
        }
        
        // tmp: ループの開始点
        // time: ループが始まるまでの時間
        // ループの長さを計算
        int loop_start = tmp;
        int loop_length = 1;
        tmp = a[tmp];
        while (tmp != loop_start) {
            tmp = a[tmp];
            loop_length++;
        }
        
        // (aaaaaa - time) % loop_length 回移動
        if (loop_length > 0) {
            long long remaining = (aaaaaa - time) % loop_length;
            tmp = loop_start;
            for (long long j = 0; j < remaining; j++) {
                tmp = a[tmp];
            }
        }
        
        ans[i] = a[tmp] + 1;  // 1-indexed
    }
    
    // 結果を出力
    for (int i = 0; i < n; i++) {
        printf("%d", ans[i]);
        if (i < n - 1) printf(" ");
    }
    printf("\n");
    
    return 0;
}
