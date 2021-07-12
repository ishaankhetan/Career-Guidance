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
from django.contrib.auth.models import User

# Create your views here.
class UserCreateForm(UserCreationForm):
    ...
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        help_texts = {
            'username': None,
            'email': None,
            'password1':None,
            'password2':None
        }


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
        return          [
                        'Politician', 
                        'Entreupreneur', 
                        'Life Coach',
                        'Management Consultant',
                        'Motivational Speaker', 

                        'https://www.indeed.com/career-advice/career-development/how-to-become-a-politician',
                        'https://alcorfund.com/insight/how-to-become-an-entrepreneur-steps-and-tips-involved/',
                        'https://www.learnhowtobecome.org/life-coach/',
                        'https://www.upgrad.com/blog/how-to-become-a-management-consultant/',
                        'https://www.briantracy.com/blog/business-success/how-to-become-a-public-speaker-4-steps/'
                        ]
    elif num ==2:
        return          [
                        'Writer',
                        'Editor',
                        'Artist',
                        'Actor',
                        'Musician',
                        
                        'https://www.locationrebel.com/how-to-become-a-writer/',
                        'https://blog.reedsy.com/freelancer/how-to-become-an-editor-guide/',
                        'https://study.com/becoming_an_artist.html',
                        'https://www.learnhowtobecome.org/actor-or-actress/',
                        'https://www.academiccourses.com/article/how-to-become-a-professional-musician/'
                        ]
    elif num ==3:
        return          [
                        'Financial Analyst',
                        'Project Manager',
                        'Management Consultant',
                        'Office Manager',
                        'Public Administrator',
                        
                        'https://www.investopedia.com/articles/financialcareers/06/financialanalyst.asp',
                        'https://www.ntaskmanager.com/blog/how-to-become-a-project-manager/',
                        'https://www.upgrad.com/blog/how-to-become-a-management-consultant/',
                        'https://www.travelperk.com/guides/office-management/become-a-great-office-manager/',
                        'https://www.successcds.net/Career/career-in-public-administration.html#:~:text=Eligibility%20for%20Public%20Administration%20course,Public%20Administration%20is%20three%20years.'
                        ]
    elif num ==4:
        return          [
                        'Software Engineer',
                        'Technical Writer',
                        'Judge',
                        'Surgeon',
                        'Lawyer',
                        
                        'https://builtin.com/software-engineering-perspectives/how-to-become-a-software-engineer',
                        'https://www.informationdevelopers.in/become-technical-writer/#:~:text=Preferred%20Skills&text=University%20degree%20or%20Technical%20Writing%20college%20diploma%20in%20relevant%20field.&text=Excellent%20oral%20and%20written%20communication%20skills.&text=Knowledge%20of%20how%20to%20create%20and%20use%20graphics%20in%20technical%20documentation.&text=Knowledge%20of%20MS%2DVisio.',
                        'https://legodesk.com/blog/legal-practice/become-a-judge/#:~:text=The%20candidate%20must%20possess%20a,High%20Courts%2C%20and%20District%20Courts.',
                        'https://www.collegedekho.com/careers/surgeon#:~:text=Eligibility%20to%20become%20Surgeon,institute%20approved%20by%20the%20MCI.',
                        'https://www.collegedekho.com/careers/lawyer#:~:text=Becoming%20a%20lawyer%20requires%20one,Diploma%20or%20Certificate%20Law%20courses.'
                        ]
    else:
        return          [
                        'Financial Analyst', 
                        'Lawyer', 
                        'Research Scientist', 
                        'Entreupreneur', 
                        'Management Consultant',
                        
                        'https://www.investopedia.com/articles/financialcareers/06/financialanalyst.asp',
                        'https://www.collegedekho.com/careers/lawyer#:~:text=Becoming%20a%20lawyer%20requires%20one,Diploma%20or%20Certificate%20Law%20courses.',
                        'https://www.indeed.com/career-advice/career-development/how-to-become-a-research-scientist',
                        'https://alcorfund.com/insight/how-to-become-an-entrepreneur-steps-and-tips-involved/',
                        'https://www.upgrad.com/blog/how-to-become-a-management-consultant/'
                        ]

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
        result = decision(result)
        return render(request,'thankyou.html',{'string0': result[0], 'string1':result[1], 'string2':result[2], 'string3':result[3], 'string4':result[4], 'link0':result[5], 'link1':result[6], 'link2':result[7], 'link3':result[8], 'link4':result[9]})
    



    form = TestForm()
    return render(request,'main4.html',{'form':form})