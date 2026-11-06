class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        x = init

        # Update rule: x = x - learning_rate * f'(x)
        for _ in range(iterations):
            derivative = 2 * x
            x = x - learning_rate * derivative
        # Round final answer to 5 decimal places
        return round(x, 5)