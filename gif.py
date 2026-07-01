import streamlit as st

st.set_page_config(page_title="Rose Surprise", layout="centered")

html = """
<!DOCTYPE html>
<html>
<head>
<style>

body{
margin:0;
display:flex;
justify-content:center;
align-items:center;
height:100vh;
overflow:hidden;
background: radial-gradient(circle at top, #1a0023, #000);
font-family:sans-serif;
}

/* Scene */
.scene{
position:relative;
width:420px;
height:600px;
}

/* Stars */
.star{
position:absolute;
width:3px;
height:3px;
background:white;
border-radius:50%;
animation:blink 2s infinite;
}

@keyframes blink{
50%{opacity:0.2;}
}

/* Title */
.text{
position:absolute;
top:20px;
width:100%;
text-align:center;
font-size:26px;
color:#ffb3c6;
text-shadow:0 0 15px #ff2d75;
}

/* Button */
button{
position:absolute;
bottom:40px;
left:50%;
transform:translateX(-50%);
padding:12px 25px;
font-size:16px;
border:none;
border-radius:25px;
cursor:pointer;
background:#ff2d75;
color:white;
box-shadow:0 0 15px #ff2d75;
}

/* Envelope */
.envelope{
position:absolute;
top:200px;
left:50%;
transform:translateX(-50%);
width:190px;
height:130px;
background:#ff4d6d;
border-radius:10px;
box-shadow:0 0 25px rgba(255,0,80,0.4);
animation:float 3s infinite;
display:flex;
justify-content:center;
align-items:center;
}

@keyframes float{
50%{transform:translateX(-50%) translateY(-10px);}
}

/* Letter */
.letter{
width:160px;
height:100px;
background:white;
border-radius:8px;
text-align:center;
padding-top:20px;
font-size:14px;
color:#ff2d75;
font-weight:bold;
}

/* Rose */
.flower{
position:absolute;
bottom:80px;
left:50%;
transform:translateX(-50%) scale(0);
}

/* Bloom animation */
.bloom{
animation:bloom 2.5s ease-out forwards;
}

@keyframes bloom{
0%{transform:translateX(-50%) scale(0) rotate(-20deg);}
60%{transform:translateX(-50%) scale(1.1) rotate(10deg);}
100%{transform:translateX(-50%) scale(1) rotate(0);}
}

/* Stem */
.stem{
width:10px;
height:240px;
background:linear-gradient(#00ff88,#0a6b2f);
margin:auto;
border-radius:20px;
}

/* Leaves */
.leaf{
position:absolute;
width:80px;
height:40px;
background:linear-gradient(#2cff6b,#0a7a30);
border-radius:80px 0;
}

.left{left:-60px;top:120px;transform:rotate(-35deg);}
.right{right:-60px;top:170px;transform:scaleX(-1) rotate(-35deg);}

/* Hidden */
.hidden{display:none;}

</style>
</head>

<body>

<div class="scene">

<!-- Stars -->
<div class="star" style="left:30px;top:60px;"></div>
<div class="star" style="left:120px;top:90px;"></div>
<div class="star" style="left:320px;top:70px;"></div>

<div class="text">🎁 A Surprise for You 🎁</div>

<!-- Envelope (START SCREEN) -->
<div id="envelope" class="envelope">
    <div class="letter">
        💌<br>
        Open me...<br>
        A surprise awaits 🌹
    </div>
</div>

<!-- Button -->
<button onclick="openSurprise()">Open Surprise</button>

<!-- Rose (HIDDEN INITIALLY) -->
<div id="rose" class="flower hidden">

<svg width="240" height="240" viewBox="0 0 240 240">

<defs>
<radialGradient id="petal">
<stop offset="0%" stop-color="#ffb3c6"/>
<stop offset="100%" stop-color="#c4003a"/>
</radialGradient>
</defs>

<g transform="translate(120,120)">

<ellipse rx="30" ry="70" fill="url(#petal)" transform="rotate(0) translate(0,-45)"/>
<ellipse rx="30" ry="70" fill="url(#petal)" transform="rotate(45) translate(0,-45)"/>
<ellipse rx="30" ry="70" fill="url(#petal)" transform="rotate(90) translate(0,-45)"/>
<ellipse rx="30" ry="70" fill="url(#petal)" transform="rotate(135) translate(0,-45)"/>
<ellipse rx="30" ry="70" fill="url(#petal)" transform="rotate(180) translate(0,-45)"/>
<ellipse rx="30" ry="70" fill="url(#petal)" transform="rotate(225) translate(0,-45)"/>
<ellipse rx="30" ry="70" fill="url(#petal)" transform="rotate(270) translate(0,-45)"/>
<ellipse rx="30" ry="70" fill="url(#petal)" transform="rotate(315) translate(0,-45)"/>

<circle r="12" fill="#ff2d75"/>

</g>
</svg>

<div class="stem"></div>
<div class="leaf left"></div>
<div class="leaf right"></div>

</div>

</div>

<script>

function openSurprise(){

    document.getElementById("envelope").style.display = "none";

    let rose = document.getElementById("rose");
    rose.classList.remove("hidden");
    rose.classList.add("bloom");

}

</script>

</body>
</html>
"""

st.components.v1.html(html, height=650)
