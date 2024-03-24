"""
Prime numbers and polar coordinate system
"""

import math
import os
from abc import ABC, abstractmethod
from functools import lru_cache

import matplotlib as mpl
import numba as nb
import numpy as np
from matplotlib import pyplot as plt


class PrimeNumber:
    """
    A class to generate prime numbers up to a given limit.
    """

    def __init__(self, limit):
        self.limit = limit
        self._primes = self._sieve_of_eratosthenes(limit)

    @property
    @lru_cache(maxsize=1)
    def primes(self):
        """
        The primes function returns a list of all prime numbers up to the number
            passed in as an argument.  The function uses the Sieve of Eratosthenes
            algorithm to generate a list of primes.
        """
        return self._primes

    @staticmethod
    @nb.njit(parallel=True)
    def _sieve_of_eratosthenes(limit):
        """
        Private method to generate prime numbers using the Sieve of Eratosthenes algorithm.
        """
        is_prime = np.ones(limit + 1, dtype=nb.boolean)
        is_prime[:2] = False
        for i in nb.prange(
            2, int(math.sqrt(limit)) + 1
        ):  # pylint: disable=E1133:not-an-iterable
            if is_prime[i]:
                is_prime[i * i :: i] = False
        return np.flatnonzero(is_prime)

    def __len__(self):
        """
        Magic method to get the number of prime numbers generated.
        """
        return len(self.primes)

    def __getitem__(self, index):
        """
        Magic method to get the prime number at a given index.
        """
        return self.primes[index]

    def __iter__(self):
        """
        Magic method to make the class iterable.
        """
        return iter(self.primes)


class PlotterBase(ABC):
    """
    Abstract base class for plotters.
    """

    def __init__(self, primes):
        """
        The __init__ function is called when the class is instantiated.
        It takes a list of primes as an argument and stores it in the object's
        """
        self.primes = primes

    @abstractmethod
    def plot(self, num_primes, save_path):
        """
        Abstract method to plot the prime numbers and save the result.
        """


class ArchimedeanSpiral(PlotterBase):
    """
    A class to plot prime numbers on an Archimedean Spiral using polar coordinates.
    """

    def plot(self, num_primes=1000, save_path="img/prime_archimedean_spiral.svg"):
        """
        The plot function plots the prime numbers on an Archimedean Spiral and saves the result as an SVG file.
        """
        primes = self.primes[:num_primes]

        # Calculate the angles and radii for the Archimedean Spiral
        angles = np.linspace(0, 7 * 2 * np.pi, len(primes), endpoint=False)
        radii = np.log(primes) / (2 * np.pi)

        fig, ax = plt.subplots(figsize=(20, 20), subplot_kw=dict(projection="polar"))

        ax.scatter(angles, radii, s=20, c="r", alpha=0.5)
        ax.set_rlabel_position(22.5)
        ax.grid(True)

        # Add corresponding numbers next to each point
        for angle, radius, prime in zip(angles, radii, primes):
            radius * np.cos(angle)
            radius * np.sin(angle)
            ax.text(angle, radius, str(prime), ha="center", va="center", fontsize=14)

        # Zoom in on the first 7 bars (or spokes) of the spiral
        ax.set_thetamin(0)
        ax.set_thetamax(7 * 2 * np.pi / len(primes))
        ax.set_rmin(0)
        ax.set_rmax(
            np.log(primes[int(7 * len(primes) / (7 * 2 * np.pi))]) / (2 * np.pi)
        )

        os.makedirs("img", exist_ok=True)
        mpl.rcParams["svg.fonttype"] = "none"
        plt.savefig(save_path, dpi=300, bbox_inches="tight", format="svg")
        print(f"Plot saved as {save_path}")


class App:
    """
    The main application class.
    """

    def __init__(self, limit):
        """
        The __init__ function initializes the class with a limit and creates an instance of PrimeNumber.
        It also creates an instance of ArchimedeanSpiral, which takes in the prime_generator as its argument.
        """
        self.prime_generator = PrimeNumber(limit)
        self.plotter = ArchimedeanSpiral(self.prime_generator)

    def run(self):
        """
        Method to run the application.
        """
        self.plotter.plot()


if __name__ == "__main__":
    app = App(10**6)
    app.run()
