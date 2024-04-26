# CACHE-SIMULATOR
SIMPLE CACHE  SIMULATOR


language - python
MAPPING - 2 way set associativity

   INDEX :  address // self.block_size: Dividing the memory address
    by the block size gives the block number that the address belongs to.
    % self.num_sets: Taking the modulus of the block number with the number
    of cache sets ensures that the index stays within the range of available cache sets.
    TAG : address // (self.block_size * self.num_sets): Dividing the memory address by the total size of a set 
          This calculation ensures that each set has a unique tag for different blocks of memory

REPLACEMENT POLICY - LRU :

    implemented using a variable order and initialising it to 0 and updates when read or 
    write operations are called
    in write if the tag bit specified isnt free by finding the min of order we replace it

WRITE POLICY - WRITE THROUGH & WRITE ALLOCATE :  

    Write through : 
    
    policy means that data written/updated into both main memory and cache memory 
    at the same time
    we implemented write through by writing the data into the memory simultaneously 
    with the cache
    when read is performed and the data isnt available in the cache it fetches from the main
    memory and adds that data into thee cache through LRU.
    ADVANTAGES:
        NO NEED OF DIRTY BIT 
        LESS RISK OF DATA LOSS
        Ensures that data in the cache is always consistent with data in the main memory.
    
    Write allocate :

    upon cache miss - the code allocates space in the cache for the data
     and updates the cache line with the new data. 

