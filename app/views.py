import os
from django.shortcuts import render, redirect
from .forms import ProposalForm


def home(request):
    return render(request, 'app/home2.html', {})


def proposal(request):
    if request.method == 'POST':
        form = ProposalForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['attachment']
            # Retrieve the original filename
            instance = form.save()  
            original_filename = uploaded_file.name
            file_name = filename = instance.attachment.name
            file_url = filename = instance.attachment.url
            print(f"ORIGINAL FILENAME: {original_filename}")
            print(f"PATH FILENAME: {file_name}")
            print(f"URL FILENAME: {file_url}")

            return redirect('home') 
    else:
        form = ProposalForm()

    return render(request, 'app/proposal_form.html', {'form': form})