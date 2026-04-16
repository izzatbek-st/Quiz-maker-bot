# Quiz Bot - Telegram Quiz Manager

Telegram bot-i test fayllarini va matnlarni avtomatik ravishda qayta ishlash va quizlarga aylantirish uchun.

## Xususiyatlari

✅ Test fayllaridan savollarni avtomatik qidirib chiqish
✅ Tekst matndan savollarni avtomatik tahlil qilish
✅ Turli formatdagi fayllarni qo'llash (Q/A, Raqamli)
✅ Telegram quizlariga o'tkazish
✅ Quizlarni tahrirlash imkoniyati
✅ Savollar va javoblarni o'zgartirish
✅ To'g'ri javobni belgilash

## O'rnatish

### 1. Talablar
- Python 3.9+
- Telegram Bot Token

### 2. Paketlarni o'rnatish

```bash
pip install -r requirements.txt
```

### 3. .env faylini sozlash

`.env.example` faylini `.env` deb nomi o'zgartiring va bot tokenini qo'ying:

```
TELEGRAM_BOT_TOKEN=your_actual_bot_token_here
```

Telegram bot token olish uchun:
1. BotFather-ga xabar yuboring: `@BotFather`
2. `/newbot` buyrug'ini ishlating
3. Botga nom bering
4. Tokenni ko'chiring

## Botni ishga tushurish

```bash
python bot.py
```

## Foydalanish

Bot 2 xil usulda savollar kiritishni qo'llab-quvvatlaydi:

### 1️⃣ Test Faylini Jo'natish
- "📄 Test faylini jo'natish" tugmasini bosing
- .txt, .pdf, .docx yoki .doc faylni yuklang
- Bot faylni avtomatik tahlil qiladi
- Quiz nomini kiriting
- Quiz tayyor bo'ladi!

### 2️⃣ Test Matnini To'g'ridan-To'g'ri Jo'natish  
- "📝 Test matnini jo'natish" tugmasini bosing
- Savollarni Q/A yoki raqamli formatda kiriting
- Bot matnni tahlil qiladi
- Quiz nomini kiriting
- Quiz tayyor bo'ladi!

### 3️⃣ Quizni Tahrirlash
- "Mening quizlarim" dan quizni tanlang
- "✏️ Tahrirlash" tugmasini bosing
- Savollarni/javoblarni o'zgartiring
- To'g'ri javobni belgilang

## Test Fayli Formatlari

### Format 1: Q/A Formati

```
Q: Pythonning versiyasi nechta?
A: Python 2
A: Python 3*
A: Python 4
A: Python 5

Q: Python qaysi tilida yozilgan?
A: C
A: C++*
A: Java
A: C#
```

**Eslatma:** To'g'ri javob oxiriga `*` qo'ying

### Format 2: Raqamli Format

```
1) Rossiyaning poytaxti qaysi?
a) Moskva (correct)
b) Davlat Hermitaji
c) Sankt-Peterburg
d) Novosibirsk

2) Avstraliyaning poytaxti?
a) Sidney
b) Kanberra (correct)
c) Melbourne
d) Brisbane
```

**Eslatma:** To'g'ri javobiga `(correct)` yoki `(to'g'ri)` qo'ying

### Qabul Qilinadigan Fayllar

- **📝 .txt** - Oddiy matn fayli (UTF-8 kodlashida)
- **📕 .pdf** - PDF fayli
- **📗 .docx** - Word fayli (yangi versiyalar)
- **📘 .doc** - Word fayli (eski versiyalar)

## Fayllar Tuzilishi

```
Quiz bot/
├── bot.py                 # Asosiy bot fayli
├── test_parser.py         # Test tahlil moduli
├── quiz_storage.py        # Quiz saqlash moduli
├── requirements.txt       # Python paketlari
├── .env.example          # Shablon config file
├── .env                  # Haqiqiy config (shaklondan)
├── quizzes/              # Saqlangan quizlar (avtomatik tuziladi)
└── README.md             # Bu fayl
```

## Xatolikni hal qilish

### Bot ishlamayapti
- `.env` faylida token to'g'ri yozilganini tekshiring
- Internet ulanishni tekshiring
- `requirements.txt` dan barcha paketlar o'rnatilganini tekshiring

### Test tahlil qilina olmadi
- Fayl formatini tekshiring (Q/A yoki raqamli)
- UTF-8 kodlashda saqlang
- Savollar `Q:` yoki raqamli format bilan boshlangan bo'lishi kerak
- Har bir savolning kamida 2 ta javobiga ega bo'lishi kerak

### Quiz saqlanomayapti
- `quizzes/` papka yaratilganini tekshiring
- Fayl ruxsatlari to'g'ri bo'lishi kerak
- Disk bo'sh joyiga ega bo'lishi kerak

### Matnni parse qila olmadi
- Format to'g'riligini tekshiring
- Savollar va javoblar aniq belgilangan bo'lishi kerak
- Faqat UTF-8 kodlashni ishlating

## Qo'shimcha Ma'lumot

Bot o'z holatini JSON fayllar ko'rinishida `quizzes/` papkasida saqlaydi.
Siz quizlarni to'lanma ravishda tahrirlashingiz va qayta ishlatishingiz mumkin.

Fayllar avtomatik ravishda `quizzes/` papkasida `{user_id}_{timestamp}_{quiz_name}.json` formatida saqlanadi.

## Muallif

Quiz Bot - Telegram quiz boshqaruvi uchun shaxsiy loyiha

## Litsenziya

MIT License
