import streamlit as st

from parse import parse
from scrape import *

st.title("AI WQeb Scraper")

url = st.text_input("Enter the website Url To Scrape")

if st.button("Scrape Site"):
    html = scrape_website(url)
    body_content = extract_body_content(html)
    body_content = clean_body_content(body_content)

    st.session_state.body_content = body_content

    with st.expander("View DOM Content"):
        st.text_area("DOOM Content",body_content,height=500)

if "body_content" in st.session_state:
    parse_description = st.text_area("What Do you want to find Out")

    if st.button("Find Out"):
        if parse_description:
            st.write("Parsing Description")
            body_batches = split_doom_content(st.session_state.body_content)
            result = parse(body_batches, parse_description)
            st.write(result)
