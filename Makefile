CFLAGS  = -Wall -Wextra -Wpedantic
CFLAGS += -O3

.PHONY: all day01 day02 day03 day04 day05 day06 day07 day08 day09
all: day01 day02 day03 day04 day05 day06 day07 day08 day09

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

solutions/day01/part1: solutions/day01/part1.c
	$(CC) $(CFLAGS) -o $@ $^

solutions/day01/part2: solutions/day01/part2.c
	$(CC) $(CFLAGS) -o $@ $^


.PHONY: clean
clean:
	$(RM) solutions/day01/part{1,2}
