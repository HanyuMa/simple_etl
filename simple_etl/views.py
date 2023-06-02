from django.http import HttpResponse
from .etl_script import trigger_etl


def trigger_etl_view(request):
    # Trigger the ETL process
    trigger_etl()
    return HttpResponse("ETL process started!\n")
