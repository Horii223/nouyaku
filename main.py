import streamlit as st

st.title('HIDDEN')

st.subheader('これはニンジャだけに伝わるHIDDENの数術...')

pest = st.selectbox(
"今回の農薬の種類は",
    ('殺菌剤','殺虫剤','殺菌殺虫剤'))

field = st.slider("今回の散布面積は", min_value = 0, max_value = 100 ,step = 5)
st.subheader(str(field)+"haを散布するということは")

if pest =='殺菌剤':
    pest1 = int(field)*5.0
    pest2 = int(field)*4.0
    pest3 = int(field)*1.0
    st.subheader("農薬全体は"+str(pest1)+"L必要なので")
    st.subheader("水が"+str(pest2)+"L")
    st.subheader("農薬は"+str(pest3)+"L")
elif pest =="殺虫剤":
    pest1 = int(field)*4.0
    pest2 = int(field)*3.0
    pest3 = int(field)*1.0
    st.subheader("農薬全体は"+str(pest1)+"L必要なので")
    st.subheader("水が"+str(pest2)+"L")
    st.subheader("農薬は"+str(pest3)+"L")
else:
    pest1 = int(field)*3.5
    pest2 = int(field)*3.0
    pest3 = int(field)*0.5
    st.subheader("農薬全体は"+str(pest1)+"L必要なので")
    st.subheader("水が"+str(pest2)+"L")
    st.subheader("農薬は"+str(pest3)+"L")
    
st.subheader("必要です")
