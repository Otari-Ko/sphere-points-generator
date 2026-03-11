import numpy as np

def random_directions(num):
    rng = np.random.default_rng()
    directions = rng.normal(0.0, 1.0, (num, 3))
    
    for i in range(num):
        dir = directions[i]
        norm = np.linalg.norm(dir)
        directions[i] = dir / norm
    
    return directions
