CFLAGS  = -Wall -Wextra -Wpedantic
CFLAGS += -O3

.PHONY: all day01 day02 day03 day04 day05 day06 day07 day08 day09 day10 day11 day12 day13 day14 day15 day16 day17 day18 day19
all: day01 day02 day03 day04 day05 day06 day07 day08 day09 day10 day11 day12 day13 day14 day15 day16 day17 day18 day19

day01: solutions/day01/part1 solutions/day01/part2
	python solutions/day01/part1.py
	python solutions/day01/part2.py
	cd solutions/day01 && ./part1 && ./part2

day02:
	python solutions/day02/part1.py
	python solutions/day02/part2.py

day03:
	python solutions/day03/part1.py
	python solutions/day03/part2.py

day04:
	python solutions/day04/part1.py
	python solutions/day04/part2.py

day05:
	python solutions/day05/part1.py
	python solutions/day05/part2.py

day06:
	python solutions/day06/part1.py
	python solutions/day06/part2.py

day07:
	python solutions/day07/part1.py
	python solutions/day07/part2.py

day08:
	python solutions/day08/part1.py
	python solutions/day08/part2.py

day09:
	python solutions/day09/part1.py
	python solutions/day09/part2.py

day10:
	python solutions/day10/part1.py
	python solutions/day10/part2.py

day11:
	python solutions/day11/part1.py
	python solutions/day11/part2.py

day12:
	python solutions/day12/part1.py
	python solutions/day12/part2.py

day13:
	python solutions/day13/part1.py
	python solutions/day13/part2.py

day14:
	python solutions/day14/part1.py
	python solutions/day14/part2.py

day15:
	python solutions/day15/part1.py
	python solutions/day15/part2.py

day16:
	python solutions/day16/part1.py
	python solutions/day16/part2.py

day17:
	python solutions/day17/part1.py
	python solutions/day17/part2.py

day18:
	python solutions/day18/part1.py
	python solutions/day18/part2.py

day19:
	python solutions/day19/part1.py
	python solutions/day19/part2.py

solutions/day01/part1: solutions/day01/part1.c
	$(CC) $(CFLAGS) -o $@ $^

solutions/day01/part2: solutions/day01/part2.c
	$(CC) $(CFLAGS) -o $@ $^


.PHONY: clean
clean:
	$(RM) solutions/day01/part{1,2}
