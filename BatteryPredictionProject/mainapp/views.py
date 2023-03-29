from django.shortcuts import redirect
from .forms import UserPredictionForm
from .models import UserPrediction,UserProfile
from .LSTM import prediction as predictionmodel


from django.shortcuts import redirect, render

def dashboard(request):
    #get all prredictions from the DB
    predictions = UserPrediction.objects.all().order_by('-timestamp')

    #Get all Registeres Users from the DB
    userprofiles = UserProfile.objects.all()

    total_predictions = predictions.count()

    total_userprofiles = userprofiles.count()

    last_prediction = predictions[0]

    context = {'predictions': predictions,'userprofiles':
     userprofiles,'total_predictions': total_predictions,
     'total_userprofiles':total_userprofiles,'last_prediction':last_prediction}
    return render(request, 'mainapp/dashboard.html',context)


def make_predictions(request):
    form = UserPredictionForm()
    if request.method == 'POST':
        form = UserPredictionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request, 'mainapp/PredictionForm.html', context)


def userprediction(request):
    pass

def Profilesettings(request):
    pass