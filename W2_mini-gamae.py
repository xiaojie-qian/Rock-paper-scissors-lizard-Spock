#!/usr/bin/env python
# coding: utf-8

# ### Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of Rock-paper-scissors that allows five choices. 
# 
# #### Each choice wins against two other choices, loses against two other choices and ties against itself. Much of RPSLS's popularity is that it has been featured in 3 episodes of the TV series "The Big Bang Theory". The Wikipedia entry for RPSLS gives the complete description of the details of the game.Scissors cuts Paper
# 
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# (and as it always has) Rock crushes Scissors

# In[55]:


import random


# In[12]:


def name_to_number(name):
    '''Build a helper function name_to_number that converts the string names - rock, spock, paper, lizard or scissors- into a number between 0 and 4'''
    if name == 'rock':
        name_to_number = 0
    elif name == 'spock': 
        name_to_number = 1
    elif name == 'paper': 
        name_to_number = 2
    elif name == 'lizard': 
        name_to_number = 3
    elif name == 'scissors': 
        name_to_number = 4
    else:
        print ('Please input rock, spock, paper, lizard or scissors')
    return name_to_number


# In[13]:


name_to_number('spock')


# In[34]:


def number_to_name(number):
    '''Build a helper function number_to_name that converts number between 0 and 4 into string names - rock, spock, paper, lizard or scissors'''
    if  number == 0:
        number_to_name = 'rock'
    elif number == 1: 
        number_to_name = 'Spock'
    elif number == 2: 
        number_to_name = 'paper'
    elif number == 3: 
        number_to_name = 'lizard'
    elif number == 4: 
        number_to_name = 'scissors'
    else:
        print ('please input a number between 0 to 4')
    return number_to_name


# In[36]:


number_to_name(4)


# #### Below is the complete program of the mini-game: 

# In[134]:


print ("\n")
def rpsls(player_choice): 
    def name_to_number(player_choice):
        if player_choice == 'rock':
            print ("Player chooces "+ player_choice)
            name_to_number = 0
        elif player_choice == 'spock': 
            print ("Player chooces "+ player_choice)
            name_to_number = 1
        elif player_choice == 'paper':     
            print ("Player chooces "+ player_choice)
            name_to_number = 2
        elif player_choice == 'lizard':    
            print ("Player chooces "+ player_choice) 
            name_to_number = 3
        elif player_choice == 'scissors':     
            print ("Player chooces "+ player_choice)
            name_to_number = 4
        else:
            print ('Please input rock, spock, paper, lizard or scissors')
        return name_to_number
    number = random.randrange(0,5)
    def number_to_name(number):
        if  number == 0:
            number_to_name = 'rock'
        elif number == 1: 
            number_to_name = 'Spock'
        elif number == 2: 
            number_to_name = 'paper'
        elif number == 3: 
            number_to_name = 'lizard'
        elif number == 4: 
            number_to_name = 'scissors'
        else:
            print ('please input a number between 0 to 4')
        return number_to_name
    
    player_number = name_to_number(player_choice)
    computer_choice = number_to_name(number)
    print('Computer choices '+ computer_choice)
    if player_number - number in range(1,3):
        print('Player wins!')
    elif number - player_number in range(1,3):
        print('Computer wins!')
    else: 
        print('Player and computer tie!')
    return rpsls


# In[135]:


rpsls('lizard')


# In[136]:


rpsls('paper')


# In[137]:


rpsls('scissors')


# In[138]:


rpsls('rock')


# In[139]:


rpsls('spock')


# #### Input your parameter into rpsls()

# In[ ]:




