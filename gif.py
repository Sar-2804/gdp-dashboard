import streamlit as st

st.set_page_config(page_title="Blooming Flower", layout="centered")

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
background:linear-gradient(#091540,#000);
}

.scene{
position:relative;
width:400px;
height:550px;
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
50%{opacity:.2;}
}

/* Flower */

.flower{
position:absolute;
bottom:40px;
left:50%;
transform:translateX(-50%);
animation:sway 4s ease-in-out infinite;
transform-origin:bottom center;
}

@keyframes sway{
0%,100%{transform:translateX(-50%) rotate(-2deg);}
50%{transform:translateX(-50%) rotate(2deg);}
}

.stem{
width:8px;
height:240px;
margin:auto;
background:linear-gradient(#66ff88,#0a7d30);
border-radius:20px;
animation:grow 2s;
}

@keyframes grow{
from{height:0;}
to{height:240px;}
}

svg{
position:absolute;
left:-110px;
top:-120px;
transform:scale(0) rotate(-30deg);
animation:bloom 2.5s ease-out forwards;
transform-origin:center;
}

@keyframes bloom{
0%{
    transform:scale(0) rotate(-40deg);
}
60%{
    transform:scale(1.1) rotate(8deg);
}
100%{
    transform:scale(1) rotate(0deg);
}
}

.leaf{
position:absolute;
width:70px;
height:35px;
background:#32cd32;
border-radius:70px 0;
}

.left{
left:-60px;
top:120px;
transform:rotate(-35deg);
}

.right{
right:-60px;
top:170px;
transform:scaleX(-1) rotate(-35deg);
}

.text{
position:absolute;
top:30px;
width:100%;
text-align:center;
font-size:30px;
color:white;
opacity:0;
animation:show 2s 3s forwards;
text-shadow:0 0 20px hotpink;
}

@keyframes show{
to{opacity:1;}
}

</style>
</head>

<body>

<div class="scene">

<div class="star" style="left:20px;top:40px;"></div>
<div class="star" style="left:90px;top:100px;"></div>
<div class="star" style="left:300px;top:60px;"></div>
<div class="star" style="left:360px;top:150px;"></div>
<div class="star" style="left:200px;top:20px;"></div>

<div class="text">🌸 For You 🌸</div>

<div class="flower">

<svg width="180" height="180">

<defs>

<radialGradient id="petal">
<stop offset="0%" stop-color="#ffd1e8"/>
<stop offset="100%" stop-color="#ff1493"/>
</radialGradient>

</defs>

<g transform="translate(90 90)">

<ellipse rx="28" ry="60" fill="url(#petal)" transform="rotate(0) translate(0,-40)"/>
<ellipse rx="28" ry="60" fill="url(#petal)" transform="rotate(45) translate(0,-40)"/>
<ellipse rx="28" ry="60" fill="url(#petal)" transform="rotate(90) translate(0,-40)"/>
<ellipse rx="28" ry="60" fill="url(#petal)" transform="rotate(135) translate(0,-40)"/>
<ellipse rx="28" ry="60" fill="url(#petal)" transform="rotate(180) translate(0,-40)"/>
<ellipse rx="28" ry="60" fill="url(#petal)" transform="rotate(225) translate(0,-40)"/>
<ellipse rx="28" ry="60" fill="url(#petal)" transform="rotate(270) translate(0,-40)"/>
<ellipse rx="28" ry="60" fill="url(#petal)" transform="rotate(315) translate(0,-40)"/>

<circle r="18" fill="gold"/>

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

st.components.v1.html(html, height=600)
