// longest common subsequence
#include <algorithm>
#include <iostream>
#include <iterator>
#include <set>
#include <utility>
#include <vector>

using namespace std;
int lcs(const vector<int> &a, const vector<int> &b, size_t m, size_t n,
        set<pair<size_t, int>> &ss) {
  if (m == 0 || n == 0) {
    return 0;
  } else if (a[m - 1] == b[n - 1]) {
    ss.insert(make_pair(m - 1, a[m - 1]));
    return 1 + lcs(a, b, m - 1, n - 1, ss);
  } else
    return max(lcs(a, b, m - 1, n, ss), lcs(a, b, m, n - 1, ss));
}

size_t c(size_t i, size_t j, size_t n) { return i * n + j; }
int lcs_dyn(const vector<int> &a, const vector<int> &b, vector<int> &ss) {
  const size_t m = a.size() + 1;
  const size_t n = b.size() + 1;
  vector<int> dp(m * n);
  for (size_t i = 1; i != m; ++i) {
    for (size_t j = 1; j != n; ++j) {
      if (a[i - 1] == b[j - 1]) {
        ss.push_back(a[i - 1]);
        dp[c(i, j, n)] = dp[c(i - 1, j - 1, n)] + 1;
      } else {
        dp[c(i, j, n)] = max(dp[c(i - 1, j, n)], dp[c(i, j - 1, n)]);
      }
    }
  }
  return dp.back();
}

int main(int, char **) {
  const vector<int> a = {1, 2, 3, 4, 5, 6, 7};
  const vector<int> b = {3, 10, 4, 11, 12, 5, 13, 7};
  set<pair<size_t, int>> sss;
  cout << lcs(a, b, a.size(), b.size(), sss) << endl;
  vector<int> ss;
  for (auto i : sss) {
    ss.push_back(i.second);
  }
  copy(begin(ss), end(ss), ostream_iterator<int>(cout, ","));
  cout << endl;
  vector<int> ss2;
  cout << lcs_dyn(a, b, ss2) << endl;
  copy(begin(ss2), end(ss2), ostream_iterator<int>(cout, ","));
  cout << endl;
  return 0;
}
