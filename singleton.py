class GameManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
            cls._instance.initialize_game()
        return cls._instance

    def initialize_game(self):
        self.score = 0
        self.level = 1
        print("Game initialized!")

    def increase_score(self, points):
        self.score += points
        print(f"Score increased to {self.score}")

    def advance_level(self):
        self.level += 1
        print(f"Advanced to level {self.level}")

# Example usage
game_manager1 = GameManager()
game_manager1.increase_score(10)
game_manager1.advance_level()

game_manager2 = GameManager()
print(game_manager1 is game_manager2)
