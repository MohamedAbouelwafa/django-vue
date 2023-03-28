# -*- coding: utf-8 -*-

from django.shortcuts import render
import datetime
# from dateutil.parser import parse

# Create your views here.

def home(request):

  # temp_date = [
  #   {
  #     'name': 'Mohamed',
  #     'phone': '123',
  #   },
  #   {
  #     'name': 'Ahmed',
  #     'phone': '456',
  #   }
  # ]
  # temp_date = sorted(temp_date, key=lambda p: p['phone'])

  temp_data = {u'2023-03-25 16:47:14.438957': u'Status update: shipped.', u'2023-03-25 17:15:17.223423': u'Status update: Devices auto provisioning results for Upload to MFR Cloud Service.', u'2023-03-25 16:47:22.948527': u'Status update: Devices auto provisioning results for Add Auth Devices.', u'2023-03-25 17:15:07.192591': u'Status update: shipped.', u'2023-03-25 17:15:17.109626': u'Status update: Devices auto provisioning results for Add Auth Devices.', u'2023-03-25 16:43:16.120551': u'Status update: submitted.'}
  # temp_data = {k.split('.')[0]: v for k, v in temp_data.items()}
  # temp_data = {k.replace(' ', '-').replace(':', '-'): v for k, v in temp_data.items()}
  # temp_data = {k.replace('-', ''): v for k, v in temp_data.items()}
  # # temp_data = {k: v for k, v in sorted(temp_data.items(), key=lambda item: datetime.datetime.strptime(item[0], '%Y-%m-%d %H:%M:%S.%f'))}
  # # temp_data = {k: temp_data[k] for k in sorted(temp_data.keys(), key=lambda item: datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S'))}
  # temp_data = {k: temp_data[k] for k in sorted(temp_data.keys())}

  temp_data = [{'date': k, 'note': v }for k, v in temp_data.items()]

  context = {
    'field': 'name',
    'temp_data': temp_data,
  }
  return render(request, 'djangoapp/shell.html', context)


def err404(request):
  return render(request, 'djangoapp/404.html')

def comp1(request):
  return render(request, 'djangoapp/comp1.html')

def comp2(request):
  return render(request, 'djangoapp/comp2.html')