import streamlit as st
import Login

def size():
    s=" "
    c=0
    with open("Certificates.txt","r") as file1:
        while(s):
            s=file1.readline()
            c+=1
    file1.close()
    return c-1

def show(CollegeID):
    file_name="Certificates.txt"
    s=" "
    col1,col2,col3,col4=st.columns(4)
    col1.write("CollegeID")
    col2.write("Certificate Organisation")
    col3.write("Name of Certificate")
    col4.write("Certificate Link")
    with open(file_name,"r") as file1:
        for _ in range(size()):
            s=file1.readline()
            s=s.strip()
            L=s.split("|")  
            if L[0]==CollegeID:
                    col1,col2,col3,col4=st.columns(4)
                    col1.write(L[0])
                    col2.write(L[1])
                    col3.write(L[2])
                    col4.write(L[3])
    file1.close()

# def search(CollegeID,password):
#     file_name="data.txt"
#     s=" "
#     with open(file_name,"r") as file1:
#         for _ in range(size()):
#             s=file1.readline()
#             s=s.strip()
#             L=s.split("|")  
#             if L[3]==CollegeID and L[4]==password:
#                 return True
#     file1.close()
#     return False

def Upload_Files(CollegeID,password):
    if Login.search(CollegeID,password):
            st.write("Please change below details only")
            st.subheader("Fill all the details correctly you cannot update again")
            Cert_Orgzn=st.text_input("Enter the name of Organization/Company")
            Cert_name=st.text_input("Enter name of certificate")
            Cert_link=st.text_input("Paste Certificate link")
            file1=open("Certificates.txt","a+")
            col1,col2,col3,col4,col5=st.columns(5)
            if col3.button("ADD CERTIFICATE"):
                if Cert_Orgzn.strip()!="" and Cert_name.strip()!="" and Cert_link.strip()!="":
                    file1.writelines([CollegeID,"|",Cert_Orgzn,"|",Cert_name,"|",Cert_link,"\n"])
                    st.success("Certificate Successfully added\nPlease add other certificate")
                else:
                    st.error("Any of the Fields cannot be empty")
                file1.close()
    else:
        st.error("Please enter your credentials correctly!!!")
        st.error("Please register if not registered!!!")