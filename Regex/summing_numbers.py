# Title: Summing Numbers

# Write a procedure called sumnums(). Your procedure must accept as input a
# single string. Your procedure must output an integer equal to the sum of
# all integer numbers (one or more digits in sequence) within that string.
# If there are no decimal numbers in the input string, your procedure must
# return the integer 0. The input string will not contain any negative integers.
#
# Example Input: "hello 2 all of you 44"
# Example Output: 46
#
# Hint: int("44") == 44

import re


def get_sum(nums):
    sum = 0
    for i in nums:
        sum += int(i)
    return sum


def get_nums_by_regex(sentence):
    r = r'\d+'
    nums = re.findall(r, sentence)
    return nums


def sumnums(sentence):
    s = sentence
    nums = get_nums_by_regex(s)
    sum = get_sum(nums)
    return sum


# This problem includes an example test case to help you tell if you are on
# the right track. You may want to make your own additional tests as well.

test_case_input = """The Act of Independence of Lithuania was signed 
on February 16, 1918, by 20 council members."""

test_case_output = 1954

if sumnums(test_case_input) == test_case_output:
    print("Test case passed.")
else:
    print("Test case failed:")
    print(sumnums(test_case_input))
