def objective_function3(x):
    return -5*x**2 + 3*x + 6

def hill_climbing_quadratic2():
    # Initial point
    x = 0.0
    step_size = 0.1

    while True:
        current_value = objective_function3(x)
        next_value1 = objective_function3(x + step_size)
        next_value2 = objective_function3(x - step_size)

        if next_value1 > current_value:
            x += step_size
        elif next_value2 > current_value:
            x -= step_size
        else:
            break

    return x, objective_function3(x)

# Perform hill climbing for y = -5x^2 + 3x + 6
optimal_x3, optimal_y3 = hill_climbing_quadratic2()
print("Optimal Solution (y = -5x^2 + 3x + 6): x =", optimal_x3, ", y =", optimal_y3)
