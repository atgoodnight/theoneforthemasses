'''
Aidan Jennings
Period 4
Fun square game
5 squares appear on screen, one flashes green, player presses the number that the square was
'''

'''
*** heres what i did for the requirements so you dont have to go through the entire code to grade it ***

Uses mouse to start the game
Keyboard to select the square that flashes (number keys)z
I used pygame
I made  classes to create the starting button and the squares
I tried to make the comments make sense
All code is in the main function
'''


import pygame
import sys
import random

#main!!
def main():

    '''
    Shows 5 squares, one changes color for 200 milliseconds
    User has to press the corresponding number on the keyboard (if it was 2nd square press 2)
    When they get 5 in a row it gives them a win and lets them play again
    User can keep playing and scoring point because this is the most fun game ever!
    '''

    pygame.init()

    #Display constants
    screen = pygame.display.set_mode((600, 400))  #Make the window size
    font = pygame.font.SysFont("Arial", 30)  #Set font to google docs font

    class Button:

        '''
        Creates the button you see at the start of the game that says start game
        Sets the size and colors of the button
        '''

        def __init__(self, x, y, width, height, text, font, color, text_color):
            #sets all the variables up in order to create the button
            self.rect = pygame.Rect(x, y, width, height)
            self.text = text
            self.font = font
            self.color = color
            self.text_color = text_color
            self.clicked = False

        def draw(self, screen):
            #Draws the button and puts the Start Game text on it
            pygame.draw.rect(screen, self.color, self.rect)
            text_surface = self.font.render(self.text, True, self.text_color)
            screen.blit(text_surface, text_surface.get_rect(center=self.rect.center))

        def check_click(self, event):
            #Check if the button was clicked so the game can start

            if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                self.clicked = True

    class Square:

        '''
        This class is to make all the squares that appaer in the game
        First function defines the variables
        Second function draws the squares on the screen
        Third function flashes the square green
        '''

        def __init__(self, x, y, size, index):
            self.rect = pygame.Rect(x, y, size, size)  #Square size
            self.color = (255, 255, 255)  #white color for the squares
            self.index = index  #Each square has an index 1-5, so that you can see if the user pressed the right key

        def draw(self, screen):
            #Draw the square with its current color so that they are all white
            pygame.draw.rect(screen, self.color, self.rect)

        def flash(self, screen):
            #Flash the square green for a brief moment, so the user can pick the correct square
            self.color = (0, 255, 0)
            self.draw(screen)
            pygame.display.flip()
            pygame.time.delay(200)  #Wait a bit so the mind can process this very difficult task!
            self.color = (255, 255, 255)  #reset color

    #Colors
    white = (255, 255, 255)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)

    #Game variables
    button = Button(150, 100, 300, 150, "Start Game!", font, blue, red)
    game_started = False
    score = 0

    #square variables
    squares = []  #List of the squares that go on the screen
    flashed_sqr = 0  #Index of the square that wil flash
    win_count = 0  #win counter to store how many times you have won


    def create_squares():

        '''
        Creates the squares
        has 5 squares that are placed next to each other
        '''

        sqr_list = []#Empty list to store the squares in

        size = 80  #Size of each square
        gap = 10  #Space between squares
        total_width = 5 * size + 5 * gap #I did the math and that is 450 pixels! (Im going to keep the equation so you can see how it is measured)
        start_x = (600 - total_width) // 2 #starts here and adds each square in the for loop below
        y = 135

        for i in range(5):
            #takes the starting place and adds a bit so they are alligned 5 in a row without clipping through each other
            x = start_x + i * (size + gap)
            sqr_list.append(Square(x, y, size, i + 1))  #Creates square byu adding it to the square list

        return sqr_list


    running = True

    while running:

        screen.fill(black)  #Black background so you can see the white squares better

        #Display win counter at the bottom of the home page
        win_count_text = font.render("Wins: " + str(win_count), True, white)
        screen.blit(win_count_text, (25, 350)) #Adds the win text so you can brag to everyone how good you are at the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #Check if the window is closed so it can stop running
                running = False

            if not game_started:
                #Shows instructions at the top of the screen so the player knows how to play
                instructions = font.render("Press number of the square!", True, white)
                screen.blit(instructions, (50, 50)) #Adds instructions to the screen

                #Show the Start Game button and check to see if it was clicked
                button.check_click(event)

                if button.clicked:  #Start the game when the button is clicked for lots of fun!
                    game_started = True  #Mark the game as started
                    squares = create_squares()  #Creates the 5 squares
                    flashed_sqr = random.randint(0, 4)  #Picks a random square to flash

                    #Wait for 1 second before flashing the next square
                    pygame.time.delay(1000)

                    #Flash the chosen one
                    squares[flashed_sqr].flash(screen)

            else:

                #Check for key presses (1-5)
                if event.type == pygame.KEYDOWN:

                    if pygame.K_1 <= event.key <= pygame.K_5:
                        key_pressed = event.key - pygame.K_1 + 1  #Convert key to number (1-5)

                        if key_pressed == squares[flashed_sqr].index:  #Check if key number is square number
                            score += 1  #Increase score if correct

                            if score == 5:  #If score reaches 5, player gets a point and game resets
                                win_count += 1  #Increase the win count for the player
                                win_text = font.render("You Win!", True, white)
                                screen.blit(win_text, (150, 150)) #Adds the win text so the player knows they won
                                pygame.display.flip()
                                pygame.time.delay(1000)  #Show win message for 1 second
                                game_started = False  #Reset the game
                                score = 0  #Reset the score (game score not the overall score)
                                button.clicked = False  #Reset the button state so they can play this fun game again

                            else:
                                #Wait for 1 second before flashing the new square, so the user has some time to rest
                                pygame.time.delay(1000)
                                flashed_sqr = random.randint(0, 4)  #Choose a random square to flash, 0-4 because 5 squares
                                squares[flashed_sqr].flash(screen)  #Flash the square that was chosen above

                        else:
                            #Incorrect guess :( reset the game and make fun of the player
                            lose_text = font.render("Haha you lost!", True, white)
                            screen.blit(lose_text, (150, 150))
                            pygame.display.flip()
                            pygame.time.delay(2000)  #Show win message for 2 seconds (let it sink in)
                            score = 0
                            button.clicked = False #Reset the button/game so they can try again
                            game_started = False


        if not game_started:

            #Shows instructions on screen
            instructions = font.render("Press number of the square!", True, white)
            screen.blit(instructions, (50, 50))
            button.draw(screen)  #Draw start button

        else:
            #Draw all squares again
            for square in squares:
                square.draw(screen)

        pygame.display.flip()

    pygame.quit()  #Quits Pygame
    sys.exit()  #Closes the program


main()