items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            chosen_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']

    return chosen_items, total_calories, total_cost


def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    costs = [items[item]['cost'] for item in item_names]
    calories = [items[item]['calories'] for item in item_names]

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1]
                               [w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    total_calories = dp[n][budget]
    total_cost = 0
    chosen_items = []
    w = budget

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(item_names[i - 1])
            total_cost += costs[i - 1]
            w -= costs[i - 1]

    return chosen_items, total_calories, total_cost


budget = 100

greedy_items, greedy_calories, greedy_cost = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Chosen items:", greedy_items)
print("Total calories:", greedy_calories)
print("Total cost:", greedy_cost)

print("\n")
dp_items, dp_calories, dp_cost = dynamic_programming(items, budget)
print("Dynamic Programming:")
print("Chosen items:", dp_items)
print("Total calories:", dp_calories)
print("Total cost:", dp_cost)
