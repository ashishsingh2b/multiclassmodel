from django.shortcuts import render
from .models import Student,Teacher,Commoninfo
# Create your views here.
def home(request):
    commondetail = Commoninfo.objects.all()
    studentdata = Student.objects.all()
    teacherdata =Teacher.objects.all()
    return render(request,'home.html',{'students':studentdata,'teachers':teacherdata,'commoninfos':commondetail})