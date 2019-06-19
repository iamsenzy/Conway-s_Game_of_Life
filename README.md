# Conway-s Game of Life
Conway's Game of Life

## Usage

```python
#Make a 30x30 table, r is for fill random nums
g = GameOfLife(30,30,r=False) 

#You can load patterns from lif_files library
g.loadPattern("pulsar")

#2 parameters is the x and y coordinate where to place
g.loadPattern("glider",10,10) #TODO it can be out of range
```

## Link
[Wiki](https://en.wikipedia.org/wiki/Conway's_Game_of_Life)
