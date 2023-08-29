import streamlit as st
import Upload as up

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

def show(CollegeID):
    file_name="Certificates.txt"
    s=" "
    with open(file_name,"r") as file1:
        col1,col2,col3,col4=st.columns(4)
        if size()==0:
            st.write("You have not uploaded any certificates")
            return
        for _ in range(size()):
            s=file1.readline()
            s=s.strip()
            L=s.split("|")  
            if L[0]==CollegeID:
                    col1.write(L[0])
                    col2.write(L[1])
                    col3.write(L[2])
                    col4.write(L[3])
    file1.close()

def login(CollegeId,password): 
    col1,col2,col3,col4,col5=st.columns(5)
    if col3.button("SHOW CERTIFICATES"):
        if search(CollegeId,password):
            up.show(CollegeId)
            return True
        else:
            st.error("Please enter your credentials correctly!!!")
            st.error("Please register if not registered!!!")
            return False