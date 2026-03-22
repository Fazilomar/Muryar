# Muryar Banki 🔈
### Voice-Powered Banking for Everyone

---

## 🚀 Try the Live Prototype

Click the link below to open and use the Muryar Banki prototype directly in your browser — no installation needed:

**👉 [https://647f957d-2b4b-41ad-b393-ac4aad6f828b-00-2ykebupszm9c5.riker.replit.dev](https://647f957d-2b4b-41ad-b393-ac4aad6f828b-00-2ykebupszm9c5.riker.replit.dev)**

> **Best experience:** Open on **Google Chrome** or **Microsoft Edge** on a phone or computer for full voice input and voice output support.

---

## The Problem

Nigeria has over **200 million people**, yet a large portion of the population — including rural traders, farmers, artisans, market women, and daily wage earners — remain **financially excluded**. The reasons are deeply rooted:

### 1. Illiteracy and Low Digital Literacy
Most traditional banking apps and USSD menus require users to read and type. For the millions of Nigerians who cannot read — or who struggle with small-screen keyboards — this is a hard barrier. A carpenter in Kano, a fish seller in Onitsha, or a palm oil trader in Ondo cannot easily navigate a banking app written in English with small buttons.

### 2. Language Barrier
Nigeria has **over 500 languages**, with four dominant ones: Hausa, Yoruba, Igbo, and Nigerian Pidgin. Most banking platforms operate only in English, leaving hundreds of millions of people unable to fully understand instructions or trust what they are doing with their money.

### 3. Fear of Making Mistakes
Illiterate users are afraid to use digital banking because:
- They cannot read confirmation messages
- They fear sending money to the wrong person
- They do not understand error messages
- There is no one to guide them in real time

### 4. Lack of Voice Interaction
Existing USSD banking works through text-only menus. There is no voice, no feedback, and no confirmation spoken back to the user. For someone who cannot read, this is effectively unusable.

### 5. Artisans and Traders Are Left Behind
Small business owners — tailors, welders, mechanics, food vendors — need to receive payments, buy airtime for business calls, and transfer money daily. Without accessible banking tools, they rely on middlemen, cash, and informal systems that are risky and costly.

---

## The Solution: Muryar Banki

**Muryar Banki** (which means *"Voice of the Bank"* in Hausa) is a voice-powered banking simulator that allows users to interact with banking services using their **natural spoken language** — no reading or typing required.

### How It Works

1. **USSD Entry** — The user dials a familiar USSD code (e.g. `*770#`) to start the session, just like they already know how to do.

2. **Language Selection** — The user picks their preferred language from five options:
   - 🇬🇧 English
   - 🇳🇬 Hausa
   - 🇳🇬 Yoruba
   - 🇳🇬 Igbo
   - 🇳🇬 Nigerian Pidgin

3. **Voice Menu** — The system speaks the available options out loud in the user's chosen language and then **listens automatically**. The user simply says what they want:
   - *"I want to check my balance"*
   - *"Buy airtime"*
   - *"I wan send money"* (Pidgin)
   - *"Ina son aika kuɗi"* (Hausa)

4. **Smart Voice Understanding** — The system detects the user's **intent from natural speech**, not rigid commands. Whether someone says "credit", "recharge", or "top up", the system understands they want airtime.

5. **Guided Step-by-Step Flow** — Every step is:
   - **Spoken aloud** (text-to-speech in the user's language)
   - **Shown visually** with large icons (💰 Balance, 📱 Airtime, 💸 Transfer)
   - **Confirmed before action** — for money transfers, the account number is read back digit by digit before the user confirms

6. **PIN Security** — The user enters their secret PIN manually on a keypad (never spoken or typed in text), keeping their account secure.

7. **Voice Confirmation** — After every transaction, the system speaks a confirmation message in the user's language:
   - *"Airtime don enter your line!"* (Pidgin)
   - *"An canja kuɗi cikin nasara!"* (Hausa)
   - *"Your account balance is ₦47,800 Naira"* (English)

8. **Random Balance Generation** — For the prototype, account balances are randomly generated in Naira to simulate a real banking response, and read out loud to the user.

### Key Features for Illiterate and Low-Literacy Users

| Feature | Purpose |
|---|---|
| 🎙️ Voice input | User speaks instead of typing |
| 🔊 Voice output | System reads everything aloud |
| 🖼️ Big picture icons | Visual recognition without reading |
| 🌍 5 Nigerian languages | Talks to users in their own tongue |
| 🔁 Auto-listen | Mic opens automatically after each prompt |
| 🗣️ Speech echo | Shows what the system heard you say |
| 🔢 Account number readback | Digits spoken one by one before confirmation |
| ✅❌ Confirm before sending | Prevents costly mistakes |
| 🔒 PIN on keypad | Secure manual entry, no speaking required |
| ↺ Start Over button | Easily reset without needing support |

---

## The AI Used

Muryar Banki uses two layers of AI that are **free and built directly into modern web browsers** — no API key or internet connection to a third-party service is required:

### 1. Web Speech API — Speech Synthesis (Text-to-Speech)
**Technology:** `window.speechSynthesis`

The browser's built-in text-to-speech engine converts all banking instructions, confirmations, and balance announcements into spoken audio. It supports multiple language codes including:
- `en-NG` — Nigerian English / Pidgin
- `ha` — Hausa
- `yo` — Yoruba
- `ig` — Igbo

This allows the system to speak to users in their native tongue without any external AI service.

### 2. Web Speech API — Speech Recognition (Voice-to-Text)
**Technology:** `window.SpeechRecognition` / `window.webkitSpeechRecognition`

The browser's built-in voice recognition engine converts the user's spoken words into text. Muryar Banki then uses a **custom keyword intent detection engine** to understand what the user wants:

- It listens across **5 languages simultaneously**
- It matches natural phrases like *"I want to buy airtime"*, *"wetin my balance"*, *"Ina son duba asusun"*
- It handles spelling variations and informal speech
- No internet call is made — recognition happens on-device in Chrome/Edge

### 3. Custom Intent Detection Engine
**Technology:** JavaScript keyword matching across multilingual dictionaries

A lightweight AI layer built into the app maps spoken words to banking actions:

```
User says → System understands → System acts
"buy airtime" → AIRTIME intent → Opens airtime flow
"I wan send" → TRANSFER intent → Opens transfer flow
"duba kuɗi" → BALANCE intent (Hausa) → Opens balance check
"na for me" → SELF intent (Pidgin) → Airtime for self
```

This engine supports multiple alternative phrases per intent per language, making it resilient to how different people naturally speak.

---

## Security Protocols

Protecting users' financial data and privacy is a core part of Muryar Banki's design — especially because the target users are often the most vulnerable to fraud and social engineering. The following security protocols are implemented across the system:

---

### 1. PIN Never Transmitted as Voice or Text

The user's secret PIN is entered **only through the physical on-screen keypad** and is never:
- Spoken aloud by the user (the mic is inactive during PIN entry)
- Displayed as readable characters on screen (shown as masked dots ●●●●)
- Transmitted to any third-party server
- Stored anywhere on the device or in the browser

This protects users from **shoulder surfing** (someone watching the screen) and **voice eavesdropping** (someone nearby hearing the PIN spoken).

---

### 2. On-Device Voice Processing — No Data Leaves the Phone

All voice recognition in Muryar Banki uses the **browser's built-in Web Speech API**, which processes audio directly on the user's device (on-device inference in Chrome/Edge). This means:

- The user's voice is **not sent to any external server** during intent detection
- No audio recordings are stored or logged
- No third-party AI company receives the user's spoken commands
- The session ends cleanly with no audio trail left behind

---

### 3. No Personal Data Collected or Stored

Muryar Banki does not collect, store, or transmit any personally identifiable information (PII). This includes:

- No name, phone number, or BVN stored
- No account numbers saved to any database after the session
- No transaction history sent to an external server
- Session data (like the entered account number) lives only in the browser's memory and is wiped the moment the user presses **Start Over** or closes the app

---

### 4. Account Number Confirmation Before Transfer

Before any money transfer is executed, the system reads the account number back to the user **digit by digit** and asks for explicit confirmation:

```
"The account number you entered is: 0, 8, 1, 2, 3, 4, 5, 6, 7, 8. Is that correct?"
```

The user must tap ✅ **Correct** to proceed, or ❌ **Re-enter** to correct a mistake. This protects against:
- **Accidental wrong transfers** caused by mis-keyed digits
- **Social engineering attacks** where a fraudster tricks a user into sending to the wrong account
- **Fat-finger errors** on small keypads

---

### 5. Session Isolation — Each Session is Fresh

Every time the user starts a session (by entering a USSD code), the app creates a completely fresh state:

- No data from a previous session is carried over
- No cookies or persistent tokens are used
- If the phone is shared (as is common in rural households), the previous user's data is not visible to the next user

---

### 6. HTTPS Encryption in Transit

When deployed, Muryar Banki is served over **HTTPS (TLS encryption)**, meaning:

- All communication between the user's browser and the server is encrypted
- Hackers on the same Wi-Fi network or mobile data network cannot intercept or read the traffic (Man-in-the-Middle protection)
- Data cannot be tampered with in transit

---

### 7. Backend API Security (FastAPI)

The backend server, built with **FastAPI**, implements the following:

- **No sensitive user data is processed server-side** — the backend only serves the frontend simulator; it does not handle PINs, account numbers, or balances
- FastAPI's automatic request validation rejects malformed or unexpected inputs, reducing the attack surface
- In a production deployment, the API would be protected with **rate limiting** to prevent brute-force attacks

---

### 8. Protection Against Social Engineering

Because the primary users are low-literacy individuals who may be easily tricked, Muryar Banki includes built-in anti-fraud design choices:

| Risk | Protection Built In |
|---|---|
| Fraudster watches screen for PIN | PIN shown only as ●●●● dots |
| Fraudster listens for PIN spoken | Mic is automatically OFF during PIN step |
| User sends to wrong account | Account number read aloud + confirmation screen |
| User panics mid-session | "Start Over" button cancels everything cleanly |
| Shared phone exposes data | No data persists between sessions |
| Phishing — fake app looks real | On-device processing; no external API calls |

---

### 9. Future Security Enhancements (Production Roadmap)

For a full production deployment, the following additional security layers would be added:

- **Biometric authentication** — fingerprint or face ID to replace PIN on supported devices
- **OTP (One-Time Password)** — SMS code sent to the registered phone number for high-value transactions
- **End-to-end encryption (E2EE)** — for all voice and data payloads between device and bank server
- **Fraud detection AI** — machine learning model that flags unusual transaction patterns (e.g. large transfer to a new account at 2am)
- **SIM card binding** — session linked to the registered SIM so the account cannot be accessed from an unfamiliar device
- **Automatic session timeout** — session expires after 60 seconds of inactivity to protect unattended phones

---

## Technology Stack

| Layer | Technology |
|---|---|
| Backend | Python · FastAPI · Uvicorn |
| Frontend | HTML5 · CSS3 · Vanilla JavaScript |
| Voice Output | Web Speech API (SpeechSynthesis) |
| Voice Input | Web Speech API (SpeechRecognition) |
| Intent AI | Custom multilingual keyword engine |
| Deployment | Replit · HTTPS (TLS) |

---

## Vision

Muryar Banki is a prototype that demonstrates how **voice AI and multilingual technology** can bridge the gap between formal banking and the millions of Nigerians who are currently excluded from it. The goal is to make every artisan, trader, farmer, and daily earner feel confident and safe using digital banking — in their own voice, in their own language.

> *"If a bank can talk to you the way your neighbor does, you will trust it."*
