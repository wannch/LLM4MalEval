def greet_user(name):
  print(f"Hello, {name}!")
def check_even_odd(number):
  if number%2==0:
    return "even"
  else:
    return "odd"
def main():
  user_name="Alice"
  greet_user(user_name)
  numbers=[1,2,3,4,5]
  for num in numbers:
    result=check_even_odd(num)
    print(f"The number {num} is {result}.")
if __name__=="__main__":
  main()