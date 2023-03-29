from unittest import TestCase, main
from project.hero import Hero


class HeroTests(TestCase):

    def setUp(self):
        self.hero = Hero('Hero', 1, 100, 100)
        self.enemy = Hero('Enemy', 1, 50, 50)

    def test_initialization(self):
        self.assertEqual('Hero', self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

        self.assertEqual('Enemy', self.enemy.username)
        self.assertEqual(1, self.enemy.level)
        self.assertEqual(50, self.enemy.health)
        self.assertEqual(50, self.enemy.damage)

    # тестваме дали се бием със себе си
    def test_fighting_yourself_error(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    # тестваме дали имаме живот за да се биеме
    def test_fight_hero_with_zero_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    # тестваме дали живота на противника ни е >= 0
    def test_fight_enemy_with_zero_health(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ve.exception))

    # тестваме при битка и равен резултат
    def test_health_and_damage_taken_and_removed_when_result_is_draw(self):
        # Arrange
        self.hero.health = self.enemy.health
        self.hero.damage = self.enemy.damage

        # Act
        result = self.hero.battle(self.enemy)

        # Assert
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy.health)
        self.assertEqual(result, 'Draw')

    def test_battle_enemy_and_win_expect_stats_improve(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual(-50, self.enemy.health)
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 55)
        self.assertEqual(self.hero.damage, 105)
        self.assertEqual(result, "You win")

    def test_battle_enemy_and_lose_expect_stats_improve(self):
        self.hero, self.enemy = self.enemy, self.hero

        result = self.hero.battle(self.enemy)

        self.assertEqual(55, self.enemy.health)
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.health, -50)
        self.assertEqual(self.hero.damage, 50)
        self.assertEqual(result, "You lose")

    def test_str(self):
        self.assertEqual(
            "Hero Hero: 1 lvl\n" +
            "Health: 100\n" +
            "Damage: 100\n",
            str(self.hero.__str__())
        )


if __name__ == "__main__":
    main()