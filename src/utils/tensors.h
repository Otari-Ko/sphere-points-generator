#pragma once

#include <cmath>
#include <Eigen/Eigen>
#include <Eigen/Geometry>

template <int64_t m, int64_t n>
using MatrixXX = Eigen::Matrix<double, m, n>;

using Matrix = Eigen::Matrix3d;
using Matrix5 = MatrixXX<5, 5>;
using Matrix6 = MatrixXX<6, 6>;
using Matrix9 = MatrixXX<9, 9>;

using Vector = Eigen::Vector3d;
using Vector5 = MatrixXX<5, 1>;
using Vector6 = MatrixXX<6, 1>;
using Vector9 = MatrixXX<9, 1>;

using VectorX = Eigen::VectorXd;

namespace
{
namespace Internal
{
/* This enumeration for symmetric 3x3 matrices is used by MSC.MARC
 * (upper part of matrix is referenced)
 * 0 3 5
 * 3 1 4
 * 5 4 2
 */
static constexpr int64_t matrixIxs1[6] = {0, 1, 2, 0, 1, 0};
static constexpr int64_t matrixIxs2[6] = {0, 1, 2, 1, 2, 2};

// These values could be used only for matrix C or E
static constexpr double coeffsValues[6] = {1.0, 1.0, 1.0, 0.5, 0.5, 0.5};
} // namespace Internal

inline Matrix deviator(const Matrix in)
{
	return in - in.trace() * (1.0 / 3.0) * Matrix::Identity();
}

inline Matrix unimodular(const Matrix in)
{
	return in / std::cbrt(in.determinant());
}

/* Order of elements in non-symmetric Matrix
 * 0 3 6
 * 1 4 7
 * 2 5 8
 */
inline Matrix basisMatrix(const int64_t in)
{
	Matrix res = Matrix::Zero();
	res(in % 3, in / 3) = 1.0;
	return res;
}

// These matrices could be used only for C or E.
inline Matrix basisSymMatrix(const int64_t in)
{
	Matrix res = Matrix::Zero();
	res(Internal::matrixIxs1[in], Internal::matrixIxs2[in]) = Internal::coeffsValues[in];
	res(Internal::matrixIxs2[in], Internal::matrixIxs1[in]) = Internal::coeffsValues[in];

	return res;
}

inline Matrix basisMatrix3(const int64_t in)
{
	Matrix res = Matrix::Zero();
	res(in % 3, in / 3) = 1.0;
	return res;
}

inline Matrix basisMatrix3(int row, int col)
{
	Matrix mat = Matrix::Zero();
	mat(row, col) = 1.0;
	return mat;
}

inline Vector6 symMatrixToVector(const Matrix& in)
{
	Vector6 res;
	for (int64_t i = 0; i < 6; ++i)
		res(i) = in(Internal::matrixIxs1[i], Internal::matrixIxs2[i]);

	return res;
}

inline Matrix vectorToSymMatrix(const Vector6& in)
{
	Matrix res;
	for (int64_t i = 0; i < 6; ++i) {
		res(Internal::matrixIxs1[i], Internal::matrixIxs2[i]) = in(i);
		res(Internal::matrixIxs2[i], Internal::matrixIxs1[i]) = in(i);
	}

	return res;
}

inline Vector9 matrixToVector(const Matrix& in)
{
	Vector9 res;
	for (int64_t i = 0; i < 9; ++i)
		res(i) = in(i % 3, i / 3);

	return res;
}

inline Matrix vectorToMatrix(const Vector9& in)
{
	Matrix res;
	for (int64_t i = 0; i < 9; ++i)
		res(i % 3, i / 3) = in(i);

	return res;
}

inline Vector6 symMatrixToVector2(const Matrix& in)
{
	Vector6 res;
	for (int64_t i = 0; i < 6; ++i)
		res(i) = in(Internal::matrixIxs1[i], Internal::matrixIxs2[i]);

	return res;
}

inline Matrix vectorToSymMatrix2(const Vector6& in)
{
	Matrix res;
	for (int64_t i = 0; i < 6; ++i) {
		res(Internal::matrixIxs1[i], Internal::matrixIxs2[i]) = in(i);
		res(Internal::matrixIxs2[i], Internal::matrixIxs1[i]) = in(i);
	}

	return res;
}

inline Matrix derToMatrix(const Matrix& mat, const Matrix6& der)
{
	Vector6 vec;

	for (int64_t i = 0; i < 6; ++i)
		vec(i) = mat(Internal::matrixIxs1[i], Internal::matrixIxs2[i]) / Internal::coeffsValues[i];

	const Vector6 tmp = der * vec;

	Matrix res;

	for (int64_t i = 0; i < 6; ++i) {
		res(Internal::matrixIxs1[i], Internal::matrixIxs2[i]) = tmp(i);
		res(Internal::matrixIxs2[i], Internal::matrixIxs1[i]) = tmp(i);
	}

	return res;
}

// trans(X) = op(X)
inline Matrix9 transOperator()
{
	Matrix9 res = Matrix9::Zero();

	res(0, 0) = 1.0;
	res(1, 3) = 1.0;
	res(2, 6) = 1.0;
	res(3, 1) = 1.0;
	res(4, 4) = 1.0;
	res(5, 7) = 1.0;
	res(6, 2) = 1.0;
	res(7, 5) = 1.0;
	res(8, 8) = 1.0;

	return res;
}

// X * in = Op(X)
inline Matrix9 matrixToProduct1(const Matrix& in)
{
	Matrix9 res = Matrix9::Zero();

	// clang-format off
	res<<in(0, 0), 0.0,      0.0,      in(1, 0), 0.0,      0.0,      in(2, 0), 0.0,      0.0,     // 1
	    0.0,      in(0, 0), 0.0,      0.0,      in(1, 0), 0.0,      0.0,      in(2, 0), 0.0,      // 2
	    0.0,      0.0,      in(0, 0), 0.0,      0.0,      in(1, 0), 0.0,      0.0,      in(2, 0), // 3
	    in(0, 1), 0.0,      0.0,      in(1, 1), 0.0,      0.0,      in(2, 1), 0.0,      0.0,      // 4
	    0.0,      in(0, 1), 0.0,      0.0,      in(1, 1), 0.0,      0.0,      in(2, 1), 0.0,      // 5
	    0.0,      0.0,      in(0, 1), 0.0,      0.0,      in(1, 1), 0.0,      0.0,      in(2, 1), // 6
	    in(0, 2), 0.0,      0.0,      in(1, 2), 0.0,      0.0,      in(2, 2), 0.0,      0.0,      // 7
	    0.0,      in(0, 2), 0.0,      0.0,      in(1, 2), 0.0,      0.0,      in(2, 2), 0.0,      // 8
	    0.0,      0.0,      in(0, 2), 0.0,      0.0,      in(1, 2), 0.0,      0.0,      in(2, 2); // 9
	// clang-format on

	return res;
}
// in^T * X = op(X)
inline Matrix9 matrixToProduct2(const Matrix& in)
{
	Matrix9 res = Matrix9::Zero();

	// clang-format off
	res<<in(0, 0), in(1, 0), in(2, 0), 0.0,      0.0,      0.0,      0.0,      0.0,      0.0,     // 1
	    in(0, 1), in(1, 1), in(2, 1), 0.0,      0.0,      0.0,      0.0,      0.0,      0.0,      // 2
	    in(0, 2), in(1, 2), in(2, 2), 0.0,      0.0,      0.0,      0.0,      0.0,      0.0,      // 3
	    0.0,      0.0,      0.0,      in(0, 0), in(1, 0), in(2, 0), 0.0,      0.0,      0.0,      // 4
	    0.0,      0.0,      0.0,      in(0, 1), in(1, 1), in(2, 1), 0.0,      0.0,      0.0,      // 5
	    0.0,      0.0,      0.0,      in(0, 2), in(1, 2), in(2, 2), 0.0,      0.0,      0.0,      // 6
	    0.0,      0.0,      0.0,      0.0,      0.0,      0.0,      in(0, 0), in(1, 0), in(2, 0), // 7
	    0.0,      0.0,      0.0,      0.0,      0.0,      0.0,      in(0, 1), in(1, 1), in(2, 1), // 8
	    0.0,      0.0,      0.0,      0.0,      0.0,      0.0,      in(0, 2), in(1, 2), in(2, 2); // 9
	// clang-format on

	return res;
}

// trans(X) * in = op(X)
inline Matrix9 matrixToProduct3(const Matrix& in)
{
	return matrixToProduct1(in) * transOperator();
}

// directional derivative of C
inline Matrix derC(const Matrix F, const Matrix dF)
{
	return dF.transpose() * F + F.transpose() * dF;
}

// derivative of C as 9x9 matrix
inline const Matrix9 derC(const Matrix& F)
{
	return matrixToProduct3(F) + matrixToProduct2(F);
}

// compute tensor (dir \otimes dir \otimes dir \otimes dir) in Marc representation
inline const Matrix6 strTensor4rank(const Vector& dir)
{
	Matrix6 res;
	for (int64_t i = 0; i < 6; ++i) {
		for (int64_t j = 0; j < 6; ++j) {
			const int64_t k = Internal::matrixIxs1[i];
			const int64_t l = Internal::matrixIxs2[i];
			const int64_t m = Internal::matrixIxs1[j];
			const int64_t n = Internal::matrixIxs2[j];

			res(i, j) = dir(k) * dir(l) * dir(m) * dir(n);
		}
	}
	return res;
}

} // namespace
