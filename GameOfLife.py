import random
from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class GameOfLife:
    def __init__(self, cols, rows, r = False):
        self.grid = [[0] * rows for i in range(cols)]
        self.cols, self.rows = cols, rows
        if r :
            self.fillRandom()
        self.next = [[0] * rows for i in range(cols)]
        self.alive, self.born = self.rules('#R 23/3')
        self.countGeneration = 0
        self.patterns = self.importPatterns()

    def fillRandom(self):
        for i in range(self.cols):
            for j in range(self.rows):
                self.grid[i][j] = random.randint(0, 1)

    def rules(self,model):
        if model[0] == '#' and (model[1] == 'R'):
            alive, born = [], []
            l = True
            for i in model[3:]:
                if i == '/':
                    l = False
                if l:
                    alive.append(int(i))
                else:
                    if i != '/':
                        born.append(int(i))
            return (alive,born)
        else:
            return ([2,3],[3])

    def changePoint(self,rules,point,neighbros):
        alive, born = rules
        if point == 0 and neighbros in born:
            return 1
        elif point == 1 and neighbros not in alive:
            return 0
        else:
            return point

    def countNeighbros(self,x,y):
        count = 0
        for i in range(-1,2):
            for j in range(-1,2):
                col = (x + i + self.cols) % self.cols
                row = (y + j + self.rows) % self.rows
                count += self.grid[col][row]
        count -= self.grid[x][y]
        return count

    def update(self):
        self.countGeneration += 1
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                point = self.grid[i][j]
                neighbros = self.countNeighbros(i,j)
                self.next[i][j] = self.changePoint((self.alive,self.born),point,neighbros)

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j] = self.next[i][j]


    def loadPattern(self, patternName, newx=42, newy=42):
        try:
            f = open('lif_files/'+patternName+'.lif', "r")
            centerx , centery = (int(self.cols/2),int(self.rows/2))
            havePos = False
            for x in f:
                if x[0] == '#' and (x[1] == 'R' or x[1] == 'N'):
                    self.alive, self.born = self.rules(x)

                if x[0] == '#' and x[1] == 'P':
                    xpos, ypos = [int(i) for i in x[2:].split()]
                    havePos = True
                    j = 0
                    continue

                if havePos:
                    for index, val in enumerate(x):
                        if centerx + xpos + j >= self.cols or centery + ypos + index >= self.rows:
                            print("Table size too small")

                        if (newx == 42 and newy == 42) :
                            if val == '.':
                                self.grid[centerx + xpos + j][centery + ypos + index] = 0
                            elif val == '*':
                                self.grid[centerx + xpos + j][centery + ypos + index] = 1
                        else:
                            if val == '.':
                                self.grid[newx + j][newy + index] = 0
                            elif val == '*':
                                self.grid[newx + j][newy + index] = 1
                    j += 1


            return True
        except:
            print("Something went wrong when load a pattern")
            return False

    def importPatterns(self):
        patterns = []
        try:
            f = open('lif_files/patterns.txt', "r")
            for x in f:
                patterns.append(x.rstrip())
            return patterns
        except:
            print("File not found.")


    def print(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j]==1:
                    print('X ',end='')
                else:
                    print('  ', end='')
            print('')
        print('')

if __name__ == '__main__':
    g = GameOfLife(30,30,r=False)
    #g.loadPattern("pulsar")
    #g.loadPattern("glider")
    str = ''
    if g.loadPattern(g.patterns[12]):
        while str != 'x' :
            clear()
            g.print()
            print('Generation: ', g.countGeneration)
            print('Press S to start automat. Press D for next generation. Press X for quit')
            str = input()
            if str == 's':
                loop = True
                try:
                    while loop:
                        clear()
                        g.print()
                        print('Press Ctrl + c to stop')
                        print('Generation: ',g.countGeneration)
                        g.update()
                        sleep(0.1)
                except KeyboardInterrupt:
                    loop = False
            elif str == 'd':
                clear()
                g.update()
                g.print()




