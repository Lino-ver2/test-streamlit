

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
"""
st.title('Streamlit 超入門')

st.write('Display Image')

img = Image.open('sample.jpg')
st.image(img, caption='HatuneMiku', use_column_width=True)

st.write('DataFrame')
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df)

df = pd.DataFrame(
    np.random.rand(20, 3),#random.rand：正規分布の乱数
    columns=['a', 'b', 'c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

df = pd.DataFrame({
    '1列目': [1,2,3,4],
    '２列目':[10, 20, 30, 40]
})
st.table(df.style.highlight_max(axis=0))

st.write('Display Image')
if st.checkbox('ShowImage'):#True, Falseを返すインタラクティブ
    img = Image.open('sample.jpg')
    st.image(img, caption='HatuneMiku', use_column_width=True)

"""



""" インタラクティブ　ウィジェット
st.sidebar.write('Intaracitve Widgets')

option = st.selectbox(  #第２引数であるoptionの名前で変数に代入することでselectされた第２引数を渡すことができる
    'あなたが好きな数字を教えてください',
    list(range(1, 11)))
'あなたの好きな数字は,', option,'です'

text = st.text_input('あなたの趣味を押してください')
'あなたの好きな数字は,', text,'です'

condition = st.slider('あなたの今日の調子は', 0, 100, 73)
'あなたの好きな数字は,', condition,'です'

text = st.sidebar.text_input('あなたの趣味を押してください')
condition = st.sidebar.slider('あなたの今日の調子は', 0, 100, 73)
'あなたの好きな数字は,', text,'です'
'あなたの今日の調子は,', condition,'です'







"""



"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
