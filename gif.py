import streamlit as st

st.set_page_config(page_title="Blooming Red Rose", layout="centered")

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
opacity:0.8;
}

@keyframes blink{
50%{opacity:0.1; transform:scale(0.7);}
}

/* Title */
.text{
position:absolute;
top:20px;
width:100%;
text-align:center;
font-size:28px;
color:#ffb3c6;
text-shadow:0 0 15px #ff2d75;
opacity:0;
animation:fadeIn 2s 2s forwards;
}

@keyframes fadeIn{
to{opacity:1;}
}

/* Flower container */
.flower{
position:absolute;
bottom:60px;
left:50%;
transform:translateX(-50%);
animation:sway 4s ease-in-out infinite;
transform-origin:bottom center;
}

@keyframes sway{
0%,100%{transform:translateX(-50%) rotate(-3deg);}
50%{transform:translateX(-50%) rotate(3deg);}
}

/* Stem */
.stem{
width:10px;
height:260px;
background:linear-gradient(#00ff88, #0a6b2f);
margin:auto;
border-radius:20px;
animation:grow 2s ease-out forwards;
transform-origin:bottom;
}

@keyframes grow{
from{height:0;}
to{height:260px;}
}

/* Leaves */
.leaf{
position:absolute;
width:80px;
height:40px;
background:linear-gradient(#2cff6b, #0a7a30);
border-radius:80px 0;
}

.left{
left:-65px;
top:120px;
transform:rotate(-35deg);
}

.right{
right:-65px;
top:170px;
transform:scaleX(-1) rotate(-35deg);
}

/* Rose SVG */
svg{
position:absolute;
left:-120px;
top:-140px;
transform:scale(0);
animation:bloom 2.5s ease-out forwards;
}

@keyframes bloom{
0%{transform:scale(0) rotate(-30deg);}
60%{transform:scale(1.1) rotate(10deg);}
100%{transform:scale(1) rotate(0deg);}
}

/* Glow center */
.glow{
filter: drop-shadow(0 0 10px #ff004c);
}

</style>
</head>

<body>

<div class="scene">

<!-- Stars -->
<div class="star" style="left:30px;top:60px;"></div>
<div class="star" style="left:120px;top:90px;"></div>
<div class="star" style="left:320px;top:70px;"></div>
<div class="star" style="left:380px;top:160px;"></div>
<div class="star" style="left:220px;top:30px;"></div>
<div class="star" style="left:80px;top:200px;"></div>

<div class="text">🌹 Blooming Red Rose 🌹 <br></div>
<div class="text">For You</div>


<div class="flower">

<!-- ROSE SVG -->
<svg width="240" height="240" viewBox="0 0 240 240" class="glow">

<defs>

<radialGradient id="petal1">
<stop offset="0%" stop-color="#ffb3c6"/>
<stop offset="100%" stop-color="#c4003a"/>
</radialGradient>

<radialGradient id="petal2">
<stop offset="0%" stop-color="#ffd1dc"/>
<stop offset="100%" stop-color="#ff004c"/>
</radialGradient>

</defs>

<g transform="translate(120,120)">

<!-- Outer petals -->
<ellipse rx="30" ry="70" fill="url(#petal1)" transform="rotate(0) translate(0,-45)"/>
<ellipse rx="30" ry="70" fill="url(#petal1)" transform="rotate(45) translate(0,-45)"/>
<ellipse rx="30" ry="70" fill="url(#petal1)" transform="rotate(90) translate(0,-45)"/>
<ellipse rx="30" ry="70" fill="url(#petal1)" transform="rotate(135) translate(0,-45)"/>
<ellipse rx="30" ry="70" fill="url(#petal1)" transform="rotate(180) translate(0,-45)"/>
<ellipse rx="30" ry="70" fill="url(#petal1)" transform="rotate(225) translate(0,-45)"/>
<ellipse rx="30" ry="70" fill="url(#petal1)" transform="rotate(270) translate(0,-45)"/>
<ellipse rx="30" ry="70" fill="url(#petal1)" transform="rotate(315) translate(0,-45)"/>

<!-- Inner petals -->
<ellipse rx="22" ry="55" fill="url(#petal2)" transform="rotate(22) translate(0,-30)"/>
<ellipse rx="22" ry="55" fill="url(#petal2)" transform="rotate(67) translate(0,-30)"/>
<ellipse rx="22" ry="55" fill="url(#petal2)" transform="rotate(112) translate(0,-30)"/>
<ellipse rx="22" ry="55" fill="url(#petal2)" transform="rotate(157) translate(0,-30)"/>
<ellipse rx="22" ry="55" fill="url(#petal2)" transform="rotate(202) translate(0,-30)"/>
<ellipse rx="22" ry="55" fill="url(#petal2)" transform="rotate(247) translate(0,-30)"/>
<ellipse rx="22" ry="55" fill="url(#petal2)" transform="rotate(292) translate(0,-30)"/>
<ellipse rx="22" ry="55" fill="url(#petal2)" transform="rotate(337) translate(0,-30)"/>

<!-- Center -->
<path d="
M-10 10
C-25 -10,-10 -30,10 -25
C30 -20,25 5,10 15
C25 25,10 35,-10 30
C-25 25,-25 15,-10 10Z"
fill="#8b0025"/>

<circle r="10" fill="#ff2d75"/>

</g>
</svg>

<div class="stem"></div>

<div class="leaf left"></div>
<div class="leaf right"></div>

</div>

</div>

</body>
</html>
"""

st.components.v1.html(html, height=650)
