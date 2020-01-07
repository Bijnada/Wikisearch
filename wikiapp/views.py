from django.shortcuts import render
from django.http import HttpResponse
import wikipedia
import fpdf

def sayhello(request):
    return HttpResponse('<h2> Helloworld <h2>')

def index(request):
    return render(request,'index.html')

def wiki(request):
    if request.method == 'POST':
        search = request.POST['search']
        pdf = fpdf.FPDF(format='letter')
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # name = input("Enter a name : ")
        result = wikipedia.summary(search)
        # print(result)
        pdf.write(5,result)
        pdf.ln()
        try:
            pdf.output("testings.pdf")
        except UnicodeEncodeError as e:
            print("Some unicode character is available")
        finally:
            return HttpResponse(result)