# README for Word Counting Hash Tables

This repository contains Python code for three different implementations of hash tables for word counting from a text file. Each implementation has a different collision resolution strategy, and they are implemented in separate classes:

1. **HashTableChain**:
    - This class uses a chaining approach for collision resolution.
    - The hash table is an array of lists, and collisions are resolved by appending elements with the same hash key to the corresponding list.
    - The key-value pairs are stored as tuples in the lists.

2. **HashTableLinProb**:
    - This class uses linear probing for collision resolution.
    - The hash table is a one-dimensional array.
    - When a collision occurs, the algorithm searches for the next available slot by linearly probing through the table.

3. **HashTableDoubleHash**:
    - This class uses double hashing for collision resolution.
    - It combines a primary hash function with a secondary hash function to determine the index for a given key.
    - If a collision occurs, the algorithm calculates a new index using the secondary hash function and steps through the table until an empty slot is found.

## How to Use

The code includes three main functions that demonstrate the usage of these hash tables:

1. **count_word_occurrences1(file_path)**:
    - This function demonstrates the use of the `HashTableChain` class.
    - It counts word occurrences from a text file specified by `file_path` and outputs the results to the console.
    - It also saves the results to a file named "Chaining.txt."

2. **count_word_occurrences2(file_path)**:
    - This function demonstrates the use of the `HashTableLinProb` class.
    - It counts word occurrences from a text file specified by `file_path` and outputs the results to the console.
    - It also saves the results to a file named "Probing.txt."

3. **count_word_occurrences3(file_path)**:
    - This function demonstrates the use of the `HashTableDoubleHash` class.
    - It counts word occurrences from a text file specified by `file_path` and outputs the results to the console.
    - It also saves the results to a file named "DoubleHashing.txt."

Before running any of these functions, make sure to replace the `text_file` variable with the path to your input text file.

## How the Code Works

1. **Initialization**:
    - Each hash table is initialized with a specified size and the path to the input text file.
    - The size determines the capacity of the hash table.

2. **Populating the Hash Table**:
    - The hash tables are populated with words from the input text file.
    - Words are converted to lowercase to ensure case-insensitive word counting.

3. **Insertion, Search, and Deletion**:
    - The hash tables support the insertion of key-value pairs (word-count pairs), searching for a word, and deleting a word.

4. **Collision Resolution**:
    - Each hash table implements a different collision resolution strategy: chaining, linear probing, or double hashing.

5. **Resizing**:
    - When the load factor (the ratio of elements to table size) exceeds a certain threshold (e.g., 80%), the hash table is resized to prevent performance degradation.

6. **Output**:
    - After processing the input text file, the code outputs the word occurrences to the console and saves them to an output file.

Feel free to use and modify this code for your own purposes, and don't forget to replace `text_file` with the path to your input text file.