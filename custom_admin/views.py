from django.contrib.admin.sites import site
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

@user_passes_test(lambda u: u.is_superuser)
def custom_admin_dashboard(request):
    app_list = site.get_app_list(request)
    context = {
        'app_list': app_list,
        'title': 'Dashboard',
        'site_title': 'Back Office',
        'site_header': 'Back Office',
    }
    return render(request, 'admin/custom_index.html', context)