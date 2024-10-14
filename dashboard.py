import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

day_df = pd.read_csv('day.csv')

# Menambahkan Windspeed_category
def categorize_windspeed(windspeed):
    windspeed_multiplied = windspeed * 67
    if 1 <= windspeed_multiplied <= 15:
        return 'breeze'
    elif 16 <= windspeed_multiplied <= 30:
        return 'moderate wind'
    elif 31 <= windspeed_multiplied <= 50:
        return 'strong wind'
    elif 51 <= windspeed_multiplied <= 75:
        return 'gale'
    elif windspeed_multiplied > 75:
        return 'storm wind'
    else:
        return 'calm'
    
day_df['windspeed_category'] = day_df['windspeed'].apply(categorize_windspeed)

# Mengubah kategori season
season_mapping = {
    1: 'springer',
    2: 'summer',
    3: 'fall',
    4: 'winter'
}

day_df['season'] = day_df['season'].map(season_mapping)

st.title("Pengaruh Musim dan Kecepatan Angin terhadap Penyewaan Sepeda")

# Chart pertama: Pengaruh musim terhadap jumlah penyewaan sepeda
st.subheader('Pengaruh Musim terhadap Jumlah Penyewaan Sepeda')
season_cnt = day_df.groupby('season')['cnt'].mean().reset_index()

fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(season_cnt['season'], season_cnt['cnt'])
ax1.set_title('Pengaruh Musim terhadap Jumlah Penyewaan Sepeda')
ax1.set_xlabel('Musim')
ax1.set_ylabel('Jumlah Penyewaan Sepeda')

st.pyplot(fig1)

st.write("Data Pengaruh Musim setelah di-sort berdasarkan Jumlah Penyewaan Sepeda:")
st.dataframe(season_cnt.sort_values(by='cnt', ascending=False))

# Chart kedua: Pengaruh kecepatan angin terhadap jumlah penyewaan sepeda
st.subheader('Pengaruh Kecepatan Angin terhadap Jumlah Penyewaan Sepeda')
windspeed_cnt = day_df.groupby('windspeed_category')['cnt'].mean()

fig2, ax2 = plt.subplots(figsize=(10, 6))
windspeed_cnt.plot(kind='bar', ax=ax2)
ax2.set_title('Pengaruh Kecepatan Angin terhadap Jumlah Penyewaan Sepeda')
ax2.set_xlabel('Kategori Kecepatan Angin')
ax2.set_ylabel('Jumlah Penyewaan Sepeda')
ax2.set_xticklabels(windspeed_cnt.index, rotation=45)

st.pyplot(fig2)

# Menampilkan data windspeed_cnt yang sudah di-sort
st.write("Data Pengaruh Kecepatan Angin setelah di-sort berdasarkan Jumlah Penyewaan Sepeda:")
st.dataframe(windspeed_cnt.sort_values(ascending=False))