import math

def hill_climbing(objective_function):
    # Initial point
    x = 0.0
    step_size = 0.1

    while True:
        current_value = objective_function(x)
        next_value1 = objective_function(x + step_size)
        next_value2 = objective_function(x - step_size)

        if next_value1 > current_value:
            x += step_size
        elif next_value2 > current_value:
            x -= step_size
        else:
            break

    optimal_x = x
    optimal_y = objective_function(optimal_x)
    return optimal_x, optimal_y

# Define objective functions
def sin_function(x):
    return math.sin(x)

def quadratic_function(x):
    return -x**2

def quadratic_function2(x):
    return -5*x**2 + 3*x + 6

# Perform hill climbing for y = sin(x)
optimal_x1, optimal_y1 = hill_climbing(sin_function)
print("Optimal Solution (y = sin(x)): x =", optimal_x1, ", y =", optimal_y1)

# Perform hill climbing for y = -x^2
optimal_x2, optimal_y2 = hill_climbing(quadratic_function)
print("Optimal Solution (y = -x^2): x =", optimal_x2, ", y =", optimal_y2)

# Perform hill climbing for y = -5x^2 + 3x + 6
optimal_x3, optimal_y3 = hill_climbing(quadratic_function2)
print("Optimal Solution (y = -5x^2 + 3x + 6): x =", optimal_x3, ", y =", optimal_y3)
