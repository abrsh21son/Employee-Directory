from django.http import  HttpResponse
from django.shortcuts import render
from employees.models import employee
def home(request):
    employees=employee.objects.all()
    context={
        'employees':employees
    }
    return render(request,'home.html',context)
    
def about(request):
    return HttpResponse("""
    <div style="
        background: linear-gradient(135deg, #f0f4f8, #d9e2ec);
        padding: 20px;
        border-radius: 12px;
        max-width: 320px;
        margin: 50px auto;
        text-align: center;
        font-family: 'Arial', sans-serif;
        box-shadow: 0 8px 16px rgba(0,0,0,0.15);
        border-top: 4px solid #1e40af;
    ">
        <h1 style="
            color: #1e40af;
            font-size: 22px;
            margin-bottom: 10px;
            font-weight: bold;
        ">
            Beautifully styled card
        </h1>
        <p style="
            color: #334155;
            font-size: 14px;
            margin: 0 0 15px 0;
        ">
            This is a compact, elegant card styled entirely with inline CSS.
        </p>
        <button style="
            padding: 8px 16px;
            background-color: #1e40af;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 14px;
        " onmouseover="this.style.backgroundColor='#3b82f6'" onmouseout="this.style.backgroundColor='#1e40af'">
            Action
        </button>
    </div>
    """)