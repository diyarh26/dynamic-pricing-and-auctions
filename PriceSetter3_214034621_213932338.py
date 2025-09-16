import numpy as np
from time import perf_counter


ALPHA_VALUES = [i for i in range(1, 11)]
BETA_VALUES = [i for i in range(1, 11)]


class PriceSetter3:
    def __init__(self, rounds):
        self.rounds = rounds
        self.alpha = 1
        self.beta = 1
        self.t = 0

    def set_price(self, t):
        mean = self.alpha / (self.alpha + self.beta)
        confidence_interval = np.sqrt(2 * np.log(self.t + 1) / (self.alpha + self.beta))
        variances = (self.alpha * self.beta) / ((self.alpha + self.beta) ** 2 * (self.alpha + self.beta + 1))
        combined_metric = mean + variances
        # price = combined_metric + confidence_interval
        return min(max(combined_metric, 0), 1)  # Ensure price is within [0, 1]

    def update(self, t, outcome):
        self.t = t
        if outcome:
            self.alpha += 2
        else:
            self.beta += 8

def simulate(simulations, rounds):
    """
    Simulate the game for the given number of rounds.

    Args:
        rounds (int): the number of rounds to simulate the game

    Returns:
        float: the average revenue of the seller
    """

    simulations_results = []
    for _ in range(simulations):

        alpha = np.random.choice(ALPHA_VALUES)
        beta = np.random.choice(BETA_VALUES)
        start = perf_counter()
        price_setter = PriceSetter3(rounds)
        end = perf_counter()
        if end - start > 1:
            raise Exception("The initialization of the price setter is too slow.")
        revenue = 0

        for t in range(rounds):
            costumer_value = np.random.beta(alpha, beta)
            start = perf_counter()
            price = price_setter.set_price(t)
            end = perf_counter()
            if end - start > 0.3:
                raise Exception("The set_price method is too slow.")
            if costumer_value >= price:
                revenue += price

            start = perf_counter()
            price_setter.update(t, costumer_value >= price)
            end = perf_counter()
            if end - start > 0.3:
                raise Exception("The update method is too slow.")

        simulations_results.append(revenue)

    return np.mean(simulations_results)


if __name__ == "__main__":
    np.random.seed(0)
    print(simulate(1000, 1000))
