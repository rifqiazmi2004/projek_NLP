import streamlit as st
import pandas as pd

tabel = pd.DataFrame({"column 1":[1,2,3,4,5], "column 2":[1,2,3,4,5]})

# Removing Header dan Footer Default
st.markdown("""
<style>
.css-dibildedgvbvh6{
    visibility:hidden;
}
.css-lv8iasiejrwi{
    visibility:hidden;
}
</style>
""", unsafe_allow_html=True)

# ------------------------TEXT STYLING---------------------------------
st.title("Latihan Ini")
st.subheader("nah ini sub-header")
st.header("I am header")

st.text("Lorem ipsum dolor sit amet")

st.markdown("# H1")
st.markdown("## H2")
st.markdown("### H3")
st.markdown("**Bold** uhuy")
st.markdown("*Italic* uhuy")
st.markdown("> Blockquote")

st.markdown("""
1. list1 
2. list2 
3.list3
""")

st.markdown("""
-list1 
-list2 
-list3
""")

st.markdown("---")
st.markdown("`code`")
st.markdown("[google](https://www.google.com)")
st.markdown("[image](image1.jpg)")

st.caption("ini caption")

st.latex(r"\begin{pmatrix}a&b\\c&d\\end{pmatrix}")

json={"a":"1,2,3", "b":"1,2,3"}
st.json(json)

code="""
print("spontan uhuy")
def func_coba()
    return 0;
"""
st.code(code, language="python")

st.markdown("# Bagian 2")
st.metric(label="wind speed", value="120ms\^-1", delta="1.4ms\^-1")

st.table(tabel)
st.dataframe(tabel)

# ---------------------------MEDIA----------------------------------
st.markdown("#Media")
st.image("image.jpg", caption="caption image", width=400)
st.audio("audio.mp3")
st.video("video.mp4")

# ----------------------------FORM-------------------------------------
st.markdown("#Form")

st.checkbox("Checkbox")

state=st.checkbox("nyoba", value=True)
if state:
    st.write("hi")
else:
    pass

def callback():
    print(st.session_state.kunci-checkbox)

state2=st.checkbox("callback", value=True, on_change=callback, key="kunci-checkbox")

radio_btn=st.radio("Pilih salah satu", options=("1","2","3"))
print(radio_btn)

# jika button di klik kode print(radio_btn) juga jalan karena gk ada pembungkus jadi
# si button fungsi secara global
def btn_func():
    print("button clicked")
btn=st.button("button", on_click=btn_func)

select=st.selectbox("ini selectbox",options=("1",'2','3','4'))
print(select)

multi_select=st.multiselect("multi select",options=('satu','dua','tiga'))
st.write(multi_select)