# This is the final assignment of Data Visualization course @coursera.org part1

#import libs
import pandas
import numpy
import matplotlib.pyplot as plt

# I. Topic Survey
# I.1. read_csv

SurveyFrame = pandas.read_csv('data/Topic_Survey_Assignment.csv')
print(SurveyFrame)

# I.2. bar plot
# Plan:
# 1. Sort the dataframe in descending order of Very interested.
SurveyFrame.sort_values(['Very interested'], ascending = False, axis = 0, inplace = True)
print(SurveyFrame)
# 2. Convert the numbers into percentages of the total number of respondents. Recall that 2, 233 respondents completed the survey. Round percentages to 2 decimal places.
for i in SurveyFrame.index:
    SurveyFrame.loc[i] = SurveyFrame.loc[i] / numpy.sum(SurveyFrame.loc[i])
print(SurveyFrame)
# As for the chart:
# use a figure size of(20, 8),
# bar width of 0.8,
# use color  # 5cb85c for the Very interested bars, color #5bc0de for the Somewhat interested bars, and color #d9534f for the Not interested bars,
# use font size 14 for the bar labels, percentages, and legend,
# use font size 16 for the title, and ,
# display the percentages above the bars as shown above, and remove the left, top, and right borders.

# %matplotlib inline

ax = SurveyFrame.plot(kind='bar', figsize=(20, 8), width=0.8,
                 color=('#5cb85c', '#5bc0de', '#d9534f'))

plt.title("Percentage of Respondents' Interest in Data Science Areas", fontsize=16)
plt.legend(fontsize = 14)
plt.xticks(fontsize = 14)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
for p in ax.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    plt.annotate('{:.2%}'.format(height), (x, y + height + 0.01), fontsize = 14)

plt.show()

