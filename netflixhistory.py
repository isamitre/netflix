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
bingeWorthy = 20 #episodes
badShows = []
for show in showDates:
    years = showDates[show]
    if len(years) < bingeWorthy:
        badShows.append(show)

# delete the less than binge worthy shows
for show in badShows:
    del(showDates[show])

# put the shows in the correc format for the graph
shows = collections.defaultdict(list)
for show in showDates:
    for i in range(14,22):
        shows[show].append(showDates[show].count(str(i)))
# print(shows)

# make the stacked bar chart
bar_chart = pygal.StackedBar()
bar_chart.title = "Netflix Binge History (> " + str(bingeWorthy) + " episodes)"
bar_chart.x_labels = map(str, range(2014, 2022))
for show in shows:
    bar_chart.add(show, shows[show])
bar_chart.render_to_file('netflix_bar_chart.svg')

# sort for the pie_chart
sorted_shows = collections.defaultdict(list)
for show in shows:
    sorted_shows[show] = sum(shows[show])
sorted_shows = dict(sorted(sorted_shows.items(), key=lambda item: item[1], reverse=True))
print(sorted_shows)


# make the pie_chart
bar_chart = pygal.Pie()
bar_chart.title = "Netflix Binge History (> " + str(bingeWorthy) + " episodes)"
for show in sorted_shows:
    bar_chart.add(show, sorted_shows[show])
bar_chart.render_to_file('netflix_pie_chart.svg')
