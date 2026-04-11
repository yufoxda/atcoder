#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        a[i]--;  // 0-indexed
    }
    
    vector<int> ans(n);
    long long aaaaaa = 1;
    for (int i = 0; i < 100; i++) {
        aaaaaa *= 10;
    }
    
    for (int i = 0; i < n; i++) {
        int tmp = a[i];
        long long time = 0;
        vector<bool> sumi(n, false);
        
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
        long long loop_length = 1;
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
        cout << ans[i];
        if (i < n - 1) cout << " ";
    }
    cout << endl;
    
    return 0;
}
