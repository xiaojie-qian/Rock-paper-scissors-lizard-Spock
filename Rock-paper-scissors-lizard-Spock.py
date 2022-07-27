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

# #### Below is the complete program of the mini-game: 

# In[13]:


import random


# In[46]:


def name_to_number(name):
    '''Build a helper function name_to_number that converts the string names - rock, spock, paper, lizard or scissors- into a number between 0 and 4'''
    if name == 'rock':
        return 0
    elif name == 'Spock': 
        return 1
    elif name == 'paper': 
        return 2
    elif name == 'lizard': 
        return 3
    elif name == 'scissors': 
        return 4
    else:
        print ('Please input rock, spock, paper, lizard or scissors')


# In[30]:


name_to_number('spock')


# In[31]:


def number_to_name(number):
    '''Build a helper function number_to_name that converts number between 0 and 4 into string names - rock, spock, paper, lizard or scissors'''
    if  number == 0:
        return 'rock'
    elif number == 1: 
        return 'Spock'
    elif number == 2: 
        return 'paper'
    elif number == 3: 
        return 'lizard'
    elif number == 4: 
        return 'scissors'
    else:
        print ('please input a number between 0 to 4')


# In[32]:


number_to_name(4)


# In[55]:


def rpsls(player_choice):
    print ("\n")
    print ("Player choices "+ player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randint(0,4)
    comp_choice = number_to_name(comp_number)    
    print('Computer choices '+ comp_choice)
    modulo = (comp_number - player_number)%5
    if modulo == 1 or modulo == 2:
        print("Computer wins!")
    elif modulo == 3 or modulo == 4:
        print("Player wins!")
    else: 
        print("Player and computer tie!")


# #### Input your parameter into rpsls()

# In[54]:


rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


# In[ ]:




