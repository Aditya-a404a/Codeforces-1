#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> boxes(m, vector<int>(3));
    for (int i = 0; i < m; ++i) {
        cin >> boxes[i][0] >> boxes[i][1] >> boxes[i][2];
    }

    vector<long long> fib(n + 2);  // To store up to fib[n]
    fib[0] = 0;
    fib[1] = 1;
    for (int i = 2; i <= n; ++i) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }

    string result = "";
    for (int i = 0; i < m; ++i) {
        int x = boxes[i][0];
        int y = boxes[i][1];
        int z = boxes[i][2];

        int minimum = min({x, y, z});
        int maximum = max({x, y, z});

        if (minimum < fib[n]) {
            result += '0';
        } else if (fib[n] + fib[n - 1] <= maximum) {
            result += '1';
        } else {
            result += '0';
        }
    }

    cout << result << endl;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        solve();
    }
    return 0;
}
