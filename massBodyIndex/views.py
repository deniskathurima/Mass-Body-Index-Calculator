from django.shortcuts import render


def bmi_calc(request):
    if request.method == "POST":
        name = request.POST.get('jina')
        weight = request.POST.get('uzito')
        height = request.POST.get('urefu')
        bmi = float(weight) / (float(height) * float(height))
        bmi_result = ""
        if bmi <= 18:
            bmi_result = "underweight"
        elif bmi <= 29:
            bmi_result = "Normal weight"
        elif bmi <= 34:
            bmi_result = "Over weight"
        else:
            bmi_result = "Obese"
        context = {"name": name, "bmi": bmi, "bmi_result": bmi_result}
        return render(request, 'index.html', context)

    return render(request, 'index.html')
