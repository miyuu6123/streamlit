# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Web App")
st.write("**これがstreamlitアプリ**")

img = Image.open("aikon.jpeg")
st.image(img,width=200)
st.video("https://youtu.be/zI9-qCpxz4o?si=bl-FddVYuedXjE9M")


answer = st.button('Say hello')

if answer == True:
     st.write('Why hello there')
else:
     st.write('Goodbye')
    
data = {
    'lat': np.random.randn(100) / 100 + 35.68,
    'lon': np.random.randn(100) / 100 + 139.75,
}
map_data = pd.DataFrame(data)
# 地図に散布図を描く
st.map(map_data)
