from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
import requests


def CustomPasswordSetRedirectView(request):
    return redirect('account_login')

def is_google_authenticated(user):
    return user.socialaccount_set.filter(provider='google').exists()

@login_required
@user_passes_test(is_google_authenticated, login_url='login')
def dados(request):
    user = request.user
    if not user.has_usable_password():
        return redirect('set_password')

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data = response.json()
    else:
        data = []
        print("Erro na solicitação da API")

    return render(request, 'dados.html', {'data': data})
