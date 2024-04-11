import random


def objective_function(x):
    # Example objective function: maximize f(x) = -x^2
    return -x ** 2


def hill_climbing(initial_position, step_size, max_iterations):
    current_position = initial_position
    current_value = objective_function(current_position)

    for iteration in range(max_iterations):
        # Generate a neighbor within the specified step size
        neighbor_position = current_position + random.uniform(-step_size, step_size)
        # Evaluate the objective function for the neighbor
        neighbor_value = objective_function(neighbor_position)

        # If the neighbor has a higher value, move to the neighbor
        if neighbor_value > current_value:
            current_position = neighbor_position
            current_value = neighbor_value

    return current_position, current_value


def main():
    # Initial parameters
    initial_position = random.uniform(-10, 10)
    step_size = 0.1
    max_iterations = 100

    # Run the Hill Climbing algorithm
    final_position, max_value = hill_climbing(initial_position, step_size, max_iterations)

    print(f"Initial Position: {initial_position}")
    print(f"Final Position: {final_position}")
    print(f"Maximum Value: {max_value}")


if __name__ == "__main__":
    main()
