from django.shortcuts import render
from django.http import HttpResponse, Http404
import random

def bmi_view(request, height, weight):
    try:
        # تبدیل قد از سانتی‌متر به متر
        height_m = height / 100
        # محاسبه BMI
        bmi = weight / (height_m * height_m)
        
        # تعیین وضعیت بر اساس BMI
        if bmi < 18.5:
            status = "کمبود وزن"
        elif bmi < 25:
            status = "وزن نرمال"
        elif bmi < 30:
            status = "اضافه وزن"
        else:
            status = "چاقی"
            
        message = f"قد شما: {height} سانتی‌متر\nوزن شما: {weight} کیلوگرم\nشاخص BMI: {bmi:.1f}\nوضعیت: {status}"
        return HttpResponse(message)
    except Exception:
        raise Http404("لطفاً مقادیر معتبر وارد کنید.")

def random_game_view(request, user_number):
    try:
        random_number = random.randint(1, 5)  
        is_winner = user_number == random_number
        
        if is_winner:
            message = f"تبریک! برنده شدید! 🎉\nعدد شما: {user_number}\nعدد تصادفی: {random_number}"
        else:
            message = f"متاسفانه باختید! 😔\nعدد شما: {user_number}\nعدد تصادفی: {random_number}"
            
        return HttpResponse(message)
    except Exception:
        raise Http404("لطفاً یک عدد معتبر وارد کنید.")

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

def multiply_view(request, a, b):
    try:
        num1 = int(a)
        num2 = int(b)
        result = num1 * num2
        html = f'''
        <html>
        <head>
            <title>عملیات ضرب</title>
            <style>
                body {{ background: #f7fafc; font-family: Tahoma, Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; }}
                .mul-box {{ background: #fff; border-radius: 16px; box-shadow: 0 4px 24px #0001; padding: 40px 60px; text-align: center; }}
                .mul-title {{ font-size: 2rem; color: #d32f2f; margin-bottom: 12px; }}
                .mul-result {{ font-size: 1.3rem; color: #333; }}
            </style>
        </head>
        <body>
            <div class="mul-box">
                <div class="mul-title">ضرب {num1} × {num2}</div>
                <div class="mul-result">نتیجه: {result}</div>
            </div>
        </body>
        </html>
        '''
        return HttpResponse(html)
    except Exception:
        raise Http404("اعداد معتبر وارد کنید.")
