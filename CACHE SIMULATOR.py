import random

MAIN_MEMORY_SIZE = 1024
CACHE_SIZE = 64
BLOCK_SIZE = 4
ASSOCIATIVITY = 2  # Two-way set associativity

main_memory = [0] * MAIN_MEMORY_SIZE

class CacheLine:
    def __init__(self):
        self.tag = None
        self.valid = False
        self.data = None
        self.order = 0  

class CacheSet:
    def __init__(self):
        self.lines = [CacheLine() for _ in range(ASSOCIATIVITY)]

class Cache:
    def __init__(self, cache_size, block_size):
        self.cache_size = cache_size
        self.block_size = block_size
        self.num_sets = cache_size // (block_size * ASSOCIATIVITY)
        self.sets = [CacheSet() for _ in range(self.num_sets)]
        self.hits = 0
        self.misses = 0

    def access_cache(self, address, write=False, data=None):
        index = (address // self.block_size) % self.num_sets
        tag = address // (self.block_size * self.num_sets)
        
        print(f"TAG: {tag} Index: {index}")  

        if write:
            print(f"Write operation at Address: 0x{address:X}, Data: {data}")
            main_memory[address] = data

            for line in self.sets[index].lines:
                if line.valid and line.tag == tag:
                    line.data = data
                    self.hits+=1
                    return
            self.misses+=1
            least_recently_used_line = min(self.sets[index].lines, key=lambda x: x.order)
            least_recently_used_line.valid = True
            least_recently_used_line.tag = tag
            least_recently_used_line.data = data
            least_recently_used_line.order += 1
            return

        else:
            for line in self.sets[index].lines:
                if line.valid and line.tag == tag:
                    line.order += 1
                    self.hits += 1
                    print(f"Read operation at Address: 0x{address:X} -> Hit, Data: {line.data}")
                    return
        
            self.misses += 1
            print(f"Read operation at Address: 0x{address:X} -> Miss")
            
            least_recently_used_line = min(self.sets[index].lines, key=lambda x: x.order)
            least_recently_used_line.valid = True
            least_recently_used_line.tag = tag
            least_recently_used_line.data = main_memory[address]
            least_recently_used_line.order += 1
            print(f"Data read from main memory: {least_recently_used_line.data}")

    def hit_ratio(self):
        total_accesses = self.hits + self.misses
        if total_accesses == 0:
            return 0
        return self.hits / total_accesses

    def miss_ratio(self):
        total_accesses = self.hits + self.misses
        if total_accesses == 0:
            return 0
        return self.misses / total_accesses

def main():
    main_memory = [random.randint(0, 255) for _ in range(MAIN_MEMORY_SIZE)]

    cache = Cache(CACHE_SIZE, BLOCK_SIZE)
    num_accesses = int(input("Enter the number of memory accesses: "))
    print("Enter the memory addresses in hexadecimal format (e.g., 0xABCDEF):")

    for _ in range(num_accesses):
        address = int(input(), 16)
        operation = input("Read or Write? (R/W): ").upper()
        if operation == 'R':
            cache.access_cache(address)
        elif operation == 'W':
            data = int(input("Enter data to write: "))
            cache.access_cache(address, write=True, data=data)
    print(f"Hit Ratio: {cache.hit_ratio()}")
    print(f"Miss Ratio: {cache.miss_ratio()}")

if __name__ == "__main__":
    main()
