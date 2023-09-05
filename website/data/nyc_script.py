import requests
import pandas as pd
import matplotlib.pyplot as plt
import mpld3

api_key = '742c6514cbef4e8a9aec2fec73ef6aeb'


start_date = '2023-08-20'
end_date = '2023-08-26'

nytemperature_data = pd.DataFrame(columns=['Date', 'Min', 'Max'])

current_date = start_date
while current_date <= end_date:
    url = f'https://api.openweathermap.org/data/3.0/onecall/day_summary?lat=40.7127281&lon=-74.0060152&date={current_date}&appid={api_key}&units=metric'
    ny_response = requests.get(url)
    ny_data = ny_response.json()
    ny_min = ny_data['temperature']['min']
    ny_max = ny_data['temperature']['max']
    nytemperature_data = nytemperature_data._append({'Date': current_date, 'Min': ny_min, 'Max': ny_max}, ignore_index=True)
    current_date = (pd.to_datetime(current_date) + pd.DateOffset(days=1)).strftime('%Y-%m-%d')


nytemperature_data.to_csv('ny_data.csv', index=False)

ny_fig1=nytemperature_data.plot(kind='bar',
        x='Date',
        y='Min',
        color='#FF81C0')

plt.title('The minimum temperatures over the week')
html_fig1 = mpld3.fig_to_html(plt.gcf())

ny_fig2=nytemperature_data.plot(kind='bar',
        x='Date',
        y='Max',
        color='#DDA0DD')

plt.title('The maximum temperatures over the week')

html_fig2 = mpld3.fig_to_html(plt.gcf())

html_table = nytemperature_data.to_html()


html_file = open("../templates/NYC.html", "a")
html_file.write(html_table)
html_file.write(html_fig1)
html_file.write(html_fig2)
html_file.close()