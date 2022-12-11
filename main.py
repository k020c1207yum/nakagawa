import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
from streamlit.elements.image import UseColumnWith

st.title("はじめてのweb part2")
st.write("Display Image")
img = Image.open("miku_haikei.jpg")
st.image(img,caption="公式が配布してた画像",use_column_width = True)


st.write("Data frame")
df = pd.DataFrame({
    "1列目": [1, 2, 3, 4],
    "2列目": [10, 20, 30, 40]
})
st.write(df)

st.dataframe(df,width= 100,height=100)
st.table(df.style.highlight_max(axis=0))


"""
# 章(マークダウン記法)
## 節
### codeを書くとき
```python

import pandas as pd

```
"""

df1 = pd.DataFrame(np.random.rand(20,3),columns=["売上","人","ああ"])
st.dataframe(df1)
st.line_chart(df1)
st.bar_chart(df1)

df2 = pd.DataFrame(np.random.rand(100,2)/[50,50]+[35.69,139.70],columns=["lat","lon"]
                   
)
st.dataframe(df2)
st.map(df2)



option = st.selectbox(
    "あなたの好きなメープルシロップを選んでください",
    ["ゴールデン","メープル","ダーク","ベリーダーク"]

)
st.write("あなたが選んだのは",option,"です。")

text1 = st.text_input("あなたの好きな食べ物教えてください")
st.write("ちなみに私はマグロと",text1,"です。")

condition = st.slider("あなたの体調具合は？",0,100,1)
"あなたは",condition,"powerです"
