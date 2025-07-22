from datetime import date
import random



FORTUNE_OUTPUT_TEMPLATE = """
{today} の {name} さんの運勢

ラッキーカラー：{lucky_color}
ラッキーナンバー：{lucky_number}
"""

class UserProfile:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

class RandomFortuneTeller:
    def __init__(self, lucky_colors, lucky_numbers):
        self.lucky_colors = lucky_colors
        self.lucky_numbers = lucky_numbers

    def tell(self, user_profile, today):
        lucky_color = random.choice(self.lucky_colors)
        lucky_number = random.choice(self.lucky_numbers)

        return FORTUNE_OUTPUT_TEMPLATE.format(
            today = today,
            name = user_profile.name,
            lucky_color = lucky_color,
            lucky_number = lucky_number
        )

def main():
    name = "Alice"
    birthday = date(2000, 1, 2)
    user_profile = UserProfile(name, birthday)
    today = date.today()

    lucky_colors = ["red", "green", "blue"]
    lucky_numbers = [1, 2, 3]
    fortunr_teller = RandomFortuneTeller(lucky_colors, lucky_numbers)

    result = fortunr_teller.tell(user_profile, today)
    print(result)

if __name__ == "__main__":
    main()