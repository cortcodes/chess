import pygame

pygame.init()
pygame.display.set_caption("Chess")
screen = pygame.display.set_mode((1100, 950))
clock = pygame.time.Clock()
running = True
BROWN = (245, 203, 167) # light spaces 
BACKGROUND = (87, 65, 18) # dark spaces
x_coords = ['8', '7', '6', '5', '4', '3', '2', '1']
y_coords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
scaled_size = (100, 100)  # Scale size for all the pieces

white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook', 
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_place = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
               (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
# load the white images
white_king = pygame.image.load('pieces/white-king.png')
white_king = pygame.transform.scale(white_king, scaled_size)
white_queen = pygame.image.load('pieces/white-queen.png')
white_queen = pygame.transform.scale(white_queen, scaled_size)
white_bishop = pygame.image.load('pieces/white-bishop.png')
white_bishop = pygame.transform.scale(white_bishop, scaled_size)
white_knight = pygame.image.load('pieces/white-knight.png')
white_knight = pygame.transform.scale(white_knight, scaled_size)
white_rook = pygame.image.load('pieces/white-rook.png')
white_rook = pygame.transform.scale(white_rook, scaled_size)
white_pawn = pygame.image.load('pieces/white-pawn.png')
white_pawn = pygame.transform.scale(white_pawn, scaled_size)

white_piece_list = []

black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook', 
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_place = [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6),
               (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]
# load the black images
black_king = pygame.image.load('pieces/black-king.png')
black_king = pygame.transform.scale(black_king, scaled_size)
black_queen = pygame.image.load('pieces/black-queen.png')
black_queen = pygame.transform.scale(black_queen, scaled_size)
black_bishop = pygame.image.load('pieces/black-bishop.png')
black_bishop = pygame.transform.scale(black_bishop, scaled_size)
black_knight = pygame.image.load('pieces/black-knight.png')
black_knight = pygame.transform.scale(black_knight, scaled_size)
black_rook = pygame.image.load('pieces/black-rook.png')
black_rook = pygame.transform.scale(black_rook, scaled_size)
black_pawn = pygame.image.load('pieces/black-pawn.png')
black_pawn = pygame.transform.scale(black_pawn, scaled_size)

black_pieces = [black_rook, black_knight, black_bishop, black_king, black_queen, black_bishop, black_knight, black_rook]
white_pieces = [white_rook, white_knight, white_bishop, white_king, white_queen, white_bishop, white_knight, white_rook]
black_pawn_rects = [black_pawn.get_rect(topleft=(i * 100, 100)) for i in range(8)]
white_pawn_rects = [white_pawn.get_rect(topleft=(i * 100, 600)) for i in range(8)]

pieces = {
    "black_king": {"image": black_king, "rect": black_king.get_rect(topleft=(400, 0))},
    "black_queen": {"image": black_queen, "rect": black_queen.get_rect(topleft=(300, 0))},
    "black_bishop1": {"image": black_bishop, "rect": black_bishop.get_rect(topleft=(200, 0))},
    "black_bishop2": {"image": black_bishop, "rect": black_bishop.get_rect(topleft=(500, 0))},
    "black_knight1": {"image": black_knight, "rect": black_knight.get_rect(topleft=(100, 0))},
    "black_knight2": {"image": black_knight, "rect": black_knight.get_rect(topleft=(600, 0))},
    "black_rook1": {"image": black_rook, "rect": black_rook.get_rect(topleft=(0, 0))},
    "black_rook2": {"image": black_rook, "rect": black_rook.get_rect(topleft=(700, 0))},
    "black_pawns": {"image": black_pawn, "rects": black_pawn_rects},
    "white_king": {"image": white_king, "rect": white_king.get_rect(topleft=(400, 700))},
    "white_queen": {"image": white_queen, "rect": white_queen.get_rect(topleft=(300, 700))},
    "white_bishop1": {"image": white_bishop, "rect": white_bishop.get_rect(topleft=(200, 700))},
    "white_bishop2": {"image": white_bishop, "rect": white_bishop.get_rect(topleft=(500, 700))},
    "white_knight1": {"image": white_knight, "rect": white_knight.get_rect(topleft=(100, 700))},
    "white_knight2": {"image": white_knight, "rect": white_knight.get_rect(topleft=(600, 700))},
    "white_rook1": {"image": white_rook, "rect": white_rook.get_rect(topleft=(0, 700))},
    "white_rook2": {"image": white_rook, "rect": white_rook.get_rect(topleft=(700, 700))},
    "white_pawns": {"image": white_pawn, "rects": white_pawn_rects}
}

captured_white = []
captured_black = []

def draw_board():
    pygame.draw.rect(screen, BACKGROUND, [0, 0, 800, 800])
    pygame.draw.line(screen, 'black', (801, 0), (801, 800), 4)
    pygame.draw.line(screen, 'black', (0, 801), (803, 801), 4)
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, BROWN, [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, BROWN, [700 - (column * 200), row * 100, 100, 100])

        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)

        # printing off the x and y coords onto the board
        font = pygame.font.SysFont('arial', 16)
        
        for i in range(8):
            if i % 2 == 0:
                x_coordtext = font.render(f'{x_coords[i]}' , True, BACKGROUND)
                y_coordtext = font.render(f'{y_coords[i]}',True, BROWN)
            else:
                x_coordtext = font.render(f'{x_coords[i]}' , True, BROWN)
                y_coordtext = font.render(f'{y_coords[i]}',True, BACKGROUND)
            screen.blit(x_coordtext, (5, 5 + (100 * i)))
            screen.blit(y_coordtext, (89 + (100 * i), 780))

def draw_pieces():
    for key, piece in pieces.items():
        if key.endswith("_pawns"):
            for rect in piece["rects"]:
                screen.blit(piece["image"], rect)
        else:
            screen.blit(piece["image"], piece["rect"])

def snap_to_grid(pos):
    grid_size = 100
    half_grid_size = grid_size // 2

    # Calculate the grid square's center where the piece should snap
    center_x = ((pos[0] // grid_size) * grid_size) + half_grid_size
    center_y = ((pos[1] // grid_size) * grid_size) + half_grid_size

    # Now calculate the top-left corner of the piece to be placed
    new_x = center_x - half_grid_size
    new_y = center_y - half_grid_size
    return new_x, new_y

def get_valid_pawn_moves(piece, current_pos):
    valid_moves = []
    direction = -1 if piece["color"] == "white" else 1  # White pawns move up (-1), black pawns move down (+1)
    start_row = 6 if piece["color"] == "white" else 1  # Starting row for white is 6, for black is 1

    # Move forward one square
    forward_pos = (current_pos[0], current_pos[1] + direction)
    if is_square_empty(forward_pos):
        valid_moves.append(forward_pos)

    # Move forward two squares if on start row
    if current_pos[1] == start_row:
        double_forward_pos = (current_pos[0], current_pos[1] + 2 * direction)
        if is_square_empty(double_forward_pos):
            valid_moves.append(double_forward_pos)

    return valid_moves

def is_square_empty(pos):
    # Implement logic to check if the given position is empty
    # You'll need a way to keep track of the board state for this
    return True  # Placeholder

def get_piece_type(piece):
    # Implement logic to determine the type of the piece (pawn, rook, etc.)
    # This could be based on the image, the key in the pieces dictionary, etc.
    return "pawn"  # Placeholder

selected_piece = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            found_piece = False
            for key, piece in pieces.items():
                if key.endswith("_pawns"):
                    for rect in piece["rects"]:
                        if rect.collidepoint(event.pos):
                            selected_piece = {"image": piece["image"], "rect": rect}
                            offset_x = rect.x - event.pos[0]
                            offset_y = rect.y - event.pos[1]
                            found_piece = True
                            break
                else:
                    if piece["rect"].collidepoint(event.pos):
                        selected_piece = piece
                        offset_x = piece["rect"].x - event.pos[0]
                        offset_y = piece["rect"].y - event.pos[1]
                        found_piece = True
                        break
                if found_piece:
                    break
        elif event.type == pygame.MOUSEBUTTONUP and selected_piece:
            mouse_pos = (event.pos[0] // 100, event.pos[1] // 100)
            piece_type = get_piece_type(selected_piece)

            if piece_type == "pawn":
                current_pos = (selected_piece["rect"].x // 100, selected_piece["rect"].y // 100)
                valid_moves = get_valid_pawn_moves(selected_piece, current_pos)

                if mouse_pos in valid_moves:
                    new_pos = snap_to_grid((mouse_pos[0] * 100, mouse_pos[1] * 100))
                    selected_piece["rect"].topleft = new_pos
                else:
                    # Snap back to original position or handle invalid move
                    pass
            else:
                # Handle other pieces
                selected_piece = None

        elif event.type == pygame.MOUSEMOTION and selected_piece:
            if "rect" in selected_piece:
                mouse_x, mouse_y = event.pos
                selected_piece["rect"].x = mouse_x + offset_x
                selected_piece["rect"].y = mouse_y + offset_y
        

    # fill the screen with a color to wipe away anything from the last frame
    screen.fill('white')
    draw_board()
    draw_pieces()
    

    # Render game here
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()