# Digikala Project

این پروژه یک نمونه ساده از سایت جنگو است که شامل یک اپلیکیشن به نام `blog_app` می‌باشد.

## امکانات پیاده‌سازی شده
- نمایش پیام خوش‌آمدگویی در مسیر `/blog/welcome/`
- نمایش جمع دو عدد ۲ و ۵ در مسیر `/blog/sum/`
- ضرب دو عدد در مسیر `/blog/<عدد اول>/<عدد دوم>/`
- بازی حدس عدد در مسیر `/blog/rand/<عدد>/`
- محاسبه BMI در مسیر `/blog/bmi/<قد>/<وزن>/`

## راه‌اندازی پروژه
1. اطمینان حاصل کنید که Python و Django روی سیستم شما نصب است.
2. پروژه را کلون کنید:
   ```
   git clone https://github.com/zahrarajaei9558-tech/web.git
   ```
3. وارد پوشه پروژه شوید:
   ```
   cd web
   ```
4. بسته‌های مورد نیاز را نصب کنید:
   ```
   pip install django
   ```
5. سرور را اجرا کنید:
   ```
   python manage.py runserver
   ```

## آدرس‌های مهم
1. پیام خوش‌آمدگویی: http://127.0.0.1:8000/blog/welcome/
2. جمع اعداد: http://127.0.0.1:8000/blog/sum/
3. ضرب اعداد (مثال: 5×3): http://127.0.0.1:8000/blog/5/3/
4. بازی حدس عدد: http://127.0.0.1:8000/blog/rand/3/
5. محاسبه BMI (قد: 170cm، وزن: 70kg): http://127.0.0.1:8000/blog/bmi/170/70/

## کد‌های جدید اضافه شده

### ۱. ویو بازی حدس عدد
```python
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
```

### ۲. ویو محاسبه BMI
```python
def bmi_view(request, height, weight):
    try:
        height_m = height / 100  # تبدیل سانتی‌متر به متر
        bmi = weight / (height_m * height_m)
        
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
```

### ۳. تنظیم مسیرها در urls.py
```python
urlpatterns = [
    # ... مسیرهای قبلی ...
    path('rand/<int:user_number>/', views.random_game_view, name='random_game'),
    path('bmi/<int:height>/<int:weight>/', views.bmi_view, name='bmi'),
]
```

## نکات مهم برای بازی حدس عدد
1. عدد تصادفی بین 1 تا 5 تولید می‌شود
2. اگر عدد شما با عدد تصادفی یکی باشد، برنده می‌شوید
3. می‌توانید بارها امتحان کنید
4. در هر بار امتحان، عدد تصادفی جدیدی تولید می‌شود

## نکات مهم برای محاسبه BMI
1. قد را به سانتی‌متر وارد کنید (مثلاً 170)
2. وزن را به کیلوگرم وارد کنید (مثلاً 70)
3. سیستم BMI شما را محاسبه و وضعیت شما را در یکی از 4 دسته زیر نمایش می‌دهد:
   - کمتر از 18.5: کمبود وزن
   - بین 18.5 تا 24.9: وزن نرمال
   - بین 25 تا 29.9: اضافه وزن
   - 30 و بالاتر: چاقی

## دسترسی به امکانات جدید
همه امکانات جدید از دو مسیر قابل دسترسی هستند:
1. با پیشوند blog:
   - `http://127.0.0.1:8000/blog/rand/3/`
   - `http://127.0.0.1:8000/blog/bmi/170/70/`
2. بدون پیشوند blog:
   - `http://127.0.0.1:8000/rand/3/`
   - `http://127.0.0.1:8000/bmi/170/70/`

## کمک و راهنمایی
اگر در استفاده از هر کدام از امکانات با مشکل مواجه شدید، لطفاً اطلاع دهید تا راهنمایی کنم.