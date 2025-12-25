import streamlit as st
import base64

st.set_page_config(page_title="🎄 Christmas Surprise", layout="centered")

# ---------- Load Music ----------
def load_music(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

music_base64 = load_music("jinglebells.mp3")

# ---------- CSS + Snow ----------
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #00111a, #003366);
    overflow: hidden;
}

.snowflake {
    color: white;
    font-size: 1em;
    position: fixed;
    top: -10px;
    animation: fall linear infinite;
}

@keyframes fall {
    to {
        transform: translateY(100vh);
    }
}

.card {
    background: rgba(255,255,255,0.15);
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    color: white;
    font-size: 20px;
    margin-top: 20px;
}

.gift {
    font-size: 80px;
    cursor: pointer;
}
</style>

<script>
for (let i = 0; i < 40; i++) {
    let snow = document.createElement("div");
    snow.className = "snowflake";
    snow.innerHTML = "❄";
    snow.style.left = Math.random() * 100 + "vw";
    snow.style.animationDuration = (Math.random() * 5 + 5) + "s";
    document.body.appendChild(snow);
}
</script>
""", unsafe_allow_html=True)

# ---------- App ----------
st.title("🎄 Christmas Surprise 🎁")
name = st.text_input("Enter your name 🎅")

if name:
    st.markdown("### 🎁 Tap the Gift Box")
    
    if st.button("🎁"):
        # Music autoplay
        st.markdown(f"""
        <audio autoplay loop>
        <source src="data:audio/mp3;base64,{music_base64}" type="audio/mp3">
        </audio>
        """, unsafe_allow_html=True)

        # Santa + Message
        st.markdown(f"""
        <div class="card">
        🎅🎄 <b>MERRY CHRISTMAS {name.upper()}!</b> 🎄🎅<br><br>

        May this Christmas bring you peace and warmth.<br>
        May your dreams shine brighter than Christmas lights.<br>
        May laughter fill your home and love fill your heart.<br>
        May the coming year bring strength, success, and happiness.<br>
        May every little moment remind you how special you are.<br><br>

        With love and warm wishes,<br>
        <b>— Samprikta Sengupta ❤️</b>
        </div>
        """, unsafe_allow_html=True)
