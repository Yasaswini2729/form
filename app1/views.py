from django.shortcuts import render

# Create your views here.
def func1(request):
    result=None
    print(request)
    if request.method=="GET":
        a=int(request.GET.get('num'))
        if a%2==0:
            result=True
        else:
            result=False
    
    #print(type(a))
    return render(request,'index.html',{'res':result})