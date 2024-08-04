import numpy as np
import matplotlib.pyplot as plt


def monte_carlo_simulation(num_trials):
    rolls = np.random.randint(1, 7, size=(num_trials, 2))
    sums = np.sum(rolls, axis=1)

    counts = np.bincount(sums)[2:]
    probabilities = counts / num_trials

    return probabilities


def plot_results(monte_carlo_probs, analytical_probs):
    sums = np.arange(2, 13)

    plt.figure(figsize=(10, 6))
    plt.bar(sums - 0.2, monte_carlo_probs, width=0.4,
            label='Monte Carlo Simulation', color='blue')
    plt.bar(sums + 0.2, analytical_probs, width=0.4,
            label='Analytical Probabilities', color='red')

    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Probability')
    plt.title('Probability Comparison of Dice Sums')
    plt.xticks(sums)
    plt.legend()
    plt.grid(axis='y')
    plt.show()


def main():
    num_trials = 100000  
    monte_carlo_probs = monte_carlo_simulation(num_trials)

    analytical_probs = np.array(
        [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36])

    print("Monte Carlo Probabilities:")
    for sum_val, prob in zip(range(2, 13), monte_carlo_probs):
        print(f"Sum {sum_val}: {prob:.4f}")

    print("\nAnalytical Probabilities:")
    for sum_val, prob in zip(range(2, 13), analytical_probs):
        print(f"Sum {sum_val}: {prob:.4f}")

    plot_results(monte_carlo_probs, analytical_probs)


if __name__ == "__main__":
    main()
