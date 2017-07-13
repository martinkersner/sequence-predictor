#!/usr/bin/env python

# Martin Kersner, m.kersner@gmail.com
# 2017/07/13
# https://plus.maths.org/content/mathematical-mysteries-hailstone-sequences

class Hailstone:
    def __init__(self, start_num):
        self.start_num = start_num
        self.hailstone_lst = [self.start_num]

    def converged(self):
        return self.hailstone_lst[-4:] == [1,4,2,1]

    def generate_sequence(self):
        current_num = self.start_num

        while True:
            if current_num % 2 == 0:
                current_num /= 2
            else:
                current_num = (3*current_num) + 1

            self.hailstone_lst.append(current_num)

            if self.converged():
                return self.hailstone_lst
