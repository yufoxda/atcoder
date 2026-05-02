#include <stdio.h>
#include <stdlib.h>

static int check_mask(long long mask, int nowmax, const long long *ll, int n) {
    int cnt = 0;
    long long now = 1;  // 0.5 を 2 倍して整数化

    for (int i = 0; i < n; i++) {
        long long prev = now;
        if ((mask >> i) & 1LL) {
            now += ll[i];
        } else {
            now -= ll[i];
        }

        if (prev * now < 0) {
            cnt++;
        }

        // 残り全てで符号変化しても nowmax を超えないなら打ち切り
        if (cnt + (n - i - 1) <= nowmax) {
            return 0;
        }
    }

    return cnt;
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1) {
        return 0;
    }

    long long *ll = (long long *)malloc((size_t)n * sizeof(long long));
    if (!ll) {
        return 1;
    }

    for (int i = 0; i < n; i++) {
        long long x;
        if (scanf("%lld", &x) != 1) {
            free(ll);
            return 0;
        }
        ll[i] = x * 2;
    }

    int ans = 0;
    long long limit = 1LL << n;
    for (long long mask = 0; mask < limit; mask++) {
        int v = check_mask(mask, ans, ll, n);
        if (v > ans) {
            ans = v;
        }
    }

    printf("%d\n", ans);
    free(ll);
    return 0;
}
