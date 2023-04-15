from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import interval
# import measurements as mn

# Замерял за день до повторения эксперемента, была построена плохая гистограмма
# К моему удивлению прогамма стала считать быстрее на 1 сек. (датасет не менял)
# list_of_values = ["01ss::538ms", "01ss::649ms", "01ss::567ms",
#     "01ss::656ms", "01ss::608ms", "01ss::611ms", "01ss::626ms", 
#     "01ss::626ms","01ss::608ms", "01ss::588ms",
#     "01ss::643ms","01ss::604ms","01ss::615ms","01ss::627ms",
#     "01ss::622ms","01ss::625ms","01ss::618ms","01ss::592ms",
#     "01ss::590ms","01ss::599ms", "01ss::598ms", "01ss::569ms",
#     "01ss::606ms","01ss::596ms","01ss::673ms","01ss::616ms",
#     "01ss::574ms","01ss::566ms","01ss::672ms","01ss::588ms",
#     "01ss::649ms", "01ss::583ms","01ss::607ms","01ss::578ms","01ss::617ms",
#     "01ss::654ms","01ss::670ms","01ss::688ms","01ss::764ms","01ss::653ms" ]

# для запуска замеров из терминала
# t=mn.t
# with open("results.txt","a") as file:
#     print(t, file=file)

# t = [0.489, 0.481, 0.478, 0.477, 0.476, 0.487, 0.478, 0.485, 0.489, 0.478, 0.486, 0.478, 0.483, 0.479, 0.483, 0.477, 0.481, 0.48, 0.485, 0.484, 0.48, 0.48, 0.48, 0.475, 0.479, 0.479, 0.477, 0.479, 0.477, 0.48, 0.476, 0.48, 0.479, 0.483, 0.477, 0.479, 0.484, 0.476, 0.475, 0.485]
t = [0.479, 0.48, 0.476, 0.482, 0.486, 0.485, 0.484, 0.485, 0.487, 0.48, 0.483, 0.478, 0.481, 0.489, 0.489, 0.478, 0.482, 0.479, 0.481, 0.486, 0.474, 0.483, 0.476, 0.485, 0.491, 0.482, 0.48, 0.483, 0.481, 0.481, 0.479, 0.482, 0.482, 0.486, 0.479, 0.469, 0.481, 0.484, 0.483, 0.483]

plt.hist(t,facecolor = 'green')
# plt.show()

(stat,p_value) = stats.normaltest(t)
print(p_value)

average = np.mean(t)
print(average)

standart_deviation = (sum(list(map(lambda x: (average-x) ** 2, t)))/(len(t)-1))**(0.5)
print(standart_deviation)

standart_deviation_average = standart_deviation/((len(t))**(0.5))
print(standart_deviation_average)

predictive_interval = interval.Interval(average - 2*standart_deviation, average + 2*standart_deviation)
print(predictive_interval)

confidence_interval = interval.Interval(average - 2*standart_deviation_average, average + 2*standart_deviation_average)
print(confidence_interval)

print(2*standart_deviation)