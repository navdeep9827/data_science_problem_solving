#!/usr/bin/env python
# coding: utf-8

# 

# In[5]:


class HashTableChain:
    def __init__(self, size, file):
        self.size = size
        self.table = [None] * size
        self.g = 31  # positive constant
        self.file = file
        
        # Populate the hash table when the object is created
        self.populate_hash_table()
        
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for item in self.table:
                if item is not None:
                    for key, value in item:
                        file.write(f'{key.capitalize()} {value}\n')

    # hash function to determine the index for a given key
    def hash_function(self, key):
        
        hash_value = 0
        for char in key:
            hash_value = self.g * hash_value + ord(char)
        index = hash_value % self.size
        return index

    # insert a key-value pair to the hash table
    
    def insert(self, key, value):
        
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, v + value)
                    break
            else:
                self.table[index].append((key, value))

    # retrve the value for a given key
    
    def search(self, key):
        
        index = self.hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        return 0

    def delete(self, key):
        
        index = self.hash_function(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    break
                    
    # Populate the hash table with words from the specified file
    
    def populate_hash_table(self):
        with open(self.file, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    word = word.lower()  
                    self.insert(word, 1)


# In[4]:


def count_word_occurrences1(file_path):
    word_count = HashTableChain(100, file_path)  # working with size = 100

    # Output the word occurrences
    for item in word_count.table:
        if item is not None:
            for key, value in item:
                print(f'{key.capitalize()} {value}')

    # Save the hash table to "Chaining.txt"
    word_count.save_to_file('Chaining.txt')

if __name__ == '__main__':
    text_file = 'dictionary.txt'  # Replace with the path to your input text file
    count_word_occurrences1(text_file)


# In[6]:


class HashTableLinProb:
    def __init__(self, size, file):
        self.size = size
        self.table = [None] * size
        self.g = 31  # positive constant
        self.file = file
        self.num_elements = 0  # to track the number of elements

        # Populate the hash table when the object is created
        self.populate_hash_table()

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for entry in self.table:
                if entry is not None:
                    key, value = entry
                    file.write(f'{key.capitalize()} {value}\n')

    # hash function to determine the index for a given key
    def hash_function(self, key):
        hash_value = 0
        for char in key:
            hash_value = self.g * hash_value + ord(char)
        index = hash_value % self.size
        return index

    # insert a key-value pair to the hash table using linear probing
    def insert(self, key, value):
        if self.num_elements >= self.size * 0.8:
            # If the load factor is too high, resize the table
            self.resize_table(self.size * 2)
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, self.table[index][1] + value)
                return
            index = (index + 1) % self.size
        self.table[index] = (key, value)
        self.num_elements += 1

    # retrieve the value for a given key
    def search(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return 0

    def delete(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                self.num_elements -= 1  # Decrement the element count
                return
            index = (index + 1) % self.size

    def resize_table(self, new_size):
        new_table = [None] * new_size
        for entry in self.table:
            if entry is not None:
                key, value = entry
                new_index = self.hash_function(key) % new_size
                while new_table[new_index] is not None:
                    new_index = (new_index + 1) % new_size
                new_table[new_index] = (key, value)
        self.size = new_size
        self.table = new_table

    # Populate the hash table with words from the specified file
    def populate_hash_table(self):
        with open(self.file, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    word = word.lower()
                    self.insert(word, 1)


# In[35]:


def count_word_occurrences2(file_path):
    word_count = HashTableLinProb(100000, file_path)   # for work corretly we have to give full size

    # Output the word occurrences
    for entry in word_count.table:
        if entry is not None:
            key, value = entry
            print(f'{key.capitalize()} {value}')

    # Save the hash table to "Probing.txt"
    word_count.save_to_file('Probing.txt')
    
if __name__ == '__main__':
    text_file = 'dictionary.txt'  
    count_word_occurrences2(text_file)


# In[7]:


class HashTableDoubleHash:
    def __init__(self, size, file):
        self.size = size  
        self.table = [None] * size  
        self.g = 31  
        self.file = file
        
        # Populate the hash table when the object is created
        self.populate_hash_table()

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for entry in self.table:
                if entry is not None:
                    key, value = entry
                    file.write(f'{key.capitalize()} {value}\n')
                # Write the key and value (capitalized) to the output file

    def hash_function(self, key):
        hash_value = 0
        for char in key:
            hash_value = self.g * hash_value + ord(char)
        index = hash_value % self.size
        return index
        # Compute the primary hash index for a given key

    def secondary_hash_function(self, key):
        hash_value = 0
        for char in key:
            hash_value = self.g * hash_value + ord(char)
        return 1 + (hash_value % (self.size - 1))
        # Compute the secondary hash (step size) for double hashing

    def insert(self, key, value):
        index = self.hash_function(key)
        step_size = self.secondary_hash_function(key)
        retries = 0
        while retries < self.size:
            if self.table[index] is None:
                self.table[index] = (key, value)
                return
            elif self.table[index][0] == key:
                self.table[index] = (key, self.table[index][1] + value)
                return
            index = (index + step_size) % self.size
            retries += 1
        self.resize_table(self.size * 2)
        # Insert a key-value pair using double hashing with resizing

    def search(self, key):
        index = self.hash_function(key)
        step_size = self.secondary_hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + step_size) % self.size
        return 0
        # Search for a key and return its value (0 if not found)

    def delete(self, key):
        index = self.hash_function(key)
        step_size = self.secondary_hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + step_size) % self.size
        # Delete a key from the hash table

    def populate_hash_table(self):
        with open(self.file, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    word = word.lower()
                    self.insert(word, 1)
        # Populate the hash table with words from the input file

    def resize_table(self, new_size):
        new_table = [None] * new_size
        for entry in self.table:
            if entry is not None:
                key, value = entry
                index = self.hash_function(key)
                step_size = self.secondary_hash_function(key)
                retries = 0
                while retries < new_size:
                    if new_table[index] is None:
                        new_table[index] = (key, value)
                        break
                    index = (index + step_size) % new_size
                    retries += 1
        self.size = new_size
        self.table = new_table
        # Resize the hash table and rehash existing entries


# In[47]:


def count_word_occurrences3(file_path):
    word_count = HashTableDoubleHash(100000, file_path) # size = 100000 for good result
    

    for entry in word_count.table:
        if entry is not None:
            key, value = entry
            print(f'{key.capitalize()} {value}')
    # Output the word occurrences to the console

    word_count.save_to_file('DoubleHashing.txt')
    # Save the hash table to an output file

if __name__ == '__main__':
    text_file = 'dictionary.txt' 
    count_word_occurrences3(text_file)

