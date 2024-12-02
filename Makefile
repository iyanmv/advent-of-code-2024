CFLAGS  = -Wall -Wextra -Wpedantic
CFLAGS += -O3

.PHONY: all day01 day02
all: day01 day02

day01: solutions/day01/part1 solutions/day01/part2
	python solutions/day01/part1.py
	python solutions/day01/part2.py
	cd solutions/day01 && ./part1 && ./part2

day02:
	python solutions/day02/part1.py
	python solutions/day02/part2.py

solutions/day01/part1: solutions/day01/part1.c
	$(CC) $(CFLAGS) -o $@ $^

solutions/day01/part2: solutions/day01/part2.c
	$(CC) $(CFLAGS) -o $@ $^


.PHONY: clean
clean:
	$(RM) solutions/day01/part{1,2}