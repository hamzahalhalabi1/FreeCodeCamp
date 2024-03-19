import copy
import random

class Hat:
    def __init__(self, **colors):
        self.colors = colors
        self.contents = [color for color, count in self.colors.items() for _ in range(count)]

    def draw(self, num_balls):
        drawn_balls = random.sample(self.contents, min(num_balls, len(self.contents)))
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Check if the drawn balls match the expected balls
        is_successful = all(drawn_balls.count(color) >= count for color, count in expected_balls.items())

        if is_successful:
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability

# Example usage:
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red": 2, "green": 1},
                  num_balls_drawn=5,
                  num_experiments=200)

print(probability)
