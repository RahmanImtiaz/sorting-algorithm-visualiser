import math
import pygame
import random
pygame.init()

class Drawinfo:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BACKGROUND = WHITE
    GRADIENTS = [(128, 128, 128), (160, 160, 160), (192, 192, 192)]
    SIDE_PADDING = 100
    TOP_PADDING = 150

    FONT = pygame.font.SysFont("comicsans", 20)
    LARGE_FONT = pygame.font.SysFont("comicsans", 30)

    def __init__(self, width, height, list):
        self.width = width
        self.height = height
        
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sorting Algorithm Visualiser")
        self.set_list(list)
    
    def set_list(self, list):
        self.list = list
        self.n = len(list)
        self.min = min(list)
        self.max = max(list)
        self.width_bar = round((self.width - self.SIDE_PADDING) / self.n)
        self.height_bar = math.floor(self.height - self.TOP_PADDING) / (self.max - self.min)

        self.start_x = self.SIDE_PADDING // 2

def generate_random_list(n, min_val, max_val):
    list = []
    for _ in range(n):
        list.append(random.randint(min_val, max_val))

    return list

def draw_list(info, color_positions={}, clear_bg=False):
    list = info.list

    if clear_bg:
        clear_rectangle = (info.SIDE_PADDING // 2, info.TOP_PADDING - 1, info.width - info.SIDE_PADDING, info.height - info.TOP_PADDING)
        pygame.draw.rect(info.window, info.BACKGROUND, clear_rectangle)

    for i, val in enumerate(list):
        x = info.start_x + i * info.width_bar
        y = info.height - ( (val - info.min) * info.height_bar )

        color = info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(info.window, color, (x, y, info.width_bar, val * info.height_bar)) # remove val

    if clear_bg:
        pygame.display.update()

def draw(info):
    info.window.fill(info.BACKGROUND)

    Controls = info.FONT.render("R - Reset, Space - Start Sort, A - Ascending, D - Descending", 1, info.BLACK)
    info.window.blit(Controls, (info.width // 2 - Controls.get_width() // 2, 50))

    SortingControls = info.FONT.render("1 - Insertion Sort, 2 - Bubble Sort", 1, info.BLACK)
    info.window.blit(SortingControls, (info.width // 2 - SortingControls.get_width() // 2, 100))

    draw_list(info)
    pygame.display.update()

def bubble_sort(info, ascending=True):
    list = info.list
    n = len(list)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if (ascending and list[j] > list[j + 1]) or (not ascending and list[j] < list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]
                draw_list(info, {j: info.GREEN, j + 1: info.RED}, clear_bg=True)
                yield True # control back to main loop once the swap is done - pause but store current state - turns into generator

    return list
 
def main():

    clock = pygame.time.Clock()
    run = True

    n = 100
    min_val = 1
    max_val = 100
    sorting = False
    ascending = True
     
    list = generate_random_list(n, min_val, max_val)
    info = Drawinfo(800, 600, list)

    sorting_algorithm = bubble_sort
    sorting_algorithm_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(60)

        if sorting:
            try:
                if sorting_algorithm_generator: # if not None
                    next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
                sorting_algorithm_generator = None
        else:
            draw(info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN: # prevents holding the button
                continue

            if pygame.key.get_pressed()[pygame.K_r]:
                list = generate_random_list(n, min_val, max_val)
                info.set_list(list)
                sorting = False
            elif pygame.key.get_pressed()[pygame.K_SPACE] and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(info, ascending)
            elif pygame.key.get_pressed()[pygame.K_a] and not sorting:
                ascending = True
            elif pygame.key.get_pressed()[pygame.K_d] and not sorting:
                ascending = False
            
    pygame.quit()  


if __name__ == "__main__":
    main()