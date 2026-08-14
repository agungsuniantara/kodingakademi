import streamlit as st

st.title("Florapedia: Flora Endemik Indonesia")

st.header("Rafflesia arnoldii")
st.subheader("The Largest Flower on Earth")

col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "link picture",
        caption="Rafflesia arnoldii",
        width=250
    )

with col2:
    st.markdown("""
    **Scientific Name:** Rafflesia arnoldii  
    **Common Name:** Corpse Flower, Padma Raksasa  
    **Status:** Critically Endangered  
    **Location:** Sumatra, Indonesia  
    **Diameter:** Up to 100 cm  
    **Weight:** Up to 11 kg  
    """)

st.header("Key Facts")
st.markdown("""
- Rafflesia arnoldii is a parasitic plant with no leaves, stems, or roots
- It only grows on the Tetrastigma vine
- It smells like rotting flesh to attract carrion flies for pollination
- The bloom lasts only 5-7 days
- It is one of three national flowers of Indonesia
""")

st.header("Conservation Status")
st.metric(label="Estimated remaining in wild", value="Fewer than 1,000", delta="-200")