from django.shortcuts import render
import ipaddress


def ip_validator(request):
        data = {"error":"", "image":""}
        #str1='10.10.10.2/24'
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        ip_ver = ipaddress.ip_address(str(ip))
        
        if ip_ver.version == 4:
            data['error'] = "Sorry, only reachable by IPv6"
        else:
            data["image"] = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/White_Persian_Cat.jpg/220px-White_Persian_Cat.jpg"
        print(data, ip_ver.version)
        return render(request, "index.html", data)
