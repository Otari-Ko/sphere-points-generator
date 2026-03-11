#include "initial_directions/initial_directions.h"
#include <fstream>
#include <iomanip>

int main() {
    const int N = 100;
    std::vector<Vector> directions = randomDirections(N);
    
    // Конвертируем в MatrixXd (N x 3)
    Eigen::MatrixXd points(N, 3);
    for (int i = 0; i < N; ++i) {
        points.row(i) = directions[i].transpose();  // Vector -> row
    }
    
    // Сохраняем в CSV с заголовком
    const static Eigen::IOFormat CSVFormat(Eigen::FullPrecision, Eigen::DontAlignCols, ", ", "\n");
    std::ofstream file("directions.csv");
    if (file.is_open()) {
        file << "x,y,z\n";
        file << points.format(CSVFormat);
        file.close();
    }
    
    return 0;
}