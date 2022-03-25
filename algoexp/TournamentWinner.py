# There's an algorithms tournament taking place in which teams of programmers compete against
# each other to solve algorithmic problems as fast as possible. Teams compete in a round robin,
# where each team faces off against all other teams. Only two teams compete against each other at a
# time, and for each competition, one team is designated the home team, while the other team is the
# away team. In each competition there's always one winner and one loser; there are no ties. A team
# receives 3 points if it wins and O points if it loses. The winner of the tournament is the team that
# receives the most amount of points.
# Given an array of pairs representing the teams that have competed against each other and an array
# containing the results of each competition, write a function that returns the winner of the
# tournament. The input arrays are named competitions and results, respectivelv. The
# competitions array has elements in the form of [homeTeam, awayTeam] , where each team
# is a string of at most 30 characters representing the name of the team. The results array
# contains information about the winner of each corresponding competition in the competitions
# array. Specifically, results[i] denotes the winner of competitions[i] , where a 1 in the
# results array means that the home team in the corresponding competition won and a 0
# results array means that the home team in the corresponding competition won and a o
# means that the away team won.
# It's guaranteed that exactly one team will win the tournament and that each team will compete
# against all other teams exactly once. It's also guaranteed that the tournament will always have at
# least two teams.

def tournamentWinner(competitions, results):
    # Write your code here.
    count = 0

    # set of all lang
    # dict with lang and 0 initialized score
    # run loop on results
    #	count=0 increase counter by 1 and find lang by comp[][] put in string and update dict
    listOfLanguages = []
    for innerList in competitions:
        listOfLanguages.extend([innerList[0], innerList[1]])
    uniqueListOfLanguages = list(set(listOfLanguages))
    ranksOfLanguages = [0 for i in range(len(uniqueListOfLanguages))]
    dictRanks = dict(dict(zip(uniqueListOfLanguages, ranksOfLanguages)))
    # print(dictRanks)
    for r in results:
        if r == 0:
            dictRanks[competitions[count][1]] += 1
        else:
            dictRanks[competitions[count][0]] += 1
        count += 1
    listKeys = list(dictRanks.keys())
    listValues = list(dictRanks.values())
    maxIndex = listValues.index(max(listValues))
    winner = listKeys[maxIndex]
    return winner
competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ]
results = [0, 0, 1]
print(tournamentWinner(competitions, results))

# res = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
# list_a = []
# for l in res:
#     list_a.extend([l[0],l[1]])
# print(list_a)

# Convert List of lists to list of Strings
# using list comprehension + join()
# test_list = [["g", "f", "g"], ["i", "s"], ["b", "e", "s", "t"]]
# res = [''.join(ele) for ele in test_list]

# list_keys = {1,2,3,4}
# list_values = {'Mon','Tue','Wed','Thu'}
# new_dict = dict(zip(list_keys, list_values))
# print(new_dict)

# new_dict = dict(x= 5, y=2)
# print(new_dict)
# new_dict1 = dict([('x',1),('y',2)])
# print(new_dict1)
# numbers2 = dict([('x', 5), ('y', -5)], z=8)
# print('numbers2 =',numbers2)
# # keyword argument is not passed
# numbers1 = dict([('x', 5), ('y', -5)])
# print('numbers1 =',numbers1)
#
# # keyword argument is also passed
# numbers2 = dict([('x', 5), ('y', -5)], z=8)
# print('numbers2 =',numbers2)
#
# # zip() creates an iterable in Python 3
# numbers3 = dict(dict(zip(['x', 'y', 'z'], [1, 2, 3])))
# print('numbers3 =',numbers3)
#
# person = {}
#
# # Using get() results in None
# print('Salary: ', person.get('salary'))
#
#
# # Using [] results in KeyError
# print(person['salary'])


# creating a new dictionary
# my_dict = {"java": 100, "python": 112, "c": 11}
#
# # list out keys and values separately
# key_list = list(my_dict.keys())
# val_list = list(my_dict.values())
#
# # print key with val 100
# position = val_list.index(100)
# print(key_list[position])
#
# # print key with val 112
# position = val_list.index(112)
# print(key_list[position])
#
# # one-liner
# print(list(my_dict.keys())[list(my_dict.values()).index(112)])