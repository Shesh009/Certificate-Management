import Login
import streamlit as st

def size():
    s=" "
    c=0
    with open("data.txt","r") as file1:
        while(s):
            s=file1.readline()
            c+=1
    file1.close()
    return c-1

def search(CollegeID,password):
    file_name="data.txt"
    s=" "
    with open(file_name,"r") as file1:
        for _ in range(size()):
            s=file1.readline()
            s=s.strip()
            L=s.split("|")  
            if L[3]==CollegeID and L[4]==password:
                return True
    file1.close()
    return False

def forgot(CollegeID,mobile,email,movie):
    file_name="data.txt"
    s=" "
    c=0
    with open(file_name,"r") as file1:
        for _ in range(size()):
            s=file1.readline()
            s=s.strip()
            L=s.split("|")  
            if L[3]==CollegeID and L[5]==email and L[1]==mobile and L[6]==movie:
                st.success("Your password is "+L[4])
                c+=1
    if c==0:
        st.error("Enter your details correctly")
    file1.close()
    return False

def profile(CollegeId,password):
    col1=st.columns(7)
    if col1[3].button("SHOW DETAILS"):
        if Login.search(CollegeId,password)==False:
            st.error("Please enter your credentials correctly!!!")
            st.error("Please register if not registered!!!")
        else:
            s=" "
            file_name="data.txt"
            s=" "
            with open(file_name,"r") as file1:
                for _ in range(size()):
                    s=file1.readline()
                    s=s.strip()
                    L=s.split("|")  
                    if L[3]==CollegeId and L[4]==password:
                        st.header("YOUR DETAILS")
                        col2=st.columns(3)
                        col2[0].subheader([" Name ",L[0]][0])
                        col2[1].subheader([" Name ",L[0]][1])
                        col3=st.columns(3)
                        col3[0].subheader([" Mobile",L[1]][0])
                        col3[1].subheader([" Mobile",L[1]][1])
                        col4=st.columns(3)
                        col4[0].subheader([" Email",L[5]][0])
                        col4[1].subheader([" Email",L[5]][1])
                        col5=st.columns(3)
                        col5[0].subheader([" College",L[2]][0])
                        col5[1].subheader([" College",L[2]][1])
                        col6=st.columns(3)
                        col6[0].subheader([" Student ID",L[3]][0])
                        col6[1].subheader([" Student ID",L[3]][1])
            file1.close()
            return False
