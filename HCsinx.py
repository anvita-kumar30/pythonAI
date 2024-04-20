import math

def objective_function1(x):
    return math.sin(x)

def hill_climbing_sin():
    # Initial point
    x = 0.0
    step_size = 0.1

    while True:
        current_value = objective_function1(x)
        next_value1 = objective_function1(x + step_size)
        next_value2 = objective_function1(x - step_size)

        if next_value1 > current_value:
            x += step_size
        elif next_value2 > current_value:
            x -= step_size
        else:
            break

    return x, objective_function1(x)

# Perform hill climbing for y = sin(x)
optimal_x1, optimal_y1 = hill_climbing_sin()
print("Optimal Solution (y = sin(x)): x =", optimal_x1, ", y =", optimal_y1)
