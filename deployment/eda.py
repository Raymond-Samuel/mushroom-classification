import streamlit as st 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import plotly.express as px 
from PIL import Image
from ucimlrepo import fetch_ucirepo

def run():
    ## membuat judul
    st.title('Mushroom Classification Prediction')

    ## membuat sub header
    st.subheader('EDA untuk Analisa Dataset Mushroom')

    ## tambahkan gambar
    image =  Image.open('mushroom.jpg')
    st.image(image, caption='Mushroom')

    ## menambahkan deskripsi
    st.write('Page ini dibuat oleh Raymond Samuel')

    ## Font Size
    ## Font terbesar
    st.write('# Dataframe')

    # fetch dataset
    mushroom = fetch_ucirepo(id=73)

    # data (as pandas dataframes)
    X = mushroom.data.features
    y = mushroom.data.targets
    df = pd.concat([X, y], axis=1)

    # Define mapping dictionaries
    cap_shape_dict = {'b': 'bell', 'c': 'conical', 'x': 'convex', 'f': 'flat', 'k': 'knobbed', 's': 'sunken'}
    cap_surface_dict = {'f': 'fibrous', 'g': 'grooves', 'y': 'scaly', 's': 'smooth'}
    cap_color_dict = {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'r': 'green', 'p': 'pink', 'u': 'purple', 'e': 'red', 'w': 'white', 'y': 'yellow'}
    bruises_dict = {'t': 'bruises', 'f': 'no'}
    odor_dict = {'a': 'almond', 'l': 'anise', 'c': 'creosote', 'y': 'fishy', 'f': 'foul', 'm': 'musty', 'n': 'none', 'p': 'pungent', 's': 'spicy'}
    gill_attachment_dict = {'a': 'attached', 'd': 'descending', 'f': 'free', 'n': 'notched'}
    gill_spacing_dict = {'c': 'close', 'w': 'crowded', 'd': 'distant'}
    gill_size_dict = {'b': 'broad', 'n': 'narrow'}
    gill_color_dict = {'k': 'black', 'n': 'brown', 'b': 'buff', 'h': 'chocolate', 'g': 'gray', 'r': 'green', 'o': 'orange', 'p': 'pink', 'u': 'purple', 'e': 'red', 'w': 'white', 'y': 'yellow'}
    stalk_shape_dict = {'e': 'enlarging', 't': 'tapering'}
    stalk_root_dict = {'b': 'bulbous', 'c': 'club', 'u': 'cup', 'e': 'equal', 'z': 'rhizomorphs', 'r': 'rooted', '?': 'missing'}
    stalk_surface_above_ring_dict = {'f': 'fibrous', 'y': 'scaly', 'k': 'silky', 's': 'smooth'}
    stalk_surface_below_ring_dict = {'f': 'fibrous', 'y': 'scaly', 'k': 'silky', 's': 'smooth'}
    stalk_color_above_ring_dict = {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'o': 'orange', 'p': 'pink', 'e': 'red', 'w': 'white', 'y': 'yellow'}
    stalk_color_below_ring_dict = {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'o': 'orange', 'p': 'pink', 'e': 'red', 'w': 'white', 'y': 'yellow'}
    veil_type_dict = {'p': 'partial', 'u': 'universal'}
    veil_color_dict = {'n': 'brown', 'o': 'orange', 'w': 'white', 'y': 'yellow'}
    ring_number_dict = {'n': 'none', 'o': 'one', 't': 'two'}
    ring_type_dict = {'c': 'cobwebby', 'e': 'evanescent', 'f': 'flaring', 'l': 'large', 'n': 'none', 'p': 'pendant', 's': 'sheathing', 'z': 'zone'}
    spore_print_color_dict = {'k': 'black', 'n': 'brown', 'b': 'buff', 'h': 'chocolate', 'r': 'green', 'o': 'orange', 'u': 'purple', 'w': 'white', 'y': 'yellow'}
    population_dict = {'a': 'abundant', 'c': 'clustered', 'n': 'numerous', 's': 'scattered', 'v': 'several', 'y': 'solitary'}
    habitat_dict = {'g': 'grasses', 'l': 'leaves', 'm': 'meadows', 'p': 'paths', 'u': 'urban', 'w': 'waste', 'd': 'woods'}
    poisonous_dict = {'e': 'edible', 'p': 'poisonous'}

    # Apply the mapping to the dataframe
    df['cap-shape'] = df['cap-shape'].map(cap_shape_dict)
    df['cap-surface'] = df['cap-surface'].map(cap_surface_dict)
    df['cap-color'] = df['cap-color'].map(cap_color_dict)
    df['bruises'] = df['bruises'].map(bruises_dict)
    df['odor'] = df['odor'].map(odor_dict)
    df['gill-attachment'] = df['gill-attachment'].map(gill_attachment_dict)
    df['gill-spacing'] = df['gill-spacing'].map(gill_spacing_dict)
    df['gill-size'] = df['gill-size'].map(gill_size_dict)
    df['gill-color'] = df['gill-color'].map(gill_color_dict)
    df['stalk-shape'] = df['stalk-shape'].map(stalk_shape_dict)
    df['stalk-root'] = df['stalk-root'].map(stalk_root_dict)
    df['stalk-surface-above-ring'] = df['stalk-surface-above-ring'].map(stalk_surface_above_ring_dict)
    df['stalk-surface-below-ring'] = df['stalk-surface-below-ring'].map(stalk_surface_below_ring_dict)
    df['stalk-color-above-ring'] = df['stalk-color-above-ring'].map(stalk_color_above_ring_dict)
    df['stalk-color-below-ring'] = df['stalk-color-below-ring'].map(stalk_color_below_ring_dict)
    df['veil-type'] = df['veil-type'].map(veil_type_dict)
    df['veil-color'] = df['veil-color'].map(veil_color_dict)
    df['ring-number'] = df['ring-number'].map(ring_number_dict)
    df['ring-type'] = df['ring-type'].map(ring_type_dict)
    df['spore-print-color'] = df['spore-print-color'].map(spore_print_color_dict)
    df['population'] = df['population'].map(population_dict)
    df['habitat'] = df['habitat'].map(habitat_dict)
    df['poisonous'] = df['poisonous'].map(poisonous_dict)

    st.dataframe(df)

    st.markdown('---')

    st.write('# EDA')

    st.write('## Distribution of Edible vs. Poisonous Mushrooms')

    fig, ax = plt.subplots()
    sns.countplot(x='poisonous', data=df, ax=ax)
    plt.title("Distribution of Edible vs. Poisonous Mushrooms")
    st.pyplot(fig)

    value_counts = df['poisonous'].value_counts()
    st.write(value_counts)

    st.markdown("Dari dataset dapat dilihat Data `edible` ada 4208 lebih banyak dariapda `poisonous` ada 3916.")

    st.markdown('---')

    st.write('## Distribution of Mushrooms by odor')

    feature_to_plot = 'odor'
    feature_to_plot = 'odor'
    fig, ax = plt.subplots()
    df[feature_to_plot].value_counts().plot(kind='bar', ax=ax)
    plt.title(f"Distribution of Mushrooms by {feature_to_plot}")
    plt.xlabel(feature_to_plot)
    plt.ylabel("Count")
    st.pyplot(fig)

    st.markdown("Mushroom terbanyak yaitu dengan `odor` = `none`, yaitu tidak ada bau.")

    st.markdown('---')

    st.markdown('## Distribution of odor by Class')

    feature_to_analyze = 'odor'
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(x=feature_to_analyze, hue='poisonous', data=df, ax=ax)
    plt.title(f"Distribution of {feature_to_analyze} by Class")
    st.pyplot(fig)

    st.markdown("Dapat dilihat dari hasil plot diatas, bahwa jamur yang `foul_odor` bisa di kategorikan sebagai poisonous")

    st.markdown('---')
    st.write('## Distribution of cap-shape by Class')
    feature_to_analyze = 'cap-shape'
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(x=feature_to_analyze, hue='poisonous', data=df)
    plt.title(f"Distribution of {feature_to_analyze} by Class")
    st.pyplot(fig)
    st.markdown('Dari dataset, pada umumnya mushroom banyak yang memiliki `cap-shape` `convex` dan `flat`, baik pada jamur `poisonous` maupun `edible`.')

    st.markdown('---')

    st.write('## Distribution of habitat by Class')
    feature_to_analyze = 'habitat'
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(x=feature_to_analyze, hue='poisonous', data=df)
    plt.title(f"Distribution of {feature_to_analyze} by Class")
    st.pyplot(fig)
    st.markdown('Dari dataset, mushroom `poisonous` lebih banyak terletak pada habitat `woods` disusul dengan `paths`.')






if __name__ == '__main__':
    run()