input = [["HTML","C#"], ["C#","Python"], ["Python","HTML"]]
results = [0,0,1]
# go through array and record count(+3) for each element in dictionary
# keep track of max count and print it

# T: O(N) | S: O(k+1) ~ O(K)
# hashmap_languages = {'':0}
# bestTeam = ""
# for each in range(len(input)):
#     winner = input[each][1-results[each]]
#     if winner not in hashmap_languages:
#         hashmap_languages[winner] = 3
#     else:
#         hashmap_languages[winner] += 3
#     if(hashmap_languages[winner] > hashmap_languages[bestTeam]):
#         bestTeam = winner
# del hashmap_languages['']
# print(hashmap_languages)
# print(bestTeam)

#########################################################################

# T: O(N) | S: O(k+1) ~ O(K)

def tournamentWinner(competitions, results):
    HOME_TEAM_WON = 1
    
    currentBestTeam = ''
    scores = {currentBestTeam : 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam

        updateScores(winningTeam, scores, 3)

        if(scores[winningTeam] > scores[currentBestTeam]):
            currentBestTeam = winningTeam
    return currentBestTeam

def updateScores(winningTeam, scores, increment):
    if winningTeam not in scores:
        scores[winningTeam] = 0
    scores[winningTeam] += increment

print(tournamentWinner(input, results))