# lcg.py

class LCG:
    def __init__(self, seed, a, c, m):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def generate(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

# Example usage:
seed = 12345  # initial seed
a = 7  # multiplier
c = 1  # increment
m = 11  # modulus

lcg = LCG(seed, a, c, m)

# Generate a list of 10 random numbers between 0 and 5
rand_nums = [lcg.generate() % 6 for _ in range(1000)]