import requests
import pandas as pd
import matplotlib.pyplot as plt
import mpld3

api_key = '742c6514cbef4e8a9aec2fec73ef6aeb'


start_date = '2023-08-20'
end_date = '2023-08-26'


hutemperature_data = pd.DataFrame(columns=['Date', 'Min', 'Max'])


current_date = start_date
while current_date <= end_date:
    url = f'https://api.openweathermap.org/data/3.0/onecall/day_summary?lat=29.7589382&lon=-95.3676974&date={current_date}&appid={api_key}&units=metric'
    hu_response = requests.get(url)
    hu_data = hu_response.json()
    hu_min = hu_data['temperature']['min']
    hu_max = hu_data['temperature']['max']
    hutemperature_data = hutemperature_data._append({'Date': current_date, 'Min': hu_min, 'Max': hu_max}, ignore_index=True)
    current_date = (pd.to_datetime(current_date) + pd.DateOffset(days=1)).strftime('%Y-%m-%d')


hu_fig1=hutemperature_data.plot(kind='bar',
        x='Date',
        y='Min',
        color='#FF81C0')

plt.title('The minimum temperatures over the week')
html_fig1 = mpld3.fig_to_html(plt.gcf())

hu_fig2=hutemperature_data.plot(kind='bar',
        x='Date',
        y='Max',
        color='#DDA0DD')

plt.title('The maximum temperatures over the week')

html_fig2 = mpld3.fig_to_html(plt.gcf())

html_table = hutemperature_data.to_html()


html_file = open("../templates/Houston.html", "a")
html_file.write(html_table)
html_file.write(html_fig1)
html_file.write(html_fig2)
html_file.close()