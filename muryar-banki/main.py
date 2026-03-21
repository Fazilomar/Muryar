from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import os
import requests

from ai import detect_intent
from voice_call import make_call

app = FastAPI()

# -------------------------------
# HOME
# -------------------------------
@app.get("/")
def home():
    return {"message": "Muryar Banki Live 🚀"}


# -------------------------------
# USSD HANDLER
# -------------------------------
@app.post("/ussd")
async def ussd(request: Request):
    form = await request.form()

    session_id = form.get("sessionId")
    phone = form.get("phoneNumber")
    text = form.get("text", "")

    if text == "":
        return (
            "CON Welcome to Muryar Banki\n"
            "1. English\n2. Hausa\n3. Yoruba\n4. Igbo\n5. Pidgin"
        )

    choice = text.split("*")[0]

    if choice in ["1", "2", "3", "4", "5"]:
        # Trigger voice call
        make_call(phone)

        return "END You will receive a voice call shortly."

    return "END Invalid option"


# -------------------------------
# VOICE IVR (Africa's Talking)
# -------------------------------
@app.post("/voice")
async def voice(request: Request):
    data = await request.form()

    is_active = data.get("isActive")
    dtmf = data.get("dtmfDigits", "")

    if is_active == "1":

        if dtmf == "":
            return """
<Response>
    <Say>Welcome to Muryar Banki.</Say>
    <Say>Press 1 to check balance.</Say>
    <Say>Press 2 to speak your request.</Say>
    <GetDigits timeout="10" finishOnKey="#">
        <Say>Enter your choice</Say>
    </GetDigits>
</Response>
"""

        elif dtmf == "1":
            return """
<Response>
    <Say>Your account balance is 10,000 naira.</Say>
</Response>
"""

        elif dtmf == "2":
            return """
<Response>
    <Say>Please speak after the beep.</Say>
    <Record finishOnKey="#" maxLength="5"/>
</Response>
"""

    return "<Response><Say>Goodbye</Say></Response>"


# -------------------------------
# PROCESS VOICE (AI)
# -------------------------------
@app.post("/process-voice")
async def process_voice(request: Request):
    data = await request.form()

    recording_url = data.get("recordingUrl")

    audio_file = "audio.wav"

    r = requests.get(recording_url)
    with open(audio_file, "wb") as f:
        f.write(r.content)

    # Simulated transcription (replace with Whisper later)
    text = "check my balance"

    intent = detect_intent(text)

    return {
        "speech_text": text,
        "intent": intent
    }


# -------------------------------
# DASHBOARD UI
# -------------------------------
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return """
    <html>
    <body>
        <h2>Muryar Banki Dashboard</h2>

        <input id="phone" placeholder="Enter phone number"/>
        <button onclick="callUser()">Call User</button>

        <pre id="output"></pre>

        <script>
        async function callUser(){
            let phone = document.getElementById("phone").value;

            let res = await fetch("/call/" + phone, {method: "POST"});
            let data = await res.json();

            document.getElementById("output").innerText =
                JSON.stringify(data, null, 2);
        }
        </script>
    </body>
    </html>
    """


# -------------------------------
# CALL ENDPOINT
# -------------------------------
@app.post("/call/{phone}")
def call(phone: str):
    return make_call(phone)


# -------------------------------
# RUN (Replit compatible)
# -------------------------------
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
