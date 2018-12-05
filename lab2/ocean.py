#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


class Ocean:

    def __init__(self, init_state):
        self.init_state = init_state
        self.len = len(init_state)
        self.state = []
        self.state.append([1, 1, 1, 1, 1, 1, 1])
        for elem in self.init_state:
            elem.insert(0, 1)
            elem.append(1)
            self.state.append(elem)
        self.state.append([1, 1, 1, 1, 1, 1, 1])

    def __str__(self):
        return '\n'.join(otvet)

    def gen_next_quantum(self):
        def count_fs(self, r, c):
            fishes = 0
            shrimps = 0
            if self.state[r-1][c-1] == 2:
                fishes += 1
            elif self.state[r-1][c-1] == 3:
                shrimps += 1
            if self.state[r-1][c] == 2:
                fishes += 1
            elif self.state[r-1][c] == 3:
                shrimps += 1
            if self.state[r-1][c+1] == 2:
                fishes += 1
            elif self.state[r-1][c+1] == 3:
                shrimps += 1
            if self.state[r][c-1] == 2:
                fishes += 1
            elif self.state[r][c-1] == 3:
                shrimps += 1
            if self.state[r][c+1] == 2:
                fishes += 1
            elif self.state[r][c+1] == 3:
                shrimps += 1
            if self.state[r+1][c-1] == 2:
                fishes += 1
            elif self.state[r+1][c-1] == 3:
                shrimps += 1
            if self.state[r+1][c] == 2:
                fishes += 1
            elif self.state[r+1][c] == 3:
                shrimps += 1
            if self.state[r+1][c+1] == 2:
                fishes += 1
            elif self.state[r+1][c+1] == 3:
                shrimps += 1
            return [fishes, shrimps]

        new_state = [0] * self.len
        for i in range(self.len):
            new_state[i] = [0] * self.len
        for raw in range(1, len(self.state) - 1):
            for c in range(1, len(self.state) - 1):
                if self.state[raw][c] == 1:
                    new_state[raw - 1][c - 1] = 1
                elif self.state[raw][c] == 2:
                    if count_fs(self, raw, c)[0] == 2 or \
                            count_fs(self, raw, c)[0] == 3:
                        new_state[raw - 1][c - 1] = 2
                    if count_fs(self, raw, c)[0] <= 1 or \
                            count_fs(self, raw, c)[0] >= 4:
                        new_state[raw - 1][c - 1] = 0
                elif self.state[raw][c] == 3:
                    if count_fs(self, raw, c)[1] == 2 or \
                            count_fs(self, raw, c)[1] == 3:
                        new_state[raw - 1][c - 1] = 3
                    if count_fs(self, raw, c)[1] <= 1 or \
                            count_fs(self, raw, c)[1] >= 4:
                        new_state[raw - 1][c - 1] = 0
                elif self.state[raw][c] == 0:
                    if count_fs(self, raw, c)[1] == 3:
                        new_state[raw - 1][c - 1] = 3
                    if count_fs(self, raw, c)[0] == 3:
                        new_state[raw - 1][c - 1] = 2
        otvet = []
        for raw in new_state:
            t = ' '.join([str(item) for item in raw])
            otvet.append(t)
        return '\n'.join(otvet)


if __name__ == '__main__':
    n_quantums = int(sys.stdin.readline())
    n_rows, n_clms = [int(i) for i in sys.stdin.readline().split()]
    init_state = []
    for i in range(n_rows):
        line = [int(i) for i in sys.stdin.readline().split()]
        init_state.append(line)

    ocean = Ocean(init_state=init_state)
    for _ in range(n_quantums):
        ocean = ocean.gen_next_quantum()
    print(ocean)
