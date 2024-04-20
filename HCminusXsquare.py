def objective_function2(x):
    return -x**2

def hill_climbing_quadratic():
    # Initial point
    x = 0.0
    step_size = 0.1

    while True:
        current_value = objective_function2(x)
        next_value1 = objective_function2(x + step_size)
        next_value2 = objective_function2(x - step_size)

        if next_value1 > current_value:
            x += step_size
        elif next_value2 > current_value:
            x -= step_size
        else:
            break

    return x, objective_function2(x)

# Perform hill climbing for y = -x^2
optimal_x2, optimal_y2 = hill_climbing_quadratic()
print("Optimal Solution (y = -x^2): x =", optimal_x2, ", y =", optimal_y2)
