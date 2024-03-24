# Prime numbers and polar coordinate system

## Prime numbers

Prime numbers are a fundamental concept in number theory and have various applications in mathematics and computer science. A prime number is a positive integer greater than 1 that is divisible only by 1 and itself.

Formally, a number $p$ is prime if and only if it satisfies the following condition:

$$
\forall a, b \in \mathbb{Z}^+, p = a \times b \implies (a = 1 \land b = p) \lor (a = p \land b = 1)
$$

In other words, $p$ cannot be expressed as the product of two positive integers other than 1 and itself.

The first few prime numbers are:

$$
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, \ldots
$$

One way to determine if a number $n$ is prime is to check if it is divisible by any number $k$ between 2 and $\sqrt{n}$. This is known as trial division, and it can be expressed mathematically as:

$$
n \text{ is prime} \iff \forall k \in \mathbb{Z}^+, 2 \leq k \leq \sqrt{n}, n \not\equiv 0 \pmod{k}
$$

## Polar coordinate system

The polar coordinate system is an alternative to the Cartesian coordinate system for representing points in a plane. Instead of representing a point using its x and y coordinates, the polar coordinate system uses a radius ($r$) and an angle ($θ$) from a fixed reference point.

![Polar coordinate system](https://tinyurl.com/3xat6p47)

In the polar coordinate system, a point $P$ is represented by an ordered pair $(r, θ)$, where:

- $r$ is the distance from P to the origin (the reference point, usually denoted as $O$).
- $θ$ is the angle between the positive $x$-axis and the line segment $OP$, measured counterclockwise from the positive $x$-axis.

The conversion between Cartesian coordinates $(x, y)$ and polar coordinates $(r, θ)$ is given by the following formulas:

$$
r = \sqrt{x^2 + y^2}
$$
$$
\theta = \tan^{-1}\left(\frac{y}{x}\right)
$$

Conversely, to convert from polar coordinates $(r, θ)$ to Cartesian coordinates $(x, y)$:

$$
x = r \cos(\theta)
$$
$$
y = r \sin(\theta)
$$

## Archimedean spiral

The Archimedean spiral, also known as the arithmetic spiral, is a spiral curve that follows the path traced by a point moving away from a fixed origin at a constant speed along a line that rotates at a constant angular velocity. It is named after the ancient Greek mathematician Archimedes.

![Archimedean spiral](https://tinyurl.com/mxdwmww8)

The equation of an Archimedean spiral in polar coordinates $(r, θ)$ is given by:

$$
r = a\theta
$$

where:
- $r$ is the radius or distance from the origin
- $θ$ is the angle measured counterclockwise from the positive $x$-axis
- a is a constant that determines the separation between successive turnings of the spiral

The Cartesian equation of the Archimedean spiral can be obtained by substituting the polar coordinate expressions for $x$ and $y$:

$$
x = a\theta\cos(\theta)
$$
$$
y = a\theta\sin(\theta)
$$

## Code implementation

The `main.py` script demonstrates the generation of prime numbers using the Sieve of Eratosthenes algorithm and their visualization on an Archimedean spiral using polar coordinates. It utilizes several libraries such as NumPy, Matplotlib, and Numba for efficient computation and plotting.

### Properties and Functions

**PrimeNumber Class:**

- `__init__(self, limit)`: Initializes the PrimeNumber class with a limit that determines the range of prime numbers to generate.
- `primes` (property): Returns a list of all prime numbers up to the specified limit using the Sieve of Eratosthenes algorithm. It utilizes memoization with LRU cache for efficiency.
- `__len__(self)`: Returns the number of prime numbers generated.
- `__getitem__(self, index)`: Retrieves the prime number at a given index.
- `__iter__(self)`: Enables iteration over the generated prime numbers.

**PlotterBase Abstract Base Class:**

- `__init__(self, primes)`: Initializes the abstract base class for plotters with a list of prime numbers.
- `plot(self, num_primes, save_path)` (abstractmethod): Abstract method to plot the prime numbers on a specific plot and save the result.

**ArchimedeanSpiral Class (Subclass of PlotterBase):**

- `plot(self, num_primes=1000, save_path="img/prime_archimedean_spiral.svg")`: Plots the prime numbers on an Archimedean Spiral using polar coordinates and saves the result as an SVG file.
    - `num_primes`: Number of prime numbers to plot on the spiral.
    - `save_path`: File path to save the generated plot as an SVG image.

**App Class:**

- `__init__(self, limit)`: Initializes the main application class with a limit for prime number generation and creates instances of PrimeNumber and ArchimedeanSpiral classes.
- `run(self)`: Runs the application by calling the plot method of the ArchimedeanSpiral class to generate and save the plot.

### Preview

![Prime numbers and polar coordinate system](img/prime_archimedean_spiral.png)
