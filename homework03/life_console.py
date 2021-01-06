import curses
import sys
from life import GameOfLife
from ui import UI


class Console(UI):

    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        horisontal_line = "+"
        for i in range(self.life.cols):
            horisontal_line += "-"
        horisontal_line += "+"

        vertical_line = "|"
        for i in range(self.life.cols):
            vertical_line += " "
        vertical_line += "|"

        screen.addstr(0, 0, horisontal_line)
        for j in range(1, self.life.rows+1):
            screen.addstr(j, 0, vertical_line)
        screen.addstr(self.life.rows+1, 0, horisontal_line)

        curses.curs_set(0)

        screen.refresh()

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        for i in range(self.life.rows):
            edited_line = ''
            edited_line += '|'
            for j in range(self.life.cols):
                if self.life.curr_generation[i][j] == 1:
                    edited_line += '*'
                else:
                    edited_line += ' '
            edited_line += '|'
            screen.addstr(i+1, 0, edited_line)
        screen.refresh()

    def run(self) -> None:
        screen = curses.initscr()
        # PUT YOUR CODE HERE
        # my_window = curses.newwin(15, 20, 0, 0)
        self.draw_borders(screen)
        while life.is_changing and not life.is_max_generations_exceed:
            life.step()
            self.draw_grid(screen)
            curses.napms(300)
        screen.addstr(self.life.rows+2, 0, "Нажмите любую клавишу, чтобы выйти.")
        c = screen.getch()
        curses.endwin()
        # print("You pressed %s which is keycode %d." % (chr(c), c))


sys_cols = 0
sys_rows = 0
sys_max_gen = 0
if len(sys.argv) <= 1:
    print("\nВызов программы со стандартными настройками.\nВызовите программу с аргументом --help для помощи.\n"
          "Стандартные настройки: поле 24x80, кол-во поколений=10\n")
else:
    for j in range(1, len(sys.argv), 2):
        i = sys.argv[j]
        if i == "--help":
            print('\n   Чтобы установить размер окна воспользуйтесь аргументами --rows <int> --cols <int>\n'
                  '   Чтобы установить максимальное число поколений в игре воспользуйтесь аргументом --max_generations <int>\n'
                  '   Приятной игры!\n')
            exit(1)
        elif i == "--rows":
            sys_rows = int(sys.argv[j+1])
        elif i == "--cols":
            sys_cols = int(sys.argv[j+1])
        elif i == "--max_generations":
            sys_max_gen = int(sys.argv[j+1])
        else:
            print("\nНеверный ключ командной строки: ", i, "\n")
            exit(1)


life = GameOfLife((24, 80))
if sys_cols == 0:
    sys_cols = 80
if sys_rows == 0:
    sys_rows = 24
if sys_max_gen == 0:
    sys_max_gen = 10

life = GameOfLife((sys_rows, sys_cols), max_generations=sys_max_gen)
ui = Console(life)
ui.run()
