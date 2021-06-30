import csv
import collections
import pygal

# with open("NetflixViewingHistory.csv", "r", encoding='utf-8') as file:
#     years = { }
#     reader = csv.reader(file, delimiter=",")
#     header = next(reader)
#
#     # reach all the shows
#     for row in reader:
#         # get just the show/movie name, not the episode
#         show = row[0].split(':')[0]
#         # get the whole year
#         year = "20" + row[1][-2:]
#
#         if year in years.keys():
#             shows = years[year]
#             years[year][show] = shows[show] + 1 if show in shows.keys() else 1
#         else:
#            years[year] = {show : 1}
#
# # get the year and show of the shows that are less than binge worthy
# bingeWorthy = 10 #episodes
# keys = collections.defaultdict(list)
# for year in years:
#     for show in years[year]:
#         if years[year][show] < bingeWorthy:
#             keys[year].append(show)
#
# # delete the less than binge worthy shows
# for year in keys:
#     shows = keys[year]
#     for show in shows:
#         del(years[year][show])



with open("NetflixViewingHistory.csv", "r", encoding='utf-8') as file:
    years = { }
    reader = csv.reader(file, delimiter=",")
    header = next(reader)

    showDates = collections.defaultdict(list)
    # reach all the shows
    for row in reader:
        show = row[0].split(':')[0]
        year = row[1][-2:]

        showDates[show].append(year)
# print(showDates)

# # get shows that were less than binge worthy
bingeWorthy = 10 #episodes
badShows = []
for show in showDates:
    years = showDates[show]
    if len(years) < bingeWorthy:
        badShows.append(show)

# delete the less than binge worthy shows
for show in badShows:
    del(showDates[show])

shows = collections.defaultdict(list)
for show in showDates:
    print(show)
    print(showDates[show])
    for i in range(14,22):
        print(showDates[show].count(str(i)))
        shows[show].append(showDates[show].count(str(i)))
    break
# print(shows)



# bar_chart = pygal.StackedBar()
# bar_chart.title = "Netflix Binge History (> 15 episodes per year)"
# bar_chart.x_labels = map(str, range(2014, 2021))
# for year in years:
#     for show
# bar_chart.render_to_file('bar_chart.svg')                          # Save the svg to a file
