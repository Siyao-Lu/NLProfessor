import http.client

conn = http.client.HTTPSConnection("apigw.it.umich.edu")

headers = {
    'X-IBM-Client-Id': "85a71c08-04ad-442c-895e-7704f72c531e",
    'Authorization': "Bearer AAIkODVhNzFjMDgtMDRhZC00NDJjLTg5NWUtNzcwNGY3MmM1MzFlSoVTqn64YOE1GksKggt9o_MXgG3WbQ5dSqtqwy2cSzcbJPztFzkhKrtuWRSkvw2x_0jW8PDFn3WG0MlG4BZbxq22PxgHxZAtWQBa22mlAUXq7XPXBylzCznyRza7Xja0qcIFwFYhhv3ug901F6NFsQ",
    'accept': "application/json"
    }

# conn.request("GET", "/um/Curriculum/SOC/Terms/2420/Classes/21631", headers=headers)
# conn.request("GET", "/um/Curriculum/SOC/Terms/REPLACE_TERMCODE/Classes/REPLACE_CLASSNUMBER", headers=headers)
# conn.request("GET", "/um/Curriculum/SOC/Terms/2420/Classes/Search/Machine_Learning", headers=headers)
# conn.request("GET", "/um/Curriculum/SOC/Terms/REPLACE_TERMCODE/Classes/REPLACE_CLASSNUMBER/CombinedSections", headers=headers)
# conn.request("GET", "/um/Curriculum/SOC/Terms/2420/Schools", headers=headers)
# conn.request("GET", "/um/Curriculum/SOC/Terms/2420/Schools/ENG/Subjects", headers=headers)
# conn.request("GET", "/um/Curriculum/SOC/Terms/2420/Schools/ENG/Subjects/EECS/CatalogNbrs", headers=headers)
conn.request("GET", "/um/Curriculum/SOC/Terms/2420/Schools/ENG/Subjects/EECS/CatalogNbrs/449", headers=headers)
''' 
{"getSOCCourseDescrResponse":{"@schemaLocation":"http://mais.he.umich.edu/schemas/getSOCCourseDescrResponse.v1 http://csprodib.dsc.umich.edu/PSIGW/PeopleSoftServiceListeningConnector/getSOCCourseDescrResponse.v1.xsd","CourseDescr":"Conversational Artificial Intelligence --- The science and art of creating conversational AI spans multiple areas in computer science. Students will\nlearn about and leverage advances in these areas to create conversational virtual assistants spanning natural language processing, dialogue management, response generation, and other applications."}}
'''

# conn.request("GET", "/um/Curriculum/SOC/Terms/REPLACE_TERMCODE/Schools/REPLACE_SCHOOLCODE/Subjects/REPLACE_SUBJECTCODE/CatalogNbrs/REPLACE_CATALOGNUMBER/Sections?IncludeAllSections=N", headers=headers)
# conn.request("GET", "/um/Curriculum/SOC/Terms/REPLACE_TERMCODE/Schools/REPLACE_SCHOOLCODE/Subjects/REPLACE_SUBJECTCODE/CatalogNbrs/REPLACE_CATALOGNUMBER/Sections/REPLACE_SECTIONNUMBER", headers=headers)
# conn.request("GET", "/um/Curriculum/SOC/Terms/REPLACE_TERMCODE/Schools/REPLACE_SCHOOLCODE/Subjects/REPLACE_SUBJECTCODE/CatalogNbrs/REPLACE_CATALOGNUMBER/Sections/REPLACE_SECTIONNUMBER/CombinedSections", headers=headers)
# conn.request("GET", "/um/Curriculum/SOC/Terms/REPLACE_TERMCODE/Schools/REPLACE_SCHOOLCODE/Subjects/REPLACE_SUBJECTCODE/CatalogNbrs/REPLACE_CATALOGNUMBER/Sections/REPLACE_SECTIONNUMBER/Instructors", headers=headers)
# conn.request("GET", "/um/Curriculum/SOC/Terms/REPLACE_TERMCODE/Schools/REPLACE_SCHOOLCODE/Subjects/REPLACE_SUBJECTCODE/CatalogNbrs/REPLACE_CATALOGNUMBER/Sections/REPLACE_SECTIONNUMBER/Meetings", headers=headers)
# conn.request("GET", "/um/Curriculum/SOC/Terms/REPLACE_TERMCODE/Schools/REPLACE_SCHOOLCODE/Subjects/REPLACE_SUBJECTCODE/CatalogNbrs/REPLACE_CATALOGNUMBER/Sections/REPLACE_SECTIONNUMBER/Textbooks", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))