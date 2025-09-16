import numpy as np
from time import perf_counter

class PriceSetter1:

    def __init__(self, rounds):
        self.rounds = rounds
        self.lower_bound = 0.0
        self.upper_bound = 1.0
        self.current_price = (self.lower_bound + self.upper_bound) / 2
        self.previous_price = self.current_price
        self.previous_outcome = None
    def set_price(self, t):
        return self.current_price

    def update(self, t, outcome):

        noise = 0.001 + np.random.uniform(-0.000001, 0.000001)
        if outcome:
            self.lower_bound = self.current_price - noise
        else:
            self.upper_bound = self.current_price + noise

        if self.previous_outcome and not outcome:
            self.upper_bound = self.previous_price

        if self.previous_price and outcome:
            self.previous_price = self.current_price

        self.current_price = (self.lower_bound + self.upper_bound) / 2
        self.previous_price = self.current_price
        self.previous_outcome = outcome


def simulate(simulations, rounds):
    """
    Simulate the game for the given number of rounds.

    Args:
        rounds (int): the number of rounds to simulate

    Returns:
        float: the revenue of the price setter
    """
    simulations_results = []
    for _ in range(simulations):
        start = perf_counter()
        price_setter = PriceSetter1(rounds)
        end = perf_counter()
        if end - start > 1:
            raise Exception("The initialization of the price setter is too slow.")
        revenue = 0
        costumer_value = np.random.uniform(0, 1)

        for t in range(rounds):
            start = perf_counter()
            price = price_setter.set_price(t)
            end = perf_counter()
            if end - start > 0.1:
                raise Exception("The set_price method is too slow.")
            if costumer_value >= price:
                revenue += price

            start = perf_counter()
            price_setter.update(t, costumer_value >= price)
            end = perf_counter()
            if end - start > 0.1:
                raise Exception("The update method is too slow.")

        simulations_results.append(revenue)

    return np.mean(simulations_results)


if __name__ == "__main__":
    np.random.seed(0)
    print(simulate(1000, 1000))
