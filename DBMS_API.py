from fastapi import FastAPI
import pymysql
import json

def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password = "YashRajSaxena@123",
        db='Mini_Project',
    )
      
    
    cur = conn.cursor()
    cur.execute("select * from StudentDetails")
    output = cur.fetchall()
    for i in output:
        print(i, type(i))

    class create_dict(dict): 
            # __init__ function 
            def __init__(self): 
                self = dict() 
            # Function to add key:value 
            def add(self, key, value): 
                self[key] = value

    def student_json_mk():
        my_dict = create_dict()
        i =1
        for row in output:
            my_dict.add(i,({"Section": row[1],"USN": row[2],"name":row[3],"Batch": row[4],"TeamName":row[5],"Guid":row[6],"report_marks":row[7], "Presentation_marks": row[8],"viva_marks":row[9], "total_marks":row[10], "Dep": row[11]}))
            i+=1

        stud_json = json.dumps(my_dict, indent=2,)

        return stud_json


    
    conn.close()
app = FastAPI()
@app.get("/student_details")
def student_detail():
    details = student_json_mk()
    return details

# Driver Code
if __name__ == "__main__" :
    mysqlconnect()

