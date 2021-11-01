from django.shortcuts import render

from .models import Report

def report(request):
    return render(request,'report.html')
def savereport(request):
    if request.method=='POST':
        location = request.POST.get('location')
        incident_department=request.POST.get('incident_dept')
        dateandtime=request.POST.get('dateandtime')
        incident_location = request.POST.get('incident_location')
        severity = request.POST.get('severity')
        suspected_cause = request.POST.get('suspected_cause')
        immediate_action_taken = request.POST.get('immediate_action_taken')
        subincident_type = request.POST.get('type')
        save_report = Report(location=location,Incident_Dept=incident_department,dateandtime=dateandtime,incident_location=incident_location,initial_severity=severity,suspected_cause=suspected_cause,immediate_action_taken=immediate_action_taken,sub_incident_type=subincident_type)
        save_report.save()
    return  render(request,'report.html')

def saved(request):

    return render(request,'saved.html')

def sent(request):
    return render(request,'sent.html')

