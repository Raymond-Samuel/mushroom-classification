import pickle
import json
import pandas as pd
import streamlit as st 

# Define mapping dictionaries
cap_shape_dict = {'b': 'bell', 'c': 'conical', 'x': 'convex', 'f': 'flat', 'k': 'knobbed', 's': 'sunken'}
cap_surface_dict = {'f': 'fibrous', 'g': 'grooves', 'y': 'scaly', 's': 'smooth'}
cap_color_dict = {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'r': 'green', 'p': 'pink', 'u': 'purple', 'e': 'red', 'w': 'white', 'y': 'yellow'}
bruises_dict = {'t': 'bruises', 'f': 'no'}
odor_dict = {'a': 'almond', 'l': 'anise', 'c': 'creosote', 'y': 'fishy', 'f': 'foul', 'm': 'musty', 'n': 'none', 'p': 'pungent', 's': 'spicy'}
gill_attachment_dict = {'a': 'attached', 'f': 'free'}
gill_spacing_dict = {'c': 'close', 'w': 'crowded'}
gill_size_dict = {'b': 'broad', 'n': 'narrow'}
gill_color_dict = {'k': 'black', 'n': 'brown', 'b': 'buff', 'h': 'chocolate', 'g': 'gray', 'r': 'green', 'o': 'orange', 'p': 'pink', 'u': 'purple', 'e': 'red', 'w': 'white', 'y': 'yellow'}
stalk_shape_dict = {'e': 'enlarging', 't': 'tapering'}
stalk_root_dict = {'b': 'bulbous', 'c': 'club', 'e': 'equal', 'r': 'rooted'}
stalk_surface_above_ring_dict = {'f': 'fibrous', 'y': 'scaly', 'k': 'silky', 's': 'smooth'}
stalk_surface_below_ring_dict = {'f': 'fibrous', 'y': 'scaly', 'k': 'silky', 's': 'smooth'}
stalk_color_above_ring_dict = {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'o': 'orange', 'p': 'pink', 'e': 'red', 'w': 'white', 'y': 'yellow'}
stalk_color_below_ring_dict = {'n': 'brown', 'b': 'buff', 'c': 'cinnamon', 'g': 'gray', 'o': 'orange', 'p': 'pink', 'e': 'red', 'w': 'white', 'y': 'yellow'}
veil_type_dict = {'p': 'partial'}
veil_color_dict = {'n': 'brown', 'o': 'orange', 'w': 'white', 'y': 'yellow'}
ring_number_dict = {'n': 'none', 'o': 'one', 't': 'two'}
ring_type_dict = {'e': 'evanescent', 'f': 'flaring', 'l': 'large', 'n': 'none', 'p': 'pendant'}
spore_print_color_dict = {'k': 'black', 'n': 'brown', 'b': 'buff', 'h': 'chocolate', 'r': 'green', 'o': 'orange', 'u': 'purple', 'w': 'white', 'y': 'yellow'}
population_dict = {'a': 'abundant', 'c': 'clustered', 'n': 'numerous', 's': 'scattered', 'v': 'several', 'y': 'solitary'}
habitat_dict = {'g': 'grasses', 'l': 'leaves', 'm': 'meadows', 'p': 'paths', 'u': 'urban', 'w': 'waste', 'd': 'woods'}
poisonous_dict = {'e': 'edible', 'p': 'poisonous'}

# Reverse the mapping dictionaries
cap_shape_dict_rev = {v: k for k, v in cap_shape_dict.items()}
cap_surface_dict_rev = {v: k for k, v in cap_surface_dict.items()}
cap_color_dict_rev = {v: k for k, v in cap_color_dict.items()}
bruises_dict_rev = {v: k for k, v in bruises_dict.items()}
odor_dict_rev = {v: k for k, v in odor_dict.items()}
gill_attachment_dict_rev = {v: k for k, v in gill_attachment_dict.items()}
gill_spacing_dict_rev = {v: k for k, v in gill_spacing_dict.items()}
gill_size_dict_rev = {v: k for k, v in gill_size_dict.items()}
gill_color_dict_rev = {v: k for k, v in gill_color_dict.items()}
stalk_shape_dict_rev = {v: k for k, v in stalk_shape_dict.items()}
stalk_root_dict_rev = {v: k for k, v in stalk_root_dict.items()}
stalk_surface_above_ring_dict_rev = {v: k for k, v in stalk_surface_above_ring_dict.items()}
stalk_surface_below_ring_dict_rev = {v: k for k, v in stalk_surface_below_ring_dict.items()}
stalk_color_above_ring_dict_rev = {v: k for k, v in stalk_color_above_ring_dict.items()}
stalk_color_below_ring_dict_rev = {v: k for k, v in stalk_color_below_ring_dict.items()}
veil_type_dict_rev = {v: k for k, v in veil_type_dict.items()}
veil_color_dict_rev = {v: k for k, v in veil_color_dict.items()}
ring_number_dict_rev = {v: k for k, v in ring_number_dict.items()}
ring_type_dict_rev = {v: k for k, v in ring_type_dict.items()}
spore_print_color_dict_rev = {v: k for k, v in spore_print_color_dict.items()}
population_dict_rev = {v: k for k, v in population_dict.items()}
habitat_dict_rev = {v: k for k, v in habitat_dict.items()}
poisonous_dict_rev = {v: k for k, v in poisonous_dict.items()}


## Load All Files

with open('model.pkl', 'rb') as file_3:
  model = pickle.load(file_3)


def run():
    with st.form('form_mushroom_default'):
        cap_shape = st.selectbox('cap-shape', options=list(cap_shape_dict.keys()), format_func=lambda x: cap_shape_dict[x])
        cap_surface = st.selectbox('cap-surface', options=list(cap_surface_dict.keys()), format_func=lambda x: cap_surface_dict[x])
        cap_color = st.selectbox('cap-color', options=list(cap_color_dict.keys()), format_func=lambda x: cap_color_dict[x])
        bruises = st.selectbox('bruises', options=list(bruises_dict.keys()), format_func=lambda x: bruises_dict[x])
        odor = st.selectbox('odor', options=list(odor_dict.keys()), format_func=lambda x: odor_dict[x])
        gill_attachment = st.selectbox('gill-attachment', options=list(gill_attachment_dict.keys()), format_func=lambda x: gill_attachment_dict[x])
        gill_spacing = st.selectbox('gill-spacing', options=list(gill_spacing_dict.keys()), format_func=lambda x: gill_spacing_dict[x])
        gill_size = st.selectbox('gill-size', options=list(gill_size_dict.keys()), format_func=lambda x: gill_size_dict[x])
        gill_color = st.selectbox('gill-color', options=list(gill_color_dict.keys()), format_func=lambda x: gill_color_dict[x])
        stalk_shape = st.selectbox('stalk-shape', options=list(stalk_shape_dict.keys()), format_func=lambda x: stalk_shape_dict[x])
        stalk_root = st.selectbox('stalk-root', options=list(stalk_root_dict.keys()), format_func=lambda x: stalk_root_dict[x])
        stalk_surface_above_ring = st.selectbox('stalk-surface-above-ring', options=list(stalk_surface_above_ring_dict.keys()), format_func=lambda x: stalk_surface_above_ring_dict[x])
        stalk_surface_below_ring = st.selectbox('stalk-surface-below-ring', options=list(stalk_surface_below_ring_dict.keys()), format_func=lambda x: stalk_surface_below_ring_dict[x])
        stalk_color_above_ring = st.selectbox('stalk-color-above-ring', options=list(stalk_color_above_ring_dict.keys()), format_func=lambda x: stalk_color_above_ring_dict[x])
        stalk_color_below_ring = st.selectbox('stalk-color-below-ring', options=list(stalk_color_below_ring_dict.keys()), format_func=lambda x: stalk_color_below_ring_dict[x])
        veil_type = st.selectbox('veil-type', options=list(veil_type_dict.keys()), format_func=lambda x: veil_type_dict[x])
        veil_color = st.selectbox('veil-color', options=list(veil_color_dict.keys()), format_func=lambda x: veil_color_dict[x])
        ring_number = st.selectbox('ring-number', options=list(ring_number_dict.keys()), format_func=lambda x: ring_number_dict[x])
        ring_type = st.selectbox('ring-type', options=list(ring_type_dict.keys()), format_func=lambda x: ring_type_dict[x])
        spore_print_color = st.selectbox('spore-print-color', options=list(spore_print_color_dict.keys()), format_func=lambda x: spore_print_color_dict[x])
        population = st.selectbox('population', options=list(population_dict.keys()), format_func=lambda x: population_dict[x])
        habitat = st.selectbox('habitat', options=list(habitat_dict.keys()), format_func=lambda x: habitat_dict[x])
        
        submitted = st.form_submit_button('Predict')

    data_inf = {
      'cap-shape': cap_shape,
      'cap-surface': cap_surface,
      'cap-color': cap_color,
      'bruises': bruises,
      'odor': odor,
      'gill-attachment': gill_attachment,
      'gill-spacing': gill_spacing,
      'gill-size': gill_size,
      'gill-color': gill_color,
      'stalk-shape': stalk_shape,
      'stalk-root': stalk_root,
      'stalk-surface-above-ring': stalk_surface_above_ring,
      'stalk-surface-below-ring': stalk_surface_below_ring,
      'stalk-color-above-ring': stalk_color_above_ring,
      'stalk-color-below-ring': stalk_color_below_ring,
      'veil-type': veil_type,
      'veil-color': veil_color,
      'ring-number': ring_number,
      'ring-type': ring_type,
      'spore-print-color': spore_print_color,
      'population': population,
      'habitat': habitat,
    } 

    if submitted:
        data_inf = pd.DataFrame([data_inf])
        data_inf = data_inf.drop(columns=['stalk-root'], axis=1)
        st.dataframe(data_inf)
        # Predict using your model
        y_pred_inf = model.predict(data_inf)
        prediction_result = 'edible' if y_pred_inf == 0 else 'poisonous'
        st.write('## prediction categories : ', str(int(y_pred_inf)))
        st.write('## prediction categories (str) : ', prediction_result)


if __name__ == '__main__':
    run()