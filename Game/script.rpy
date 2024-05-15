# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define g = Character("Gael", color = "FF660E")
define n = Character("")
define s = Character("Sofí")
define r = Character("Rogelio", color = "5A5A5A")
define m = Character("Profa. Marta")
define d = Character("???", color = "000000")

#Fondos
image Coffee = im.Blur("E_Coffee.png", 1.25)
image Cuarto = im.Blur("E_Cuarto.png", 1.1)
image Fondita In = im.Blur("E_Fondita_In.png", 1.25)
image Fondita Out = im.Blur("E_Fondita_Out.png", 1.25)
image Gallery = im.Blur("E_Gallery.png", 1.25)
image Park = im.Blur("E_Park.png", 1.25)
image Uni In = im.Blur("E_Uni_In.png", 1.25)
image Uni Out = im.Blur("E_Uni_Out.png", 1.25)

#image logo blurred = im.Blur("logo.png", 1.5)

#Personaje
###Rogelio

# NVL characters are used for the phone texting
init -1 python:
    phone_position_x = 0.5
    phone_position_y = 0.5
define p_nvl = Character(kind=nvl, callback=Phone_SendSound)
define s_nvl = Character("Sofí", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)


# El juego comienza aquí.

label start:

    $ player_name = renpy.input("¿Cuál es tu nombre?")

    $ player_name = player_name.strip()

    define fadehold = Fade(0.5, 1.0, 0.5)
    jump dia_1
    # Now the other characters in the game can greet the player.
    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.
    #scene
    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.
    #show 
    # Presenta las líneas del diálogo.

label dia_1:
    scene Coffee with dissolve
    play music "Cafeteria.mp3"
    n "Es una tarde como cualquier otra. Estás en la cafetería esperando a que llegue tu amiga Sofía."
    n "Has estado esperando 25 minutos y no hay rastro de ella."
    player_name "…"
    n "Suena tu celular."
    s_nvl "Holaaaa [player_name], aquí Sofí!" 
    s_nvl "No voy a llegar. Perdón :¨\["
    n "Suspiras, ella siempre hace eso. Sabes que tiene algo entre manos."
    s_nvl "Perooo, va ir mi primo Rogelio en mi lugar..."
    s_nvl "Diviertensee ;)"
    n "Sabes que no vale la pena esperar. Así que decides levantarte de tu asiento."
    n "Pero..."
    play sound "hit.mp3"
    n "Chocas con alguien."

    show rogelio happy t
    r "¿[player_name], eres tú?"

    show rogelio happy s
    n "Con una sonrisa incómoda te sientas de nuevo."
    n "Rogelio se sienta y empieza a llamar la atención del mesero."

    show rogelio happy t at left with move
    r "Dame un pastel de chocolate y un café semidescremado con espuma a 186°"
    show rogelio happy s
    n "El mesero se nota fastidiado por su actitud, pero trata de ser amable al esperar tu pedido."
    player_name "Para mi-"
    show rogelio annoyed t
    r "A ella dale una ensalada."
    show rogelio annoyed s
    player_name "Pero-"
    show rogelio annoyed t
    r "Que se ve que le hace falta…"
    show rogelio annoyed s
    n "Este día va a ser largo."
    show rogelio happy t  at center with move
    r "Bueno [player_name], ¿que quieres saber de mí?"
    show rogelio happy s

    menu:

     "…":
         show rogelio happy t at center
         r "¿Qué? ¿Te sorprendí mucho? Suelo causar ese efecto."

     "Uh…¿Qué estudias?":
         show rogelio annoyed t at center
         r "No necesito estudiar, pronto voy a heredar la empresa de mi papi"
         show rogelio happyp t
         r "Al fin ya pronto se muere."

     "Uhm, y… ¿A qué horas te vas?":
         show rogelio happy t at center
         r "Cuando seas mi novia, me iré linda."

    show rogelio happyp s at center
    n "Qué incómodo…"
    n "Por suerte llegó el mesero con los pedidos."
    show rogelio happyp s at left with move
    n "..."
    show rogelio happyp s at center with move
    n "Estabas convencida que jamás habías visto una ensalada tan insípida en tu vida."
    player_name "…"
    show rogelio annoyed t
    r "Seamos claros. Se como son las de tu tipo."
    n "{b}{size=+10}???{/size}{/b}"
    show rogelio happyp t
    r "Ana Sofi me contó de tu situación económica así que podemos solucionar nuestros problemas. "
    show rogelio happy t
    extend "¿Me entiendes?"
    show rogelio happyp s

    menu:

     "Huir":
         n "Pero antes de poder hacer algo, escuchas un grito frente tuyo."
         scene Coffee with vpunch
         play sound "hit.mp3"

     "Huir":
         n "Pero antes de poder hacer algo, escuchas un grito frente tuyo."
         scene Coffee with vpunch
         play sound "hit.mp3"
    
    show rogelio shock at left with dissolve
    show gael n shock at right with dissolve
    n "Un chico le tiró su café por accidente a Rogelio."
    show rogelio angry at left
    show gael n meh s at right
    r "¡¿Eres tonto o qué?!"
    show rogelio annoyed c at left
    show gael n meh t at right
    g "Ay, perdona fue un accidente"
    show rogelio angry at left
    show gael n meh s at right
    r "¿Sabes con quién estás tratando?"
    show rogelio annoyed c at left
    n "Observas la cómica situación, tratando de no reírte en su cara. "
    extend "Pero era muy difícil."
    n "Rogelio se acerca a ti furioso."
    hide gael n meh s at right with dissolve
    show rogelio angry at center with move
    r "¿Sabes? Pudiste haber tenido la cita de tu vida pero gracias a este tipejo te la perdiste."
    hide rogelio angry with dissolve
    n "No sabes como  reaccionar ante tales palabras, mientras lo ves tomar sus cosas al irse del café."
    n "Vaya lío."
    show gael n meh s with dissolve
    player_name "Oye ¿Estas bien?"
    show gael n sad t
    g "No te preocupes por mí, mejor dime ¿tú estás bien?"
    show gael n angry t
    g "Qué ese tipo era todo un personaje ¡eh!"
    show gael n angry s
    player_name "Si, ni que lo digas…"
    show gael n meh t
    g "Bueno… digamos que el \“accidente”, no fue tan así."
    show gael n normal t
    g "Verás yo quería ayudarte un poco, ya que te veías muy incomoda."
    show gael n normal s
    n "Que agradable sujeto."
    player_name "Ay muchas gracias, ¿puedo pagarte tu café o algo?"
    show gael n nervous t
    g "Pues… con una cita sería suficiente"
    show gael n nervous s
    n "Si, sabías que no podías confiar en la buena fé ¿Pero qué responderle?"

    menu:

     "Si, ¿por qué no?":
         show gael n blush s
         g "{i}{size=-10}Wow, no pensé que funcionaría…{/i}{/size}"
         show gael n blush t
         g "¡Bien! Uhm, entonces te entrego mi número, ¿va?"
         show gael n blush s
         n "El chico comienza a escribirlo en una servilleta. Se le ve contento."
         show gael n blush t
         g "Ok, entonces ¡te veo luego!"
         hide gael n blush t with dissolve
         n "Ves al chico irse tan rápido como apareció."
         n "Después de aquella escena, el mesero se acerca con la cuenta."
         player_name "Ay, ¿por qué me metiste en esto Sofi?"
         stop music fadeout 1.0
         scene Cuarto with dissolve
         play music "Cuarto.mp3"
         n "Unas horas más tarde, estás en tu habitación jugando con los bordes de la servilleta."
         n "¿Sería muy pronto para llamar? "
         extend "Nah"
         #play sound 
         d "¿hola?"
         n "Escuchas del otro lado de la línea la voz de una señora."
         d "Buenos días, ¿vas a pedir algo a domicilio?"
         n "Rápidamente colgaste. Qué vergüenza…"
         player_name "Ni una cita ni otra"
         player_name "Ugh…"
         n "Decepcionada del día, decides mejor dormir y tratar de olvidar todo."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_2


     "No, así estoy bien":
         show gael n nervous t
         g "Ah, bueno… si, creo que me lo busque"
         show gael n sad s
         show gael n normal t
         g "Disfruta tu comida" 
         n "El chico se va incómodo."
         hide gael n normal s with dissolve
         player_name "Pero que chicos que me tope hoy…"
         n "Después de aquella escena, un mesero se acerca con la cuenta."
         player_name "Ay, ¿por qué me metiste en esto Sofi?"
         scene Cuarto with dissolve
         n "Unas horas más tarde, estás en tu habitación"
         n "Decepcionada del día, decides mejor dormir y tratar de olvidar todo."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_2



label dia_2:

 # Finaliza el juego:
    return
