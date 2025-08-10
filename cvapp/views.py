from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .models import CV
from .forms import CVForm
from django.core.paginator import Paginator
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from cvapp.models import CustomUser
from django.contrib.auth import login
from django.contrib import messages

@login_required
def home(request):
    return render(request, 'cvapp/home.html',{'cvs': cvs})

@login_required
def cv_list(request):
    cvs = CV.objects.all()  # Affichage de tous les CVs
    return render(request, 'cvapp/cv_list.html', {'cvs': cvs})


@login_required
def cv_detail(request, pk):
    cv = get_object_or_404(CV, id=pk)  # Remplacez 'id' par la clé primaire correcte
    return render(request, 'cvapp/cv_detail.html', {'cv': cv})


@login_required
def cv_create(request):
    if request.method == 'POST':
        form = CVForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cvapp/cv_list.html')
    else:
        form = CVForm()
    return render(request, 'cvapp/cv_create.html', {'form': form})


@login_required
def cv_edit(request, pk):
    cv = get_object_or_404(CV, pk=pk) # Si la demande est un POST, nous mettons à jour le CV
    if request.method == 'POST':
        form = CVForm(request.POST, instance=cv)
        if form.is_valid():
            form.save()
            messages.success(request, 'CV modifié avec succès !')
            return redirect('cv_detail', pk=cv.pk)  # Redirige vers la page de détails du CV modifié
    else:
        form = CVForm(instance=cv)

    return render(request, 'cvapp/cv_edit.html', {'form': form, 'cv': cv})

@login_required
def cv_delete(request, pk):
    cv = get_object_or_404(CV, pk=pk)  # Récupérer le CV avec l'ID donné

    if request.method == 'POST':  # Vérifie si la demande est de type POST pour confirmer la suppression
        cv.delete()  # Supprimer le CV
        return redirect('cv_list')  # Redirige vers la liste des CV

    return render(request, 'cvapp/cv_confirm_delete.html', {'cv': cv})  # Affiche la page de confirmation



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CVForm
from .models import CV

@login_required
def submit_cv(request):
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES)
        
        if form.is_valid():
            try:
                cv = form.save(commit=False)
                cv.user = request.user  # Associer le CV à l'utilisateur
                cv.save()
                
                messages.success(request, 'CV soumis avec succès !')
                return redirect('cv_success')

            except Exception as e:
                print("Erreur lors de l'enregistrement :", e)
                messages.error(request, "Une erreur est survenue lors de l'enregistrement.")
        
        else:
            messages.error(request, "Le formulaire contient des erreurs.")
            print("Erreurs du formulaire :", form.errors)

    else:
        form = CVForm()

    return render(request, 'cvapp/submit_cv.html', {'form': form})





@login_required
def cv_success(request):
    return render(request, 'cvapp/cv_success.html')

@login_required
def download_cv(request, pk):
    try:
        cv = CV.objects.get(pk=pk)
        # Simule un fichier téléchargé, tu peux adapter selon le besoin
        response = HttpResponse(cv.summary, content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename="{cv.full_name}.txt"'
        return response
    except CV.DoesNotExist:
        return HttpResponse("CV introuvable", status=404)


@login_required
def download_all_cvs(request):
    # Logique pour télécharger tous les CVs sous forme de ZIP
    return HttpResponse("Téléchargement de tous les CVs non implémenté.")

# Mise à jour d'un CV
@login_required
def cv_update(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    if request.method == 'POST':
        form = CVForm(request.POST,request.FILES, instance=cv)
        if form.is_valid():
            form.save()
            return redirect('cv_list',pk=cv.pk)  # Redirige vers la liste des CVs
    else:
        form = CVForm(instance=cv)
    return render(request, 'cvapp/cv_update.html', {'form': form})

@login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Afficher un message d'erreur
            return render(request, 'login.html', {'error': 'Identifiants incorrects'})
    return render(request, 'login.html')
    from django.contrib.auth.views import LoginView

@login_required
def payment(request):
    if request.method == 'POST':
        # Logique pour traiter le paiement
        request.user.profile.has_paid = True
        request.user.profile.save()
        return redirect('create_cv')
    return render(request, 'cvapp/payment.html')

def logout_view(request):
    logout(request)  # Déconnecte l'utilisateur
    return redirect('home')  # Redirige vers la page d'accueil


def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistrer l'utilisateur
            messages.success(request, 'Votre compte a été créé avec succès !')  # Message de succès
            return redirect('login')  # Redirection vers la page de connexion ou une autre page
        else:
            print(form.errors)  # Affiche les erreurs dans la console Django
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')  # Message d'erreur
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'cvapp/signup.html', {'form': form})

@login_required
def profile_view(request):
    # Vérifie si l'utilisateur est authentifié
    if request.user.is_authenticated:
        user = CustomUser.objects.get(username=request.user.username)
        return render(request, 'cvapp/profile.html', {'user': user})
    else:
        return redirect('login')  # Redirige si l'utilisateur n'est pas connecté

@login_required
def home_view(request):
    return render(request, 'cvapp/home.html')


