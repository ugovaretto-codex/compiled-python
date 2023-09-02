// longest common subsequence
#include <algorithm>
#include <chrono>
#include <fstream>
#include <iostream>
#include <iterator>
#include <random>
#include <vector>

using namespace std;
using namespace chrono;

size_t c(size_t i, size_t j, size_t n) { return i * n + j; }
int lcs_dyn(const vector<int> &a, const vector<int> &b) {
  const size_t m = a.size() + 1;
  const size_t n = b.size() + 1;
  vector<int> dp(m * n);
  for (size_t i = 1; i != m; ++i) {
    for (size_t j = 1; j != n; ++j) {
      if (a[i - 1] == b[j - 1]) {
        dp[c(i, j, n)] = dp[c(i - 1, j - 1, n)] + 1;
      } else {
        dp[c(i, j, n)] = max(dp[c(i - 1, j, n)], dp[c(i, j - 1, n)]);
      }
    }
  }
  return dp.back();
}

void Init(vector<int> &v) {
  // First create an instance of an engine.
  random_device rnd_device;
  // Specify the engine and distribution.
  mt19937 mersenne_engine{rnd_device()}; // Generates random integers
  uniform_int_distribution<int> dist{1, 100};

  auto gen = [&dist, &mersenne_engine]() { return dist(mersenne_engine); };
  generate(begin(v), end(v), gen);
}

int main(int argc, char **argv) {
  size_t size = 10000;
  if (argc == 2) {
    size = stoi(argv[1]);
  }
  vector<int> a(size);
  vector<int> b(size);
  Init(a);
  Init(b);
  auto t1 = high_resolution_clock::now();
  const int s = lcs_dyn(a, b);
  auto t2 = high_resolution_clock::now();
  auto tf = duration<float>(t2 - t1);
  cout << "C++," << size << ',' << tf.count() << endl;
  // deal with optimisation: make sure the output is used
  ofstream os("/dev/null");
  os << s;
  return 0;
}
