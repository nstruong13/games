import curses
import random



def next_move(key_input):
	new_snake_loc = []
	return_val = []
	if key_input == curses.KEY_UP:
		new_snake_loc = [snake_loc[-1][0]-1,snake_loc[-1][1]]
		return_val.append(new_snake_loc)
		return_val.append(curses.KEY_UP)
	elif key_input ==curses.KEY_DOWN:
		new_snake_loc= [snake_loc[-1][0]+1,snake_loc[-1][1]]
		return_val.append(new_snake_loc)
		return_val.append(curses.KEY_DOWN)
	elif key_input ==curses.KEY_LEFT:
		new_snake_loc = [snake_loc[-1][0],snake_loc[-1][1]-1]
		return_val.append(new_snake_loc)
		return_val.append(curses.KEY_LEFT)
	elif key_input== curses.KEY_RIGHT:
		new_snake_loc = [snake_loc[-1][0],snake_loc[-1][1]+1]
		return_val.append(new_snake_loc)
		return_val.append(curses.KEY_RIGHT)
	return return_val

def check_boundary(cur_loc):
	if cur_loc[0] > height - 2:
		cur_loc[0] = 1
	if cur_loc[0] < 1:
		cur_loc[0] = height-2
	if cur_loc[1] > width - 2:
		cur_loc[1] = 1
	if cur_loc[1] < 1:
		cur_loc[1] = width - 2
	return cur_loc


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)


begin_x = 0
begin_y = 0
height = 20
width = 30
win = curses.newwin(height, width, begin_y, begin_x)
win.keypad(1)
win.border(0)
item = [5,5]
win.addstr(item[0],item[1],"+")
snake_loc = []
snake_loc.append([1,1])
snake_loc.append([1,2])
snake_loc.append([1,3])
win.addstr(snake_loc[0][0],snake_loc[0][1],"@")
win.addstr(snake_loc[1][0],snake_loc[1][1],"@")
win.addstr(snake_loc[2][0],snake_loc[2][1],"@")
win.nodelay(1)
speed = 100
# curses.halfdelay(speed)
win.refresh()
score = 0
update = False
prev_input = curses.KEY_RIGHT
lose = False

while score<20:
	if update:
		speed -=5
		update = False
	win.timeout(speed)
	key_input = win.getch()
	temp = next_move(key_input)
	if not temp:
		new_snake_loc = next_move(prev_input)[0]
	else:
		new_snake_loc = temp[0]
		prev_input= temp[1]
	for loc in snake_loc:
		if loc[0] == new_snake_loc[0] and loc[1] == new_snake_loc[1]:
			lose = True
	if lose:
		break

	new_snake_loc = check_boundary(new_snake_loc)
	to_remove = snake_loc.pop(0)
	win.addstr(to_remove[0],to_remove[1]," ")
	snake_loc.append(new_snake_loc)
	if new_snake_loc[0] == item[0] and new_snake_loc[1] == item[1]:
		add_snake_loc = next_move(prev_input)[0]
		add_snake_loc = check_boundary(add_snake_loc)
		snake_loc.append(add_snake_loc)
		item = [random.randint(1,height-2),random.randint(1,width-2)]
		win.addstr(item[0],item[1],"+")
		score+=1
	for loc in snake_loc:
		win.addstr(loc[0],loc[1],"@")

	win.refresh()


curses.endwin()
stdscr.keypad(False)
curses.echo()
