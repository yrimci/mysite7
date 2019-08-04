'''
Created on 2019. 7. 27.

@author: 405-19

HTML에 들어갈 <form>의 <input>을 관리하는 클래스 정의
model form은 미리 만들어져있는 models클래스를 가져올 때 쓰는 것.

'''
from django import forms
from vote.models import Choice, Question
#Question 모델클래스와 연동된 Form 클래스 정의
#모델클래스와 Form클래스를 연동시킬려면 ModelForm클래스를 상속받아야함
class QuestionForm(forms.ModelForm):
    #ModelForm클래스에서는 Meta클래스를 정의함으로써 어떤 모델클래스와 연동하는지 어떤 변수값을 사용할 것인지 작성
    class Meta: #Meta는 앞에 대문자로 써줘야함
        #model, fields, exclude(변수들)
        #model: 어떤 모델클래스와 연동했는지 저장하는 변수
        #fields, exclude 중 한개의 변수를 사용해 사용할 변수 정의
        model=Question
        fields=['title'] #title변수값을 기입할 수 있도록 정의
        #exclude=['pub_date']  #: pub_date를 제외한 나머지 변수를 기입할 수 있도록 정의
        
#Choice 모델클래스와 연동된 ChoiceForm 클래스 정의
class ChoiceForm(forms.ModelForm):
    class Meta:
        model=Choice
        #q변수와 name변수를 접근할 수 있도록 설정
        fields=['name']
        fields=['q']
        #exclude=['votes']
        