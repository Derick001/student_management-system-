from django.shortcuts import render,redirect
from .models import Student
from .forms import UpdateForm
from django.db.models import Q

# Create your views here.
def student_page(request):
    all_studs = Student.objects.all()
    return render(request, 'db/student.html', {'all_students':all_studs})

def new_student(request):
    if request.method=="POST":
        method=request.POST
        first_name=method['first_name']
        last_name=method['last_name']
        other_name=method['other_name']
        course=method['course']
        address=method['address']
        d_o_b=method['d_o_b']
        new_student=Student.objects.create(first_name=first_name, last_name=last_name,other_name=other_name,
        course=course, d_o_b=d_o_b,address=address)
        new_student.save()
        all_studs = Student.objects.all()
        return redirect('student_page')
    return render(request, 'db/addStudent.html')

def delete_student(request, pk):
    update_student = Student.objects.get(id=pk)
    update_student.delete()
    all_studs = Student.objects.all()
    return redirect('student_page')

def update_student(request,pk):
    update=Student.objects.get(id=pk)
    updateform=UpdateForm(instance=update)
    if request.method=="POST":
        updateform=UpdateForm(request.POST, instance=update)
        if updateform.is_valid():
            updateform.save()
            all_studs = Student.objects.all()
        return redirect('student_page')
    return render(request, 'db/updatestudent.html', {'update':update, 'updateform':updateform})

def search_name(request):
    if request.method == "POST":
        name = request.POST["q"]
        retrived_student = Student.objects.filter(first_name = name)
        if retrived_student:
            return render(request, "db/student.html", context={"all_studs":retrived_student} )
    return render(request, "db/student.html"  )
    # else:
    #     all_studs= Student.objects.all()
    #     context={
    #         'all_stud':all_studs
    #     } 
    # return redirect('student_page', context)
