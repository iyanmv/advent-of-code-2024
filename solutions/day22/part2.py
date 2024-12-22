from pathlib import Path

from part1 import get_next_number


module_path = Path(__file__).resolve().parent


def get_prices(secret_number, rounds):
    prices = [secret_number % 10]
    for i in range(rounds):
        secret_number = get_next_number(secret_number)
        prices.append(secret_number % 10)
    return prices


def get_diffs(prices):
    diffs = []
    for price in prices:
        diffs.append([price[i + 1] - price[i] for i in range(len(price) - 1)])
    return diffs


def get_bananas(list_prices, seq):
    bananas = 0
    for l in list_prices:
        for i in range(len(l) - 4):
            if tuple(_[1] for _ in l[i:i + 4]) == seq:
                bananas += l[i + 3][0]
                break
    return bananas


def get_scores(prices, diffs):
    scores = {}
    for j, _ in enumerate(prices):
        score = {}
        price, diff = prices[j], diffs[j]
        for i in range(len(diff) - 3):
            seq = tuple(_ for _ in diff[i:i + 4])
            bananas = price[i + 4]
            if seq not in score:
                score[seq] = bananas
        for seq, bananas in score.items():
            if seq not in scores:
                scores[seq] = bananas
            else:
                scores[seq] += bananas
    return scores


def part_2(nums):
    prices = []

    for n in nums:
        prices.append(get_prices(n, 2000))

    diffs = get_diffs(prices)
    scores = get_scores(prices, diffs)

    max_bananas = max(scores.values())
    for seq, bananas in scores.items():
        if bananas == max_bananas:
            break

    return seq, max_bananas


if __name__ == "__main__":
    with open(module_path / "input", "r") as file:
        nums = map(int, file.read().splitlines())

    solution = part_2(nums)

    print("Advent of Code 2024 (day 22 - Python)")
    print(f"Solution for part 2: {solution}")
