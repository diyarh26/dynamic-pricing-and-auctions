import numpy as np
from scipy.stats import beta as beta_dist
from time import perf_counter



class PriceSetter2:
    def __init__(self, rounds, alpha, beta):
        self.rounds = rounds
        self.alpha = alpha
        self.beta = beta
        prices = np.linspace(0, 1, 1000)
        expected_revenues = [(price, price * (1 - beta_dist.cdf(price, self.alpha, self.beta))) for price in prices]
        self.optimal_price = max(expected_revenues, key=lambda x: x[1])[0]

    def set_price(self, t):
            return self.optimal_price

    def update(self, t, outcome):
        pass




def simulate(simulations, rounds, alpha, beta):
    simulations_results = []
    for _ in range(simulations):
        start = perf_counter()
        price_setter = PriceSetter2(rounds, alpha, beta)
        end = perf_counter()
        if end - start > 3:
            raise Exception("The initialization of the price setter is too slow.")
        revenue = 0

        for t in range(rounds):
            customer_value = np.random.beta(alpha, beta)
            start = perf_counter()
            price = price_setter.set_price(t)
            end = perf_counter()
            if end - start > 0.1:
                raise Exception("The set_price method is too slow.")

            if customer_value >= price:
                revenue += price

            start = perf_counter()
            price_setter.update(t, customer_value >= price)
            end = perf_counter()
            if end - start > 0.1:
                raise Exception("The update method is too slow.")

        simulations_results.append(revenue)

    return np.mean(simulations_results)


ALPHA_BETA_VALUES = [(2, 2), (4, 2), (2, 4), (4, 4), (8, 2), (2, 8), (8, 8)]
THRESHOLDS = [258, 409, 158, 284, 571, 89, 314
              ]
if __name__ == "__main__":
    np.random.seed(0)
    beta_parameters = [(2, 2), (4, 2), (2, 4), (4, 4), (8, 2), (2, 8), (8, 8)]
    for i, (alpha, beta) in enumerate(beta_parameters):
        print(f"Simulating for alpha={alpha}, beta={beta}")
        revenue = simulate(1000, 1000, alpha, beta)
        print(f"Average revenue: {revenue}")
        if revenue < THRESHOLDS[i]:
            raise Exception("The revenue is too low.")

    print("All tests passed.")