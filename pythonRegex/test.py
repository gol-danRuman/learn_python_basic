import re

value = 'https://storage.googleapis.com/dummy-bucket-test/Course%20for%20Codehub/DeepLearning-Module1-Unit1/OOP-in-Python.ipynb'
plain_courseName = 'Course for Codehub'
def changeURLToNotebookLink(value,coursename):
    return re.sub(r'(.*?)(/)'+coursename+'/', '/notebooks/', value)

def changeCourseName(plain_courseName):
    return re.sub(r"\s+", "-", plain_courseName)
print('generated link :: {}'.format(changeURLToNotebookLink(value, plain_courseName)))
print('Remove all spaces using RegEx:\n', changeCourseName(plain_courseName), sep='')