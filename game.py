import time
import winsound
from Player import Player
import curses
from curses import newwin
from curses import wrapper

f_scene = 'scene.txt'
scene = open(f_scene,'r').read()
pos_player1 = scene.index('1')
pos_player2 = scene.index('2')
if 'x' in scene :
    pos_obstacle = scene.index('x')
content =['Play','Scoreboard','Instructions','Exit']
player1 = Player(input('First player, enter your name:'))
player2 = Player(input('Second player, enter your name:'))


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(content):
        x = w//2 - len(row)//2
        y = h//2 - len(content)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
        	stdscr.addstr(y, x, row)
        stdscr.refresh()

import curses
from curses import newwin
from curses import wrapper


def main(stdscr):
    winsound.PlaySound("Music.wav", winsound.SND_ASYNC)
    stdscr.clear()
    stdscr.addstr(4,12,'Welcome to Fancy Fencing ! Loading ... ')
    stdscr.refresh()
    time.sleep(3)
    stdscr.clear()
    stdscr.refresh()
    win = curses.newwin(12,90,10,10)
    win.border()
    sh,sw= win.getmaxyx()
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row = 0

    print_menu(win, current_row)
    pos1=pos_player1
    pos_y1 =5
    pos_y2 =5
    pos2=pos_player2
    scr1 =0
    scr2= 0
    blockingtime = 0.2
    start_time = time.time()

    while True:
        winsound.PlaySound("Music.wav", winsound.SND_ASYNC)
        win.keypad(True)
        key = win.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1

        elif key == curses.KEY_DOWN and current_row < len(content)-1:
            current_row += 1

        elif key == curses.KEY_ENTER or key in [10, 13]:
            print(win, "You selected '{}'".format(content[current_row]))
            win.getch()
            if content[current_row] == 'Exit':
                break
            elif content[current_row] == 'Scoreboard':
                win.clear()
                win.addstr(0,25, 'SCOREBOARD')
                win.addstr(5,0, '|SCORE '+ player1.name +' : ' + str(scr1)+ '|SCORE '+player2.name +' : ' +str(scr2))
                win.refresh()
                win.getch()
            elif content[current_row] == 'Instructions':
                win.clear()
                win.addstr(2,10,'Moves for '+ player1.name +' '*30 +'Moves for '+player2.name )
                win.addstr(0,4,'WARNING: going beyong the scene will crash the game')
                win.addstr(4,0,'To move right click:   d'+' '*30+'right arrow')
                win.addstr(5,0,'To move left click:    q'+' '*30+'left arrow')
                win.addstr(6,0,'To jump right click:   e'+' '*30+'m')
                win.addstr(7,0,'To jump left click:    a'+' '*30+'l')
                win.addstr(8,0,'To attack click:       z'+' '*30+'o')
                win.addstr(9,0,'To block click:        s'+' '*30+'p')
                win.addstr(10,10,'To go back to the menu : Click on g.')
                win.refresh()
                win.getch()
            if content[current_row] == 'Play':
                stdscr.clear()
                win.clear()
                win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                win.addstr(6,pos_player1-1,open('moves_players\\head.txt','r').read())
                win.addstr(6,pos_player2-1,open('moves_players\\head.txt','r').read())
                win.addstr(7,pos_player1,open('moves_players\\body.txt','r').read())
                win.addstr(7,pos_player1+1, '_/')
                win.addstr(7,pos_player2,open('moves_players\\body.txt','r').read())
                win.addstr(7,pos_player2-2, '\_')
                win.addstr(8,pos_player1,open('moves_players\\body.txt','r').read())
                win.addstr(8,pos_player2,open('moves_players\\body.txt','r').read())
                win.addstr(9,pos_player1-1, '/|')
                win.addstr(9,pos_player2,'|\\')
                stdscr.addstr(22,0,'#'*90)
                stdscr.refresh()
                stdscr.getch()
                win.refresh()
                win.getch()


                defense_mode = False


                while True :
                    win.keypad(True)
                    key1 = win.getch()
                    key2 = win.getch()

                    if key1==ord('d'):
                        defense_mode = False
                        pos1+=player1.speed
                        win.clear()
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos1+1, '_/')
                        win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos2-2, '\_')
                        win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9,pos1-1, '/|')
                        win.addstr(9,pos2,'|\\')
                        win.refresh()
                        win.getch()
                    if key1 == ord('q') :
                        defense_mode = False
                        pos1-=player1.speed
                        win.clear()
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos1+1, '_/')
                        win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos2-2, '\_')
                        win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9,pos1-1, '/|')
                        win.addstr(9,pos2,'|\\')
                        win.refresh()
                        win.getch()
                    if key1 ==ord('e'):
                        defense_mode = False
                        win.clear()
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6-player1.speed,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7-player1.speed,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7-player1.speed,pos1+1, '_/')
                        win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos2-2, '\_')
                        win.addstr(8-player1.speed,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9-player1.speed,pos1-1, '/|')
                        win.addstr(9,pos2,'|\\')
                        win.refresh()
                        time.sleep(0.005)
                        win.clear()
                        pos1=pos1+player1.speed
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6-player1.speed,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7-player1.speed,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7-player1.speed,pos1+1, '_/')
                        win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos2-2, '\_')
                        win.addstr(8-player1.speed,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9-player1.speed,pos1-1, '/|')
                        win.addstr(9,pos2,'|\\')
                        win.refresh()
                        time.sleep(0.005)
                        win.clear()
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos1+1, '_/')
                        win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos2-2, '\_')
                        win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9,pos1-1, '/|')
                        win.addstr(9,pos2,'|\\')
                        time.sleep(0.005)
                        win.refresh()
                        win.getch()           
                    if key1 == ord('a'):
                        defense_mode = False
                        win.clear()
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(5,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(6,pos1+1, '_/')
                        win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos2-2, '\_')
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos1-1, '/|')
                        win.addstr(9,pos2,'|\\')
                        win.refresh()
                        time.sleep(0.005)
                        win.clear()
                        pos1=pos1-player1.speed
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(5,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(6,pos1+1, '_/')
                        win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos2-2, '\_')
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos1-1, '/|')
                        win.addstr(9,pos2,'|\\')
                        win.refresh()
                        time.sleep(0.005)
                        win.clear()
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos1+1, '_/')
                        win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos2-2, '\_')
                        win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9,pos1-1, '/|')
                        win.addstr(9,pos2,'|\\')
                        time.sleep(0.005)
                        win.refresh()
                        win.getch()  
                    if key1 == ord('z'):
                        start_time = time.time()
                        win.clear()    
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos1+1, '__')
                        win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos2-2, '\_')
                        win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9,pos1-1, '/|')
                        win.addstr(9,pos2,'|\\')
                        win.refresh()
                        win.getch()
                        elapsed_time = time.time()
                        if elapsed_time > start_time+blockingtime:
                            if defense_mode==False and (player1.ar)>=abs(pos2-pos1)-player2.dr  :
                                scr1+=1
                                pos1 = pos_player1
                                pos2 = pos_player2
                                win.clear()
                                win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                                win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                                win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                                win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                                win.addstr(7,pos1+1, '_/')
                                win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                                win.addstr(7,pos2-2, '\_')
                                win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                                win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                                win.addstr(9,pos1-1, '/|')
                                win.addstr(9,pos2,'|\\')
                                win.refresh()
                                win.getch()
                            defense_mode = False
                    if key1 == ord('s'):
                        defense_mode = True
                        win.clear()
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos1+1, '_|')
                        win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos2-2, '\_')
                        win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9,pos1-1, '/|')
                        win.addstr(9,pos2,'|\\')
                        win.refresh()
                        win.getch()
                        
                    if key2==curses.KEY_LEFT:
                        defense_mode = False
                        pos2=pos2-player2.speed
                        win.clear()
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos1+1, '_/')
                        win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos2-2, '\_')
                        win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9,pos1-1, '/|')
                        win.addstr(9,pos2,'|\\')
                        win.refresh()
                        win.getch()
                    if key2==curses.KEY_RIGHT:
                        defense_mode = False
                        pos2=pos2+player2.speed
                        win.clear()
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos1+1, '_/')
                        win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos2-2, '\_')
                        win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9,pos1-1, '/|')
                        win.addstr(9,pos2,'|\\')
                        win.refresh()
                        win.getch()
                    if key2==ord('l'):
                        defense_mode = False
                        win.clear()
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6-player2.speed,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos1+1, '_/')
                        win.addstr(7-player2.speed,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7-player2.speed,pos2-2, '\_')
                        win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8-player2.speed,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9,pos1-1, '/|')
                        win.addstr(9-player2.speed,pos2,'|\\')
                        win.refresh()
                        time.sleep(0.001)
                        pos2=pos2-player2.speed
                        win.clear()
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6-player2.speed,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos1+1, '_/')
                        win.addstr(7-player2.speed,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7-player2.speed,pos2-2, '\_')
                        win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8-player2.speed,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9,pos1-1, '/|')
                        win.addstr(9-player2.speed,pos2,'|\\')
                        win.refresh()
                        time.sleep(0.001)
                        win.clear()
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos1+1, '_/')
                        win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos2-2, '\_')
                        win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9,pos1-1, '/|')
                        win.addstr(9,pos2,'|\\')
                        win.refresh()
                        win.getch()
                    if key2==ord('m'):
                        defense_mode = False
                        win.clear()
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6-player2.speed,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos1+1, '_/')
                        win.addstr(7-player2.speed,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7-player2.speed,pos2-2, '\_')
                        win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8-player2.speed,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9,pos1-1, '/|')
                        win.addstr(9-player2.speed,pos2,'|\\')
                        win.refresh()
                        time.sleep(0.001)
                        pos2=pos2+player2.speed
                        win.clear()
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6-player2.speed,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos1+1, '_/')
                        win.addstr(7-player2.speed,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7-player2.speed,pos2-2, '\_')
                        win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8-player2.speed,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9,pos1-1, '/|')
                        win.addstr(9-player2.speed,pos2,'|\\')
                        win.refresh()
                        time.sleep(0.001)
                        win.clear()
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos1+1, '_/')
                        win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos2-2, '\_')
                        win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9,pos1-1, '/|')
                        win.addstr(9,pos2,'|\\')
                        win.refresh()
                        win.getch()
                    if key2==ord('p'):
                        defense_mode = True
                        win.clear()
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos1+1, '_/')
                        win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos2-2, '|_')
                        win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9,pos1-1, '/|')
                        win.addstr(9,pos2,'|\\')
                        win.refresh()
                        win.getch()
                    
                    if key2==ord('o'):
                        start_time = time.time()
                        defense_mode = False 
                        win.clear()
                        win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                        win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                        win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                        win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos1+1, '_/')
                        win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(7,pos2-2, '__')
                        win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                        win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                        win.addstr(9,pos1-1, '/|')
                        win.addstr(9,pos2,'|\\')
                        win.refresh()
                        win.getch()
                        elapsed_time = time.time()
                        if elapsed_time > start_time+blockingtime:
                            if defense_mode==False and (player2.ar)>=abs(pos2-pos1)-player1.dr  :
                                scr2+=1
                                pos1 = pos_player1
                                pos2 = pos_player2
                                win.clear()
                                win.addstr(0,3,'|Score ' +player1.name+' : '+str(scr1) +' |Score '+ player2.name+' : ' +str(scr2))
                                win.addstr(6,pos1-1,open('moves_players\\head.txt','r').read())
                                win.addstr(6,pos2-1,open('moves_players\\head.txt','r').read())
                                win.addstr(7,pos1,open('moves_players\\body.txt','r').read())
                                win.addstr(7,pos1+1, '_/')
                                win.addstr(7,pos2,open('moves_players\\body.txt','r').read())
                                win.addstr(7,pos2-2, '\_')
                                win.addstr(8,pos1,open('moves_players\\body.txt','r').read())
                                win.addstr(8,pos2,open('moves_players\\body.txt','r').read())
                                win.addstr(9,pos1-1, '/|')
                                win.addstr(9,pos2,'|\\')
                                win.refresh()
                                win.getch()
                            defense_mode = False
                    if scr1 == 5:
                        winsound.PlaySound("Winner.wav", winsound.SND_ASYNC)
                        win.clear()
                        win.addstr('Game Over : '+ player1.name +' has won')
                        win.refresh()
                        win.getch()
                        scr1=0
                        time.sleep(1)
                        break
                    if scr2 == 5: 
                        winsound.PlaySound("Winner.wav", winsound.SND_ASYNC)
                        win.clear()
                        win.addstr('Game Over : '+ player2.name +' has won')
                        win.refresh()
                        win.getch()
                        scr2=0
                        time.sleep(1)
                        break
                    if key1 == ord('g'):
                        break
                    if pos1 ==1 or pos1 == sw-1 or pos2 == 1 or pos2==sw-1 :
                        win.clear()
                        win.addstr('Crash !')
                        win.refresh()
                        win.getch()
                        time.sleep(1)
                        break
                    

                    
                    
                        
                        
    
                    
        print_menu(win, current_row)
        
        
wrapper(main)