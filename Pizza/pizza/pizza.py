class Pizza:

    rows = 0
    cols = 0
    l = 0
    h = 0
    table  = []



    def __init__(self,rows,cols,l,h,table):
        self.rows = rows
        self.cols = cols
        self.l = l
        self.h = h
        self.table = table

    def print_pizza(self):
        print ("Rows " + self.rows+ "\tCols " + self.cols + "\tL "+self.l + "\t H "+self.h )
