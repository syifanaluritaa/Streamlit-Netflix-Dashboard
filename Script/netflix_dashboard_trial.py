#Library
import streamlit as st
import pandas as pd
import plotly.express as px

#Configure
st.set_page_config(
    page_title="Netflix Analytics Dashboard",
    page_icon="🎬",
    layout="wide"
)

#Data
@st.cache_data
def load_data():
    df = pd.read_csv("D:/Streamlit Dashboard/netflix_titles.csv")
    # Membersihkan kolom data_added untuk diambil tahunnya saja (opsional)
    df['date_added'] = df['date_added'].str.strip()
    df['year_added'] = pd.to_datetime(df['date_added'], format='%B %d, %Y', errors='coerce').dt.year
    return df
df = load_data()

#Header
st.title("🎬 Netflix Data Analytics Dashboard")
st.markdown("Dashboard interaktif untuk mengeksplorasi konten film dan acara TV di Netflix.")
st.markdown("---")

#Sidebar
st.sidebar.header("Filter Konten")

#Filter 1: Tipe Konten
all_types = ["Semua"] + list(df['type'].unique())
selected_type = st.sidebar.selectbox("Pilih Tipe Konten", all_types)

#Filter 2: Negara
top_countries = df['country'].dropna().value_counts().head(20).index.tolist()
all_countries = ["Semua"] + top_countries
selected_country = st.sidebar.selectbox("Pilih Negara Asal", all_countries)

#SIDE BAR
st.sidebar.markdown("---")
st.sidebar.caption("💡 Created by Syifa Nalurita Azahra")

filtered_df = df.copy()
if selected_type != "Semua":
    filtered_df = filtered_df[filtered_df['type'] == selected_type]
if selected_country != "Semua":
    filtered_df = filtered_df[filtered_df['country'].str.contains(selected_country, na=False)]

#KPI
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Judul", len(filtered_df))
with col2:
    total_movies = len(filtered_df[filtered_df['type'] == 'Movie'])
    st.metric("Total Movies", total_movies)
with col3:
    total_tv_shows = len(filtered_df[filtered_df['type'] == 'TV Show'])
    st.metric("Total TV Shows", total_tv_shows)

st.markdown("---")

#VISUALISASI
layout_col1, layout_col2 = st.columns(2)

with layout_col1:
    st.subheader("📊 Distribusi Tipe Konten")
    # Pie chart untuk melihat proporsi Movie vs TV Show
    type_counts = filtered_df['type'].value_counts().reset_index()
    type_counts.columns = ['Tipe', 'Jumlah']
    fig_pie = px.pie(type_counts, values='Jumlah', names='Tipe', 
                     color_discrete_sequence=['#E50914', '#221F1F'],
                     hole=0.4)
    st.plotly_chart(fig_pie, use_container_width=True)

with layout_col2:
    st.subheader("📈 Tren Rilis Konten Berdasarkan Tahun")
    #Line chart tren 
    release_trend = filtered_df.groupby('release_year').size().reset_index(name='Jumlah')
    # Lomot tahun
    release_trend = release_trend[release_trend['release_year'] >= 2000]
    
    fig_line = px.line(release_trend, x='release_year', y='Jumlah',
                       labels={'release_year': 'Tuben Rilis', 'Jumlah': 'Jumlah Konten'},
                       markers=True)
    fig_line.update_traces(line_color='#E50914')
    st.plotly_chart(fig_line, use_container_width=True)

st.markdown("---")

#Raw Data
st.subheader("🔍 Sampel Data Interaktif")
st.markdown("Berikut adalah data yang sudah difilter. Kamu bisa mengurutkan langsung melalui tabel di bawah ini:")
st.dataframe(filtered_df[['show_id', 'type', 'title', 'director', 'country', 'release_year', 'rating']].head(100), use_container_width=True)