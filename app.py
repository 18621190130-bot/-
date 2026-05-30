import streamlit as st

st.title("📚 图书推荐系统")

st.write("请输入你的兴趣，比如：科幻、爱情、悬疑")

user_input = st.text_area("你的兴趣：")

if st.button("开始推荐"):
    st.write("你输入的是：", user_input)