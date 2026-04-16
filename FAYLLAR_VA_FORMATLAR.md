# Bot Qabul Qilinadigan Fayllar Va Formatlar

## 📁 QABUL QILINADIGAN FAYLLAR

Bot quyidagi fayl turlarini qo'llaydi:

| Fayl Turi | Kengaytmasi | Holati |
|-----------|-----------|--------|
| **Matn fayli** | `.txt` | ✅ To'liq qo'llab-quvvatlanadi |
| **PDF** | `.pdf` | ✅ To'liq qo'llab-quvvatlanadi |
| **Word (yangi)** | `.docx` | ✅ To'liq qo'llab-quvvatlanadi |
| **Word (eski)** | `.doc` | ✅ To'liq qo'llab-quvvatlanadi |

### Muhim Eslatmalar:

1. **PDF Fayllar**: 
   - Text sifatida saqlangan PDF'lar eng yaxshi tahlil bo'ladi
   - Scan qilingan PDF'lardan (rasmlar) savol ajratib bo'lmaydi

2. **Word Fayllar**:
   - Paragraflardagi matn
   - Jadvallar ichidagi matn
   - Ikkalasi ham avtomatik o'qiladi

3. **Matn Fayllar**:
   - UTF-8 kodlanishida bo'lishi kerak
   - Har qanday matn editori bilan yaratilishi mumkin

---

## 📋 QABUL QILINADIGAN FORMAT TURLAR

Bot **4 xil test formatni** avtomatik ravishda aniqlab tahlil qiladi:

### 1️⃣ Q/A FORMAT

**Tavsif**: Savol va javoblar Q: va A: prefiksli bo'ladi

```
Q: Olma nima?
A: Sabzavot
A: Meva*
A: Piyoz

Q: Tog'o nima?
A: Tepa
A: Yomg'in*
A: Suv
```

**Xususiyatlari:**
- To'g'ri javob oxiriga `*` qo'yiladi
- Bitta savol va uni javoblarini alohida qatorlarda
- Savol `Q:` bilan boshlanadi
- Javoblar `A:` bilan boshlanadi

---

### 2️⃣ RAQAMLI FORMAT (Qavs bilan)

**Tavsif**: Savol va javoblar raqamli bo'ladi, harf javoblar

```
1) Olma nima?
a) Sabzavot
b) Meva (correct)
c) Piyoz

2) Tog'o nima?
a) Tepa
b) Yomg'in (to'g'ri)
c) Suv
```

**Xususiyatlari:**
- Savol: `1)`, `2)`, `3)` kabi raqam + qavs
- Javob: `a)`, `b)`, `c)` kabi harf + qavs
- To'g'ri javob: `(correct)` yoki `(to'g'ri)` belgisi

---

### 3️⃣ SODDA RAQAMLI FORMAT (Eng sodda)

**Tavsif**: Savol va javoblar raqamli, lekin qavssiz - bo'sh bilan ajratiladi

```
1 Olma nima?
a Meva
b Piyoz
c Sabzavot

2 Nok nima?
a Meva
b Sabzavot
c Piyoz
```

**Xususiyatlari:**
- Savol: `1 `, `2 `, `3 ` kabi raqam + bo'sh
- Javob: `a `, `b `, `c ` kabi harf + bo'sh
- Qavs va belgilar kerak emas
- **ENG SODDA VA UNIVERSAL FORMAT**

---

### 4️⃣ UNNUMBERED FORMAT

**Tavsif**: Savollar belgilanmagan, javoblar alohida qatorlarda

```
Olma nima?
Meva
Piyoz
Sabzavot

Tog'o nima?
Tepa
Yomg'in
Suv
```

**Xususiyatlari:**
- Savol `?` belgisi bilan tugaydi
- Javoblar - keyingi qatorlar
- Raqam yoki prefikslar kerak emas
- To'g'ri javob belgilanmasa, birinchisi to'g'ri hisoblanadi

---

## ✅ TO'G'RI JAVOB BELGILASH USULLARI

Bot to'g'ri javobni aniqlovchi **3 usulni** qabul qiladi:

### 1. **Asterisk (*) belgisi** (barcha formatda)

```
A: Meva*
yoki
a) Meva*
yoki
a Meva*
```

### 2. **(correct) belgisi** (raqamli formatda)

```
b) Meva (correct)
yoki
b Meva (correct)
```

### 3. **(to'g'ri) belgisi** (Uzbek tilida)

```
b) Meva (to'g'ri)
yoki
b Meva (to'g'ri)
```

---

## ⚠️ MUHIM TALABLAR

### Savollar uchun:

1. ✅ **Har savol eng kamida 2 ta javobga ega bo'lishi kerak**
   ```
   XATO ❌:
   1) Savol?
   a) Bitta javob
   
   TO'G'RI ✅:
   1) Savol?
   a) Javob 1
   b) Javob 2
   ```

2. ✅ **To'g'ri javob belgilanmasa, birinchisi to'g'ri hisoblanadi**
   ```
   1) Savol?
   a) To'g'ri javob (o'zgartirilmagan bo'lsa, bu to'g'ri)
   b) Javob 2
   c) Javob 3
   ```

3. ✅ **Savol `?` belgisi bilan tugashi tavsiya etiladi**
   ```
   TO'G'RI ✅:
   1) Olma nima?
   
   XATO ❌:
   1) Olma nima
   ```

---

## 📊 FORMAT ANIQLANISHI

Bot avtomatik ravishda quyidagi tartibda format aniqlaydi:

1. **Q/A Formatni** qidiradi (Q: va A: belgisi)
2. **Sodda Raqamli Formatni** qidiradi (1 , 2 , 3 ...)
3. **Raqamli Formatni** qidiradi (1), 2), 3)...)
4. **Unnumbered Formatni** qidiradi (savollar `?` bilan)

---

## 🎯 NAJOT: FAYLNI TAYYORLASH

### Yaxshi Misol: `.txt` faylda

```
1 Rossiyaning poytaxti qaysi?
a Moskva*
b Sankt-Peterburg
c Novosibir

2 Qaysi davlat Osiyadagi eng katta?
a Rossiya*
b Xitoy
c Hind

3 Birinchi bo'lib kosmosga uyg'in qilgan davlat?
a Amerika
b Rossiya*
c Fransiya
```

**Ushbu faylni PDF yoki Word formatiga o'girish mumkin - bot o'qiy oladi!**

---

## 🚀 QADAMLAR

1. **Faylni tayyorlang** (txt, pdf, docx, doc)
2. **Formatni tanlang** (Yuqoridagi 4 formatdan biri)
3. **Botga jo'nating** ("📄 Test faylini jo'natish" tugmasi)
4. **Bot avtomatik tahlil qiladi** va savollarni topadi
5. **Quiz nomini kiriting**
6. **Quiz tayyor!** ✅

---

## ❓ TEZ-TEZI SAVOLLAR

**Q: Agar fayl tahlil bo'lmasa?**
- Faylning encoding'i UTF-8 ekanligini tekshiring
- Format'ni qayta tekshiring
- Har savol 2+ javobga ega ekanligini tekshiring
- Bot qo'llanmadagi misollarni ko'ring

**Q: Scan qilingan PDF o'qiladi mi?**
- Yo'q, faqat text sifatida saqlangan PDF'lar o'qiladi

**Q: Jadvallardagi savollar o'qiladi mi?**
- Ha, Word jadvallaridagi matn avtomatik o'qiladi

**Q: Qancha savol biz qo'sha olamiz?**
- Cheksiz! Faylning hajmi muammoga aylangan paytgacha

---

## 📧 YORDAM

Agar fayl tahlil bo'lmasa:
1. Bot qo'llanmasidagi misollarni tekshiring
2. Faylni qayta tayyorlang
3. `/help` buyrug'i bilan bot qo'llanmasini ko'ring
