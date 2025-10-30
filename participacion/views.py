from django.shortcuts import render

# Create your views here.
def formulario_equipo(request):
    datos = None
    if request.method == 'POST':
        nombredeequipo = request.POST.get('nombredeequipo')
        nombredejefe = request.POST.get('nombredejefe')
        membresia = request.POST.get('membresia')
        cantidad = request.POST.get('cantidad')
        #multiplica membresia por cantidad y lo guarda en una variable total
        total = int(membresia) * int(cantidad)
    

        datos = {
            'nombredeequipo': nombredeequipo,
            'nombredejefe': nombredejefe,    
            'total': total
        }


    return render(request,'formulario.html',{'datos':datos})
