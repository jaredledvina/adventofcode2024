#!/usr/bin/env python3
"""
Advent of Code - Day 2
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
    >>> part1(['7 6 4 2 1', '1 2 7 8 9', '9 7 6 2 1', '1 3 2 4 5', '8 6 4 4 1', '1 3 6 7 9'])
    2
    """
    total_safe = 0
    for report in puzzle_input:
        levels = [int(level) for level in report.split(' ')]
        safe = False
        ascending = all(l1 > l2 for l1, l2, in zip(levels, levels[1:]))
        descending = all(l1 < l2 for l1, l2, in zip(levels, levels[1:]))
        if ascending or descending:
            for index, level in enumerate(levels):
                if index+1 < len(levels):
                    if 0 < abs(level-levels[index+1]) < 4:
                        safe = True
                    else:
                        safe = False
                        break
        if safe:
            total_safe += 1

    return total_safe

def check_safe(levels):
    ascending = all(l1 > l2 for l1, l2, in zip(levels, levels[1:]))
    descending = all(l1 < l2 for l1, l2, in zip(levels, levels[1:]))
    safe = False
    if ascending or descending:
        for index, level in enumerate(levels):
            if index+1 < len(levels):
                if 0 < abs(level-levels[index+1]) < 4:
                    safe = True
                else:
                    safe = False
                    break
    return safe

def part2(puzzle_input):
    """
    >>> part2(['7 6 4 2 1', '1 2 7 8 9', '9 7 6 2 1', '1 3 2 4 5', '8 6 4 4 1', '1 3 6 7 9'])
    4
    """
    total_safe = 0
    for report in puzzle_input:
        levels = [int(level) for level in report.split(' ')]
        if not check_safe(levels):
            for index, level in enumerate(levels):
                reduced_levels = levels[:index] + levels[index+1:]
                if check_safe(reduced_levels):
                    total_safe += 1
                    break
        else:
            total_safe += 1
    return total_safe


def main():
    """
    Do eet
    """
    puzzle_input = read_input()
    print(part1(puzzle_input))
    print(part2(puzzle_input))


if __name__ == '__main__':
    main()
