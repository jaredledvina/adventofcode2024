#!/usr/bin/env python3
"""
Advent of Code - Day 1
"""
import os

def read_input():
    """
    Reads the puzzle input
    """
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path, encoding='utf-8') as input_file:
        puzzle_input = input_file.read().splitlines()
    return puzzle_input


def part1(puzzle_input):
    """
    >>> part1(['3   4', '4   3', '2   5', '1   3', '3   9', '3   3'])
    11
    """
    total_distance = 0
    column_a = []
    column_b = []
    for line in puzzle_input:
        columns = line.split('   ')
        column_a.append(int(columns[0]))
        column_b.append(int(columns[1]))
    column_a = sorted(column_a)
    column_b = sorted(column_b)
    for pair in zip(column_a, column_b):
        total_distance += abs(pair[0] - pair[1])
    return total_distance


def part2(puzzle_input):
    """
    >>> part2(['3   4', '4   3', '2   5', '1   3', '3   9', '3   3'])
    31
    """
    similarity_score = 0
    column_a = []
    column_b = []
    for line in puzzle_input:
        columns = line.split('   ')
        column_a.append(int(columns[0]))
        column_b.append(int(columns[1]))
    for entry in column_a:
        appearances = column_b.count(entry)
        similarity_score += entry * appearances

    return similarity_score

def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == '__main__':
    main()
