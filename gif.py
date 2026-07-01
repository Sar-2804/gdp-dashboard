import streamlit as st

st.set_page_config(page_title="Realistic Flower", layout="centered")

html_code = """
<!DOCTYPE html>
<html>
<head>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
}

body{
background:radial-gradient(circle at top,#10132b,#000);
overflow:hidden;
display:flex;
justify-content:center;
align-items:center;
height:100vh;
font-family:Arial;
}

.scene{
position:relative;
width:400px;
height:600px;
}

/* Floating particles */

.spark{
position:absolute;
width:4px;
height:4px;
background:white;
border-radius:50%;
opacity:.6;
animation:float 8s linear infinite;
}

.spark:nth-child(1){left:20%;animation-delay:0s;}
.spark:nth-child(2){left:60%;animation-delay:2s;}
.spark:nth-child(3){left:80%;animation-delay:4s;}
.spark:nth-child(4){left:40%;animation-delay:1s;}
.spark:nth-child(5){left:10%;animation-delay:5s;}

@keyframes float{

0%{
transform:translateY(500px);
opacity:0;
}

20%{
opacity:1;
}

100%{
transform:translateY(-100px);
opacity:0;
}

}

/* Flower */

.flower{
    position:absolute;
    bottom:70px;
    left:50%;
    width:180px;
    height:320px;
    transform:translateX(-50%);
    animation:sway 5s ease-in-out infinite;
}

/* Petals */

.petal{
    position:absolute;
    width:70px;
    height:100px;

    left:55px;
    top:-40px;

    background:radial-gradient(circle at 30% 20%,
        #ffd4ea 0%,
        #ff6ab0 45%,
        #ff0088 100%);

    border-radius:50% 50% 40% 40%;

    transform-origin:50% 100%;
    opacity:0;
    animation:bloom 1s forwards;

    box-shadow:0 0 20px rgba(255,20,147,.4);
}

/* Petal positions */

.p1{transform:rotate(0deg) scale(.1);animation-delay:2s;}
.p2{transform:rotate(45deg) scale(.1);animation-delay:2.1s;}
.p3{transform:rotate(90deg) scale(.1);animation-delay:2.2s;}
.p4{transform:rotate(135deg) scale(.1);animation-delay:2.3s;}
.p5{transform:rotate(180deg) scale(.1);animation-delay:2.4s;}
.p6{transform:rotate(225deg) scale(.1);animation-delay:2.5s;}
.p7{transform:rotate(270deg) scale(.1);animation-delay:2.6s;}
.p8{transform:rotate(315deg) scale(.1);animation-delay:2.7s;}

.p1{--r:0deg;}
.p2{--r:45deg;}
.p3{--r:90deg;}
.p4{--r:135deg;}
.p5{--r:180deg;}
.p6{--r:225deg;}
.p7{--r:270deg;}
.p8{--r:315deg;}

@keyframes bloom{
    from{
        opacity:0;
        transform:rotate(var(--r)) scale(.1);
    }
    to{
        opacity:1;
        transform:rotate(var(--r)) scale(1);
    }
}

/* Flower center */

.center{
    position:absolute;
    width:40px;
    height:40px;

    left:70px;
    top:-5px;

    border-radius:50%;

    background:radial-gradient(circle,#fffad2,#ffd000,#ffb300);

    box-shadow:
    0 0 15px yellow,
    0 0 30px orange,
    0 0 60px gold;

    animation:pulse 2s infinite;
}
.left{
    top:120px;
    left:-70px;
    transform:rotate(-35deg);
    animation:leftleaf 3s ease-in-out infinite;
}

.right{
    top:170px;
    right:-70px;
    transform:scaleX(-1) rotate(-35deg);
    animation:rightleaf 3s ease-in-out infinite;
}

@keyframes leftleaf{
    50%{
        transform:rotate(-25deg);
    }
}

@keyframes rightleaf{
    50%{
        transform:scaleX(-1) rotate(-25deg);
    }
}

@keyframes pulse{

50%{

box-shadow:
0 0 30px yellow,
0 0 60px orange,
0 0 90px gold;

}

}

/* Text */

.text{

position:absolute;
top:40px;
width:100%;
text-align:center;
font-size:30px;
color:white;
letter-spacing:2px;

opacity:0;

animation:show 2s 4s forwards;

text-shadow:
0 0 10px pink,
0 0 20px hotpink;

}

@keyframes show{

to{
opacity:1;
}

}

</style>

</head>

<body>

<div class="scene">

<div class="spark"></div>
<div class="spark"></div>
<div class="spark"></div>
<div class="spark"></div>
<div class="spark"></div>

<div class="text">
🌸 CODE_ZENITH.AI 🌸
</div>

<div class="flower">

    <div class="stem"></div>

    <div class="leaf left"></div>
    <div class="leaf right"></div>

    <div class="petal p1"></div>
    <div class="petal p2"></div>
    <div class="petal p3"></div>
    <div class="petal p4"></div>
    <div class="petal p5"></div>
    <div class="petal p6"></div>
    <div class="petal p7"></div>
    <div class="petal p8"></div>

    <div class="center"></div>

</div>

</div>

</body>
</html>
"""

st.components.v1.html(html_code, height=650)
