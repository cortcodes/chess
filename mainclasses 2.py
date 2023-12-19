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
    def __init__(self, image_path, position, color):
        self.image = pygame.transform.scale(pygame.image.load(image_path), (100, 100))
        self.position = position
        self.color = color
        self.rect = self.image.get_rect(topleft=self.position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

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
            ('black-rook.png', (700, 0), 'black')
        ]

        white_pieces = [
            ('white-rook.png', (0, 700), 'black'),
            ('white-knight.png', (100, 700), 'black'),
            ('white-bishop.png', (200, 700), 'black'),
            ('white-queen.png', (300, 700), 'black'),
            ('white-king.png', (400, 700), 'black'),
            ('white-bishop.png', (500, 700), 'black'),
            ('white-knight.png', (600, 700), 'black'),
            ('white-rook.png', (700, 700), 'black')
        ]

        for img, pos, color in black_pieces:
            piece = ChessPiece(f'pieces/{img}', pos, color)
            self.pieces.append(piece)
        
        for img, pos, color in white_pieces:
            piece = ChessPiece(f'pieces/{img}', pos, color)
            self.pieces.append(piece)

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


# Create a ChessBoard instance
chessboard = ChessBoard()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Handle other events like mouse clicks to move pieces

    # Game logic
    # ...

    # Render the game
    screen.fill('white')  # Clear screen
    chessboard.draw(screen)  # Draw the chessboard and pieces

    pygame.display.flip()  # Update the display
    clock.tick(60)

pygame.quit()
