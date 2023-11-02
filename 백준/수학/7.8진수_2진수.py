number = input()
oct_numbers = {
  0: '000',
  1: '001',
  2: '010',
  3: '011',
  4: '100',
  5: '101',
  6: '110',
  7: '111'
}
bin_result = []

for i in number:
  bin_result.append(oct_numbers[int(i)])

result = list(''.join(bin_result))
while result and result[0] == '0':
  result.pop(0)

if result:
  print(''.join(result))
else:
  print(0)