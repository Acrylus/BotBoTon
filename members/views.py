from django.shortcuts import render
from django.http import JsonResponse
from members.models.C import to_correct_word, to_show_highlight

# Create your views here.
def predict_view(request):
    if request.method == 'POST':
        input_data = request.POST.get('input_data')
        if input_data:
            corrected = to_correct_word(input_data)
            highlighted = to_show_highlight(input_data, corrected)
            return JsonResponse({'prediction': corrected, 'highlighted': highlighted})
    return render(request, 'dashboard.html')   