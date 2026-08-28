import arcade


class Explosion:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.radius = 5
        self.max_radius = 35

        self.lifetime = 0.5
        self.timer = 0

    def update(self, delta_time):
        self.timer += delta_time
        self.radius += 60 * delta_time

        if self.timer >= self.lifetime:
            return True

        return False

    def draw(self):
        # Calculate transparency
        alpha = int(255 * (1 - self.timer / self.lifetime))

        # Outer circle
        arcade.draw_circle_filled(
            self.x,
            self.y,
            self.radius,
            (255, 0, 0, alpha)
        )

        # Middle circle
        arcade.draw_circle_filled(
            self.x,
            self.y,
            self.radius * 0.7,
            (255, 165, 0, alpha)
        )

        # Inner circle
        arcade.draw_circle_filled(
            self.x,
            self.y,
            self.radius * 0.4,
            (255, 255, 0, alpha)
        )