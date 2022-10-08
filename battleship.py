# battleship.py

import random
import turtle

class Boat():
    def __init__(self, length):
        self.length = length
        self.sunk = False
        self.ship_list = self.create_ship_list()
        self.sunk_list = self.create_sunk_list()

    def create_ship_list(self):
        ship_list = []
        for i in range(self.length):
            ship_list.append('O')
        return ship_list

    def create_sunk_list(self):
        sunk_list = []
        for i in range(self.length):
            sunk_list.append('H')
        return sunk_list

class Battleship():
    def __init__(self):
        self.l = Boat(2)
        self.m = Boat(3)
        self.n = Boat(3)
        self.o = Boat(4)
        self.p = Boat(5)
        self.q = Boat(2)
        self.r = Boat(3)
        self.s = Boat(3)
        self.t = Boat(4)
        self.u = Boat(5)
        self.screen = turtle.setup(1000, 860)
        turtle.bgcolor("lightblue")
        self.turtle1 = turtle.Turtle()
        self.turtle1.hideturtle()
        self.turtle1.speed(0)
        self.turtle1.pensize(1)
        self.grid_width = 1
        self.sq_width = 30
        self.radius = 5
        self.board_height = (self.sq_width * 22 + self.grid_width * 21 +
                            self.sq_width * 2)
        self.board_width = self.sq_width * 11 + self.grid_width * 12
        self.pos_x = self.board_width // -2
        self.pos_y = self.board_height // -2
        self.game_list_top = self.populate_game_list_top()
        self.game_list_bottom = self.populate_game_list_bottom()
        self.ship1 = 0
        self.start_row1 = 0
        self.start_column1 = 0
        self.orientation1 = 1
        self.strike1 = 1
        self.ship2 = 0
        self.start_row2 = 0
        self.start_column2 = 0
        self.orientation2 = 1
        self.strike2 = 1
        self.ship3 = 0
        self.start_row3 = 0
        self.start_column3 = 0
        self.orientation3 = 1
        self.strike3 = 1
        self.ship4 = 0
        self.start_row4 = 0
        self.start_column4 = 0
        self.orientation4 = 1
        self.strike4 = 1
        self.ship5 = 0
        self.start_row5 = 0
        self.start_column5 = 0
        self.orientation5 = 1
        self.strike5 = 1
        self.winner_player = False
        self.winner_computer = False
        
    def draw_gameboard(self):
        self.turtle1.color("green")
        self.turtle1.up()
        self.turtle1.setposition(self.pos_x, self.pos_y)
        self.turtle1.down()
        self.turtle1.left(90)
        for i in range(2):
            self.turtle1.forward(self.board_height)
            self.turtle1.right(90)
            self.turtle1.forward(self.board_width)
            self.turtle1.right(90)
        self.turtle1.right(90)
        self.turtle1.up()
        # draw horizontal lines
        row = 0
        for i in range(10):
            self.turtle1.setposition(self.pos_x + self.sq_width +
                    self.grid_width, self.pos_y + self.sq_width * (row + 1) +
                                     self.grid_width * row)
            self.turtle1.down()
            self.turtle1.forward(self.board_width - self.sq_width)
            self.turtle1.up()
            row += 1
        row = 0
        for i in range(10):
            self.turtle1.setposition(self.pos_x + self.sq_width +
                    self.grid_width, self.pos_y + self.sq_width * 13 +
                    self.grid_width * 12 + self.sq_width * (row + 1) +
                                     self.grid_width * row)
            self.turtle1.down()
            self.turtle1.forward(self.board_width - self.sq_width)
            self.turtle1.up()
            row += 1
        # draw verticle lines
        self.turtle1.left(90)
        column = 0
        for i in range(10):
            self.turtle1.setposition(self.pos_x + self.sq_width + self.sq_width
                    * column + self.grid_width * (column + 1), self.pos_y)
            self.turtle1.down()
            self.turtle1.forward(self.sq_width * 10 + self.grid_width * 10)
            self.turtle1.up()
            column += 1
        column = 0
        for i in range(10):
            self.turtle1.setposition(self.pos_x + self.sq_width + self.sq_width
                    * column + self.grid_width * (column + 1),
                    self.pos_y + self.sq_width * 13 + self.grid_width * 12)
            self.turtle1.down()
            self.turtle1.forward(self.sq_width * 10 + self.grid_width * 10)
            self.turtle1.up()
            column += 1
        # draw rectangles
        self.turtle1.fillcolor("green")
        self.turtle1.setposition(self.pos_x, self.pos_y + self.sq_width * 11 +
                                 self.grid_width * 11)
        self.turtle1.right(90)
        self.turtle1.begin_fill()
        self.turtle1.forward(self.board_width)
        self.turtle1.left(90)
        self.turtle1.forward(self.sq_width * 2)
        self.turtle1.left(90)
        self.turtle1.forward(self.board_width)
        self.turtle1.left(90)
        self.turtle1.forward(self.sq_width * 2)
        self.turtle1.left(90)
        self.turtle1.end_fill()
        self.turtle1.up()
        # draw sides
        self.turtle1.setposition(self.pos_x - self.sq_width, self.pos_y -
                                 self.sq_width)
        self.turtle1.left(90)
        self.turtle1.down()
        self.turtle1.begin_fill()
        for i in range(2):
            self.turtle1.forward(self.board_height + self.sq_width * 2)
            self.turtle1.right(90)
            self.turtle1.forward(self.sq_width)
            self.turtle1.right(90)
        self.turtle1.end_fill()
        self.turtle1.up()
        self.turtle1.right(90)
        self.turtle1.setposition(self.pos_x - self.sq_width, self.pos_y +
                                 self.board_height + self.sq_width)
        self.turtle1.down()
        self.turtle1.begin_fill()
        for i in range(2):
            self.turtle1.forward(self.board_width + self.sq_width * 2)
            self.turtle1.right(90)
            self.turtle1.forward(self.sq_width)
            self.turtle1.right(90)
        self.turtle1.end_fill()
        self.turtle1.up()
        self.turtle1.right(90)
        self.turtle1.setposition(self.pos_x + self.board_width + self.sq_width,
                                 self.pos_y + self.board_height + self.sq_width)
        self.turtle1.down()
        self.turtle1.begin_fill()
        for i in range(2):
            self.turtle1.forward(self.board_height + self.sq_width * 2)
            self.turtle1.right(90)
            self.turtle1.forward(self.sq_width)
            self.turtle1.right(90)
        self.turtle1.end_fill()
        self.turtle1.up()
        self.turtle1.right(90)
        self.turtle1.setposition(self.pos_x + self.board_width + self.sq_width,
                                 self.pos_y - self.sq_width)
        self.turtle1.down()
        self.turtle1.begin_fill()
        for i in range(2):
            self.turtle1.forward(self.board_width + self.sq_width * 2)
            self.turtle1.right(90)
            self.turtle1.forward(self.sq_width)
            self.turtle1.right(90)
        self.turtle1.end_fill()
        self.turtle1.up()
        self.turtle1.right(180)
        # draw letters
        letters = "ABCDEFGHIJ"
        self.turtle1.color("black")
        for i in range(10):
            self.turtle1.setposition(self.pos_x + self.sq_width // 2,
                    self.pos_y + self.sq_width * i +
                    self.grid_width * i)
            self.turtle1.write(letters[9 - i], align = "center",
                               font = ("Arial", 18, "bold"))
        for i in range(10):
            self.turtle1.setposition(self.pos_x + self.sq_width // 2,
                    self.pos_y + self.sq_width * 13 + self.grid_width * 11 +
                    self.sq_width * i + self.grid_width * i)
            self.turtle1.write(letters[9 - i], align = "center",
                               font = ("Arial", 18, "bold"))
        # draw numbers
        for i in range(10):
            self.turtle1.setposition(self.pos_x + self.sq_width + self.sq_width
                    // 2 + self.sq_width * i + self.grid_width * i,
                    self.pos_y + self.sq_width * 10 + self.grid_width * 10)
            self.turtle1.write(str(i + 1), align = "center",
                               font = ("Arial", 18, "bold"))
        for i in range(10):
            self.turtle1.setposition(self.pos_x + self.sq_width + self.sq_width
                    // 2 + self.sq_width * i + self.grid_width * i,
                    self.pos_y + self.sq_width * 23 + self.grid_width * 21)
            self.turtle1.write(str(i + 1), align = "center",
                               font = ("Arial", 18, "bold"))
##        # draw black circles
##        for i in range(10):
##            for j in range(10):
##                self.draw_circle_top(i + 1, j + 1, "black")
##        for i in range(10):
##            for j in range(10):
##                self.draw_circle_bottom(i + 1, j + 1, "black")

    def draw_circle_top(self, row, column, color):
        self.turtle1.color(color)
        self.turtle1.fillcolor(color)
        self.turtle1.setposition(self.pos_x + self.sq_width + self.grid_width +
                self.sq_width // 2 + self.sq_width * (column - 1) +
                self.grid_width * (column - 1), self.pos_y + self.sq_width * 13
                + self.sq_width // 2 + self.grid_width * 11
                - self.radius + self.sq_width * (10 - row) + self.grid_width *
                (10 - row))
        self.turtle1.down()
        self.turtle1.begin_fill()
        self.turtle1.circle(self.radius)
        self.turtle1.end_fill()
        self.turtle1.up()

    def draw_circle_bottom(self, row, column, color):
        self.turtle1.color(color)
        self.turtle1.fillcolor(color)
        self.turtle1.setposition(self.pos_x + self.sq_width + self.grid_width +
                self.sq_width // 2 + self.sq_width * (column - 1) +
                self.grid_width * (column - 1), self.pos_y + self.sq_width // 2
                - self.radius + self.sq_width * (10 - row) + self.grid_width *
                (10 - row))
        self.turtle1.down()
        self.turtle1.begin_fill()
        self.turtle1.circle(self.radius)
        self.turtle1.end_fill()
        self.turtle1.up()

    def draw_boat_bottom(self, ship_name, row, column, orientation):
        # orientation is int 1-4, row and column are starting points
        if orientation == 1:
            self.turtle1.setposition(self.pos_x + self.sq_width +
                    self.grid_width * 3 + self.sq_width * (column - 1) +
                    self.grid_width * (column - 1), self.pos_y + self.sq_width
                    - self.grid_width * 2 + self.sq_width * (10 - row) +
                    self.grid_width * (10 - row))
            self.turtle1.color("grey")
            self.turtle1.fillcolor("grey")
            self.turtle1.down()
            self.turtle1.begin_fill()
            for i in range(2):
                self.turtle1.forward(self.sq_width - self.grid_width * 4)
                self.turtle1.right(90)
                self.turtle1.forward(self.sq_width * ship_name.length +
                        self.grid_width * (ship_name.length - 1) -
                        self.grid_width * 4)
                self.turtle1.right(90)
            self.turtle1.end_fill()
            self.turtle1.up()
            # draw black circles
            for i in range(ship_name.length):
                self.draw_circle_bottom(row + i, column, "black")
            # add ship to game list
            self.add_ship_bottom(ship_name, row, column, orientation)
        elif orientation == 2:
            self.turtle1.setposition(self.pos_x + self.sq_width * 2 +
                    self.sq_width * (column - 1) + self.grid_width *
                    (column - 1), self.pos_y + self.sq_width -
                    self.grid_width * 2 + self.sq_width * (10 - row) +
                    self.grid_width * (10 - row))
            self.turtle1.color("grey")
            self.turtle1.fillcolor("grey")
            self.turtle1.down()
            self.turtle1.begin_fill()
            self.turtle1.right(90)
            for i in range(2):
                self.turtle1.forward(self.sq_width - self.grid_width * 4)
                self.turtle1.right(90)
                self.turtle1.forward(self.sq_width * ship_name.length +
                        self.grid_width * (ship_name.length - 1) -
                        self.grid_width * 4)
                self.turtle1.right(90)
            self.turtle1.end_fill()
            self.turtle1.left(90)
            self.turtle1.up()
            # draw black circles
            for i in range(ship_name.length):
                self.draw_circle_bottom(row, column - i, "black")
            # add ship to game list
            self.add_ship_bottom(ship_name, row, column, orientation)
        elif orientation == 3:
            self.turtle1.setposition(self.pos_x + self.sq_width * 2 +
                    self.sq_width * (column - 1) + self.grid_width *
                    (column - 1), self.pos_y + self.grid_width * 2 +
                    self.sq_width
                    * (10 - row) + self.grid_width * (10 - row))
            self.turtle1.color("grey")
            self.turtle1.fillcolor("grey")
            self.turtle1.down()
            self.turtle1.begin_fill()
            self.turtle1.right(180)
            for i in range(2):
                self.turtle1.forward(self.sq_width - self.grid_width * 4)
                self.turtle1.right(90)
                self.turtle1.forward(self.sq_width * ship_name.length +
                        self.grid_width * (ship_name.length - 1) -
                        self.grid_width * 4)
                self.turtle1.right(90)
            self.turtle1.end_fill()
            self.turtle1.left(180)
            self.turtle1.up()
            # draw black circles
            for i in range(ship_name.length):
                self.draw_circle_bottom(row - i, column, "black")
            # add ship to game list
            self.add_ship_bottom(ship_name, row, column, orientation)
        elif orientation == 4:
            self.turtle1.setposition(self.pos_x + self.sq_width +
                    self.grid_width * 3 +
                    self.sq_width * (column - 1) + self.grid_width *
                    (column - 1), self.pos_y +
                    self.grid_width * 2 + self.sq_width * (10 - row) +
                    self.grid_width * (10 - row))
            self.turtle1.color("grey")
            self.turtle1.fillcolor("grey")
            self.turtle1.down()
            self.turtle1.begin_fill()
            self.turtle1.left(90)
            for i in range(2):
                self.turtle1.forward(self.sq_width - self.grid_width * 4)
                self.turtle1.right(90)
                self.turtle1.forward(self.sq_width * ship_name.length +
                        self.grid_width * (ship_name.length - 1) -
                        self.grid_width * 4)
                self.turtle1.right(90)
            self.turtle1.end_fill()
            self.turtle1.right(90)
            self.turtle1.up()
            # draw black circles
            for i in range(ship_name.length):
                self.draw_circle_bottom(row, column + i, "black")
            # add ship to game list
            self.add_ship_bottom(ship_name, row, column, orientation)

    def draw_boat_top(self, ship_name, row, column, orientation):
        # orientation is int 1-4, row and column are starting points
        if orientation == 1:
##            self.turtle1.setposition(self.pos_x + self.sq_width +
##                    self.grid_width * 3 + self.sq_width * (column - 1) +
##                    self.grid_width * (column - 1), self.pos_y +
##                    self.sq_width * 14 + self.grid_width * 11
##                    - self.grid_width * 2 + self.sq_width * (10 - row) +
##                    self.grid_width * (10 - row))
##            self.turtle1.color("grey")
##            self.turtle1.fillcolor("grey")
##            self.turtle1.down()
##            self.turtle1.begin_fill()
##            for i in range(2):
##                self.turtle1.forward(self.sq_width - self.grid_width * 4)
##                self.turtle1.right(90)
##                self.turtle1.forward(self.sq_width * ship_name.length +
##                        self.grid_width * (ship_name.length - 1) -
##                        self.grid_width * 4)
##                self.turtle1.right(90)
##            self.turtle1.end_fill()
##            self.turtle1.up()
##            # draw black circles
##            for i in range(ship_name.length):
##                self.draw_circle_top(row + i, column, "black")
            # add ship to game list
            self.add_ship_top(ship_name, row, column, orientation)
        elif orientation == 2:
##            self.turtle1.setposition(self.pos_x + self.sq_width * 2 +
##                    self.sq_width * (column - 1) + self.grid_width *
##                    (column - 1), self.pos_y + self.sq_width * 14 +
##                    self.grid_width * 11 -
##                    self.grid_width * 2 + self.sq_width * (10 - row) +
##                    self.grid_width * (10 - row))
##            self.turtle1.color("grey")
##            self.turtle1.fillcolor("grey")
##            self.turtle1.down()
##            self.turtle1.begin_fill()
##            self.turtle1.right(90)
##            for i in range(2):
##                self.turtle1.forward(self.sq_width - self.grid_width * 4)
##                self.turtle1.right(90)
##                self.turtle1.forward(self.sq_width * ship_name.length +
##                        self.grid_width * (ship_name.length - 1) -
##                        self.grid_width * 4)
##                self.turtle1.right(90)
##            self.turtle1.end_fill()
##            self.turtle1.left(90)
##            self.turtle1.up()
##            # draw black circles
##            for i in range(ship_name.length):
##                self.draw_circle_top(row, column - i, "black")
            # add ship to game list
            self.add_ship_top(ship_name, row, column, orientation)
        elif orientation == 3:
##            self.turtle1.setposition(self.pos_x + self.sq_width * 2 +
##                    self.sq_width * (column - 1) + self.grid_width *
##                    (column - 1), self.pos_y + self.sq_width * 13 +
##                    self.grid_width * 11 + self.grid_width * 2 +
##                    self.sq_width
##                    * (10 - row) + self.grid_width * (10 - row))
##            self.turtle1.color("grey")
##            self.turtle1.fillcolor("grey")
##            self.turtle1.down()
##            self.turtle1.begin_fill()
##            self.turtle1.right(180)
##            for i in range(2):
##                self.turtle1.forward(self.sq_width - self.grid_width * 4)
##                self.turtle1.right(90)
##                self.turtle1.forward(self.sq_width * ship_name.length +
##                        self.grid_width * (ship_name.length - 1) -
##                        self.grid_width * 4)
##                self.turtle1.right(90)
##            self.turtle1.end_fill()
##            self.turtle1.left(180)
##            self.turtle1.up()
##            # draw black circles
##            for i in range(ship_name.length):
##                self.draw_circle_top(row - i, column, "black")
            # add ship to game list
            self.add_ship_top(ship_name, row, column, orientation)
        elif orientation == 4:
##            self.turtle1.setposition(self.pos_x + self.sq_width +
##                    self.grid_width * 3 +
##                    self.sq_width * (column - 1) + self.grid_width *
##                    (column - 1), self.pos_y + self.sq_width * 13 +
##                    self.grid_width * 11 +
##                    self.grid_width * 2 + self.sq_width * (10 - row) +
##                    self.grid_width * (10 - row))
##            self.turtle1.color("grey")
##            self.turtle1.fillcolor("grey")
##            self.turtle1.down()
##            self.turtle1.begin_fill()
##            self.turtle1.left(90)
##            for i in range(2):
##                self.turtle1.forward(self.sq_width - self.grid_width * 4)
##                self.turtle1.right(90)
##                self.turtle1.forward(self.sq_width * ship_name.length +
##                        self.grid_width * (ship_name.length - 1) -
##                        self.grid_width * 4)
##                self.turtle1.right(90)
##            self.turtle1.end_fill()
##            self.turtle1.right(90)
##            self.turtle1.up()
##            # draw black circles
##            for i in range(ship_name.length):
##                self.draw_circle_top(row, column + i, "black")
            # add ship to game list
            self.add_ship_top(ship_name, row, column, orientation)

    def populate_game_list_top(self):
        game_list = []
        for i in range(10):
            small_list = []
            for j in range(10):
                small_list.append("O")
            game_list.append(small_list)
        return game_list

    def populate_game_list_bottom(self):
        game_list = []
        for i in range(10):
            small_list = []
            for j in range(10):
                small_list.append("O")
            game_list.append(small_list)
        return game_list

    def add_ship_bottom(self, ship_name, row, column, orientation):
        # adds ship to game_list_bottom
        if orientation == 1:
            for i in range(ship_name.length):
                if ship_name == self.l:
                    self.game_list_bottom[row - 1 + i][column - 1] = \
                     str('l') + ',' + str(row + i) + '_' + str(column) +\
                     ';' + str(i)
                elif ship_name == self.m:
                    self.game_list_bottom[row - 1 + i][column - 1] = \
                     str('m') + ',' + str(row + i) + '_' + str(column) +\
                     ';' + str(i)
                elif ship_name == self.n:
                    self.game_list_bottom[row - 1 + i][column - 1] = \
                     str('n') + ',' + str(row + i) + '_' + str(column) +\
                     ';' + str(i)
                elif ship_name == self.o:
                    self.game_list_bottom[row - 1 + i][column - 1] = \
                     str('o') + ',' + str(row + i) + '_' + str(column) +\
                     ';' + str(i)
                elif ship_name == self.p:
                    self.game_list_bottom[row - 1 + i][column - 1] = \
                     str('p') + ',' + str(row + i) + '_' + str(column) +\
                     ';' + str(i)
        elif orientation == 2:
            for i in range(ship_name.length):
                if ship_name == self.l:
                    self.game_list_bottom[row - 1][column - 1 - i] = \
                     str('l') + ',' + str(row) + '_' + str(column - i) +\
                     ';' + str(i)
                elif ship_name == self.m:
                    self.game_list_bottom[row - 1][column - 1 - i] = \
                     str('m') + ',' + str(row) + '_' + str(column - i) +\
                     ';' + str(i)
                elif ship_name == self.n:
                    self.game_list_bottom[row - 1][column - 1 - i] = \
                     str('n') + ',' + str(row) + '_' + str(column - i) +\
                     ';' + str(i)
                elif ship_name == self.o:
                    self.game_list_bottom[row - 1][column - 1 - i] = \
                     str('o') + ',' + str(row) + '_' + str(column - i) +\
                     ';' + str(i)
                elif ship_name == self.p:
                    self.game_list_bottom[row - 1][column - 1 - i] = \
                     str('p') + ',' + str(row) + '_' + str(column - i) +\
                     ';' + str(i)
        elif orientation == 3:
            for i in range(ship_name.length):
                if ship_name == self.l:
                    self.game_list_bottom[row - 1 - i][column - 1] = \
                     str('l') + ',' + str(row - i) + '_' + str(column) +\
                     ';' + str(i)
                elif ship_name == self.m:
                    self.game_list_bottom[row - 1 - i][column - 1] = \
                     str('m') + ',' + str(row - i) + '_' + str(column) +\
                     ';' + str(i)
                elif ship_name == self.n:
                    self.game_list_bottom[row - 1 - i][column - 1] = \
                     str('n') + ',' + str(row - i) + '_' + str(column) +\
                     ';' + str(i)
                elif ship_name == self.o:
                    self.game_list_bottom[row - 1 - i][column - 1] = \
                     str('o') + ',' + str(row - i) + '_' + str(column) +\
                     ';' + str(i)
                elif ship_name == self.p:
                    self.game_list_bottom[row - 1 - i][column - 1] = \
                     str('p') + ',' + str(row - i) + '_' + str(column) +\
                     ';' + str(i)
        elif orientation == 4:
            for i in range(ship_name.length):
                if ship_name == self.l:
                    self.game_list_bottom[row - 1][column - 1 + i] = \
                     str('l') + ',' + str(row) + '_' + str(column + i) +\
                     ';' + str(i)
                elif ship_name == self.m:
                    self.game_list_bottom[row - 1][column - 1 + i] = \
                     str('m') + ',' + str(row) + '_' + str(column + i) +\
                     ';' + str(i)
                elif ship_name == self.n:
                    self.game_list_bottom[row - 1][column - 1 + i] = \
                     str('n') + ',' + str(row) + '_' + str(column + i) +\
                     ';' + str(i)
                elif ship_name == self.o:
                    self.game_list_bottom[row - 1][column - 1 + i] = \
                     str('o') + ',' + str(row) + '_' + str(column + i) +\
                     ';' + str(i)
                elif ship_name == self.p:
                    self.game_list_bottom[row - 1][column - 1 + i] = \
                     str('p') + ',' + str(row) + '_' + str(column + i) +\
                     ';' + str(i)

    def add_ship_top(self, ship_name, row, column, orientation):
        # adds ship to game_list_bottom
        if orientation == 1:
            for i in range(ship_name.length):
                if ship_name == self.q:
                    self.game_list_top[row - 1 + i][column - 1] = \
                     str('q') + ',' + str(row + i) + '_' + str(column) +\
                     ';' + str(i)
                elif ship_name == self.r:
                    self.game_list_top[row - 1 + i][column - 1] = \
                     str('r') + ',' + str(row + i) + '_' + str(column) +\
                     ';' + str(i)
                elif ship_name == self.s:
                    self.game_list_top[row - 1 + i][column - 1] = \
                     str('s') + ',' + str(row + i) + '_' + str(column) +\
                     ';' + str(i)
                elif ship_name == self.t:
                    self.game_list_top[row - 1 + i][column - 1] = \
                     str('t') + ',' + str(row + i) + '_' + str(column) +\
                     ';' + str(i)
                elif ship_name == self.u:
                    self.game_list_top[row - 1 + i][column - 1] = \
                     str('u') + ',' + str(row + i) + '_' + str(column) +\
                     ';' + str(i)
        elif orientation == 2:
            for i in range(ship_name.length):
                if ship_name == self.q:
                    self.game_list_top[row - 1][column - 1 - i] = \
                     str('q') + ',' + str(row) + '_' + str(column - i) +\
                     ';' + str(i)
                elif ship_name == self.r:
                    self.game_list_top[row - 1][column - 1 - i] = \
                     str('r') + ',' + str(row) + '_' + str(column - i) +\
                     ';' + str(i)
                elif ship_name == self.s:
                    self.game_list_top[row - 1][column - 1 - i] = \
                     str('s') + ',' + str(row) + '_' + str(column - i) +\
                     ';' + str(i)
                elif ship_name == self.t:
                    self.game_list_top[row - 1][column - 1 - i] = \
                     str('t') + ',' + str(row) + '_' + str(column - i) +\
                     ';' + str(i)
                elif ship_name == self.u:
                    self.game_list_top[row - 1][column - 1 - i] = \
                     str('u') + ',' + str(row) + '_' + str(column - i) +\
                     ';' + str(i)
        elif orientation == 3:
            for i in range(ship_name.length):
                if ship_name == self.q:
                    self.game_list_top[row - 1 - i][column - 1] = \
                     str('q') + ',' + str(row - i) + '_' + str(column) +\
                     ';' + str(i)
                elif ship_name == self.r:
                    self.game_list_top[row - 1 - i][column - 1] = \
                     str('r') + ',' + str(row - i) + '_' + str(column) +\
                     ';' + str(i)
                elif ship_name == self.s:
                    self.game_list_top[row - 1 - i][column - 1] = \
                     str('s') + ',' + str(row - i) + '_' + str(column) +\
                     ';' + str(i)
                elif ship_name == self.t:
                    self.game_list_top[row - 1 - i][column - 1] = \
                     str('t') + ',' + str(row - i) + '_' + str(column) +\
                     ';' + str(i)
                elif ship_name == self.u:
                    self.game_list_top[row - 1 - i][column - 1] = \
                     str('u') + ',' + str(row - i) + '_' + str(column) +\
                     ';' + str(i)
        elif orientation == 4:
            for i in range(ship_name.length):
                if ship_name == self.q:
                    self.game_list_top[row - 1][column - 1 + i] = \
                     str('q') + ',' + str(row) + '_' + str(column + i) +\
                     ';' + str(i)
                elif ship_name == self.r:
                    self.game_list_top[row - 1][column - 1 + i] = \
                     str('r') + ',' + str(row) + '_' + str(column + i) +\
                     ';' + str(i)
                elif ship_name == self.s:
                    self.game_list_top[row - 1][column - 1 + i] = \
                     str('s') + ',' + str(row) + '_' + str(column + i) +\
                     ';' + str(i)
                elif ship_name == self.t:
                    self.game_list_top[row - 1][column - 1 + i] = \
                     str('t') + ',' + str(row) + '_' + str(column + i) +\
                     ';' + str(i)
                elif ship_name == self.u:
                    self.game_list_top[row - 1][column - 1 + i] = \
                     str('u') + ',' + str(row) + '_' + str(column + i) +\
                     ';' + str(i)
                    
    def update_ship_list_bottom(self, row, column):
        # add "H" to ship_list
        code = self.game_list_bottom[row - 1][column - 1]
        index_comma = code.find(',')
        index_semicol = code.find(';')
        ship_name = code[:index_comma]
        ship_pos = int(code[index_semicol + 1:])
        if ship_name == 'l':
            self.l.ship_list[ship_pos] = "H"
        elif ship_name == 'm':
            self.m.ship_list[ship_pos] = "H"
        elif ship_name == 'n':
            self.n.ship_list[ship_pos] = "H"
        elif ship_name == 'o':
            self.o.ship_list[ship_pos] = "H"
        elif ship_name == 'p':
            self.p.ship_list[ship_pos] = "H"

    def update_ship_list_top(self, row, column):
        # add "H" to ship_list
        code = self.game_list_top[row - 1][column - 1]
        index_comma = code.find(',')
        index_semicol = code.find(';')
        ship_name = code[:index_comma]
        ship_pos = int(code[index_semicol + 1:])
        if ship_name == 'q':
            self.q.ship_list[ship_pos] = "H"
        elif ship_name == 'r':
            self.r.ship_list[ship_pos] = "H"
        elif ship_name == 's':
            self.s.ship_list[ship_pos] = "H"
        elif ship_name == 't':
            self.t.ship_list[ship_pos] = "H"
        elif ship_name == 'u':
            self.u.ship_list[ship_pos] = "H"

    def ship_sunk_bottom(self, ship_name):
        if ship_name == 'l':
            if self.l.ship_list == self.l.sunk_list:
                return True
        elif ship_name == 'm':
            if self.m.ship_list == self.m.sunk_list:
                return True
        elif ship_name == 'n':
            if self.n.ship_list == self.n.sunk_list:
                return True
        elif ship_name == 'o':
            if self.o.ship_list == self.o.sunk_list:
                return True
        elif ship_name == 'p':
            if self.p.ship_list == self.p.sunk_list:
                return True
        return False

    def ship_sunk_top(self, ship_name):
        if ship_name == 'q':
            if self.q.ship_list == self.q.sunk_list:
                return True
        elif ship_name == 'r':
            if self.r.ship_list == self.r.sunk_list:
                return True
        elif ship_name == 's':
            if self.s.ship_list == self.s.sunk_list:
                return True
        elif ship_name == 't':
            if self.t.ship_list == self.t.sunk_list:
                return True
        elif ship_name == 'u':
            if self.u.ship_list == self.u.sunk_list:
                return True
        return False
        

    def computer_turn(self):
        good_choice = False
        while good_choice == False:
            # ship 5
            if self.ship5 != 0:
                if self.orientation5 == 1:
                    #print("ship5 orientation 1")
                    row = self.start_row5 + self.strike5
                    column = self.start_column5
                    if 0 < row < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.orientation5 = 3
                            self.strike5 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.orientation5 = 3
                            self.strike5 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            
                            self.strike5 += 1
                            if self.ship_sunk_bottom(self.ship5):
                                print("Ship is sunk!")
                                self.ship5 = 0
                                self.orientation5 = 1
                                self.strike5 = 1
                            
                    else:
                        self.orientation5 = 3
                        self.strike5 = 1
                elif self.orientation5 == 3:
                    #print("ship5 orientation 3")
                    row = self.start_row5 - self.strike5
                    column = self.start_column5
                    if 0 < row < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.orientation5 = 2
                            self.strike5 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.orientation5 = 2
                            self.strike5 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            
                            self.strike5 += 1
                            if self.ship_sunk_bottom(self.ship5):
                                print("Ship is sunk!")
                                self.ship5 = 0
                                self.orientation5 = 1
                                self.strike5 = 1
                            
                    else:
                        self.orientation5 = 2
                        self.strike5 = 1
                elif self.orientation5 == 2:
                    #print("ship5 orientation 2")
                    row = self.start_row5
                    column = self.start_column5 - self.strike5
                    if 0 < column < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.orientation5 = 4
                            self.strike5 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.orientation5 = 4
                            self.strike5 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            
                            self.strike5 += 1
                            if self.ship_sunk_bottom(self.ship5):
                                print("Ship is sunk!")
                                self.ship5 = 0
                                self.orientation5 = 1
                                self.strike5 = 1
                            
                    else:
                        self.orientation5 = 4
                        self.strike5 = 1
                elif self.orientation5 == 4:
                    #print("ship5 orientation 4")
                    row = self.start_row5
                    column = self.start_column5 + self.strike5
                    if 0 < column < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.ship5 = 0
                            self.orientation5 = 1
                            self.strike5 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.ship5 = 0
                            self.orientation5 = 1
                            self.strike5 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            
                            self.strike5 += 1
                            if self.ship_sunk_bottom(self.ship5):
                                print("Ship is sunk!")
                                self.ship5 = 0
                                self.orientation5 = 1
                                self.strike5 = 1
                            
                    else:
                        self.ship5 = 0
                        self.orientation5 = 1
                        self.strike5 = 1
            # ship 4
            elif self.ship4 != 0:
                if self.orientation4 == 1:
                    #print("ship4 orientation 1")
                    row = self.start_row4 + self.strike4
                    column = self.start_column4
                    if 0 < row < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.orientation4 = 3
                            self.strike4 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.orientation4 = 3
                            self.strike4 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            if ship_name == self.ship4:
                                self.strike4 += 1
                                if self.ship_sunk_bottom(self.ship4):
                                    print("Ship is sunk!")
                                    self.ship4 = 0
                                    self.orientation4 = 1
                                    self.strike4 = 1
                            else:
                                # New ship
                                self.strike4 = 1
                                self.orientation4 = 3
                                # start new ship
                                self.ship5 = ship_name
                                self.orientation5 = 1
                                self.strike5 = 1
                                self.start_row5 = row
                                self.start_column5 = column
                    else:
                        self.orientation4 = 3
                        self.strike4 = 1
                elif self.orientation4 == 3:
                    #print("ship4 orientation 3")
                    row = self.start_row4 - self.strike4
                    column = self.start_column4
                    if 0 < row < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.orientation4 = 2
                            self.strike4 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.orientation4 = 2
                            self.strike4 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            if ship_name == self.ship4:
                                self.strike4 += 1
                                if self.ship_sunk_bottom(self.ship4):
                                    print("Ship is sunk!")
                                    self.ship4 = 0
                                    self.orientation4 = 1
                                    self.strike4 = 1
                            else:
                                # New ship
                                self.strike4 = 1
                                self.orientation4 = 2
                                # start new ship
                                self.ship5 = ship_name
                                self.orientation5 = 1
                                self.strike5 = 1
                                self.start_row5 = row
                                self.start_column5 = column
                    else:
                        self.orientation4 = 2
                        self.strike4 = 1
                elif self.orientation4 == 2:
                    #print("ship4 orientation 2")
                    row = self.start_row4
                    column = self.start_column4 - self.strike4
                    if 0 < column < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.orientation4 = 4
                            self.strike4 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.orientation4 = 4
                            self.strike4 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            if ship_name == self.ship4:
                                self.strike4 += 1
                                if self.ship_sunk_bottom(self.ship4):
                                    print("Ship is sunk!")
                                    self.ship4 = 0
                                    self.orientation4 = 1
                                    self.strike4 = 1
                            else:
                                # New ship
                                self.strike4 = 1
                                self.orientation4 = 4
                                # start new ship
                                self.ship5 = ship_name
                                self.orientation5 = 1
                                self.strike5 = 1
                                self.start_row5 = row
                                self.start_column5 = column
                    else:
                        self.orientation4 = 4
                        self.strike4 = 1
                elif self.orientation4 == 4:
                    #print("ship4 orientation 4")
                    row = self.start_row4
                    column = self.start_column4 + self.strike4
                    if 0 < column < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.ship4 = 0
                            self.orientation4 = 1
                            self.strike4 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.ship4 = 0
                            self.orientation4 = 1
                            self.strike4 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            if ship_name == self.ship4:
                                self.strike4 += 1
                                if self.ship_sunk_bottom(self.ship4):
                                    print("Ship is sunk!")
                                    self.ship4 = 0
                                    self.orientation4 = 1
                                    self.strike4 = 1
                            else:
                                # New ship
                                self.ship4 = 0
                                self.strike4 = 1
                                self.orientation4 = 1
                                # start new ship
                                self.ship5 = ship_name
                                self.orientation5 = 1
                                self.strike5 = 1
                                self.start_row5 = row
                                self.start_column5 = column
                    else:
                        self.ship4 = 0
                        self.orientation4 = 1
                        self.strike4 = 1
            # ship 3
            elif self.ship3 != 0:
                if self.orientation3 == 1:
                    #print("ship3 orientation 1")
                    row = self.start_row3 + self.strike3
                    column = self.start_column3
                    if 0 < row < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.orientation3 = 3
                            self.strike3 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.orientation3 = 3
                            self.strike3 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            if ship_name == self.ship3:
                                self.strike3 += 1
                                if self.ship_sunk_bottom(self.ship3):
                                    print("Ship is sunk!")
                                    self.ship3 = 0
                                    self.orientation3 = 1
                                    self.strike3 = 1
                            else:
                                # New ship
                                self.strike3 = 1
                                self.orientation3 = 3
                                # start new ship
                                self.ship4 = ship_name
                                self.orientation4 = 1
                                self.strike4 = 1
                                self.start_row4 = row
                                self.start_column4 = column
                    else:
                        self.orientation3 = 3
                        self.strike3 = 1
                elif self.orientation3 == 3:
                    #print("ship3 orientation 3")
                    row = self.start_row3 - self.strike3
                    column = self.start_column3
                    if 0 < row < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.orientation3 = 2
                            self.strike3 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.orientation3 = 2
                            self.strike3 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            if ship_name == self.ship3:
                                self.strike3 += 1
                                if self.ship_sunk_bottom(self.ship3):
                                    print("Ship is sunk!")
                                    self.ship3 = 0
                                    self.orientation3 = 1
                                    self.strike3 = 1
                            else:
                                # New ship
                                self.strike3 = 1
                                self.orientation3 = 2
                                # start new ship
                                self.ship4 = ship_name
                                self.orientation4 = 1
                                self.strike4 = 1
                                self.start_row4 = row
                                self.start_column4 = column
                    else:
                        self.orientation3 = 2
                        self.strike3 = 1
                elif self.orientation3 == 2:
                    #print("ship3 orientation 2")
                    row = self.start_row3
                    column = self.start_column3 - self.strike3
                    if 0 < column < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.orientation3 = 4
                            self.strike3 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.orientation3 = 4
                            self.strike3 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            if ship_name == self.ship3:
                                self.strike3 += 1
                                if self.ship_sunk_bottom(self.ship3):
                                    print("Ship is sunk!")
                                    self.ship3 = 0
                                    self.orientation3 = 1
                                    self.strike3 = 1
                            else:
                                # New ship
                                self.strike3 = 1
                                self.orientation3 = 4
                                # start new ship
                                self.ship4 = ship_name
                                self.orientation4 = 1
                                self.strike4 = 1
                                self.start_row4 = row
                                self.start_column4 = column
                    else:
                        self.orientation3 = 4
                        self.strike3 = 1
                elif self.orientation3 == 4:
                    #print("ship3 orientation 4")
                    row = self.start_row3
                    column = self.start_column3 + self.strike3
                    if 0 < column < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.ship3 = 0
                            self.orientation3 = 1
                            self.strike3 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.ship3 = 0
                            self.orientation3 = 1
                            self.strike3 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            if ship_name == self.ship3:
                                self.strike3 += 1
                                if self.ship_sunk_bottom(self.ship3):
                                    print("Ship is sunk!")
                                    self.ship3 = 0
                                    self.orientation3 = 1
                                    self.strike3 = 1
                            else:
                                # New ship
                                self.ship3 = 0
                                self.strike3 = 1
                                self.orientation3 = 1
                                # start new ship
                                self.ship4 = ship_name
                                self.orientation4 = 1
                                self.strike4 = 1
                                self.start_row4 = row
                                self.start_column4 = column
                    else:
                        self.ship3 = 0
                        self.orientation3 = 1
                        self.strike3 = 1
            # ship 2
            elif self.ship2 != 0:
                if self.orientation2 == 1:
                    #print("ship2 orientation 1")
                    row = self.start_row2 + self.strike2
                    column = self.start_column2
                    if 0 < row < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.orientation2 = 3
                            self.strike2 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.orientation2 = 3
                            self.strike2 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            if ship_name == self.ship2:
                                self.strike2 += 1
                                if self.ship_sunk_bottom(self.ship2):
                                    print("Ship is sunk!")
                                    self.ship2 = 0
                                    self.orientation2 = 1
                                    self.strike2 = 1
                            else:
                                # New ship
                                self.strike2 = 1
                                self.orientation2 = 3
                                # start new ship
                                self.ship3 = ship_name
                                self.orientation3 = 1
                                self.strike3 = 1
                                self.start_row3 = row
                                self.start_column3 = column
                    else:
                        self.orientation2 = 3
                        self.strike2 = 1
                elif self.orientation2 == 3:
                    #print("ship2 orientation 3")
                    row = self.start_row2 - self.strike2
                    column = self.start_column2
                    if 0 < row < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.orientation2 = 2
                            self.strike2 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.orientation2 = 2
                            self.strike2 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            if ship_name == self.ship2:
                                self.strike2 += 1
                                if self.ship_sunk_bottom(self.ship2):
                                    print("Ship is sunk!")
                                    self.ship2 = 0
                                    self.orientation2 = 1
                                    self.strike2 = 1
                            else:
                                # New ship
                                self.strike2 = 1
                                self.orientation2 = 2
                                # start new ship
                                self.ship3 = ship_name
                                self.orientation3 = 1
                                self.strike3 = 1
                                self.start_row3 = row
                                self.start_column3 = column
                    else:
                        self.orientation2 = 2
                        self.strike2 = 1
                elif self.orientation2 == 2:
                    #print("ship2 orientation 2")
                    row = self.start_row2
                    column = self.start_column2 - self.strike2
                    if 0 < column < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.orientation2 = 4
                            self.strike2 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.orientation2 = 4
                            self.strike2 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            if ship_name == self.ship2:
                                self.strike2 += 1
                                if self.ship_sunk_bottom(self.ship2):
                                    print("Ship is sunk!")
                                    self.ship2 = 0
                                    self.orientation2 = 1
                                    self.strike2 = 1
                            else:
                                # New ship
                                self.strike2 = 1
                                self.orientation2 = 4
                                # start new ship
                                self.ship3 = ship_name
                                self.orientation3 = 1
                                self.strike3 = 1
                                self.start_row3 = row
                                self.start_column3 = column
                    else:
                        self.orientation2 = 4
                        self.strike2 = 1
                elif self.orientation2 == 4:
                    #print("ship2 orientation 4")
                    row = self.start_row2
                    column = self.start_column2 + self.strike2
                    if 0 < column < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.ship2 = 0
                            self.orientation2 = 1
                            self.strike2 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.ship2 = 0
                            self.orientation2 = 1
                            self.strike2 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            if ship_name == self.ship2:
                                self.strike2 += 1
                                if self.ship_sunk_bottom(self.ship2):
                                    print("Ship is sunk!")
                                    self.ship2 = 0
                                    self.orientation2 = 1
                                    self.strike2 = 1
                            else:
                                # New ship
                                self.ship2 = 0
                                self.strike2 = 1
                                self.orientation2 = 1
                                # start new ship
                                self.ship3 = ship_name
                                self.orientation3 = 1
                                self.strike3 = 1
                                self.start_row3 = row
                                self.start_column3 = column
                    else:
                        self.ship2 = 0
                        self.orientation2 = 1
                        self.strike2 = 1
            
            # ship 1
            elif self.ship1 != 0:
                if self.orientation1 == 1:
                    #print("ship1 orientation 1")
                    row = self.start_row1 + self.strike1
                    column = self.start_column1
                    if 0 < row < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.orientation1 = 3
                            self.strike1 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.orientation1 = 3
                            self.strike1 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            if ship_name == self.ship1:
                                self.strike1 += 1
                                if self.ship_sunk_bottom(self.ship1):
                                    print("Ship is sunk!")
                                    self.ship1 = 0
                                    self.orientation1 = 1
                                    self.strike1 = 1
                            else:
                                # New ship
                                self.strike1 = 1
                                self.orientation1 = 3
                                # start new ship
                                self.ship2 = ship_name
                                self.orientation2 = 1
                                self.strike2 = 1
                                self.start_row2 = row
                                self.start_column2 = column
                    else:
                        self.orientation1 = 3
                        self.strike1 = 1
                elif self.orientation1 == 3:
                    #print("ship1 orientation 3")
                    row = self.start_row1 - self.strike1
                    column = self.start_column1
                    if 0 < row < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.orientation1 = 2
                            self.strike1 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.orientation1 = 2
                            self.strike1 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            if ship_name == self.ship1:
                                self.strike1 += 1
                                if self.ship_sunk_bottom(self.ship1):
                                    print("Ship is sunk!")
                                    self.ship1 = 0
                                    self.orientation1 = 1
                                    self.strike1 = 1
                            else:
                                # New ship
                                self.strike1 = 1
                                self.orientation1 = 2
                                # start new ship
                                self.ship2 = ship_name
                                self.orientation2 = 1
                                self.strike2 = 1
                                self.start_row2 = row
                                self.start_column2 = column
                    else:
                        self.orientation1 = 2
                        self.strike1 = 1
                elif self.orientation1 == 2:
                    #print("ship1 orientation 2")
                    row = self.start_row1
                    column = self.start_column1 - self.strike1
                    if 0 < column < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.orientation1 = 4
                            self.strike1 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.orientation1 = 4
                            self.strike1 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            if ship_name == self.ship1:
                                self.strike1 += 1
                                if self.ship_sunk_bottom(self.ship1):
                                    print("Ship is sunk!")
                                    self.ship1 = 0
                                    self.orientation1 = 1
                                    self.strike1 = 1
                            else:
                                # New ship
                                self.strike1 = 1
                                self.orientation1 = 4
                                # start new ship
                                self.ship2 = ship_name
                                self.orientation2 = 1
                                self.strike2 = 1
                                self.start_row2 = row
                                self.start_column2 = column
                    else:
                        self.orientation1 = 4
                        self.strike1 = 1
                elif self.orientation1 == 4:
                    #print("ship1 orientation 4")
                    row = self.start_row1
                    column = self.start_column1 + self.strike1
                    if 0 < column < 11:
                        if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            self.ship1 = 0
                            self.orientation1 = 1
                            self.strike1 = 1
                            good_choice = True
                        elif self.game_list_bottom[row - 1][column - 1] == "M"\
                             or self.game_list_bottom[row - 1][column - 1] == \
                             "H":
                            self.ship1 = 0
                            self.orientation1 = 1
                            self.strike1 = 1
                        else:
                            self.draw_circle_bottom(row, column, "red")
                            code = self.game_list_bottom[row - 1][column - 1]
                            ship_name = code[0]
                            self.update_ship_list_bottom(row, column)
                            self.game_list_bottom[row - 1][column - 1] = "H"
                            good_choice = True
                            if ship_name == self.ship1:
                                self.strike1 += 1
                                if self.ship_sunk_bottom(self.ship1):
                                    print("Ship is sunk!")
                                    self.ship1 = 0
                                    self.orientation1 = 1
                                    self.strike1 = 1
                            else:
                                # New ship
                                self.ship1 = 0
                                self.strike1 = 1
                                self.orientation1 = 1
                                # start new ship
                                self.ship2 = ship_name
                                self.orientation2 = 1
                                self.strike2 = 1
                                self.start_row2 = row
                                self.start_column2 = column
                    else:
                        self.ship1 = 0
                        self.orientation1 = 1
                        self.strike1 = 1
            else:
                row = random.randint(1, 10)
                column = random.randint(1, 10)
                if self.game_list_bottom[row - 1][column - 1] == "O":
                            self.draw_circle_bottom(row, column, "white")
                            self.game_list_bottom[row - 1][column - 1] = "M"
                            good_choice = True
                elif self.game_list_bottom[row - 1][column - 1] == "M"\
                     or self.game_list_bottom[row - 1][column - 1] == \
                     "H":
                    good_choice = False
                else:
                    # Hit
                    self.draw_circle_bottom(row, column, "red")
                    code = self.game_list_bottom[row - 1][column - 1]
                    ship_name = code[0]
                    self.update_ship_list_bottom(row, column)
                    self.game_list_bottom[row - 1][column - 1] = "H"
                    good_choice = True
                    self.ship1 = ship_name
                    self.strike1 = 1
                    self.orientation1 = 1
                    self.start_row1 = row
                    self.start_column1 = column
                    if self.ship_sunk_bottom(self.ship1):
                        print("Ship is sunk!")
                        self.ship1 = 0
                        self.orientation1 = 1
                        self.strike1 = 1

    def all_ships_sunk_top(self):
        if (self.ship_sunk_top('q') and self.ship_sunk_top('r') and
            self.ship_sunk_top('s') and self.ship_sunk_top('t') and
            self.ship_sunk_top('u')):
            self.winner_player = True

    def all_ships_sunk_bottom(self):
        if (self.ship_sunk_bottom('l') and self.ship_sunk_bottom('m') and
               self.ship_sunk_bottom('n') and self.ship_sunk_bottom('o') and
               self.ship_sunk_bottom('p')):
            self.winner_computer = True

    def player_turn(self):
        good_move = False
        while good_move == False:
            good_choice = False
            while good_choice == False:
                try:
                    code = input("Enter letter and number of strike. E.g. 'B10': ")
                    code = code.upper()
                    row_letter = code[0]
                    column = int(code[1:])
                    if row_letter in "ZABCDEFGHIJ":
                        row = "ZABCDEFGHIJ".find(row_letter)
                        if 0 < row < 11 and 0 < column < 11:
                            good_choice = True
                except:
                    good_choice == False
            # begin turn with row and column
            if self.game_list_top[row - 1][column - 1] == "O":
                self.draw_circle_top(row, column, "white")
                self.game_list_top[row - 1][column - 1] = "M"
                good_move = True
            elif self.game_list_top[row - 1][column - 1] == "M" or \
                 self.game_list_top[row - 1][column - 1] == "H":
                good_move = False
                print("Already played. Choose again....")
            else:
                # Hit
                good_move = True
                self.draw_circle_top(row, column, "red")
                code = self.game_list_top[row - 1][column - 1]
                ship_name = code[0]
                self.update_ship_list_top(row, column)
                self.game_list_top[row - 1][column - 1] = "H"
                if self.ship_sunk_top(ship_name):
                    print("You sank a ship!")

    def computer_choose_boats(self):
        comp_dict = {0:self.q, 1:self.r, 2:self.s, 3:self.t, 4:self.u}
        for i in range(5):
            good_choice = False
            while good_choice == False:
                row = random.randint(1, 10)
                column = random.randint(1, 10)
                orientation = random.randint(1, 4)
                if orientation == 1:
                    end_row = row + (comp_dict[i].length - 1)
                    if 0 < end_row < 11:
                        # no boats cross
                        boat_list = []
                        for j in range(comp_dict[i].length):
                            boat_list.append(
                                self.game_list_top[row - 1 + j][column - 1])
                        if boat_list == comp_dict[i].ship_list:
                            good_choice = True
                elif orientation == 3:
                    end_row = row - (comp_dict[i].length - 1)
                    if 0 < end_row < 11:
                        # no boats cross
                        boat_list = []
                        for j in range(comp_dict[i].length):
                            boat_list.append(
                                self.game_list_top[row - 1 - j][column - 1])
                        if boat_list == comp_dict[i].ship_list:
                            good_choice = True
                elif orientation == 2:
                    end_column = column - (comp_dict[i].length - 1)
                    if 0 < end_column < 11:
                        # no boats cross
                        boat_list = []
                        for j in range(comp_dict[i].length):
                            boat_list.append(
                                self.game_list_top[row - 1][column - 1 - j])
                        if boat_list == comp_dict[i].ship_list:
                            good_choice = True
                elif orientation == 4:
                    end_column = column + (comp_dict[i].length - 1)
                    if 0 < end_column < 11:
                        # no boats cross
                        boat_list = []
                        for j in range(comp_dict[i].length):
                            boat_list.append(
                                self.game_list_top[row - 1][column - 1 + j])
                        if boat_list == comp_dict[i].ship_list:
                            good_choice = True
            self.draw_boat_top(comp_dict[i], row, column, orientation)
                    
    def player_choose_boats(self):
        print("Player must now place 5 ships.")
        player_dict = {0:self.l, 1:self.m, 2:self.n, 3:self.o, 4:self.p}
        for i in range(5):
            print("Ship has length: " + str(player_dict[i].length))
            good_placement = False
            while good_placement == False:
                # get start position
                good_choice = False
                while good_choice == False:
                    try:
                        code = input("Enter starting position of ship."
                                     " E.g. 'B10': ")
                        code = code.upper()
                        row_letter = code[0]
                        start_column = int(code[1:])
                        if row_letter in "ZABCDEFGHIJ":
                            start_row = "ZABCDEFGHIJ".find(row_letter)
                            if 0 < start_row < 11 and 0 < start_column < 11:
                                good_choice = True
                    except:
                        good_choice == False
                # get end position
                good_choice = False
                while good_choice == False:
                    try:
                        code = input("Enter ending position of ship."
                                     " E.g. 'B10': ")
                        code = code.upper()
                        row_letter = code[0]
                        end_column = int(code[1:])
                        if row_letter in "ZABCDEFGHIJ":
                            end_row = "ZABCDEFGHIJ".find(row_letter)
                            if 0 < end_row < 11 and 0 < end_column < 11:
                                good_choice = True
                    except:
                        good_choice == False
                # set orientation
                if start_row < end_row:
                    orientation = 1
                elif start_row > end_row:
                    orientation = 3
                elif start_column > end_column:
                    orientation = 2
                elif start_column < end_column:
                    orientation = 4
                # boat must be on grid and not cross other boats
                if orientation == 1:
                    true_end_row = start_row + (player_dict[i].length - 1)
                    if 0 < true_end_row < 11:
                        # no boats cross
                        boat_list = []
                        for j in range(player_dict[i].length):
                            boat_list.append(self.game_list_bottom
                                    [start_row - 1 + j][start_column - 1])
                        if boat_list == player_dict[i].ship_list:
                            good_placement = True
                        else:
                            print("Boats cannot cross.")
                elif orientation == 3:
                    true_end_row = start_row - (player_dict[i].length - 1)
                    if 0 < true_end_row < 11:
                        # no boats cross
                        boat_list = []
                        for j in range(player_dict[i].length):
                            boat_list.append(self.game_list_bottom
                                    [start_row - 1 - j][start_column - 1])
                        if boat_list == player_dict[i].ship_list:
                            good_placement = True
                        else:
                            print("Boats cannot cross.")
                elif orientation == 2:
                    true_end_column = start_column - (player_dict[i].length - 1)
                    if 0 < true_end_column < 11:
                        # no boats cross
                        boat_list = []
                        for j in range(player_dict[i].length):
                            boat_list.append(self.game_list_bottom
                                    [start_row - 1][start_column - 1 - j])
                        if boat_list == player_dict[i].ship_list:
                            good_placement = True
                        else:
                            print("Boats cannot cross.")
                elif orientation == 4:
                    true_end_column = start_column + (player_dict[i].length - 1)
                    if 0 < true_end_column < 11:
                        # no boats cross
                        boat_list = []
                        for j in range(player_dict[i].length):
                            boat_list.append(self.game_list_bottom
                                    [start_row - 1][start_column - 1 + j])
                        if boat_list == player_dict[i].ship_list:
                            good_placement = True
                        else:
                            print("Boats cannot cross.")
            self.draw_boat_bottom(player_dict[i], start_row, start_column,
                                  orientation)
                        
                

def main():
    game = Battleship()
    game.draw_gameboard()

    game.player_choose_boats()
    game.computer_choose_boats()
    

    
    while not (game.winner_player or game.winner_computer):

        game.player_turn()
        game.all_ships_sunk_top()
        if not game.winner_player:
            game.computer_turn()
            game.all_ships_sunk_bottom()

    
    if game.winner_player == True:
        print("You sank all my ships!!!!")
    elif game.winner_computer == True:
        print("I sank all your ships!!!!")


    
main()
