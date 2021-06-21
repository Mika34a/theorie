# s_annealing.py
#
# Programmeertheorie
# Merel Florian, Michael Verdel, Joshua van Zanten
#
# - Implements a simulated annealing algorithm to connect houses to batteries with capacity. 

def run(self, smartgrid):
    pass
#Herhaal:
    #Kies een random start state
    start_state = smartgrid.connections_dict
    cost_old = smartgrid.cost
    #Kies start temperatuur
    T = 100
    #Herhaal N iteraties:
    for i in range(0, 50):
        #Doe een kleine random aanpassing
        new_dict = start_state.change_r()
        cost_new = new_dict.cost

        #Als random( ) > kans(oud, nieuw, temperatuur): (acceptatiekans = 2^( score_old – score_new ) / temperatuur)

        if cost_new < cost_old:
            cost_old = cost_new
        else:
            accept_p = 2^(start_state - cost_new) / T
            if ...
                #Maak de aanpassing ongedaan

        #Verlaag temperatuur
        T -= 1