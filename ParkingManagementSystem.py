import pygame, sys
from pygame.locals import *

pygame.init()


#constants
WIDTH = 1266
HEIGHT = 668

#colors           R    G    B
BGCOLOR        = (31,  31,  31 )
WHITE          = (255, 255, 255)
BLACK          = (0,   0,   0  )
GREY           = (85,  85,  85 )
GREEN          = (0,   128, 0  )
RED            = (255, 0,   0  )
LIGHTBLUE      = (0,   0,   200)
BGCOLOR2       = (196, 196, 196)
LIGHTGREY      = (245, 245, 245)
EXTRALIGHTBLUE = (36,  90,  191)
CYAN           = (39,  175, 107)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Parking Management System")

#states
run = True
screenOne = True
menuScreen = False

# username and there passwords
data = {"Divyanshu1593":"password"}

class AdminLogin:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.email = ""
        self.mobileNumber = ""
        self.signinButtonClicked = False
        self.forgottenPasswordClicked = False
        self.resetButtonClicked = False
        self.innerBox1Clicked = False
        self.innerBox2Clicked = False
        self.boxHeight = (40*HEIGHT)/100  # 40% of the screen height
        self.boxWidth = (40*WIDTH)/100  # 40% of the screen width

    def draw(self):
        global textRect3,innerBoxWidth,innerBoxHeight,leftPadding,paddingLeft,paddingUp
        #outer box
        paddingUp = (HEIGHT - self.boxHeight)/3
        paddingLeft = (WIDTH - self.boxWidth)/2
        pygame.draw.rect(win, WHITE, (paddingLeft, paddingUp, self.boxWidth, self.boxHeight))

        # inner boxes
        innerBoxHeight = self.boxHeight/8
        innerBoxWidth = self.boxWidth*0.9  # 90% of the box's width
        leftPadding = 0.05*self.boxWidth  # 5% of the box's width
        #local initializations
        innerBox1Color = GREY
        innerBox2Color = GREY
        innerBoxBorder1 = 1
        innerBoxBorder2 = 1
        if self.innerBox1Clicked:
            innerBox1Color = BLACK
            innerBoxBorder1 = 3
        if self.innerBox2Clicked:
            innerBox2Color = BLACK
            innerBoxBorder2 = 3
        pygame.draw.rect(win, innerBox1Color, (leftPadding + paddingLeft, 2*innerBoxHeight + paddingUp, innerBoxWidth, innerBoxHeight), innerBoxBorder1)
        pygame.draw.rect(win, innerBox2Color, (leftPadding + paddingLeft, 4*innerBoxHeight + paddingUp, innerBoxWidth, innerBoxHeight), innerBoxBorder2)
        pygame.draw.rect(win, GREEN, (leftPadding + paddingLeft, 6*innerBoxHeight + paddingUp, innerBoxWidth, innerBoxHeight))

        #bliting texts
        textSize = int((innerBoxHeight)*0.59)
        textSize2 = int(textSize*0.8)
        
        font = pygame.font.Font("freesansbold.ttf", textSize)
        font2 = pygame.font.Font("freesansbold.ttf", textSize2)

        if self.forgottenPasswordClicked:
            text = font.render("EMAIL", True, GREY, WHITE)
            text2 = font.render("MOBILE NUMBER", True, GREY, WHITE)
            text3 = font2.render("Sign in", True, LIGHTBLUE, WHITE)
            text4 = font.render("RESET", True, WHITE, GREEN)
            text5 = font2.render(self.email, True, BLACK,WHITE)
            text6 = font2.render(self.mobileNumber, True, BLACK, WHITE)
        else:
            text = font.render("USER NAME", True, GREY, WHITE)
            text2 = font.render("PASSWORD", True, GREY, WHITE)
            text3 = font2.render("Forgot Password?", True, RED, WHITE)
            text4 = font.render("SIGN IN", True, WHITE, GREEN)
            text5 = font2.render(self.username, True, BLACK,WHITE)
            text6 = font2.render("."*len(admin.password), True, BLACK, WHITE)
            
        textRect = text.get_rect()
        textRect2 = text2.get_rect()
        textRect3 = text3.get_rect()
        textRect4 = text4.get_rect()
        textRect5 = text5.get_rect()
        textRect6 = text6.get_rect()
        
        textRect.left = leftPadding + 3 + paddingLeft
        textRect.top = 1*innerBoxHeight + paddingUp + (innerBoxHeight/4)
        textRect2.left = leftPadding + 3 + paddingLeft
        textRect2.top = 3*innerBoxHeight + paddingUp + (innerBoxHeight/4)
        textRect3.right = leftPadding + innerBoxWidth + paddingLeft
        textRect3.top = 5*innerBoxHeight + paddingUp + (innerBoxHeight/4)
        textRect4.center = (leftPadding+paddingLeft+innerBoxWidth/2, 6*innerBoxHeight + paddingUp + innerBoxHeight/2)
        textRect5.left = leftPadding + 10 + paddingLeft
        textRect5.top = 2*innerBoxHeight + paddingUp + (innerBoxHeight/4)
        textRect6.left = leftPadding + 10 + paddingLeft
        textRect6.top = 4*innerBoxHeight + paddingUp + (innerBoxHeight/4)
        
        win.blit(text, textRect)
        win.blit(text2, textRect2)
        win.blit(text3, textRect3)
        win.blit(text4, textRect4)
        win.blit(text5, textRect5)
        win.blit(text6, textRect6)

        #hadding text
        textSize3 = int((0.5*paddingUp)*0.59)
        font3 = pygame.font.Font("freesansbold.ttf", textSize3)
        text7 = font3.render("Parking Management System", True, WHITE, BGCOLOR)
        textRect7 = text7.get_rect()
        textRect7.center = (WIDTH/2,paddingUp/2)
        win.blit(text7, textRect7)

    def actions(self,x,y):
        if (x>textRect3.left and x<textRect3.right) and (y>textRect3.top and y<textRect3.bottom):
            self.innerBox1Clicked = False
            self.innerBox2Clicked = False
            if self.forgottenPasswordClicked:
                self.forgottenPasswordClicked = False
            else:
                admin.forgottenPasswordClicked = True
        elif (x>leftPadding+paddingLeft and x<leftPadding+paddingLeft+innerBoxWidth) and (y>2*innerBoxHeight+paddingUp and y<3*innerBoxHeight+paddingUp):
            self.innerBox2Clicked = False
            if self.innerBox1Clicked:
                self.innerBox1Clicked = False
            else:
                self.innerBox1Clicked = True
        elif (x>leftPadding+paddingLeft and x<leftPadding+paddingLeft+innerBoxWidth) and (y>4*innerBoxHeight+paddingUp and y<5*innerBoxHeight+paddingUp):
            self.innerBox1Clicked = False
            if self.innerBox2Clicked:
                self.innerBox2Clicked = False
            else:
                self.innerBox2Clicked = True
        elif (x>leftPadding+paddingLeft and x<leftPadding+paddingLeft+innerBoxWidth) and (y>6*innerBoxHeight+paddingUp and y<7*innerBoxHeight+paddingUp):
            if self.username in data and data[self.username] == self.password:
                self.signinButtonClicked = True

class Menu:
    def __init__(self):
        self.selected = "Dashboard"

    def draw(self):
        global headerHeight, sidebarWidth
        win.fill(BGCOLOR2)

        #header
        headerHeight = int(0.09*HEIGHT) #9% of the height of the screen
        pygame.draw.rect(win, WHITE, (0, 0, WIDTH, headerHeight))
        #bliting text
        textSize = int((headerHeight)*0.8)
        font = pygame.font.Font("freesansbold.ttf",textSize)
        text = font.render("Admin", True, CYAN, WHITE)
        textRect = text.get_rect()
        textRect.bottom = headerHeight - 3
        textRect.left = 10
        win.blit(text, textRect)
        #image of login logo
        loginLogo = pygame.image.load("adminLogo.png")
        loginLogo = pygame.transform.scale(loginLogo, (int(0.05*WIDTH), headerHeight-2))
        loginLogoRect = loginLogo.get_rect()
        loginLogoRect.top = 1
        loginLogoRect.right = WIDTH-1
        win.blit(loginLogo, loginLogoRect)

        #sidebar
        sidebarWidth = int(WIDTH*0.2) # 20% of the width of the screen
        pygame.draw.rect(win, WHITE, (0, headerHeight, sidebarWidth, HEIGHT-headerHeight))
        #sidebar inner boxes
        sidebarBoxHeight = int(0.07*(HEIGHT-headerHeight))  # 7% of the height of the sidebar
        def drawSmallBox(boxNumber, imageAdress, txt):
            if txt == self.selected:
                pygame.draw.rect(win, LIGHTGREY, (0,(boxNumber*sidebarBoxHeight)+headerHeight, sidebarWidth, sidebarBoxHeight))
            else:
                pygame.draw.rect(win, LIGHTGREY, (0,(boxNumber*sidebarBoxHeight)+headerHeight, sidebarWidth, sidebarBoxHeight), 1)
            #img
            img = pygame.image.load(imageAdress)
            sidebarLogoWidth = int(0.15*sidebarWidth)  # 15% of the sidebar width
            img = pygame.transform.scale(img, (sidebarLogoWidth, sidebarBoxHeight-2))
            imgRect = img.get_rect()
            imgRect.center = (sidebarLogoWidth/2, (sidebarBoxHeight*boxNumber)+sidebarBoxHeight/2 + headerHeight)
            win.blit(img, imgRect)
            #bliting text
            textSize = int((sidebarBoxHeight)*0.5)
            font = pygame.font.Font("freesansbold.ttf",textSize)
            if txt == self.selected:
                text = font.render(txt, True, EXTRALIGHTBLUE, LIGHTGREY)
            else:
                text = font.render(txt, True, GREY, WHITE)
            textRect = text.get_rect()
            textRect.top = (sidebarBoxHeight*boxNumber) + headerHeight + (sidebarBoxHeight - (textRect.bottom-textRect.top))/2
            textRect.left = sidebarLogoWidth + 3
            win.blit(text, textRect)

        menu = ["Dashboard","Vehical Category","Add Vehicle","Manage Vehicle","Reports","Search Vehicle"]
        images = ["Dashboard.png","Category.jpg","Plus.png","manage.png","report.png","search.png"]
        for i in range(len(menu)):
            drawSmallBox(i,images[i],menu[i])

class Dashboard:
    def __init__(self):
        self.todaysVehicleEntries = 0
        self.yesterdaysVehicleEntries = 0
        self.sevenDaysVehicleEntries = 0
        self.totalvehicleEntries = 0

    def draw(self):
        workingAreaHeight = HEIGHT - headerHeight
        workingAreaWidth = WIDTH - sidebarWidth
        paddingWidth = int(0.15*(workingAreaWidth/2))  # 15% of the working area
        paddingHeight = int(0.15*(workingAreaHeight/2))  # 15% of the working area
        smallBoxHeight = int((workingAreaHeight/2) - paddingHeight*2)
        smallBoxWidth = int((workingAreaWidth/2) - paddingWidth*2)

        #drawing boxes
        pygame.draw.rect(win, WHITE, (sidebarWidth+paddingWidth, headerHeight+paddingHeight, smallBoxWidth, smallBoxHeight))
        pygame.draw.rect(win, WHITE, (sidebarWidth+paddingWidth, (workingAreaHeight/2) + headerHeight+paddingHeight, smallBoxWidth, smallBoxHeight))
        pygame.draw.rect(win, WHITE, (sidebarWidth+paddingWidth + (workingAreaWidth/2), headerHeight+paddingHeight, smallBoxWidth, smallBoxHeight))
        pygame.draw.rect(win, WHITE, (sidebarWidth+paddingWidth + (workingAreaWidth/2), headerHeight+paddingHeight + (workingAreaHeight/2), smallBoxWidth, smallBoxHeight))

admin = AdminLogin()
menu = Menu()
db = Dashboard()

#main loop
while run:
    #event handling loop
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if screenOne:
            if admin.innerBox1Clicked:
                if event.type == pygame.KEYDOWN:
                    if admin.forgottenPasswordClicked:
                        if event.key == pygame.K_BACKSPACE:
                            admin.email = admin.email[:-1]
                        else:
                            admin.email += event.unicode
                    else:
                        if event.key == pygame.K_BACKSPACE:
                            admin.username = admin.username[:-1]
                        else:
                            admin.username += event.unicode
            elif admin.innerBox2Clicked:
                if event.type == pygame.KEYDOWN:
                    if admin.forgottenPasswordClicked:
                        if event.key == pygame.K_BACKSPACE:
                            admin.mobileNumber = admin.email[:-1]
                        else:
                            admin.mobileNumber += event.unicode
                    else:
                        if event.key == pygame.K_BACKSPACE:
                            admin.password = admin.password[:-1]
                        else:
                            admin.password += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                admin.actions(x,y)

    win.fill(BGCOLOR)
    if admin.signinButtonClicked:
        menuScreen = True
        screenOne = False
    if menuScreen:
        menu.draw()
    if screenOne:
        admin.draw()
    elif menu.selected == "Dashboard":              # chances of error here
        db.draw()
    pygame.display.update()
