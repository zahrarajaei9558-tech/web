from django.shortcuts import render
from django.http import HttpResponse

def welcome_view(request):
    html = '''
    <html>
    <head>
        <title>خوش آمدید</title>
        <style>
            body { background: #f7fafc; font-family: Tahoma, Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; }
            .welcome-box { background: #fff; border-radius: 16px; box-shadow: 0 4px 24px #0001; padding: 40px 60px; text-align: center; }
            .welcome-title { font-size: 2.2rem; color: #1976d2; margin-bottom: 12px; }
            .welcome-msg { font-size: 1.3rem; color: #333; }
        </style>
    </head>
    <body>
        <div class="welcome-box">
            <div class="welcome-title">به اقبال خوش آمدید</div>
            <div class="welcome-msg">از بازدید شما خوشحالیم!</div>
        </div>
    </body>
    </html>
    '''
    return HttpResponse(html)

def sum_view(request):
    result = 2 + 5
    html = f'''
    <html>
    <head>
        <title>جمع اعداد</title>
        <style>
            body {{ background: #f7fafc; font-family: Tahoma, Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; }}
            .sum-box {{ background: #fff; border-radius: 16px; box-shadow: 0 4px 24px #0001; padding: 40px 60px; text-align: center; }}
            .sum-title {{ font-size: 2rem; color: #388e3c; margin-bottom: 12px; }}
            .sum-result {{ font-size: 1.3rem; color: #333; }}
        </style>
    </head>
    <body>
        <div class="sum-box">
            <div class="sum-title">جمع ۲ و ۵</div>
            <div class="sum-result">نتیجه: {result}</div>
        </div>
    </body>
    </html>
    '''
    return HttpResponse(html)
