import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.lines import Line2D


data = pd.read_csv('weather_2023.csv')


print(data.columns.tolist())

# добавление макс и мин температур на график
date, temp = [], []

for i in data['DATE']:
    date.append(i)

for j in data['TAVG']:
    temp.append(j)

# print(date)
# print(temp)

# значения оси Х и Y
x_val = list(range(1, 366))
y_val = temp

fig, ax = plt.subplots(1,1, figsize=(12,5))



# дата макс и мин температур
max_t_date = temp.index(max(temp))
min_t_date = temp.index(min(temp))

max_t = max(temp)
min_t = min(temp)

# обьбозначение макс и мин температуры на графике
max_min = [
    Line2D([0], [0], marker='o', color='w', label=(f"Max avg temperature: {max_t} : {date[max_t_date]}"),
                          markerfacecolor='r', markersize=8),
    Line2D([0], [0], marker='o', color='w', label=(f"Min avg temperature: {min_t} : {date[min_t_date]}"),
                          markerfacecolor='b', markersize=8),
         ]



ax.legend(handles=max_min, loc='upper left')

# обозначение кривой
ax.plot(x_val, y_val, linewidth=1)


# отображение точек на графике
ax.scatter(x_val, y_val, s=7, color='black')

# отображение min max температур на графике
ax.scatter(max_t_date + 1, max_t, s=10, color='red')
ax.scatter(min_t_date + 1, min_t, s=10, color='blue')

# добавление линии 0℃
ax.axhline(y=0, color="grey", linestyle="--")

# параметры названия осей и графика
ax.set_title("График температуры в Санкт-Петербурге 2023г.", fontsize=20)
ax.set_ylabel("Temperature °C", fontsize=15)
ax.set_xlabel("Dates", fontsize=15)

# диапазон осей
ax.axis([0, 370, -30, 40])

# отображение месяцев на оси Х
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth = range(1, 13)))

#сетка на графике
plt.grid()


# функция показывающая информацию о точке по лкм
x = x_val
y = y_val

new_date = []
new_t = []

for j in temp:
    new_t.append(str(j)+' °C')


for i in date:
    new_date.append(i[-5:])

# собираем два списка (дата и температура) в один
lst = [list(tup) for tup in zip(new_date, new_t)]

labels = lst


def on_click(event):
    if event.button == 1:  # Левая кнопка мыши
        x_click, y_click = event.xdata, event.ydata


        for i in range(len(x)):
            if abs(x[i] - x_click) < 0.5 and abs(y[i] - y_click) < 0.5:
                ax.annotate(labels[i], xy=(x[i], y[i]), xytext=(5, 0),
                    textcoords="offset points",
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"),
                    annotation_clip=False)

                fig.canvas.draw()
                break

            if event.button == 2:
                break


# Подключаем обработчик событий

fig.canvas.mpl_connect('button_press_event', on_click)



plt.show()