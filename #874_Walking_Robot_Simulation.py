import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


commands = [4,-1,4,-2,4,-2,5,-1,2,-3,7,-2,8]
obstacles = [[2,4],[-4,11]]


directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
curDirection = 0
start = [0, 0]
maxDistance = 0
path = [[0, 0]]

for command in commands:
    if command < 0:
        if command == -1:
            curDirection = (curDirection + 1) % 4
        elif command == -2:
            curDirection = (curDirection - 1) % 4
    else:
        while command:
            if directions[curDirection][0] == 0:
                if [start[0], start[1] + directions[curDirection][1]] in obstacles:
                    command = 1
                else:
                    start[1] += directions[curDirection][1]
            elif directions[curDirection][1] == 0:
                if [start[0] + directions[curDirection][0], start[1]] in obstacles:
                    command = 1
                else:
                    start[0] += directions[curDirection][0]
            command -= 1
            if start[0] ** 2 + start[1] ** 2 > maxDistance:
                maxDistance = start[0] ** 2 + start[1] ** 2
            path.append(start.copy())

# Extract the obstacles from the wrapper instance
x_obs = [coordinate[0] for coordinate in obstacles]
y_obs = [coordinate[1] for coordinate in obstacles]

x_path = [coordinate[0] for coordinate in path]
y_path = [coordinate[1] for coordinate in path]

fig, ax = plt.subplots()

# Set the limits based on the coordinates
min_x, max_x = min(x_path + x_obs) - 1, max(x_path + x_obs) + 1
min_y, max_y = min(y_path + y_obs) - 1, max(y_path + y_obs) + 1

plt.xlim(min_x, max_x)
plt.ylim(min_y, max_y)
ax.set(xlim=(min_x, max_x), ylim=(min_y, max_y), aspect='equal')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


# Plot the obstacles
plt.scatter(x_obs, y_obs, marker='o', c='orange', label="Obstacles")

# Plot the path
#plt.plot(x_path, y_path, marker='', c='b', label="Path")

# Mark the start and end points
plt.scatter(x_path[0], y_path[0], marker='s', c='g', label="Start")
plt.scatter(x_path[-1], y_path[-1], marker='s', c='r', label="End")

def animate(i, xs=[], ys=[]):
    xs.append(x_path[i])
    ys.append(y_path[i])
    if(x_path[i] == x_path[i-1]) and (y_path[i] == y_path[i-1]):
        plt.plot(xs, ys, c="r")
    else:
        plt.plot(xs, ys,c="b")


ani = FuncAnimation(fig, animate, interval=700)

plt.grid()
plt.legend()
plt.show()
