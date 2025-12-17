from django.shortcuts import render

def home(request):
    # Landing page for AScienti Sols
    return render(request, "core/index.html")

def admin_demo(request):
    # Admin dashboard demo page (front-end only)
    return render(request, "core/admin-dashboard.html")

def certificates(request):
    # Certificates page (front-end only)
    return render(request, "core/certificates.html")

def announcements(request):
    # Announcements page (front-end only)
    return render(request, "core/announcements.html")
