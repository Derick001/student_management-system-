from django.shortcuts import render,redirect
from .models import Teacher
from . forms import TeacherForm

# Create your views here.
def teachers_page(request):
    all_teacher=Teacher.objects.all()
    return render(request, 'db/index.html', {'all_teach':all_teacher})

def add_teacher(request):
    if request.method=="POST":
        method=request.POST
        first_name=method['first_name']
        last_name=method['last_name']
        other_name=method['other_name']
        address=method['address']
        new_teacher=Teacher.objects.create(first_name=first_name,
        last_name=last_name,
        other_name=other_name,
        address=address)
        new_teacher.save()
        all_teacher=Teacher.objects.all()
        return redirect('teachers_page')
    return render(request, 'db/add_teacher.html')

def delete_teacher(request,pk):
    delete=Teacher.objects.get(id=pk)
    delete.delete()
    return redirect('teachers_page')
    # all_teacher=Teacher.objects.all()
    # return render(request, 'db/index.html', context={'all_teach':all_teacher})

def update_teacher(request,pk):
    all_teach=Teacher.objects.get(id=pk)
    update_teacher=TeacherForm(instance=all_teach)
    if request.method=="POST":
        update_teacher=TeacherForm(request.POST,instance=all_teach)
        if update_teacher.is_valid():
            update_teacher.save()
            all_teacher=Teacher.objects.all()
        return redirect("teachers_page")
    return render(request, 'db/update.html', {'all_teach':all_teach, 'update_teacher':update_teacher})

def search_teacher(request):
    if request.method == "POST":
        name = request.POST["z"]
        retrived_teacher = Teacher.objects.filter(first_name = name)
        if retrived_teacher:
            return render(request, "db/index.html", context={"all_teacher":retrived_teacher})
    return render(request, "db/index.html")


