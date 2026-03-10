#include <vector>

#include "matplotlibcpp.h"

namespace plt = matplotlibcpp;

int main() {
  std::vector<double> y = {1, 3, 2, 4};
  plt::plot(y);
  plt::savefig("minimal.pdf");
}
