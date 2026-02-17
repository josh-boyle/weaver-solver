# Weaver Word Ladder Solver

A Python implementation of a word ladder solver using Breadth-First Search (BFS) to compute the shortest transformation path between two valid dictionary words.

Inspired by the https://wordwormdormdork.com/weaver/

## Problem

Given a start word and an end word of equal length, transform the start word into the end word by changing one letter at a time. Each intermediate word must exist in the dictionary. Goal is to find a path with the least number of steps

Variant: Weaver X is a variant that also allows adding or subtracting 1 letter.

## Approach

- Construct implicit graph of valid dictionary words
- Use Breadth-First Search (BFS) to explore transformations
- Track parent relationships to reconstruct shortest path


## Example

Input:
python solve.py -s love -e hate

Output:
love → hove → have → hate

additionally flag --bidir or -b for bidirectional bfs
## Future Improvements

- Expose as web interface
- Change dictionary to better align with weaver dictionary
