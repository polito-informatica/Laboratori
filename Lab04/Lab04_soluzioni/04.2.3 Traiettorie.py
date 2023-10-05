# Esercizio 04.2.3
# Traiettorie

#  Simulate the motion of a projectile.
#

# Define constant variables.
DELTA_T = 0.01

# Read the initial velocity from the user.
v = float(input("Enter the initial velocity: "))
v0 = v

count = 1  # number of computation steps
s = v * DELTA_T
while s > 0:  # While the canon ball hasn't returned to the ground.
    # Display the position and velocity every second.
    if count % 100 == 0:  # print only every 100 steps
        t = count // 100
        exact = -0.5 * 9.81 * t * t + v0 * t
        print(f"At time {t} position is {s:.2f} and velocity is {v:.2f}. (Exact formula position is {exact:.2f})")

    # Update the position and velocity.
    s = s + v * DELTA_T
    v = v - 9.81 * DELTA_T
    count = count + 1
