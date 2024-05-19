from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    
    if request.method == "POST":

        doctor = request.POST.get('department')
        username = request.POST.get('username')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        phone = request.POST.get('phone')

        # Send confirmation email to the user
        send_mail(
            "Thank You for Booking an Appoinment ",
            f"Dear {username},\n\nThank you for Booking an Appoinment. Please use the below crediantial to login and see your prescribtion, lab result and more. \n\nEmail: {email} \nPassword: {email}",
            'H-DOC <cabetech27@gmail.com>',  # Use your desired sender name and email here
            [email],
            fail_silently=False,
        )
        return render(request, "frontend/base.html")
    
    else:
        return render(request, "frontend/base.html")