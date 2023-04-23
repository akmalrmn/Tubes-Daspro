class LCG: # algoritma Linear Congruential Generator (LCG) menggunakan seed
    def __init__(self, seed, a, c, m):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def generate(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

seed = 12345  # initial seed
a = 7  # multiplier
c = 1  # increment
m = 11  # modulus

lcg = LCG(seed, a, c, m)

# Membuat array yang isinya angka antara 0 dan 5 dengan asumsi user tidak akan menggunakan RNG lebih dari 999999 kali
rand_nums = [lcg.generate() % 6 for _ in range(99999)]

# Membuat array yang isinya angka antara 1 dan 5
rand_nums2 = [(lcg.generate() % 5) + 1 for _ in range(99999)]