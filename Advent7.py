import statistics

positions = [16,1,2,0,4,2,7,1,2,14]

mean = int(statistics.mean(positions))
median = statistics.median(positions)

part1_fuel = sum(abs(x - median) for x in positions)

def fuel_usage(position, ideal):
    difference = abs(position - ideal)
    fuel_used = sum(1+x for x in range(difference))
    return fuel_used

part2_fuel = sum(fuel_usage(x, mean) for x in positions)

print(part1_fuel)
print(part2_fuel)









