from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, authenticate
from .forms import DataForm
from . import models
from django.core.mail import send_mail
from .forms import TestForm
import numpy as np
from sklearn.cluster import KMeans
import random
import matplotlib.pyplot as plt

# Create your views here.

class signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('main')
    template_name = 'signup.html'

class getInfo(generic.CreateView):
    form_class = DataForm
    success_url = reverse_lazy('login')
    template_name = 'main.html'


def yon():
    a=random.choice([0,1])
    return a

X = np.array([[yon() for x in range(10)] for x in range(300)])
print(X)
kmeans = KMeans(n_clusters=5)
kmeans.fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)   



def decision(num):
    base ="Your ideal jobs are:\n"
    if num ==1:
        return base+"Politician, Business Owner, Life Coach"
    elif num ==2:
        return base+ '''Writer,
                        Editor,
                        Artist,
                        Actor,
                        Musician'''
    elif num ==3:
        return base+''' Credit Analyst,
                        Insurance Adjuster,
                        Financial Counselor,
                        Project Manager,
                        Management Consultant,
                        Office Manager,
                        Public Administrator'''
    elif num ==4:
        return base+ '''Software developer,
Technical writer,
Judge,
Surgeon,
Executive attorney'''
    else:
        return base+" Financial Analyst, Lawyer, Scientist, Entreupreneur, Management Consultant"

def test(request):

    if request.method == 'POST':
       

        
        Q1 = int(request.POST['Q1'])
        Q2 = int(request.POST['Q2'])
        Q3 =int(request.POST['Q3'])
        Q4 = int(request.POST['Q4'])
        Q5 = int(request.POST['Q5'])
        Q6 = int(request.POST['Q6'])
        Q7 = int(request.POST['Q7'])
        Q8 = int(request.POST['Q8'])
        Q9 = int(request.POST['Q9'])
        Q10 = int(request.POST['Q10'])

        tlist= (int(Q1),int(Q2),int(Q3),int(Q4),int(Q5),int(Q6),int(Q7),int(Q8),int(Q9),int(Q10))
        error =[]
        for cet in centroids:
            error.append(sum(np.square(np.subtract(cet,tlist)))) 
        result=error.index(min(error))
        print(result)
        return render(request,'thankyou.html',{'result': decision(result)})
    



    form = TestForm()
    return render(request,'main4.html',{'form':form})