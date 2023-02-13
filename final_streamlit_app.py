import numpy             as np
import folium   
import pandas            as pd
import seaborn           as sns
import streamlit         as st
import geopandas   
import matplotlib.pyplot as plt

from folium.plugins   import MarkerCluster
from streamlit_folium import folium_static

# Configura a página para o formato indicado em 'layout'
st.set_page_config(layout='wide')

# Configura os arredondamentos no pandas
pd.set_option ('display.float_format', lambda x: '% .2f' % x)

# Carrega e mantem os dados em cache, melhorando um pouco a performance do código
# Função que carrega os dataset
#@st.cache(allow_output_mutation=True)
def get_data(path):
    data = pd.read_csv(path)

    return data

# Carrega e mantem os dados em cache
# Cria o geofile com a utilização do geopandas para aplicação nos mapas
@st.cache(allow_output_mutation=True)
def get_geofile(path2):
    geofile = geopandas.read_file(path2)

    return geofile

# Tratamento dos dados
@st.cache(allow_output_mutation=True)
def data_cleaning(data):
    #====================
    # TRATAMENTO DE DADOS
    #====================
    #==================================================================
    # Convert from object to datetime
    data['date'] = pd.to_datetime(data['date'])
    
    # Create feature that show the house and renovation age
    data['house_age'] = data['yr_built'].apply(lambda x: 2015 - x)
    data['renovation_age'] = data['yr_renovated'].apply(lambda x: 2015 - x if x > 0 else 0)
    
    # Create feature that show the type of the house
    data['house_type'] = data['bedrooms'].apply(lambda x: 'studio' if x <= 1 else 
                                                      'apartment' if (x > 1) & (x <= 3) else 'house')
    
    # Create feature that translate the feature "condition_type" to conceptual information
    data['condition_evaluation'] = data['condition'].apply(lambda x: '1_bad' if x <= 2 else
                                                                 '2_regular' if (x > 2) & (x < 5) else
                                                                 '3_good')
    
    # Create feature 'year' and 'month'
    data['month'] = data['date'].dt.month
    data['year'] = data['date'].dt.year
    
    # Create feature that show the season when the house was sale
    data['season_of_sale'] = data['month'].apply(lambda x: 'winter' if (x == 12) | (x == 1) | (x == 2) else
                                                       'spring' if (x > 2) & (x < 6) else
                                                       'fall' if (x > 8) & (x < 12) else
                                                       'summer')
    
    data['bathrooms'] = data['bathrooms'].round().astype('int64')
    
    # Convert sqft to m²
    data['sqft_living'] = data['sqft_living'].apply(lambda x: (x/10.764) if x > 0 else 0)
    data['sqft_lot'] = data['sqft_lot'].apply(lambda x: (x/10.764) if x > 0 else 0)
    data['sqft_above'] = data['sqft_above'].apply(lambda x: (x/10.764) if x > 0 else 0)
    data['sqft_basement'] = data['sqft_basement'].apply(lambda x: (x/10.764) if x > 0 else 0)
    data['bathrooms'] = data['bathrooms'].round()
    # Rename columns form sqft to m2
    data = data.rename(columns={'sqft_living':'m2_living',
                              'sqft_lot':'m2_lot',
                              'sqft_above':'m2_above',
                              'sqft_basement':'m2_basement'})
    # drop useless features
    data = data.drop(['condition', 'grade', 'yr_built', 'yr_renovated', 'sqft_living15', 'sqft_lot15'], axis=1)

    return data

# Plota o mapa com a concentração de imóveis por região(zipcode)
def data_preview(data):
    
    st.title('HOUSE ROCKET PROJECT')
    
    st.header('General Data')
    st.dataframe(data)
    
    #data = data.sample(1)
    
    # Cria o mapa base que receberá os pontos.
    density_map = folium.Map(location=[data['lat'].mean(), data['long'].mean()], default_zoom_start=15)

    # Cria os marcadores individuais com as informações de cada imóvel
    marcadores = MarkerCluster().add_to(density_map)        
    for i, j in data.iterrows():
        folium.Marker([j['lat'], j['long']], popup='Imóvel com {0} m², {1} quartos, {2} banheiros,\
                     de {3} anos, vendido por US$ {4}, em: {5}'.format(j['m2_living'],
                                                                            j['bedrooms'],
                                                                            j['bathrooms'],
                                                                            j['house_age'],
                                                                            j['price'],
                                                                            j['date']) ).add_to(marcadores)

    # Plota o mapa
    st.header('Region Concentration')
    folium_static(density_map, width=1200)

    return data

# Cria e plota a tabela de estatística descritiva
def statistics(data):
    num_attributes = data.select_dtypes(exclude=['object', 'datetime64'] )
    # Central tendency
    mean = pd.DataFrame(num_attributes.apply(np.mean))
    median = pd.DataFrame(num_attributes.apply(np.median))
    
    # Dispersion
    std = pd.DataFrame(num_attributes.apply(np.std))
    min_ = pd.DataFrame(num_attributes.apply(np.min))
    max_ = pd.DataFrame(num_attributes.apply(np.max))
    
    # União dos dfs
    num_stats = pd.concat([min_, max_, mean, median, std], axis=1).reset_index()
    num_stats.columns = ['Attributes', 'Min', 'Max', 'Mean', 'Median', 'STD']
    
    # Impressão do df com estatística descritiva
    st.header('Statistic Analysis')
    st.dataframe(num_stats)

    return None

# Cria e plota a visualização dos gráficos
def data_visual(data):
    st.title('Data Visualization')
    c1, c2, = st.columns((1, 1))

    c1.header('Avrg price x Property type')
    df = data[['price', 'house_type']].groupby('house_type').mean().reset_index()
    fig, ax = plt.subplots(figsize=(8,6))
    ax = sns.barplot(data=df, x='house_type', y='price')
    c1.pyplot(fig)

    c2.header('Avrg price x Property age')
    df = data[['price', 'house_age']].groupby('house_age').mean().reset_index()
    fig, ax = plt.subplots(figsize=(8,6))
    ax = sns.lineplot(data=df, x='house_age', y='price')
    c2.pyplot(fig)

    return None

def price_heatmap(data, geofile):
    
    st.title('Region/price Density')
    
    df = data[['zipcode', 'price']].groupby('zipcode').mean().reset_index()
    df.columns = ['ZIP', 'PRICE']

    geofile = geofile[geofile['ZIP'].isin(df['ZIP'].tolist())]

    region_price_map = folium.Map(location=[data['lat'].mean(), data['long'].mean()], default_zoom_start=15)

    region_price_map.choropleth(data=df, 
                                geo_data=geofile, 
                                columns=['ZIP', 'PRICE'], 
                                key_on='feature.properties.ZIP', 
                                fill_color='YlOrRd',
                                fill_opacity=0.5,
                                line_opacity=0.2,
                                legend_name='Preço médio')

    folium_static(region_price_map, width=1200, height=600) 

    return None

def filtering_data(data):

# Filtro de preço
    st.sidebar.header('Filters')
    st.sidebar.subheader('Select Maximum Price')

    min_price = int(data['price'].min())
    max_price = int(data['price'].max())
    avg_price = int(data['price'].mean())

    f_price = st.sidebar.slider('Price', min_price, max_price, avg_price, step=1000)

    data = data[data['price'] <= f_price]

# Filtro idade máxima
    st.sidebar.subheader('Select Maximum House Age')
    
    min_age = int(data['house_age'].min())
    max_age = int(data['house_age'].max())
    avg_age = int(data['house_age'].mean())

    f_age = st.sidebar.slider('Max Age', min_age, max_age, avg_age, step=5)

    data = data[data['house_age'] <= f_age]

# Filtro imóvel reformado
    st.sidebar.subheader("About the building's structure")
    was_reformed = st.sidebar.checkbox('I want reformed buildings')
    if was_reformed:
        data = data[data['renovation_age'] > 0]

    else:
        pass

# filtro waterview
    st.sidebar.subheader('About the View')
    waterview = st.sidebar.checkbox('I want waterview')
    if waterview:
        data = data[data['waterfront'] == 1]
    else: 
        pass

# Filtro qualidade da vista
    f_view = st.sidebar.multiselect('View quality', sorted(data['view'].unique()))
    if f_view != []:
        data = data[data['view'].isin(f_view)]

    else:
        pass

# Filtro estado de conservação
    st.sidebar.subheader('About the Conservation Status')
    f_conservation = st.sidebar.multiselect('Which conservation states do you accept',\
                                            sorted(data['condition_evaluation'].unique()))

    if f_conservation != []:
        data = data.loc[data['condition_evaluation'].isin(f_conservation)]

    else:
        pass

# Filtro de qtdd quartos
    st.sidebar.subheader('About the Building Plan')
    f_bedrooms = st.sidebar.multiselect('How many bedrooms do you want?', sorted(data['bedrooms'].unique()))
    if f_bedrooms != []:
        data = data.loc[data['bedrooms'].isin(f_bedrooms)]

    else:
        pass
    
# Filtro qtdd banheiros
    f_bathrooms = st.sidebar.multiselect('How many bathrooms do you want?', sorted(data['bathrooms'].unique()))
    if f_bathrooms != []:
        data = data.loc[data['bathrooms'].isin(f_bathrooms)]

    else:
        pass

# Filtro qtdd andares
    f_floors = st.sidebar.multiselect('How many floors do you want?', sorted(data['floors'].unique()))
    if f_floors != []:
        data = data.loc[data['floors'].isin(f_floors)]

    else:
        pass

    # Filtro estação do ano
    st.sidebar.subheader('About the Season of sale')
    f_season = st.sidebar.multiselect('Year Season', data['season_of_sale'].unique())
    if f_season != []:
        data = data.loc[data['season_of_sale'].isin(f_season)]

    else:
        pass

    return data

if __name__ == '__main__':

# Extract
    path = 'datasets\\kc_house_data.csv'
    path2 = 'datasets\\zipcodes.geojson'
    
# Load
    data = data_cleaning(get_data(path))
    geofile = get_geofile(path2)

# Transformation
    data = filtering_data(data)
    data_preview(data)
    statistics(data)
    data_visual(data)
    price_heatmap(data, geofile)

