import arcade

from config.settings import DAMAGE_NUMBER_LIFETIME, DAMAGE_NUMBER_SPEED

class DamageNumber:
    def __init__(self, x, y, damage):
        self.damage = damage
        self.lifetime = DAMAGE_NUMBER_LIFETIME
        self.elapsed_time = 0

        self.x = x
        self.y = y

    def update(self, delta_time):
        self.elapsed_time += delta_time
        self.y += DAMAGE_NUMBER_SPEED * delta_time

    def draw(self):
        arcade.draw_text(
            f"-{self.damage}",
            self.x,
            self.y,
            arcade.color.RED,
            16,
            anchor_x="center"
        )

    def is_finished(self):
        return self.elapsed_time >= self.lifetime

class DamageNumberList:
    def __init__(self):
        self.damage_numbers = []

    def add(self, x, y, damage):
        self.damage_numbers.append(
            DamageNumber(x, y, damage)
        )

    def update(self, delta_time):
        for damage_number in self.damage_numbers[:]:
            damage_number.update(delta_time)

            if damage_number.is_finished():
                self.damage_numbers.remove(damage_number)

    def draw(self):
        for damage_number in self.damage_numbers:
            damage_number.draw()

    def clear(self):
        self.damage_numbers.clear()