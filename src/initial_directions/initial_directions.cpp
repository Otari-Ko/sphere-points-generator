#include "initial_directions.h"

std::vector<Vector> randomDirections(const int num) {
    
    std::random_device seed;
    std::mt19937 engine(seed());

    std::normal_distribution<double> gauss(0.0, 1.0);

    std::vector<Vector> res(num);   

    for (size_t i = 0; i < num; ++i) {
        const double x = gauss(engine);
        const double y = gauss(engine);
        const double z = gauss(engine);
        
        Vector direction(x, y, z);
        direction.normalize();

        res[i] = direction;
    }

    return res;
}
