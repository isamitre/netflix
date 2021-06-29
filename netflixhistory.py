import csv
import collections

with open("NetflixViewingHistory.csv", "r", encoding='utf-8') as file:
    years = { }
    reader = csv.reader(file, delimiter=",")
    header = next(reader)

    # reach all the shows
    for row in reader:
        # get just the show/movie name, not the episode
        show = row[0].split(':')[0]
        # get the whole year
        year = "20" + row[1][-2:]

        if year in years.keys():
            shows = years[year]
            years[year][show] = shows[show] + 1 if show in shows.keys() else 1
        else:
           years[year] = {show : 1}

# get the year and show of the shows that are less than binge worthy
bingeWorthy = 10 #episodes
keys = collections.defaultdict(list)
for year in years:
    for show in years[year]:
        if years[year][show] < bingeWorthy:
            keys[year].append(show)

# delete the less than binge worthy shows
for year in keys:
    shows = keys[year]
    for show in shows:
        del(years[year][show])

print(years)
