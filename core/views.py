from django.shortcuts import render

def get_theme_template(request, page_name):
    # Get theme from query params or cookies
    theme = request.GET.get('theme') or request.COOKIES.get('theme')
    
    # Map page names to file names if necessary
    page_map = {
        'index': 'index.html',
        'dashboard': 'admin-dashboard.html' if not theme or theme == 'default' else 'dashboard.html',
        'announcements': 'announcements.html',
        'certificates': 'certificates.html',
    }
    
    filename = page_map.get(page_name, f"{page_name}.html")
    
    if theme and theme != 'default' and theme in ['theme2', 'theme3', 'theme4']:
        return f"core/{theme}/{page_name}.html"
    return f"core/{filename}"

def home(request):
    theme = request.GET.get('theme')
    response = render(request, get_theme_template(request, 'index'))
    if theme:
        response.set_cookie('theme', theme)
    return response

def admin_demo(request):
    return render(request, get_theme_template(request, 'dashboard'))

def certificates(request):
    return render(request, get_theme_template(request, 'certificates'))

def announcements(request):
    return render(request, get_theme_template(request, 'announcements'))
