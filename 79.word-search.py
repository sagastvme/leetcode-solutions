# @before-stub-for-debug-begin
from python3problem79 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=startfrom typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def find_next_letter(next_letter_index, current_row, current_col, letters_used):
            def is_row_in_bounds(row):
                return 0 <= row < len(board)
            
            def is_col_in_bounds(col):
                return 0 <= col < len(board[0])
            
            if next_letter_index == len(word):
                return True

            target_letter = word[next_letter_index]
            
            adjacent_rows = [current_row - 1, current_row + 1]
            adjacent_rows = list(filter(is_row_in_bounds, adjacent_rows))
            
            adjacent_cols = [current_col - 1, current_col + 1]
            adjacent_cols = list(filter(is_col_in_bounds, adjacent_cols))
            
            for row in adjacent_rows:
                coordinates = f"{row}:{current_col}"
                if board[row][current_col] == target_letter and coordinates not in letters_used:
                    letters_used.add(coordinates)
                    if find_next_letter(next_letter_index + 1, row, current_col, letters_used):
                        return True
                    letters_used.remove(coordinates)  # 🟢 Backtrack

            for col in adjacent_cols:
                coordinates = f"{current_row}:{col}"
                if board[current_row][col] == target_letter and coordinates not in letters_used:
                    letters_used.add(coordinates)
                    if find_next_letter(next_letter_index + 1, current_row, col, letters_used):
                        return True
                    letters_used.remove(coordinates)  # 🟢 Backtrack

            return False

        for row_index, row in enumerate(board):
            for col_index, cell_letter in enumerate(row):
                if cell_letter == word[0]:
                    coordinates = f"{row_index}:{col_index}"
                    letters_used = set()
                    letters_used.add(coordinates)
                    if find_next_letter(1, row_index, col_index, letters_used):
                        return True

        return False

  
# @lc code=end

