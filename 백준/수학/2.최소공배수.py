T = int(input())
result = []

def gcd(num1, num2):
  if num2 == 0:
    print(num1)
    return num1
  return gcd(num2, num1 % num2)

def lcm(num1, num2):
  return num1 * num2 / gcd(num1, num2)

for _ in range(T):
  a, b = map(int, input().split())
  result.append(int(lcm(a, b)))

for element in result:
  print(element)