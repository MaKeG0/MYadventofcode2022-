"""
--- Day 1: Calorie Counting ---
--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""
elf:int=0
sum_cal:int=0
three_elves:list[int]=[0,0,0]
three_max_cal :list[int]=[0,1,2]
with open ("calories.txt", "r") as calories_list:
    for calories in calories_list:
        if calories == "\n":
            min_cal=min(three_max_cal)
            if sum_cal>min_cal:
                for index, max_cal in enumerate(three_max_cal):
                    if min_cal==max_cal:
                        three_max_cal[index]=sum_cal
                        three_elves[index]=elf
            elf+=1
            sum_cal=0
        else:
            sum_cal+=int(calories)
tot=0
for max_cal in three_max_cal:
    tot+=max_cal

print(f"The elfs with the most calories are n: {three_elves} with a total of {tot} calories.")