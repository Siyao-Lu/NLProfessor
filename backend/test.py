import http.client

conn = http.client.HTTPSConnection("apigw.it.umich.edu")

headers = {
    'X-IBM-Client-Id': "85a71c08-04ad-442c-895e-7704f72c531e",
    'Authorization': "Bearer AAIkODVhNzFjMDgtMDRhZC00NDJjLTg5NWUtNzcwNGY3MmM1MzFlSoVTqn64YOE1GksKggt9o_MXgG3WbQ5dSqtqwy2cSzcbJPztFzkhKrtuWRSkvw2x_0jW8PDFn3WG0MlG4BZbxq22PxgHxZAtWQBa22mlAUXq7XPXBylzCznyRza7Xja0qcIFwFYhhv3ug901F6NFsQ",
    'accept': "application/json"
    }
# secrete: T6oX3aM6uW6tU8yH5lI0bL0vF7lP4tU0iQ1yG1vW2cW6vW1sC6
# scope: umscheduleofclasses
# encoded: ODVhNzFjMDgtMDRhZC00NDJjLTg5NWUtNzcwNGY3MmM1MzFlOlQ2b1gzYU02dVc2dFU4eUg1bEkwYkwwdkY3bFA0dFUwaVExeUcxdlcyY1c2dlcxc0M2
conn.request("GET", "/um/Curriculum/SOC/Terms", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))