number = list(input())
bin_numbers = {
  '000': 0,
  '001': 1,
  '010': 2,
  '011': 3,
  '100': 4,
  '101': 5,
  '110': 6,
  '111': 7
}

while len(number) % 3 != 0:
  number.insert(0, '0')

s_numbers = ''.join(number)
oct_number = ''

for i in range(0, len(s_numbers), 3):
  oct_number += str(bin_numbers.get(s_numbers[i:i+3]))

print(oct_number)