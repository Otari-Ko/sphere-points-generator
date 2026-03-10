cmake_minimum_required(VERSION 3.22)
project(SpherePointsGenerator LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose Debug or Release" FORCE)
endif()

add_compile_options(-Wno-deprecated-declarations)

# Python
find_package(Python3 COMPONENTS Interpreter Development QUIET)
# Eigen
find_package(Eigen3 REQUIRED)

add_library(matplotlibcpp INTERFACE)
target_include_directories(matplotlibcpp INTERFACE ../3rd_party/matplotlib_cpp)

add_executable(eigen_test tests/eigen_test.cpp)
target_link_libraries(eigen_test PRIVATE 
    Eigen3::Eigen 
    matplotlibcpp
)

add_executable(matplotlibcpp_test tests/matplotlibcpp_test.cpp)
target_link_libraries(matplotlibcpp_test PRIVATE 
    matplotlibcpp
    Python3::Python
)
