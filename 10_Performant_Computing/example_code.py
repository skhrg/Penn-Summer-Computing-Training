# collate values by id

first_values = []
first_ids = []
second_values = []
second_ids = []

with open("input_0.txt", "r") as handle:
    for line in handle.readlines():
        num, id = line.strip().split(" ")

        first_values.append(float(num))
        first_ids.append(int(id))

with open("input_1.txt", "r") as handle:
    for line in handle.readlines():
        num, id = line.strip().split(" ")

        second_values.append(float(num))
        second_ids.append(int(id))

diffs = []
for value, id in zip(first_values, first_ids):
    for s_value, s_id in zip(second_values, second_ids):
        if s_id == id:
            diffs.append(abs(value - s_value))

print('Difference between codes')
print(sum(diffs))
