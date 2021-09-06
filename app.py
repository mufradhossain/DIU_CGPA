from urllib.request import urlopen
import json
import streamlit as st
hide_streamlit_style = """
        <style>
        
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
html_temp = """
<body style="background-color:red;">
<div style="background-color:#1A4645 ;padding:10px">
<h2 style="color:white;text-align:center;">Calculate DIU CGPA</h2>
<p style="color:white;text-align:center;">Enter your DIU ID to calculate your CGPA</p>
</div>
</body>
"""
st.markdown(html_temp, unsafe_allow_html=True)





studentID = st.text_input("Enter your DIU ID")


if st.button('Get CGPA'):
    studentinfo_url = "http://software.diu.edu.bd:8189/result/studentInfo?studentId="+str(studentID)
    semesterinfo_url = "http://software.diu.edu.bd:8189/result/semesterList"
    response = urlopen(studentinfo_url)
    studentinfo_json = json.loads(response.read())
    response = urlopen(semesterinfo_url)
    semesterinfo_json = json.loads(response.read())
    semesterlength = len(semesterinfo_json)
    semesters=[]
    for x in range(semesterlength):
        semesters.append(semesterinfo_json[x]['semesterId'])
        fullresult={}
        for semester in semesters:
            result_url="http://software.diu.edu.bd:8189/result?grecaptcha=&semesterId="+str(semester)+"&studentId="+str(studentID)
            response = urlopen(result_url)
            semesterresult_json = json.loads(response.read())
            fullresult[semesterresult_json[0]['semesterId']]=semesterresult_json
            if semesterresult_json[0]['semesterId']== studentinfo_json['semesterId']:
                break


    fullresult_keys = list(fullresult.keys())


    total_credits=0
    total_cgpa=0


    st.text("Name: "+ studentinfo_json["studentName"])
    st.text('ID: '+studentinfo_json["studentId"])
    st.text("Program: "+studentinfo_json["programName"])




    for y in fullresult_keys:

        semester_credits=0
        semester_sgpa=0


        for x in range(len(fullresult[y])):


            total_credits = total_credits + fullresult[y][x]['totalCredit']


            total_cgpa = total_cgpa + ((fullresult[y][x]['pointEquivalent'])*(fullresult[y][x]['totalCredit']))
    CGPA= total_cgpa/total_credits


    st.text("Total Credits Completed: "+ str(int(total_credits)))
    number = 3.1415926
    st.success(f"CGPA: {CGPA:.2f}")
    
