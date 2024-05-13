from django import forms

class Student(forms.Form):
    name = forms.CharField()
    mail = forms.EmailField()
    mobile =forms.IntegerField()
    rollno = forms.IntegerField()
    feedback =forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        print("validating name filed")
        inputname = self.cleaned_data['name']
        if len(inputname)<4:
             raise forms.ValidationError(" NAME minimum length should be foue character")
        return inputname # this is indiviual validation

    
    
    #def clean(self):#this ek se kisi bhi field ko validating kar sakte
     #   print("total form validation")
      # print("validating name")
       # inputname = total_cleaned_data['name']
        #if inputname[0].lower !='d':
         #   forms.ValidationError('name should start with d')
          