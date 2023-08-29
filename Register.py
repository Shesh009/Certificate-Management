import streamlit as st
import Profile as prof

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
            if L[3]==CollegeID:
                return True
    file1.close()
    return False

def User_register():
    st.subheader("Fill all the details correctly you cannot update again")
    name=st.text_input("Full Name")
    mobile=st.text_input("Mobile Number")
    email=st.text_input("Email (gmail,hotmail,outlook)")
    college=st.text_input("Enter your college Name")
    College_id=st.text_input("Enter your student id")
    movie=st.text_input("Enter your favourite movie name (Used when you forgot your password) ")
    password=st.text_input("Enter your password")
    confirm_password=st.text_input("Please confirm your password")
    if st.checkbox("I agree to terms and conditions"):
        col=st.columns(5)
        if col[2].button("REGISTER"):
            if name.strip()=="" or mobile.strip()=="" or email.strip()=="" or college.strip()=="" or College_id.strip()=="" or movie.strip()=="" or password.strip()=="":
                st.error("Any Field cannot be empty")
            elif (x.isalpha() and x.isspace() for x in name)==False:
                st.error("Name should not contain only alphabets")
            elif mobile.isnumeric()==False or (len(mobile)!=10):
                st.error("Mobile number should be correct")
            elif "@gmail.com" not in email and "@hotmail" not in email and "@outlook" not in email:
                st.error("Invalid Email")
            elif password!=confirm_password:
                st.error("Password and confirm password are not same!!")
            else:
                if search(College_id,password)==False:
                    file1=open("data.txt","a+")
                    file1.writelines([name,"|",mobile,"|",college,"|",College_id,"|",password,"|",email,"|",movie,"\n"])
                    file1.close()
                    st.success("You have Registered Successfully")
                else:
                    st.error("You have already Registered")

def forgot_password():
    CollID=st.text_input("Enter your student ID")
    mobile_num=st.text_input("Enter your mobile number")
    email_ID=st.text_input("Enter your Email ID")
    movie_name=st.text_input("Enter the given movie name")
    col10=st.columns(5)
    if col10[2].button("GET PASSWORD"):
        prof.forgot(CollID,mobile_num,email_ID,movie_name)