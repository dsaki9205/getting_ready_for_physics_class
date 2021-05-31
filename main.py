train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


#task 1
def f_to_c(f_temp):
  return(f_temp - 32)* 5/9
 
#task 2
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

#task 3
def c_to_f(c_temp):
  return (c_temp * 9/5) + 32

#task 4
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

#task 5
def get_force (mass, acceleration):
  return mass * acceleration

#task 6
train_force = get_force(train_mass, train_acceleration)
#task 7
print("The GE train supplies " + str(train_force) +  " Newtons of force.")

#task 8
def get_energy(mass, c=3*10**8):
  return mass * c **2

# task 9
bomb_energy = get_energy(bomb_mass)

#task 10
print("A 1kg bomb supplies " + str(bomb_energy) + " joules")

#task 11
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

#task 12
train_work = get_work(train_mass, train_acceleration, train_distance)
#task 13
print("The GE train does " + str(train_work) +  " Joules of work over " + str(train_distance) + " meters.")