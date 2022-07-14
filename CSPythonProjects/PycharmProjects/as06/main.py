"""
1. Load in dictionary as a list all uppercase and sorted alphabetically
2. iterate through each character in grid checking the strings in all directions
    a. each string will then be searched for in dictionary list using binary search
    b. added to a new list if found
3. alphabetize list
5. return list
"""
import sys
import time

def word_frags(word):
    """
    returns all possible fragments within the given string
    """
    if len(word) >= min_len:
        for i in range(min_len, len(word) + 1):
            if spell_check(word[0:i]):
                final.append(word[0:i])


def spell_check(word):
    """
    returns true if given word is in loaded dictionary
    """
    low = 0
    high = len(real_words1) - 1
    while low <= high:
        mid = (low + high) // 2
        if real_words1[mid] == word:
            return True
        elif real_words1[mid] > word:
            high = mid - 1
        else:
            low = mid + 1
    return False

tic = time.perf_counter()
grid = open('/Users/bridg3r/PycharmProjects/as06/test_grid')
grid = grid.readlines()
grid = [x.strip().upper() for x in grid]
min_len = 5 # int(sys.argv[1])
path_file = '/Users/bridg3r/Desktop/wordlist.10000.txt'  # sys.argv[2]
real_words0 = open(path_file)
real_words1 = real_words0.readlines()
real_words1 = [x.strip().upper() for x in real_words1]  # if is character
real_words1.sort()
grid_n = len(grid)
final = []
for row, letters in enumerate(grid):
    for column, letter in enumerate(letters):
        east = letters[column:grid_n]  # EAST
        word_frags(east)
        west = letters[column::-1]  # WEST
        word_frags(west)
        if len(west) >= min_len:
            for i in range(min_len, len(west)+1):
                if spell_check(west[0:i]):
                    final.append(west[0:i])
        north = ''
        for i in range(row, -1, -1):  # NORTH
            north += grid[i][column]
        word_frags(north)
        south = ''
        for i in range(row, grid_n):  # SOUTH
            south += grid[i][column]
        word_frags(south)
        northeast = ''  # NORTHEAST
        j = row
        i = column
        while j > -1 and i < grid_n:
            northeast += grid[j][i]
            i += 1
            j -= 1
        word_frags(northeast)
        northwest = ''  # NORTHWEST
        j = row
        i = column
        while j > -1 and i > -1:
            northwest += grid[j][i]
            i -= 1
            j -= 1
        word_frags(northwest)
        southeast = ''  # SOUTHEAST
        j = row
        i = column
        while j < grid_n and i < grid_n:
            southeast += grid[j][i]
            j += 1
            i += 1
        word_frags(southeast)
        southwest = ''  #SOUTHWEST
        j = row
        i = column
        while j < grid_n and i > -1:
            southwest += grid[j][i]
            i -= 1
            j += 1
        word_frags(southwest)
final.sort()
for index, items in enumerate(final):
    if index == 0 or items != final[index-1]:
        print(items)
toc = time.perf_counter()
print(toc-tic)