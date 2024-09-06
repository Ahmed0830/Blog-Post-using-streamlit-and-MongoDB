import streamlit as st
import database as db
from streamlit_option_menu import option_menu
import streamlit_shadcn_ui as ui
st.title("Blog Your Journey")

selected = option_menu(
    menu_title= None,
    options = ["New Blog", "Blogs"],
    icons= [":writing_hand:", ":page_with_curl:"],
    orientation="horizontal"
)
st.markdown("""
<style>
.transparent-card {
    background-color: #321dw3;  /* Make the background transparent */
}
</style>
""", unsafe_allow_html=True)
    
if selected == "New Blog":
    with st.form("blog", clear_on_submit=True):
        blog_title = st.text_input("Blog Title")
        blog_input = st.text_area("Start Writing Your Own Blog")
        submitted = st.form_submit_button("Upload Your Blog")

        if submitted:
            db.upload_blog(blog_title, blog_input)
            # st.write(blog_title)
            # st.write(blog_input)
            st.success("Blog Upload Successfully")

if selected == "Blogs":
    items = db.fetch_all_blogs()
    blogs = [[item["title"], item["blog"]] for item in items]
    # blogs = [item["blog"] for item in items]
    id = 1
    for blog in blogs:
        with ui.card(key = id):
            ui.element("span", children=["Title: " + blog[0]], className="transparent-card text-white-800 text-m font-medium m-3")
            ui.element("span", children=[blog[1]], className="transparent-card text-white-200 text-sm font-small flex flex-col")
            id+=1
            # st.write(blog[0])
            # st.write(blog[1])