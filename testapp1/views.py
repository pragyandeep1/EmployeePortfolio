from django.shortcuts import render
from testapp1.models import Employee
from django.db.models import Q,Avg,Max,Min,Sum,Count

# Create your views here.
def aggregate_view(request):
    avg = Employee.objects.all().aggregate(Avg('esal'))
    max = Employee.objects.all().aggregate(Max('esal'))
    min = Employee.objects.all().aggregate(Min('esal'))
    sum = Employee.objects.all().aggregate(Sum('esal'))
    count = Employee.objects.all().aggregate(Count('esal'))
    my_dict = {'avg':avg['esal__avg'], 'max':max['esal__max'], 'min':min['esal__min'],'sum':sum['esal__sum'],'count':count['esal__count']}
    return render(request,'testapp1/aggregate.html',my_dict)

def display_view(request):
    # emp_list = Employee.objects.all()
    # emp_list = Employee.objects.get_emp_sorted_by('ename')
    # emp_list = Employee.objects.get_emp_sorted_by('-esal')
    emp_list = Employee.objects.get_emp_sal_range(18000, 20000)
    return render(request,'testapp1/index.html',{'emp_list':emp_list})
