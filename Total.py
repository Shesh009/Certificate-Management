import Register as Register
import Searching as Searching
import Login as log
import Upload as upload
import Profile as prof
import streamlit as st
from streamlit_option_menu import option_menu

# st.set_page_config(page_title = "This is a Multipage WebApp")
selected=option_menu(
        menu_title=None,
        options=["Home","Register","Upload","Certificates","Profile","Forgot Password"],
        icons=["house","r-circle","cloud-plus","link","person-circle","key"],
        default_index=0,
        orientation="horizontal"
    )


if selected=="Home":
    col=st.columns(5)
    col[2].header("WELCOME")
    st.write("--------------------------------------")
    col1=st.columns(2)
    col1[0].image("https://img.freepik.com/premium-photo/security-cyberspace-system-lock-network-cyber-digital-technology-protection-information-generative-ai_163305-192942.jpg?w=740")
    col1[1].write(" ")
    col1[1].write(" ")
    col1[1].write(" ")
    col1[1].write(" ")
    col1[1].subheader('''We warmly welcome you to the website where you can store any kind of certificates in one place.''')
    col1[1].subheader("You can secure your certificates by accessing them only with your Student ID and password.")
    col1[1].subheader("Easy way to manage your certificates.")
    st.write("--------------------------------------")
    col2=st.columns(2)
    col2[0].subheader("STEPS TO FOLLOW")
    col2[0].subheader("1.Register yourself in REGISTER section if not registered.")
    col2[0].subheader("2.Upload your certificates in UPLOAD section.")
    col2[0].subheader("3.Goto to CERTIFICATES section to view your certificates which are uploaded already.")
    col2[0].subheader("4.Use PROFILE section to view you details submitted.")
    col2[1].write("")
    col2[1].write("")
    col2[1].image("https://t3.ftcdn.net/jpg/04/98/10/04/360_F_498100428_I8Ww5c65aSd8aY3IXZwi02dUJCKMplOM.jpg")
    st.write("--------------------------------------")
    col3=st.columns(2)
    col3[0].write(" ")
    col3[0].write(" ")
    col3[0].write(" ")
    col3[0].image("https://www.picpedia.org/chalkboard/images/instructions.jpg")
    col3[1].header("INSTRUCTIONS")
    col3[1].subheader("1.Fill all your details correctly while REGISTERing.")
    col3[1].subheader("2.There is no chance to edit to your details submitted.")
    col3[1].subheader("3.If you have forgot your password you can use FORGOT PASSWORD section.")
    col3[1].subheader("4.Please upload the certificate in link format by converting image,pdf to link.")
    col3[1].subheader("5.Open only in desktop mode.")
    st.write("--------------------------------------")
    col4=st.columns(3)
    col4[2].image("https://www.seekpng.com/png/detail/195-1957268_contact-us-icons-png.png")
    col4[0].subheader("CONTACT US")
    col4[0].subheader("📞 +91 8790067206")
    col4[0].subheader("✉ akulasheshu4@gmail.com")
    col4[0].subheader("📍 UCEOU")
    col4[0].subheader("👬 Students of UCEOU")
# st.sidebar.success("Select Any Page from here")
elif selected=="Register":
    Register.User_register()
elif selected=="Certificates":
    CollegeId=st.text_input("Enter your StudentID")
    password=st.text_input("Enter your Password")
    log.login(CollegeId,password)
elif selected=="Upload":
    CollegeId=st.text_input("Enter your StudentID")
    password=st.text_input("Enter your Password")
    col=st.columns(7)
    upload.Upload_Files(CollegeId,password)
elif selected=="Profile":
    CollegeId=st.text_input("Enter your StudentID")
    password=st.text_input("Enter your Password")
    prof.profile(CollegeId,password)
elif selected=="Forgot Password":
    Register.forgot_password()
