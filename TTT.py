# Name      : Ankush Singh
# A.K.A     : Ankush Tech Creator (ATC)
# Email     : ankush4singh@gmail.com
import random

print('Code By : Ankush Singh')
print('GitHub  : https://GitHub.com/ATCtech')
print('Website : http://AnkushTechCreator.com\n')
board={
    'TL':'-','TM':'-','TR':'-',
    'ML':'-','MM':'-','MR':'-',
    'BL':'-','BM':'-','BR':'-'
}

possible_places=['TL','TM','TR','ML','MM','MR','BL','BM','BR']
total_turns=0
game_ended=False
player_turn=True

def init():
    global player_turn
    global total_turns
    global possible_places
    global game_ended
    
    board["TL"]='-';board["TM"]='-';board["TR"]='-'
    board["ML"]='-';board["MM"]='-';board["MR"]='-'
    board["BL"]='-';board["BM"]='-';board["BR"]='-'
    
    total_turns=0
    player_turn=True
    game_ended=False
    possible_places=['TL','TM','TR','ML','MM','MR','BL','BM','BR']
    
    print('Place your X/O on the board using the following commands\n')
    print('TL|TM|TR')
    print('ML|MM|MR')
    print('BL|BM|BR\n')
    print('e.g. if you want to place in the top right place, type TR')
    print('e.g. if you want to place in the bottom middle place, type BM\n')

def print_board():
    print(f'{board["TL"]}|{board["TM"]}|{board["TR"]}')
    print(f'{board["ML"]}|{board["MM"]}|{board["MR"]}')
    print(f'{board["BL"]}|{board["BM"]}|{board["BR"]}\n')
    
def play_again():
    again = input('\nWanna Play Again? (y/n) : ')
    if(again=='y'):
        play()
    else :
        print('Thanks For Playing')

def who_won(p):
    global game_ended
    if p=='X':
        print('You Won, congrats')
    elif p=='O':
        print('Computer Won, lmao')
    game_ended=True
    play_again()
    
    
def chk_win():
    #check horizontally
    if   board['TL']==board['TM']==board['TR']!='-':
        who_won(board['TM'])
    elif board['ML']==board['MM']==board['MR']!='-':
        who_won(board['MM'])
    elif board['BL']==board['BM']==board['BR']!='-':
        who_won(board['BM'])
    #check vertically
    elif board['TL']==board['ML']==board['BL']!='-':
        who_won(board['ML'])
    elif board['TM']==board['MM']==board['BM']!='-':
        who_won(board['MM'])
    elif board['TR']==board['MR']==board['BR']!='-':
        who_won(board['MR'])
    #check diagonally
    elif board['TL']==board['MM']==board['BR']!='-':
        who_won(board['MM']) 
    elif board['TR']==board['MM']==board['BL']!='-':
        who_won(board['MM'])
        

def play():
    global player_turn
    global total_turns
    init()
    while total_turns<9 and not game_ended:
        if player_turn :
            while True :
                place=input('Your Turn : ')
                if place in possible_places :
                    board[place]='X'
                    del possible_places[possible_places.index(place)]
                    break
                else :
                    print('\nwrong input try again\n')
            player_turn=False
        else :
            place = random.choice(possible_places)
            print(f'Computers Turn : {place}')
            board[place]='O'
            del possible_places[possible_places.index(place)]
            player_turn=True
        print_board()
        chk_win()
        total_turns+=1
    if total_turns>=9:
        print('lol, its a tie\n')
        play_again()
        
        
play()
    
    



