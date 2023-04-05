import streamlit as st
import speedtest
import time
sp = speedtest.Speedtest()
st.set_page_config(page_title='Speed test',page_icon="🌐",layout="centered",
    menu_items={
    'Get Help': '90859https://www.facebook.com/groups/344863832904246/user/1000283385/',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
    )
st.write("---")

col1,col2,col = st.columns(3)
with col2:
    btn = st.button("wifi Speed test")
st.write("")
if btn:
    col3,col4,col5 = st.columns(3)
    with col4:
        with st.spinner('Wait for it...'):
            time.sleep(5)
    
    with col3:
        
        with st.spinner('Wait for it...'):
            time.sleep(1)
        download_speed = sp.download() / 1_000_000 # in Mbps
        st.info(f"Download Speed: {str(download_speed)[0:5]} Mbps")
    with col4:
        with st.spinner('Wait for it...'):
            time.sleep(2)
        upload_speed = sp.upload() / 1_000_000 # in Mbps
        st.info(f"Upload Speed: {str(upload_speed)[0:5]} Mbps")
    with col5:
        with st.spinner('Wait for it...'):
            time.sleep(2)
        ping = sp.results.ping # in ms
        st.info(f"Ping: {str(ping)[0:5]} ms")
        
st.write(" ")
st.write("---") 
st.write(" ")   
st.header("Copyright © 2023 , Credite : [Jasser](https://www.facebook.com/jasser.razzek.3/) .")
