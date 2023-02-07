import streamlit as st
import pandas as pd
import seaborn as sns

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_voitures = pd.read_csv(link)

df_voitures['continent'] = df_voitures['continent'].str.replace('.', '')
df_voitures['continent'] = df_voitures['continent'].astype('category')

st.title('Bienvenue sur notre application de voitures')

st.caption('Je fais quelques tests')

viz_correlation = sns.heatmap(df_voitures.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True),
                                annot = True
								)
st.header('Heatmap associée à la matrice de corrélation :')
st.pyplot(viz_correlation.figure,clear_figure=True)


#viz_pairplot = sns.pairplot(df_voitures, hue = 'continent')

#st.write('Pairplot pour regarder les corrélations avec un filtre sur le continent :')
#st.pyplot(viz_pairplot.figure)

viz_barplot = sns.barplot(data = df_voitures,
							x = 'cylinders',
							y = 'cubicinches',
							hue = 'continent')
st.header('cylinders/cubicinches : ')
st.pyplot(viz_barplot.figure,clear_figure=True)

#st.bar_chart(data = df_voitures, x = 'cylinders', y = 'cubicinches')


df_voitures['continent'] = df_voitures['continent'].str.strip()
df_voitures_europe = df_voitures[df_voitures['continent'] == 'Europe']
df_voitures_japan = df_voitures[df_voitures['continent'] == 'Japan']
df_voitures_us = df_voitures[df_voitures['continent'] == 'US']

option = st.radio(
    'Quel pays souhaitez-vous choisir ?',
    ('Europe', 'US', 'Japan'))

st.write('You selected:', option)


if option == 'US' :
    data_choisi = df_voitures_us
elif option =='Japan' :
    data_choisi = df_voitures_japan
else :
    data_choisi = df_voitures_europe

viz_barplot_choisi = sns.barplot(data = data_choisi,
									x = 'cylinders',
									y = 'cubicinches',
									)
st.header('cylinders/cubicinches pour le pays sélectionné')
st.pyplot(viz_barplot_choisi.figure,clear_figure=True)