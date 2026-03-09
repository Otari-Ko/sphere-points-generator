#include <iostream>
#include <Eigen/Dense>

int main() {
    Eigen::Matrix3d A;
    A << 1, 2, 3,
         4, 5, 6,
         7, 8, 10;

    std::cout << "Тест Eigen OK!\n";
    std::cout << "Матрица A:\n" << A << "\n\n";

    double det = A.determinant();
    std::cout << "Определитель: " << det << "\n";

    Eigen::Matrix3d inv = A.inverse();
    std::cout << "Обратная матрица:\n" << inv << "\n";

    Eigen::Matrix3d I_check = A * inv;
    std::cout << "A * inv(A) =\n" << I_check << "\n";

    if (I_check.isIdentity(Eigen::NumTraits<double>::epsilon())) {
        std::cout << "✅ Eigen работает идеально!\n";
    }
    return 0;
}
