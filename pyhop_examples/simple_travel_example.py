"""
The "travel from home to the park" example from my lectures.
Author: Dana Nau <nau@cs.umd.edu>, May 31, 2013
This file should work correctly in both Python 2.7 and Python 3.2.
"""

import pyhop

def taxi_rate(dist):
    return (1.5 + 0.5 * dist)

def walk(state,a,x,y):
    if state.loc[a] == x:
        state.loc[a] = y
        return state
    else: return False

def call_taxi(state,a,x):
    state.loc['taxi'] = x
    return state
    
def ride_taxi(state,a,x,y):
    if state.loc['taxi']==x and state.loc[a]==x:
        state.loc['taxi'] = y
        state.loc[a] = y
        state.owe[a] = taxi_rate(state.dist[x][y])
        return state
    else: return False

def pay_driver(state,a):
    if state.cash[a] >= state.owe[a]:
        state.cash[a] = state.cash[a] - state.owe[a]
        state.owe[a] = 0
        return state
    else: return False

def buy_plane_ticket(state,a,cost):
    if state.cash[a] >= cost:
        state.cash[a] = state.cash[a] - cost
        return state
    else: return False

def fly_on_plane(state,a,dest):
    if state.loc[a]=='airport':
        state.loc[a] = dest
        return state
    else: return False

pyhop.declare_operators(walk, call_taxi, ride_taxi, pay_driver, buy_plane_ticket, fly_on_plane)
print('')
pyhop.print_operators()


def travel_by_foot(state,a,x,y):
    if state.dist[x][y] <= 2:
        return [('walk',a,x,y)]
    return False

def travel_by_taxi(state,a,x,y):
    if state.cash[a] >= taxi_rate(state.dist[x][y]):
        return [('call_taxi',a,x), ('ride_taxi',a,x,y), ('pay_driver',a)]
    return False

pyhop.declare_methods('travel',travel_by_foot, travel_by_taxi)


def travel_by_plane(state,a,x,y,cost):
    if state.cash[a] >= (cost + taxi_rate(state.dist[x]['airport'])):
        if state.dist[x]['airport'] <= 2:
            return [('buy_plane_ticket',a),('walk',a,x,'airport'),('fly_on_plane',a,x,y)]
        else:
            return [('buy_plane_ticket',a,cost), ('call_taxi',a,x), ('ride_taxi',a,x,'airport'), ('pay_driver',a), ('fly_on_plane',a,y)]
    return False

pyhop.declare_methods('flying',travel_by_plane)

print('')
pyhop.print_methods()

state1 = pyhop.State('state1')
state1.loc = {'me':'home'}
state1.cash = {'me':20}
state1.owe = {'me':0}
state1.dist = {'home':{'park':8}, 'park':{'home':8}}

print("""
********************************************************************************
Call pyhop.pyhop(state1,[('travel','me','home','park')]) with different verbosity levels
********************************************************************************
""")

print("- If verbose=0 (the default), Pyhop returns the solution but prints nothing.\n")
pyhop.pyhop(state1,[('travel','me','home','park')])

print('- If verbose=1, Pyhop prints the problem and solution, and returns the solution:')
pyhop.pyhop(state1,[('travel','me','home','park')],verbose=1)

print('- If verbose=2, Pyhop also prints a note at each recursive call:')
pyhop.pyhop(state1,[('travel','me','home','park')],verbose=2)

print('- If verbose=3, Pyhop also prints the intermediate states:')
pyhop.pyhop(state1,[('travel','me','home','park')],verbose=3)

state2 = pyhop.State('state2')
state2.loc = {'Sammy':'Oxy'}
state2.cash = {'Sammy':40}
state2.owe = {'Sammy':0}
state2.dist = {'Oxy':{'home':20}, 'home':{'Oxy':20}}

pyhop.pyhop(state2,[('travel','Sammy','Oxy','home')],verbose=1)

state3 = pyhop.State('state3')
state3.loc = {'Lex':'Oxy'}
state3.cash = {'Lex':1000}
state3.owe = {'Lex':0}
state3.dist = {'Oxy':{'airport':25}, 'airport':{'Oxy':25}, 'airport':{'New York':1000}, 'New York':{'airport':1000}}

pyhop.pyhop(state3,[('flying','Lex','Oxy','New York',500)],verbose=1)