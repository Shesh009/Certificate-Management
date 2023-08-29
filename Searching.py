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

search("100521729002","Sheshu@009")