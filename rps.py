print('Lets play Rock Paper Scissors!\nYou have to get a score of 3')
player = input('Rock,paper or scissor(r,p,s): ')
tries = 3
score = 0
while True:
    import random
    list1 = ['rock','paper','scissor']
    comp_out = random.choice(list1)
    
    
    #Player chooses scissor
    if player.lower() == comp_out[0]:
        print('Same Choice!')
        print('Computer score :{}'.format(3 - tries))
        print('Your score :{}'.format(score))
    elif player.lower() == 's':
        if comp_out == 'rock':
            print('Computer wins! its a rock from comp!')
            tries = tries - 1
            print('Computer score :{}'.format(3 - tries))
            print('Your score :{}'.format(score))
        elif comp_out == 'paper':
            print('You win this one! Comp chose paper')
            score = score + 1
            print('Computer score :{}'.format(3 - tries))
            print('Your score :{}'.format(score))
    
    #Player chooses rock 
    elif player.lower() == 'r':
        if comp_out == 'paper':
            print('Computer wins! its a paper from comp!')
            tries = tries - 1
            print('Computer score :{}'.format(3 - tries))
            print('Your score :{}'.format(score))
        elif comp_out == 'scissor':
            print('You win this one! Comp chose scissor')
            score = score + 1
            print('Computer score :{}'.format(3 - tries))
            print('Your score :{}'.format(score))
    
    #Player chooses paper
    elif player.lower() == 'p':
        if comp_out == 'scissor':
            print('Computer wins! scissor from comp!')
            tries = tries - 1
            print('Computer score :{}'.format(3 - tries))
            print('Your score :{}'.format(score))
        elif comp_out == 'rock':
            print('You win this one! Comp chose rock')
            score = score + 1
            print('Computer score :{}'.format(3 - tries))
            print('Your score :{}'.format(score))
            
    # Player wins 
    if score == 3:
        print('You win the game!')
        break
        
    if tries == 0:
        print('Computer wins')
        break
    
    print('\n')
    player = input('Rock,paper or scissor(r,p,s): ')