class Pizza:

    r = 0
    c = 0
    l = 0
    h = 0
    cells  = []



    def __init__(self,rows,cols,l,h,table):
        self.r = rows
        self.c = cols
        self.l = l
        self.h = h
        self.cells = table

    def print_table(self):
        print ("cells:")
        for i in range(0,len(self.cells)):
            for j in range(0,len(self.cells[i])):
                print (self.cells[i][j])

    def print_pizza(self):
        print ("r " + self.r+ "\tc " + self.c + "\tL "+self.l + "\tH "+self.h )
        self.print_table()
