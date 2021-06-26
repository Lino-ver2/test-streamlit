

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


""" 
st.write('SelectBox')
option = st.selectbox(  #第２引数であるoptionの名前で変数に代入することでselectされた第２引数を渡すことができる
    'あなたが好きな数字を教えてください',
    list(range(1, 11)))

'あなたの好きな数字は,', option,'です'
"""