#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 18:51:22 2024

@author: hannahcorenblum
"""



def calculate_variance(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    squared_diff = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_diff) / n
    return variance

def main():
    numbers = []
    for i in range(1, 6):
        number = float(input(f"number {i}: "))
        numbers.append(number)

    variance = calculate_variance(numbers)
    print(f"The variance of {numbers} is {variance:.2f}")

if __name__ == "__main__":
    print("Enter 5 numbers:")
    main()
