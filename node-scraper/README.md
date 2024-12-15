# مستندات پروژه

این پروژه یک سرویس Node.js است که با استفاده از Playwright، داده‌های صفحات وب را دریافت می‌کند و از Express برای مدیریت درخواست‌ها استفاده می‌کند. برای امنیت بیشتر، احراز هویت با استفاده از یک توکن استاتیک انجام می‌شود که در فایل `.env` ذخیره شده است.

---

## ویژگی‌ها

- دریافت محتوای HTML یک صفحه وب از طریق Playwright
- استفاده از Express برای مدیریت API
- احراز هویت با توکن استاتیک برای ایمن کردن سرویس

---

## پیش‌نیازها

- Node.js نسخه 14 یا بالاتر
- نصب مرورگرهای مورد نیاز Playwright

---

## نصب و راه‌اندازی

### 1. کلون کردن مخزن

ابتدا پروژه را کلون کنید:

```bash
git clone https://github.com/alihajiali/galaxy-script.git
cd galaxy-script/node-scraper
```

### 2. نصب وابستگی‌ها

با استفاده از دستور زیر بسته‌های مورد نیاز را نصب کنید:

```bash
npm install
```

### 3. ایجاد فایل `.env`

یک فایل `.env` در ریشه پروژه ایجاد کرده و محتوای زیر را در آن قرار دهید:

```env
AUTH_TOKEN=your_static_token_here
```

به جای `your_static_token_here`، یک توکن امن وارد کنید.

### 4. اجرای پروژه

برای اجرای پروژه، دستور زیر را اجرا کنید:

```bash
npm start
```

سرویس روی پورت 3000 اجرا خواهد شد.

---

## استفاده از API

### Endpoint: `/scrape`

#### نوع درخواست:

`GET`

#### هدر مورد نیاز:

- `Authorization`: مقدار توکن به فرمت زیر ارسال شود:
  ```
  Bearer <your_token>
  ```

#### پارامترهای کوئری:

- `url`: آدرس صفحه‌ای که می‌خواهید محتوای آن را دریافت کنید.

#### نمونه درخواست:

```bash
curl -X GET "http://localhost:3000/scrape?url=http://example.com" \
-H "authorization: your_static_token_here"
```

#### نمونه پاسخ موفق:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Example Domain</title>
</head>
<body>
  <h1>Example Domain</h1>
  <p>This domain is for use in illustrative examples in documents.</p>
</body>
</html>
```

#### نمونه پاسخ خطا:

- در صورت عدم ارسال توکن:

  ```json
  {
    "error": "Missing authentication token."
  }
  ```
- در صورت ارسال توکن نامعتبر:

  ```json
  {
    "error": "Invalid authentication token."
  }
  ```

---

## ساخت و اجرای پروژه با Docker

### 1. ساخت تصویر Docker

```bash
docker build -t node-scraper .
```

### 2. اجرای کانتینر Docker

```bash
docker run -p 3000:3000 --env-file .env node-scraper
```

---

## وابستگی‌ها

- [Node.js](https://nodejs.org/)
- [Express](https://expressjs.com/)
- [Playwright](https://playwright.dev/)
- [dotenv](https://github.com/motdotla/dotenv)

---

## نکات امنیتی

- از توکن‌های قوی و پیچیده برای مقدار `AUTH_TOKEN` استفاده کنید.
- در محیط تولید، اطمینان حاصل کنید که فایل `.env` در دسترس عموم قرار نگیرد.

---

## توسعه‌دهنده

- علی حاجی علی
