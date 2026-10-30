# ProMaxRubika

**Professional Development for Rubika**  
یک چارچوب Async و ماژولار پایتون برای ساخت کلاینت حساب کاربری روبیکا با قابلیت اتصال Transport مستقل.

- نام پکیج: `promaxrubika`
- نسخه: `0.1.0`
- سازنده: **FAITR** — [@FAITR_PV](https://rubika.ir/FAITR_PV)
- کانال رسمی روبیکا: [@promaxrubika](https://rubika.ir/promaxrubika)
- مجوز: MIT
- حداقل نسخه پایتون: 3.11

> **وضعیت پروتکل:** این نسخه پروتکل شبکه روبیکا را پیاده‌سازی نمی‌کند. هیچ endpoint، روش احراز هویت، payload یا امضای رمزنگاری مستندنشده‌ای حدس زده نشده است. برای اتصال واقعی باید یک Adapter مبتنی بر مستندات معتبر و قابل بررسی برای `BaseTransport` نوشته شود. هسته رویدادها، فیلترها، ذخیره محلی Session، بسته‌بندی و تست‌ها پیاده‌سازی شده‌اند.

## نصب

```bash
python -m pip install .
```

## نمونه آفلاین رویدادها

```python
import asyncio
from promaxrubika import Client, MessageEvent, filters

async def main():
    app = Client(session={})

    @app.on_message(filters.text)
    async def on_message(event):
        print(event.text)

    await app.dispatch(MessageEvent(text="سلام", chat_id="demo"))

asyncio.run(main())
```

این نمونه برای آزمایش هسته رویدادهاست و به روبیکا متصل نمی‌شود.

## اتصال واقعی

تا زمان ارائه و بررسی پروتکل معتبر، اتصال شبکه در نسخه اصلی فعال نیست. متد `start()` بدون Adapter خطای روشن `ConnectionError` ایجاد می‌کند و علت آن `UnsupportedFeatureError` است.

## امکانات پیاده‌سازی‌شده در نسخه 0.1.0

- چرخه عمر Async کلاینت و context manager
- مدل رویداد پیام و ثبت Handler
- فیلترهای ترکیبی متن، ورودی، خروجی، دستور و Regex
- توزیع محلی رویداد برای تست و اتصال Adapter
- ذخیره JSON برای Session با محدودیت دسترسی فایل در سیستم‌عامل‌های پشتیبانی‌شده
- استثناهای اختصاصی و سیستم لاگ
- ساختار استاندارد پکیج، تست‌ها، مثال‌ها و مستندات فارسی/انگلیسی

## قابلیت‌های نیازمند Adapter و پروتکل معتبر

ورود و احراز هویت، OTP، اتصال زنده، ارسال و دریافت واقعی پیام، فهرست گفتگوها، مخاطبین، گروه‌ها، کانال‌ها، آپلود و دانلود رسانه و دریافت رویداد از سرور هنوز پیاده‌سازی نشده‌اند.

## امنیت

فایل Session را مانند رمز عبور محرمانه نگه دارید. آن را در GitHub قرار ندهید و محتوایش را در لاگ چاپ نکنید. محدودیت دسترسی فایل، رمزنگاری نیست.

## اجرای تست‌ها

```bash
python -m pip install -e ".[dev]"
python -m unittest discover -s tests -v
```

## هویت پروژه

ساخته‌شده توسط **FAITR** · کانال رسمی روبیکا: **@promaxrubika**  
Professional Development for Rubika.
