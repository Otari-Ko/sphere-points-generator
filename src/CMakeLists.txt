cmake_minimum_required(VERSION 3.22)

# Define the project name and set it to use C++ as the primary language
project(SpherePointsGenerator LANGUAGES CXX)

# Set C++ standard to C++20 and enforce strict compliance
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Define the maximum number of errors before compilation stops (for GCC/Clang)
set(MAX_ERRORS "3")

# Set Release mode as the default build type if not specified
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release CACHE STRING "Choose Debug or Release" FORCE)
endif()

# Include directories for third-party dependencies and project sources
include_directories(SYSTEM 3rd_party)

add_executable(eigen_test tests/eigen_test.cpp)
