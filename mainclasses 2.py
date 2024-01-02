import pygame


pygame.init()

pygame.display.set_caption("Chess")
screen = pygame.display.set_mode((1100, 950))

clock = pygame.time.Clock()
running = True
BROWN = (245, 203, 167) # light spaces 
BACKGROUND = (87, 65, 18) # dark spaces
y_coords = ['8', '7', '6', '5', '4', '3', '2', '1']
x_coords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


# ChessPiece class
class ChessPiece:

    BORDER_WIDTH = 2
    BORDER_COLOR = (255, 255, 0)

    def __init__(self, image_path, position, color, piece_type):
        self.image = pygame.transform.scale(pygame.image.load(image_path), (100, 100))
        self.position = position
        self.color = color
        self.rect = self.image.get_rect(topleft=self.position)
        self.piece_type = piece_type

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        pygame.draw.rect(screen, self.BORDER_COLOR, self.rect, self.BORDER_WIDTH)

    # be able to access the board state

class Pawn(ChessPiece):
    pass

class Rook(ChessPiece):
    pass

class Knight(ChessPiece):
    pass

class Bishop(ChessPiece):
    pass

class Queen(ChessPiece):
    pass

class King(ChessPiece):
    pass


# ChessBoard class
class ChessBoard:
    def __init__(self):
        self.pieces = []
        self.load_pieces()

    def load_pieces(self):
        black_pieces = [
            ('black-rook.png', (0, 0), 'black'),
            ('black-knight.png', (100, 0), 'black'),
            ('black-bishop.png', (200, 0), 'black'),
            ('black-queen.png', (300, 0), 'black'),
            ('black-king.png', (400, 0), 'black'),
            ('black-bishop.png', (500, 0), 'black'),
            ('black-knight.png', (600, 0), 'black'),
            ('black-rook.png', (700, 0), 'black'),
            ('black-pawn.png', (0, 100), 'black')
        ]

        white_pieces = [
            ('white-rook.png', (0, 700), 'white'),
            ('white-knight.png', (100, 700), 'white'),
            ('white-bishop.png', (200, 700), 'white'),
            ('white-queen.png', (300, 700), 'white'),
            ('white-king.png', (400, 700), 'white'),
            ('white-bishop.png', (500, 700), 'white'),
            ('white-knight.png', (600, 700), 'white'),
            ('white-rook.png', (700, 700), 'white'),
            ('white-pawn.png', (0, 600), 'white')
        ]

        for img, pos, color in black_pieces[:8]:
            piece = ChessPiece(f'pieces/{img}', pos, color, '')
            self.pieces.append(piece)
        
        for img, pos, color in white_pieces[:8]:
            piece = ChessPiece(f'pieces/{img}', pos, color, '')
            self.pieces.append(piece)

        for i in range(8):
            black_pawn = ChessPiece(f'pieces/black-pawn.png', (0 + (100 * i), 100), 'black', '')
            white_pawn = ChessPiece(f'pieces/white-pawn.png', (0 + (100 * i), 600), 'white', '')
            self.pieces.append(black_pawn)
            self.pieces.append(white_pawn)


    def draw(self, screen):
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
                    x_coordtext = font.render(f'{y_coords[i]}' , True, BACKGROUND)
                    y_coordtext = font.render(f'{x_coords[i]}',True, BROWN)
                else:
                    x_coordtext = font.render(f'{y_coords[i]}' , True, BROWN)
                    y_coordtext = font.render(f'{x_coords[i]}',True, BACKGROUND)
                screen.blit(x_coordtext, (5, 5 + (100 * i)))
                screen.blit(y_coordtext, (89 + (100 * i), 780))

        # Draw pieces
        for piece in self.pieces:
            piece.draw(screen)


class RunGame:
    def __init__(self):
        self.selected_piece = None
        self.offset_x = 0
        self.offset_y = 0
        
    def mbd(self, event, chessboard):
        for piece in chessboard.pieces:
            if piece.rect.collidepoint(event.pos):
                self.selected_piece = piece

                # Calculate offsets to center the piece on the mouse cursor
                self.offset_x = piece.rect.width // 2
                self.offset_y = piece.rect.height // 2
                break

    def mbu(self):
        if self.selected_piece:
                # Snap piece position to grid
                self.selected_piece.rect.x = (self.selected_piece.rect.x // 100) * 100
                self.selected_piece.rect.y = (self.selected_piece.rect.y // 100) * 100
                self.selected_piece = None

    def mm(self, event):
        if self.selected_piece:
            # Update piece position to keep cursor at its center
            self.selected_piece.rect.x = event.pos[0] - self.offset_x
            self.selected_piece.rect.y = event.pos[1] - self.offset_y


# Create a ChessBoard instance
chessboard = ChessBoard()
run_game = RunGame()

running = True
selected_piece = None
offset_x, offset_y = 0, 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            run_game.mbd(event, chessboard)
        elif event.type == pygame.MOUSEBUTTONUP:
            run_game.mbu()
        elif event.type == pygame.MOUSEMOTION:
            run_game.mm(event)

    # Render the game
    screen.fill('white')
    chessboard.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
