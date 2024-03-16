from django import forms


g=[['MALE','male'],['FEMALE','female']]
c=[['python','sql'],['java','django'],['web','js']]

class NameForm(forms.Form):
    sname=forms.CharField()
    sage=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':10,'rows':6}))
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #gender=forms.ChoiceField(choices=g)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    #course=forms.MultipleChoiceField(choices=c)

