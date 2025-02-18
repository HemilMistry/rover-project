# The inputs for the rover will be captured via a text file which is found attached labelled "roverinput.txt"
fileName = "roverinput.txt"

# Movement class for the rover
class Movement:
    def __init__(self):
        self.max_x = 0
        self.max_y = 0

    def deploy(self, fileName):
        with open(fileName) as file:
            # Counting the number of rovers which will be deployed
            rovers = len(file.readlines()) // 2
            file.seek(0)
            file.readline()
            # Loops through all the rovers which have been assigned
            for i in range(rovers):
                # String manipulation to obtain the initial rover position and the commands it has to follow
                initial_pos = file.readline().rstrip()
                movement_commands = file.readline().strip()

                initial_pos_list = initial_pos.split(" ")
                # Assigns the initial position as x and y and direction values
                x = initial_pos_list[0]
                y = initial_pos_list[1]
                direction  = initial_pos_list[2]
                
                # Sets up each rover as a class and will process each rover one at a time
                rover = Rover(int(x), int(y), direction)
                rover.initialiseMax(fileName)
                for j in movement_commands:
                    rover.update_position(j)    
                rover.print_rover_values(i+1)
                

# Rover class to initialise the rover
class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    # Defines the maximum space available
    def initialiseMax(self, fileName):
        with open(fileName) as file:
        # Process for splitting the max coordinate values
            max = file.readline().rstrip()
            maxsplit = max.split(" ")
            self.max_x = maxsplit[0]
            self.max_y = maxsplit[1]
        
    
    def update_position(self, command):
        # Selection to go through all of the commands which are applied to the rover
        if command == "M":
            if self.direction == "N":
                if self.y > int(self.max_y):
                    self.y = self.max_y
                else:
                    self.y += 1
            elif self.direction == "E":
                if self.x > int(self.max_x):
                    self.x = self.max_x
                else:
                    self.x += 1
            elif self.direction == "S":
                if self.y > int(self.max_y):
                    self.y = self.max_y
                else:
                    self.y -= 1
            elif self.direction == "W":
                if self.x > int(self.max_x):
                    self.x = self.max_x
                else:
                    self.x -= 1
        elif command == "L":
            if self.direction == "N":
                self.direction = "W"
            elif self.direction == "W":
                self.direction = "S"
            elif self.direction == "S":
                self.direction = "E"
            elif self.direction == "E":
                self.direction = "N"
        elif command == "R":
            if self.direction == "N":
                self.direction = "E"
            elif self.direction == "W":
                self.direction = "N"
            elif self.direction == "S":
                self.direction = "W"
            elif self.direction == "E":
                self.direction = "S"

    # Printed out values of each rover's final position
    def print_rover_values(self, rover_val):
        print(self.x, self.y, self.direction)


c = Movement()
c.deploy(fileName)

