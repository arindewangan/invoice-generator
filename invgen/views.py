from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def pdf(request):
    if request.method=='POST':
        pname = request.POST['pname']
        price = request.POST['price']
        qty = request.POST['qty']
        total = int(price)*int(qty)
        inv = request.POST['inv']
        date = request.POST['date']
        
        vname = request.POST['vname']
        vaddress = request.POST['vaddress']
        vphone = request.POST['vphone']
        
        cname = request.POST['cname']
        caddress = request.POST['caddress']
        cphone = request.POST['cphone']
        params = {
                'pname': pname,
                'price': price,
                'qty': qty,
                'vname': vname,
                'vaddress': vaddress,
                'vphone': vphone,
                'cname': cname,
                'caddress': caddress,
                'cphone': cphone,
                'inv': inv,
                'date': date,
                'total': total
            }    
        
        return render(request,'pdf.html',params)
    return render(request,'pdf.html')
    
