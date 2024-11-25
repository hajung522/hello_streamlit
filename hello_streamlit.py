import streamlit as st
st.write('Hello world!')

# st.header('st.button')

# if st.button('Say hello'):
#      st.write('Why hello there')
# else:
#      st.write('Goodbye')

# st.header('st.slider')

# st.subheader('Slider')

# age = st.slider('당신의 나이는?', 0, 130, 25)
# st.write("나는 ", age, '살입니다')

# st.header('st.selectbox')

# option = st.selectbox(
#      '가장 좋아하는 색상은 무엇인가요?',
#      ('파랑', '빨강', '초록'))

# st.write('당신이 좋아하는 색상은 ', option)

# options = st.multiselect(
#      '가장 좋아하는 색상은 무엇인가요',
#      ['초록', '노랑', '빨강', '파랑'],
#      ['노랑', '빨강'])

# st.write('당신이 선택한 색상:', options)

# icecream = st.checkbox('아이스크림')
# coffee = st.checkbox('커피')
# cola = st.checkbox('콜라')

# if icecream:
#      st.write("좋아요! 여기 더 많은 🍦")
# if coffee: 
#      st.write("알겠습니다, 여기 커피 있어요 ☕")
# if cola:
#      st.write("여기 있어요 🥤")

# st.latex(r'''
# a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
# \sum_{k=0}^{n-1} ar^k =
# a \left(\frac{1-r^{n}}{1-r}\right)
# ''')