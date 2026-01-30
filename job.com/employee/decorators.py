from django.shortcuts import redirect,render


def employee_login_required(function):
    def wrappeer(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('user_login')
        else:
            if request.user.role != 'USER':
                return render(request, "404.html")
        return function(request,*args,**kwargs)
    return wrappeer