from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *
from .models import *


@api_view(['GET'])
def Getinfo(request):
    a = Info.objects.all().order_by('-id')[0:1]
    ser = InfoSerializer(a, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getslider(request):
    b = Slider.objects.all().order_by('-id')[0:5]
    ser = SliderSerializer(b, many=True)
    return Response(ser.data)



@api_view(['GET'])
def Getprojects(request):
    c = Projects.objects.all()
    ser = ProjectsSerializer(c, many=True)
    return Response(ser.data)



@api_view(['GET'])
def Gettechnopark(request):
    a = Technopark.objects.all().order_by('-id')[:6]
    ser = TechnoparkSerilaizer(a, many=True)
    return Response(ser.data)



@api_view(['GET'])
def Getsection(request):
    b = Section.objects.all()
    ser = SectionSerializer(b, many=True)
    return Response(ser.data)

@api_view(['GET'])
def Getpostal(request):
    c = Postalservices.objects.all()
    ser = PostalSerializer(c, many=True)
    return Response(ser.data)



@api_view(['POST'])
def Postboglanish(request):
    fullname = request.POST.get('fullname') 
    phone = request.POST.get('phone')
    text = request.POST.get('text')
    a = Boglanish.objects.create(fullname=fullname, phone=phone, text=text)
    ser = BoglanishSerializer(a)
    return Response(ser.data)



@api_view(['GET'])
def Getmobileoperators(request):
    e = Mobileoperators.objects.all()
    ser = MobileoperatorsSerializer(e, many=True)
    return Response(ser.data)



@api_view(['GET'])
def Getinternetproviders(request):
    f = Internetproviders.objects.all()
    ser = InternetprovidersSerializer(f, many=True)
    return Response(ser.data)



@api_view(['GET'])
def Getouraudience(request):
    g = OurAudience.objects.all().order_by('-id')[:5]
    ser = OurAudienceSerializer(g, many=True)
    return Response(ser.data)



@api_view(['GET'])
def Getpercentage(request):
    h = Percentage.objects.all().order_by('-id')[:4]
    ser = PercentageSerializer(h, many=True)
    return Response(ser.data)



@api_view(['GET'])
def Getresidents(request):
    i = Residents.objects.all().order_by('-id')[:5]
    ser = ResidentsSerializer(i, many=True)
    return Response(ser.data)



@api_view(['GET'])
def Getteam(request):
    j = Team.objects.all().order_by('-id')[0:1]
    ser = TeamSerializer(j, many=True)
    return Response(ser.data)



@api_view(['GET'])
def Getcoimages(request):
    k = Coimages.objects.all().order_by('-id')[0:2]
    ser = CoimagesSerializer(k, many=True)
    return Response(ser.data)



@api_view(['GET'])
def Getcoworking(request):
    l = Coworking.objects.all().order_by('-id')[0:2]
    ser = CoworkingSerializer(l, many=True)
    return Response(ser.data)



@api_view(['GET'])
def Getinfrastructure(request):
    m = InfrastructureSlider.objects.all().order_by('-id')[:5]
    ser = InfrastructureSliderSerializer(m, many=True)
    return Response(ser.data)



@api_view(['GET'])
def Getstudydirections(request):
    n = StudyDirections.objects.all().order_by('-id')[:5]
    ser = StudydirectionsSerializer(n, many=True)
    return Response(ser.data)



@api_view(['GET'])
def Getitacademy(request):
    o = ItAcademy.objects.all()
    ser = ItAcademySerializer(o, many=True)
    return Response(ser.data)



@api_view(['GET'])
def Getstartupdirections(request):
    q = StartupDirections.objects.all()
    ser = StartupDirectionsSerializer(q, many=True)
    return Response(ser.data)



@api_view(['GET'])
def Getincubationcenters(request):
    r = IncubationCenters.objects.all()
    ser = IncubationCentersSerializer(r, many=True)
    return Response(ser.data)



@api_view(['GET'])
def Getraqamlashtirish(request):
    s = Raqamlashtirishchizmalari.objects.all().order_by('-id')[0:1]
    ser = RaqamlashtirishchizmatlariSerializer(s, many=True)
    return Response(ser.data)



@api_view(['POST'])
def Postcontact(request):
    fullname = request.POST.get('fullname') 
    phone = request.POST.get('phone')
    text = request.POST.get('text')
    email = request.POST.get('email')
    Contact.objects.create(fullname=fullname, phone=phone, text=text, email=email)
    return Response(['Created!'])



@api_view(['GET'])
def Getxizmatturi(request):
    u = XizmatTuri.objects.all().order_by('-id')[:3]
    ser = XizmatTuriSerializer(u, many=True)
    return Response(ser.data)



@api_view(['GET'])
def Getxizmatlar(request):
    v = Xizmatlar.objects.all()
    ser = XizmatlarSerializer(v, many=True)
    return Response(ser.data)



@api_view(['POST'])
def Postapplication(request):
    fullname = request.POST.get('fullname') 
    phone = request.POST.get('phone')
    text = request.POST.get('text')
    email = request.POST.get('email')
    xizmat = request.POST.get('xizmat')
    xizmat = XizmatTuri.objects.get(id=xizmat)
    a = Application.objects.create(xizmat=xizmat, fullname=fullname, phone=phone, text=text, email=email)
    ser = ApplicationSerializer(a)
    return Response(ser.data)
