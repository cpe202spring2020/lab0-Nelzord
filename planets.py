def weight_on_planets():
   # write your code here
   x = int(input("What do you weigh on earth?"))
   m, j = x * .38, x * 2.34
   print("\nOn Mars you would weigh " + str(m) + " pounds." + "\nOn Jupiter you would weigh " + str(j) + " pounds.")


if __name__ == '__main__':
   weight_on_planets()