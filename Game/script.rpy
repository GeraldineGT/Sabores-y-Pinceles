# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define g = Character("Gael", color = "FF660E")
define n = Character("")
define s = Character("Sofí")
define r = Character("Rogelio", color = "5A5A5A")
define m = Character("Profa. Marta", color = "4C9900")
define w = Character("Mesero", color = "000000")
define d = Character("???", color = "000000")
define c = Character("Cajero", color = "000000")
define c1 = Character("Señor", color = "000000")
define c2 = Character("Cliente", color = "000000")
define c3 = Character("Clienta", color = "000000")
define a = Character("Chico del café", color = "000000")

#Fondos
image Coffee = im.Blur("E_Coffee.png", 1.25)
image Cuarto = im.Blur("E_Cuarto.png", 1.1)
image Fondita In = im.Blur("E_Fondita_In.png", 1.25)
image Fondita Out = im.Blur("E_Fondita_Out.png", 1.25)
image Gallery = im.Blur("E_Gallery.png", 1.25)
image Park = im.Blur("E_Park.png", 1.25)
image Uni In = im.Blur("E_Uni_In.png", 1.25)
image Uni Out = im.Blur("E_Uni_Out.png", 1.25)
image Tienda = im.Blur("E_Fondita_Out.png", 1.5)
image closer = im.Blur("E_Fondita_CU.png", 2)

#image logo blurred = im.Blur("logo.png", 1.5)

#Personaje
###Rogelio

# NVL characters are used for the phone texting
init -1 python:
    phone_position_x = 0.5
    phone_position_y = 0.5
define p_nvl = Character("[player_name]", kind=nvl, callback=Phone_SendSound)
define s_nvl = Character("Sofí", kind=nvl, callback=Phone_ReceiveSound)
define g_nvl = Character("Gael", kind=nvl, callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

#jump
transform jumper:
 ease .04 yoffset 24
 ease .04 yoffset 20
 ease .03 yoffset 16
 ease .02 yoffset 12
 ease .01 yoffset 8
 ease .01 yoffset 4
 ease .01 yoffset 0


init python:
    def setup_puzzle1():
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc)
    
    def piece_drop1(dropped_on, dragged_piece):
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False
            finished_pieces += 1

            if finished_pieces == page_pieces:
                renpy.jump("dia_9_norm1_p2")

init python:
    def hsetup_puzzle1():
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc)
    
    def hpiece_drop1(dropped_on, dragged_piece):
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False
            finished_pieces += 1

            if finished_pieces == page_pieces:
                renpy.jump("hdia_9_norm1_p2")

init python:
    def setup_puzzle2():
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc)
    
    def piece_drop2(dropped_on, dragged_piece):
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False
            finished_pieces += 1

            if finished_pieces == page_pieces:
                renpy.jump("dia_9_norm2_p2")

init python:
    def hsetup_puzzle2():
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc)
    
    def hpiece_drop2(dropped_on, dragged_piece):
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False
            finished_pieces += 1

            if finished_pieces == page_pieces:
                renpy.jump("hdia_9_norm2_p2")

init python:
    def setup_puzzle01():
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc)
    
    def piece_drop01(dropped_on, dragged_piece):
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False
            finished_pieces += 1

            if finished_pieces == page_pieces:
                renpy.jump("dia_9_good1p2")

init python:
    def hsetup_puzzle01():
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc)
    
    def hpiece_drop01(dropped_on, dragged_piece):
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False
            finished_pieces += 1

            if finished_pieces == page_pieces:
                renpy.jump("dia_9_good1p2")

init python:
    def setup_puzzle02():
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc)
    
    def piece_drop02(dropped_on, dragged_piece):
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False
            finished_pieces += 1

            if finished_pieces == page_pieces:
                renpy.jump("dia_9_good2p2")

init python:
    def hsetup_puzzle02():
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc)
    
    def hpiece_drop02(dropped_on, dragged_piece):
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False
            finished_pieces += 1

            if finished_pieces == page_pieces:
                renpy.jump("hdia_9_good2p2")

init python:
    def setup_puzzle3():
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc)
    
    def piece_drop3(dropped_on, dragged_piece):
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False
            finished_pieces += 1

            if finished_pieces == page_pieces:
                renpy.jump("dia_9_bad_p2")

init python:
    def hsetup_puzzle3():
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc)
    
    def hpiece_drop3(dropped_on, dragged_piece):
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False
            finished_pieces += 1

            if finished_pieces == page_pieces:
                renpy.jump("hdia_9_bad_p2")

##########################
default page_pieces = 4
default full_page_size = (916, 914)
default piece_cordinates = [(127, 87), (580, 87), (127, 540), (580, 540)]
default initial_piece_coordinates = []
default finished_pieces = 0


# El juego comienza aquí.

label start:

    $ player_name = renpy.input("¿Cuál es tu nombre?")

    $ player_name = player_name.strip()

    n "\¿Cuál es tu género?"
    menu:
        "Mujer":
            define fadehold = Fade(0.5, 1.0, 0.5)
            jump dia_1
        "Hombre":
            define fadehold = Fade(0.5, 1.0, 0.5)
            jump hdia_1
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
    r "\¿[player_name], eres tú?"

    show rogelio happy s
    n "Con una sonrisa incómoda te sientas de nuevo."
    n "Rogelio se sienta y empieza a llamar la atención del mesero."

    show rogelio happy t at left with move
    show mesero happy at right with dissolve
    w "¿Qué van a-"
    show mesero s at right
    r "Dame un pastel de chocolate y un café semidescremado con espuma a 156°F"
    show rogelio happy s at left
    n "El mesero se nota fastidiado por su actitud, pero trata de ser amable contigo."
    show mesero happy at right
    w "Y ¿Para usted?"
    player_name "Para mi-"
    show rogelio annoyed t at left
    show mesero s at right
    r "A ella dale una ensalada."
    show rogelio annoyed s at left
    player_name "Pero-"
    show rogelio annoyed t at left
    r "Que se ve que le hace falta…"
    show rogelio annoyed s at left
    show mesero uncomfy at right
    w "¿Ok?"
    hide mesero uncomfy with dissolve
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
    show rogelio happyp s at left with move
    show mesero s at right with dissolve
    n "Por suerte llegó el mesero con los pedidos."
    n "..."
    hide mesero s with dissolve
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
         n "Pero antes de poder hacer algo, escuchas un grito frente a ti."
         scene Coffee with vpunch
         play sound "hit.mp3"

     "Huir":
         n "Pero antes de poder hacer algo, escuchas un grito frente a ti."
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
    d "Ay, perdona fue un accidente"
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
    n "No sabes como reaccionar ante tales palabras, mientras lo ves tomar sus cosas al irse del café."
    n "Vaya lío."
    show gael n meh s with dissolve
    player_name "Oye ¿Estas bien?"
    show gael n sad t
    d "No te preocupes por mí, mejor dime ¿tú estás bien?"
    show gael n angry t
    d "Qué ese tipo era todo un personaje ¡eh!"
    show gael n angry s
    player_name "Si, ni que lo digas…"
    show gael n meh t
    d "Bueno… digamos que el \“accidente”, no fue tan así."
    show gael n normal t
    d "Verás yo quería ayudarte un poco, ya que te veías muy incomoda."
    show gael n normal s
    n "Que agradable sujeto."
    player_name "Ay muchas gracias, ¿puedo pagarte tu café o algo?"
    show gael n nervous t
    d "Pues… con una cita sería suficiente"
    show gael n nervous s
    n "Si, sabías que no podías confiar en la buena fé de la gente ¿Pero qué responderle?"
    menu:

     "Si, ¿por qué no?":
         show gael n blush s
         d "{i}{size=-10}Wow, no pensé que funcionaría…{/i}{/size}"
         show gael n blush t
         d "¡Bien! Uhm, entonces te entrego mi número, ¿va?"
         show gael n blush s
         n "El chico comienza a escribirlo en una servilleta. Se le ve contento."
         show gael n blush t
         d "Ok, entonces ¡te veo luego!"
         hide gael n blush t with dissolve
         n "Ves al chico irse tan rápido como apareció."
         #show mesero s at dissolve
         n "Después de aquella escena, el mesero se acerca con la cuenta."
         player_name "Ay, ¿por qué me metiste en esto Sofi?"
         #hide mesero s at dissolve
         stop music fadeout 1.0
         scene Cuarto with dissolve
         play music "Cuarto.mp3"
         n "Unas horas más tarde, estás en tu habitación jugando con los bordes de la servilleta."
         n "¿Sería muy pronto para llamar? "
         extend "Nah"
         play sound "ReceiveText.ogg"
         d "¿hola?"
         n "Escuchas del otro lado de la línea la voz de una señora."
         d "Buenos días, ¿vas a pedir algo a domicilio?"
         n "Rápidamente colgaste. Qué vergüenza…"
         player_name "Ni una cita ni otra"
         player_name "Ugh…"
         n "Decepcionada del día, decides mejor dormir y tratar de olvidar todo."
         scene black with dissolve
         jump dia_2_good


     "No, así estoy bien":
         show gael n nervous2 t
         d "Ah, bueno… si, creo que me lo busque"
         show gael n normal t
         d "Disfruta tu comida"
         show gael n nervous2 s
         n "El chico se va incómodo."
         hide gael n nervous s with dissolve
         player_name "Pero que chicos que me tope hoy…"
         #show mesero s at dissolve
         n "Después de aquella escena, un mesero se acerca con la cuenta."
         player_name "Ay, ¿por qué me metiste en esto Sofi?"
         #hide mesero s at dissolve
         scene Cuarto with dissolve
         play music "Cuarto.mp3"
         n "Unas horas más tarde, estás en tu habitación"
         n "Decepcionada del día, decides mejor dormir y tratar de olvidar todo."
         scene black with dissolve
         jump dia_2_normal

label dia_2_good:
    scene Cuarto with dissolve
    n "Después de un merecido descanso, te alistas para ir a la Universidad."
    scene Uni In with dissolve
    play music "Uni.mp3"
    n "La clase de la profesora Marta comenzó. Explicando todo acerca de la presentación de final de semestre, que sería en un par de semanas."
    show marta normal t with dissolve
    m "¡Chicos! ¡Logré que nos prestarán uno de los auditorios del museo de la ciudad para nuestra exposición!"
    show marta normal s
    n "Algunos alumnos se alegraron mientras otros les daba igual."
    show marta normal t
    m "Entonces procuren entregar una pintura digna del espacio ¡Así que esfuércense!"
    hide marta normal s with dissolve
    n "Sabías bien que no solo se refería a la técnica, si no a tener buenos materiales."
    n "Igual a…"
    extend" necesitas dinero."
    n "Dinero que te gastaste ayer por culpa de ese tonto."
    n "Dinero que no tienes…"
    player_name "Ughhhhhhh"
    scene Uni Out with dissolve
    play music "Park.mp3"
    n "Sales de la clase, aún pensando que puedes hacer. No es como si las oportunidades cayeran del cielo."
    scene Uni Out with vpunch
    play sound "hit.mp3"
    n "Por estar dando vueltas al asunto, chocaste con el tablón de anuncios. Haciendo que uno de los panfletos cayera a tus manos."
    n "{size=+10}SE BUSCA AYUDANTE{/size}"
    player_name "¿Quién lo diría?"
    extend " Si caen del cielo."
    n "No perdías nada al intentar ir a preguntar ¿verdad?"

    scene Fondita Out with dissolve
    n "Caminaste por unos minutos. El lugar no era tan lejano como creías, eso era un punto a favor."
    scene Fondita In with dissolve
    play sound "shop bell.mp3"
    play music "Cafeteria.mp3"
    n "La fondita parecía espaciosa y un poco concurrida. La decoración y ambiente hogareño se sentía como un abrazo cálido."
    n "Definitivamente el lugar tenía su encanto."
    show gael m normal s with dissolve
    n "Mientras más te acercabas a la barra principal, notabas un rostro familiar."
    show gael m shock at jumper
    n "{b}{size=+10}!!!{/size}{/b}"
    n "Bueno, esto empieza a explicar muchas cosas."
    show gael m nervous s
    d "…"
    player_name "Oh"
    show gael m nervous t
    a "¡H-Hola!"
    show gael m nervous s
    n "No puedes evitar sonreír un poco al verlo tan avergonzado."
    player_name "No creí que volvería a verte tan pronto."
    extend " Aunque ahora entiendo el por que cuando llamé me preguntaron si quería pedir algo."
    show gael m sad t
    a "{i}{size=-10}Chale, si eras tú.{/i}{/size}"
    show gael m nervous t
    a "Qué vergüenza, de verdad lo siento."
    a "Es que ya se me hace costumbre que pidan el número del lugar y no esperaba que dijeras que si ayer, entonces los cables se me cruzaron y solo escribí el primer número que pasó por mi mente. Ya después me di cuenta, pero no sabía cómo encontrarte y-"
    show gael m sad s
    n "No pudiste soportarlo más y una risita escapó de tus labios."
    player_name "Perdón, es solo que me alegra saber que tenía una explicación. Ya me estaba montando teorías en la cabeza."
    show gael m nervous t
    a "Bueno… uhm "
    extend "¿y qué te trae aquí?"
    show gael m nervous s

    n "Sacaste de tus bolsillos el panfleto."
    player_name "Vi esto en la universidad, y estaba pensando en postularme para el trabajo de mesera."
    player_name "Pero no sabía que tú trabajabas aquí…"

    menu:

     "Te vas por la vergüenza":
         show gael m nervous2 s
         player_name "Ay, como que acabo de recordar que debo hacer algo"
         player_name "Adiós"
         hide gael m nervous s with dissolve
         stop music fadeout 1.0
         scene Fondita Out with dissolve
         n "Qué horror. No esperabas encontrarlo y podrás necesitar dinero pero para nada te quedarás unos segundos más."
         play sound "bicycle.mp3"
         d "¡Oye! ¡Muévete!"
         n "Oh no..."
         scene Fondita Out with vpunch
         play sound "crash.mp3"
         scene black with dissolve
         n "..."
         scene final 0 with dissolve
         n " "
         n "Has conseguido el final 0."
         return
         ####Final 0###


     "Te quedas":
         player_name "Pero no importa, necesito el trabajo"
         player_name "Así que, ¿qué debo hacer?"
         show gael m normal t
         a "Bueno… antes que nada necesitamos saber que tienes lo necesario para trabajar aquí."
         show gael m blush t
         a "¡Pero no te preocupes! El día de prueba va a ser remunerado"
         hide gael m blush t with dissolve
         n "Después de unas horas trabajando en la fondita, emepezaste a familiarizarte con tu alrededor."
         n "Cuando menos lo notaste, Gael se acerca."
         show gael m normal t with dissolve
         a "Creo que podrías afinar algunas cosas, pero tienes las habilidades necesarias para trabajar aquí."
         a "¡Así que bienvenida!"
         hide gael m normal s with dissolve
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_3_good

label dia_2_normal:
    scene Cuarto with dissolve
    n "Después de un merecido descanso, te alistas para ir a la Universidad."
    scene Uni In with dissolve
    play music "Uni.mp3"
    n "La clase de la profesora Marta comenzó. Explicando todo acerca de la presentación de final de semestre, que sería en un par de semanas."
    show marta normal t with dissolve
    m "¡Chicos! ¡Logré que nos prestarán uno de los auditorios del museo de la ciudad para nuestra exposición!"
    show marta normal s
    n "Algunos alumnos se alegraron mientras otros les daba igual."
    show marta normal t
    m "Entonces procuren entregar una pintura digna del espacio ¡Así que esfuércense!"
    hide marta normal s with dissolve
    n "Sabías bien que no solo se refería a la técnica, si no a tener buenos materiales."
    n "Igual a…"
    extend " necesitas dinero."
    n "Dinero que te gastaste ayer por culpa de ese tonto."
    n "Dinero que no tienes…"
    player_name "Ughhhhhhh"
    scene Uni Out with dissolve
    play music "Park.mp3"
    n "Sales de la clase, aún pensando que puedes hacer. No es como si las oportunidades cayeran del cielo."
    scene Uni Out with vpunch
    play sound "hit.mp3"
    n "Por estar dando vueltas al asunto, chocaste con el tablón de anuncios. Haciendo que uno de los panfletos cayera a tus manos."
    n "{size=+10}SE BUSCA AYUDANTE{/size}"
    player_name "¿Quién lo diría?"
    extend " Si caen del cielo."
    n "No perdías nada al intentar ir a preguntar ¿verdad?"

    scene Fondita Out with dissolve
    n "Caminaste por unos minutos. El lugar no era tan lejano como creías, eso era un punto a favor."
    scene Fondita In with dissolve
    play sound "shop bell.mp3"
    play music "Cafeteria.mp3"
    n "La fondita parecía espaciosa y un poco concurrida. La decoración y ambiente hogareño se sentía como un abrazo cálido."
    n "Definitivamente el lugar tenía su encanto."
    show gael m normal s with dissolve
    n "Mientras más te acercabas a la barra principal, notabas un rostro familiar."
    show gael m shock at jumper
    n "{b}{size=+10}!!!{/size}{/b}"
    show gael m sad s
    n "No puede ser."
    show gael m nervous2 t
    n "Oh…"
    player_name "..."
    show gael m nervous2 s
    n "De todas las personas que existen, tenía que ser ese chico quién trabajará aquí."
    show gael m nervous2 t
    a "Uhm, ¿Qué te trae aquí?"
    show gael m nervous2 s

    n "Sacaste de tus bolsillos el panfleto."
    player_name "Vi esto en la universidad, y estaba pensando en postularme para el trabajo de mesera."
    player_name "Pero no sabía que tú trabajabas aquí…"

    menu:

     "Te vas":
         show gael m nervous2 s
         player_name "Ay, como que acabo de recordar que debo hacer algo"
         player_name "Adiós"
         hide gael m nervous s with dissolve
         stop music fadeout 1.0
         scene Fondita Out with dissolve
         n "Qué horror. No esperabas encontrarlo y podrás necesitar dinero pero para nada te quedarás unos segundos más."
         play sound "bicycle.mp3"
         d "¡Oye! ¡Muévete!"
         n "Oh no..."
         scene Fondita Out with vpunch
         play sound "crash.mp3"
         scene black with dissolve
         n "..."
         scene final 0 with dissolve
         n " "
         n "Has conseguido el final 0."
         return
         ####Final 0###

     "Te quedas":
         player_name "Pero no importa, necesito el trabajo"
         player_name "Así que, ¿qué debo hacer?"
         show gael m normal t
         a "Bueno… antes que nada necesitamos saber que tienes lo necesario para trabajar aquí."
         show gael m blush t
         a "¡Pero no te preocupes! El día de prueba va a ser remunerado"
         hide gael m blush t with dissolve
         n "Después de unas horas trabajando en la fondita, emepezaste a familiarizarte con tu alrededor."
         n "Cuando menos lo notaste, Gael se acerca."
         show gael m normal t with dissolve
         a "Creo que podrías afinar algunas cosas, pero tienes las habilidades necesarias para trabajar aquí."
         a "¡Así que bienvenida!"
         hide gael m normal s with dissolve
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_3_normal

label dia_3_good:
    scene Uni Out with dissolve
    play music "Park.mp3"
    n "Al día siguiente continuaste con tus actividades con normalidad."
    n "Después de una larga clase, llegó el descanso..."
    extend "que tu amiga aprovecho como excusa para hablar."
    show asof nervous s with dissolve
    player_name "No entiendo cómo pudiste hacerme esto…"
    show asof nervous t
    s "¡Ya me disculpé muchas veces hoy [player_name]!"
    show asof nervous s
    player_name "No es suficiente…"
    show asof shock t
    s "¡¿Qué iba a saber yo que ese wey era un patán?!"
    hide asof shock t
    show sof nervous t
    s "Solo lo veo en Navidad y ni le hablo, pero se me hacía guapo y dije "
    extend "\“¡ah! tal vez le sirva a mi bestie\”"
    hide sof nervous t
    show asof nervous s
    player_name "ugh…"
    show asof meh
    s "Ya perdoname, te prometo que no vuelvo a hacer algo así."
    show asof close2
    player_name "Es la tercera vez…"
    hide asof close2
    show sof nervous t
    s "Lo se pero ya no va haber cuarta."
    show sof nervous s
    player_name "Y lo peor de todo, es que tuve que pagar su cuenta."
    hide sof nervous s
    show asof shock s
    s "{b}{size=+10}!!!{/size}{/b}"
    player_name "Y no pidió poquito…"
    show asof serious t
    s "Ay supongo que me lo debí imaginar, por eso mi tío lo quiere desheredar."
    show asof close2
    s "..."
    hide asof close2
    show sof shock t
    s "Oye pero ¿Cómo vas a pagar tus materiales para el proyecto final?"
    player_name "De hecho, justo ayer conseguí trabajo."
    hide sof shock t
    show asof shock s
    player_name "Y eso es otro problema."
    hide asof shock s
    show sof shock t 
    s "¿Qué? ¿Por qué?"
    show sof shock s
    player_name "Por que la cita no acabo con que Rogelio me dejo, si no que otro chavo se metió en el asunto."
    show sof shock s at jumper
    s "{b}{size=+10}???{/size}{/b}"
    player_name "Él tiró todo su café en Rogelio para sacarme de ahí."
    show sof nervous t
    s "Eso es bueno ¿no?"
    hide sof nervous t
    show asof nervous s
    player_name "Pues…"

    menu:

     "Hablar bien":
         player_name "No te voy a mentir, era mi tipo."
         show asof happy s
         player_name "Hasta su número me dio y todo."
         hide asof happy s
         show sof happy t
         s "Girl ya ves ¿que mis planes no son tan malos? Puedes juzgar mis métodos pero no mis resultados."
         hide sof happy t
         show asof nervous s
         player_name "Pero se confundió y anotó otra cosa."
         hide asof nervous s
         show sof normal t
         jump dia_3_pt2_good

     "Hablar mal":
         player_name "Resultó que tenía otras intenciones…"
         show asof shock t
         s "Ay, ¿Pues qué pasó?"
         show asof serious s
         player_name "Fue demasiado directo, ¡ni su nombre sé y me pidió una cita!"
         hide asof serious s
         show sof happy t
         s "Ay, pues hubieras aprovechado"
         show sof happy s
         player_name "¡Ni loca!"
         show sof happy t
         s "Si dios quita, dios da"
         show sof happy s
         player_name "Ugh…"
         show sof normal t
         jump dia_3_pt2_normal

label dia_3_normal:
    scene Uni Out with dissolve
    play music "Park.mp3"
    n "Al día siguiente continuaste con tus actividades con normalidad."
    n "Después de una larga clase, llegó el descanso..."
    extend "que tu amiga aprovecho como excusa para hablar."
    show asof nervous s with dissolve
    player_name "No entiendo cómo pudiste hacerme esto…"
    show asof nervous t
    s "¡Ya me disculpé muchas veces hoy [player_name]!"
    show asof nervous s
    player_name "No es suficiente…"
    show asof shock t
    s "¡¿Qué iba a saber yo que ese wey era un patán?!"
    hide asof shock t
    show sof nervous t
    s "Solo lo veo en Navidad y ni le hablo, pero se me hacía guapo y dije "
    extend "\“¡ah! tal vez le sirva a mi bestie\”"
    hide sof nervous t
    show asof nervous s
    player_name "ugh…"
    show asof meh
    s "Ya perdoname, te prometo que no vuelvo a hacer algo así."
    show asof close2
    player_name "Es la tercera vez…"
    hide asof close2
    show sof nervous t
    s "Lo se pero ya no va haber cuarta."
    show sof nervous s
    player_name "Y lo peor de todo, es que tuve que pagar su cuenta."
    hide sof nervous s
    show asof shock s
    s "{b}{size=+10}!!!{/size}{/b}"
    player_name "Y no pidió poquito…"
    show asof serious t
    s "Ay supongo que me lo debí imaginar, por eso mi tío lo quiere desheredar."
    show asof close2
    s "..."
    hide asof close2
    show sof shock t
    s "Oye pero ¿Cómo vas a pagar tus materiales para el proyecto final?"
    player_name "De hecho, justo ayer conseguí trabajo."
    hide sof shock t
    show asof shock s
    player_name "Y eso es otro problema."
    hide asof shock s
    show sof shock t 
    s "¿Qué? ¿Por qué?"
    show sof shock s
    player_name "Por que la cita no acabo con que Rogelio me dejo, si no que otro chavo se metió en el asunto."
    show sof shock s at jumper
    s "{b}{size=+10}???{/size}{/b}"
    player_name "Él tiró todo su café en Rogelio para sacarme de ahí."
    show sof nervous t
    s "Eso es bueno ¿no?"
    hide sof nervous t
    show asof nervous s
    player_name "Pues…"


    menu:

     "Hablar bien":
         player_name "No te voy a mentir, era lindo."
         hide asof nervous s
         show sof happy t
         s "Girl ya ves ¿que mis planes no son tan malos? Puedes juzgar mis métodos pero no mis resultados."
         hide sof happy t
         show asof nervous s
         player_name "Pero fue muy directo de repente y mejor lo deje."
         hide asof nervous s
         show sof normal t
         jump dia_3_pt2_good

     "Hablar mal":
         player_name "Resultó que tenía otras intenciones…"
         hide asof nervous s
         show sof shock t
         s "Ay, ¿Pues qué pasó?"
         hide sof shock t
         show asof serious s
         player_name "Fue demasiado directo, ¡ni su nombre sé y me pidió una cita!"
         hide asof serious s
         show sof happy t
         s "Ay, pues hubieras aprovechado"
         show sof happy s
         player_name "¡Ni loca!"
         show sof happy t
         s "Si dios quita, dios da"
         show sof happy s
         player_name "Ugh…"
         show sof normal t
         jump dia_3_pt2_normal

label dia_3_pt2_good:
    s "Ok ¿Y qué tiene que ver con tu trabajo?"
    hide sof normal t
    show asof normal s
    player_name "Pues resulta que es mi compañero de trabajo…"
    show asof shock t
    s "Ay no amix, esto ya parece Wittpad"
    show asof shock s
    player_name "No empieces Ana Sofí"
    hide asof shock s
    show sof shock t
    s "Es que, o sea"
    s "¿Qué probabilidad hay de que eso te pase?"
    hide sof shock t
    show asof shock s
    player_name "La verdad ni se si me voy a quedar ahí por mucho tiempo."
    player_name "Tal vez hasta renuncie cuando junte para los materiales."
    show asof meh
    s "Ay [player_name], tu siempre tan \“positiva\”"
    show asof close2
    player_name "Es que no entiendes Sofí, es algo raro."
    show asof meh
    s "Si tu lo dices..."
    hide asof meh with dissolve
    n "Mientras regresabas al salón, observaste a alguien caminando del lado contrario."
    show gael n normal s with dissolve
    player_name "{i}{size=-10}¿Acaso es?{/size}{/i}"
    hide gael n normal s with dissolve
    player_name "{i}{size=-10}Creo que ya estoy alucinando cosas...{/size}{/i}"

    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Horas más tarde"
    n "Después de unas horas trabajando, finalmente encuentras un momento de descanso."
    d "Día pesado ¿eh?"
    n "Volteas a la dirección de la voz."
    show gael m normal s with dissolve
    player_name "…"
    show gael m nervous2 t
    a "{i}{size=-10}Público pesado…{/size}{/i}"
    show gael m nervous2 s
    a "{i}{size=-10}Cofcof{/size}{/i}"
    show gael m normal t
    a "Uhm…ahora que lo pienso, ni siquiera conozco tu nombre."
    show gael m normal s
    player_name "[player_name]. Mi nombre es [player_name]."
    n "..."
    show gael m normal t
    g "Bueno... el mio es Gael, um...mucho gusto"
    player_name "Ah, un gusto."
    show gael m normal s
    n "..."
    show gael m meh s
    n "Qué incómodo."
    n "Supones que es mejor romper el hielo que seguir fingiendo limpiar la barra en silencio."
    show gael m normal s

    menu:
      "Preguntar sobre el trabajo":
            player_name "Uhm, y entonces ¿desde cuando trabajas acá?"
            show gael m normal t
            g "De hecho, es negocio de mi familia. Así que desde hace tiempo supongo. Aunque ahorita estoy estudiando entonces ha sido un poco complicado el manejo."
            show gael m normal s

            menu:
                "Preguntar sobre su carrera":
                    player_name "Oh, y ¿qué estudias?"
                    show gael m normal t
                    g "Veterinaria. "
                    extend "En la Universidad de Miralta."
                    show gael m nervous2 t
                    g "...y creo que descubrí hoy que tú también estudias ahí, ¿verdad?"
                    show gael m normal s
                    player_name "Ah sí, estudió artes plásticas..."
                    n "Paraste en seco."
                    player_name "Aguanta…"
                    n "..."
                    n "..."
                    n "{b}{size=+10}!!!{/size}{/b}"
                    player_name "¡Así que si eras tú!"
                    show gael m nervous2 s at jumper
                    g "{b}{size=+10}!!!{/size}{/b}"
                    show gael m nervous2 t
                    g "Supongo que no soy un bueno ocultando cosas…"
                    extend "ja…"
                    show gael m nervous2 s
                    n "..."

                    menu:
                      "Y… ¿Qué tanto escuchaste?":
                            show gael m normal t
                            g "Bueno, no es como si te estuviera espiando ¿si?, solo estaba ahí pegando volantes y una cosa llevo a otra."
                            show gael m nervous t
                            g "Además que me halago saber que soy tu tipo"
                            show gael m nervous s

      "Preguntar sobre su carrera":
            player_name "Oh, y ¿qué estudias?"
            show gael m normal t
            g "Veterinaria. "
            extend "En la Universidad de Miralta."
            show gael m nervous2 t
            g "...y creo que descubrí hoy que tú también estudias ahí, ¿verdad?"
            show gael m normal s
            player_name "Ah sí, estudió artes plásticas..."
            n "Paraste en seco."
            player_name "Aguanta…"
            n "..."
            n "..."
            n "{b}{size=+10}!!!{/size}{/b}"
            player_name "¡Así que si eras tú!"
            show gael m nervous2 s at jumper
            g "{b}{size=+10}!!!{/size}{/b}"
            show gael m nervous2 t
            g "Supongo que no soy un bueno ocultando cosas…"
            extend "ja…"
            show gael m nervous2 s
            n "..."

            menu:
                      "Y… ¿Qué tanto escuchaste?":
                            show gael m normal t
                            g "Bueno, no es como si te estuviera espiando ¿si?, solo estaba ahí pegando volantes y una cosa llevo a otra."
                            show gael m nervous t
                            g "Además que me halago saber que soy tu tipo"
                            show gael m nervous s

    n "Gael se acerca a ti y te ofrece tu pago del día."
    show gael m normal t
    g "El punto es que... "
    g "Entiendo que este sea un trabajo rápido para tí, pero realmente creo que lo estás haciendo bien. Capaz y hasta ayudes a que este lugar sea más interesante."
    g "Así que…¿qué dices?"
    show gael m normal s
 
    menu:
     "Que verguenza, mejor renuncias":
         player_name "Lo siento, creo que será mejor hasta aquí."
         show gael m sad s
         n "Tomas las propinas de tu bolsillo."
         player_name "Aún así gracias."
         n "Dejas tu mandil en la barra, y te retiras avergonzada de la fonda."
         n "No puedes creer que te escuchó diciendo eso acerca de él."
         hide gael m sad s with dissolve
         scene Tienda with dissolve
         stop music fadeout 1.0
         n "Caminas por un rato, llegando a una gran papelería."
         n "Tomas de los pasillos algunos materiales para tu proyecto."
         n "Al llegar al cajero, mientras más artículos pasan, te das cuenta que el número de la cuenta incrementa más"
         extend "…y más."
         c "Bueno, va a ser $1550 pesos."
         n "{b}{size=+10}!!!{/size}{/b}"
         n "Tuviste que regresar más de la mitad de las cosas."
         n "No sabes como vas a poder entregar tu proyecto ahora."
         scene black with dissolve
         n "..."
         scene final 1 with dissolve
         n " "
         n "Has conseguido el final 1."
         return
         ####Final 1###

     "Te quedas":
         n "Sonreíste al escuchar sus palabras."
         player_name "Gracias, eres muy convincente ¿lo sabes?"
         hide gael m normal s with dissolve
         n "Continuas trabajando por un rato más. Clientes vienen y van. Parecía que el día sería bueno."
         n "Hasta que todo se arruinó."
         n "Un señor entra y se sienta enojado en una de las mesas de atrás."
         n "Tomas un respiro y te acercas. Sabías que este no sería como los otros clientes."
         show don s with dissolve
         player_name "Buenas tardes. Le entregó el menú-"
         show don t
         c1 "No, no. Dígame cuál es el especial."
         show don s
         player_name "A-Ah, bueno es una ensalada César."
         show don t
         c1 "¿César? ¿Quién es ese tal César?"
         show don s
         player_name "No, no. Así se llama la ensalada que tiene pollo y-"
         show don t
         c1 "¿Ensalada? ¿Acaso me dices gordo?"
         show don s
         play music "No.mp3"
         player_name "Ay, no. Espere, no me referia a eso. Es que ese es nuestro especial del día."
         show don t
         c1 "Creo que se muy bien lo que entendí, y ¡no voy a permitir que me falten el respeto de esta forma!"
         show don s at left with move
         show gael m meh t at right
         g "Disculpe, ¿Está todo bien aquí?"
         show don t at left
         show gael m meh s at right
         c1 "Su mesera resultó ser muy inútil, deberían ser más exigentes con las personas que contratan aquí."
         show don s at left
         player_name "A ver, yo no he hecho nada. Solo le explicaba el menú."
         show don t at left
         c1 "¡Ah! ¿Entonces me estás diciendo mentiroso?"
         show gael m angry s at right
         c1 "Debí suponer que no debía esperar tanto de una pocilga como está."
         show don s at left
         show gael m angry t at right
         g "Bueno, si no le gusta el menú. Hay bastantes lugares a dos cuadras que puede ir, donde sé que habrá comida más acorde a lo que busca."
         show don nerv s at left
         show gael m meh s at right
         c1 "{b}{size=+10}!!!{/size}{/b}"
         show don nerv t at left
         c1 "Ugh, que pésimo servicio…"
         hide don nerv t with dissolve
         play music "Cafeteria.mp3"
         show gael m nervous2 t at center with dissolve
         g "Ugh, con cosas como estas, entiendo el por que piensas en renunciar."
         show gael m normal t
         g "Pero, por favor no te desanimes. Al final todo se resolverá."
         show gael m blush t
         g "Y si no, vendré ayudarte cuantas veces ocupes"
         show gael m normal s
         n "No entendías por qué, pero sus palabras te ayudaron a tranquilizarte."
         n "Tal vez tenga razón. Nada va a ser tan malo."
         hide gael m normal s with dissolve
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_4

label dia_3_pt2_normal:
    s "Ok \¿Y qué tiene que ver con tu trabajo?"
    hide sof normal t
    show asof normal s
    player_name "Pues resulta que es mi compañero de trabajo…"
    show asof shock t
    s "Ay no amix, esto ya parece Wittpad"
    show asof shock s
    player_name "No empieces Ana Sofí"
    hide asof shock s
    show sof shock t
    s "Es que, o sea"
    s "\¿Qué probabilidad hay de que eso te pase?"
    hide sof shock t
    show asof shock s
    player_name "La verdad ni se si me voy a quedar ahí por mucho tiempo."
    player_name "Tal vez hasta renuncie cuando junte para los materiales."
    show asof meh
    s "Ay [player_name], tu siempre tan \“positiva\”"
    show asof close2
    player_name "Es que no entiendes Sofí, es algo raro."
    show asof meh
    s "Si tu lo dices..."
    hide asof meh with dissolve
    n "Mientras regresabas al salón, observaste a alguien caminando del lado contrario."
    show gael n normal s with dissolve
    player_name "{i}{size=-10}¿Acaso es?{/size}{/i}"
    hide gael n normal s with dissolve
    player_name "{i}{size=-10}Creo que ya estoy alucinando cosas...{/size}{/i}"

    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Horas más tarde"
    n "Después de unas horas trabajando, finalmente encuentras un momento de descanso."
    d "Día pesado ¿eh?"
    n "Volteas a la dirección de la voz."
    show gael m normal s with dissolve
    player_name "…"
    show gael m nervous2 t
    a "{i}{size=-10}Público pesado…{/size}{/i}"
    show gael m nervous2 s
    a "{i}{size=-10}Cofcof{/size}{/i}"
    show gael m normal t
    a "Uhm…ahora que lo pienso, ni siquiera conozco tu nombre."
    show gael m normal s
    player_name "[player_name]. Mi nombre es [player_name]."
    n "..."
    show gael m normal t
    g "Bueno... el mio es Gael, um...mucho gusto"
    player_name "Ah, un gusto."
    show gael m normal s
    n "..."
    show gael m meh s
    n "Qué incómodo."
    n "Supones que es mejor romper el hielo que seguir fingiendo limpiar la barra en silencio."
    menu:
      "Preguntar sobre el trabajo":
            player_name "Uhm, y entonces ¿desde cuando trabajas acá?"
            show gael m normal t
            g "De hecho, es negocio de mi familia. Así que desde hace tiempo supongo. Aunque ahorita estoy estudiando entonces ha sido un poco complicado el manejo."
            show gael m normal s

            menu:
                "Preguntar sobre su carrera":
                    player_name "Oh, y ¿qué estudias?"
                    show gael m normal t
                    g "Veterinaria. "
                    extend "En la Universidad de Miralta."
                    show gael m nervous2 t
                    g "...y creo que descubrí hoy que tú también estudias ahí, ¿verdad?"
                    show gael m normal s
                    player_name "Ah sí, estudió artes plásticas..."
                    n "Paraste en seco."
                    player_name "Aguanta…"
                    n "..."
                    n "..."
                    n "{b}{size=+10}!!!{/size}{/b}"
                    player_name "¡Así que si eras tú!"
                    show gael m nervous2 s at jumper
                    g "{b}{size=+10}!!!{/size}{/b}"
                    show gael m nervous2 t
                    g "Supongo que no soy un bueno ocultando cosas…"
                    extend "ja…"
                    show gael m nervous2 s
                    n "..."

                    menu:
                      "Y… ¿Qué tanto escuchaste?":
                            show gael m normal t
                            g "Bueno, no es como si te estuviera espiando ¿si?, solo estaba ahí pegando volantes y una cosa llevo a otra."
                            show gael m nervous t
                            g "Además que me halago saber que soy tu tipo"
                            show gael m nervous s

      "Preguntar sobre su carrera":
            player_name "Oh, y ¿qué estudias?"
            show gael m normal t
            g "Veterinaria. "
            extend "En la Universidad de Miralta."
            show gael m nervous2 t
            g "...y creo que descubrí hoy que tú también estudias ahí, ¿verdad?"
            show gael m normal s
            player_name "Ah sí, estudió artes plásticas..."
            n "Paraste en seco."
            player_name "Aguanta…"
            n "..."
            n "..."
            n "{b}{size=+10}!!!{/size}{/b}"
            player_name "¡Así que si eras tú!"
            show gael m nervous2 s at jumper
            g "{b}{size=+10}!!!{/size}{/b}"
            show gael m nervous2 t
            g "Supongo que no soy un bueno ocultando cosas…"
            extend "ja…"
            show gael m nervous2 s
            n "..."

            menu:
                      "Y… ¿Qué tanto escuchaste?":
                            show gael m normal t
                            g "Bueno, no es como si te estuviera espiando ¿si?, solo estaba ahí pegando volantes y una cosa llevo a otra."
                            show gael m nervous t
                            g "Además que me halago saber que soy tu tipo"
                            show gael m nervous s

    n "Gael se acerca a ti y te ofrece tu pago del día."
    show gael m normal t
    g "El punto es que... "
    g "Entiendo que este sea un trabajo rápido para tí, pero realmente creo que lo estás haciendo bien. Capaz y hasta ayudes a que este lugar sea más interesante."
    g "Así que…¿qué dices?"
    show gael m normal s

    menu:

     "Mejor renuncias":
         player_name "Lo siento, creo que será mejor hasta aquí."
         show gael m sad s
         n "Tomas las propinas de tu bolsillo."
         player_name "Aún así gracias."
         n "Dejas tu mandil en la barra, y te retiras tranquilamente de la fonda"
         hide gael m sad s with dissolve
         scene Tienda with dissolve
         stop music fadeout 1.0
         n "Caminas por un rato, llegando a una gran papelería."
         n "Tomas de los pasillos algunos materiales para tu proyecto."
         n "Al llegar al cajero, mientras más artículos pasan, te das cuenta que el número de la cuenta incrementa más"
         extend "…y más."
         c "Bueno, va a ser $1550 pesos."
         n "{b}{size=+10}!!!{/size}{/b}"
         n "Tuviste que regresar más de la mitad de las cosas."
         n "No sabes como vas a poder entregar tu proyecto ahora."
         scene black with dissolve
         n "..."
         scene final 1 with dissolve
         n " "
         n "Has conseguido el final 1."
         return
         ####Final 1###

     "Te quedas":
         n "Sonreíste al escuchar sus palabras."
         player_name "Gracias, eres muy convincente ¿lo sabes?"
         hide gael m normal s with dissolve
         n "Continuas trabajando por un rato más. Clientes vienen y van. Parecía que el día sería bueno."
         n "Hasta que todo se arruinó."
         n "Un señor entra y se sienta enojado en una de las mesas de atrás."
         n "Tomas un respiro y te acercas. Sabías que este no sería como los otros clientes."
         show don s with dissolve
         player_name "Buenas tardes. Le entregó el menú-"
         show don t
         c1 "No, no. Dígame cuál es el especial."
         show don s
         player_name "A-Ah, bueno es una ensalada César."
         show don t
         c1 "¿César? ¿Quién es ese tal César?"
         show don s
         player_name "No, no. Así se llama la ensalada que tiene pollo y-"
         show don t
         c1 "¿Ensalada? ¿Acaso me dices gordo?"
         play music "No.mp3"
         show don s
         player_name "Ay, no. Espere, no me referia a eso. Es que ese es nuestro especial del día."
         show don t
         c1 "Creo que se muy bien lo que entendí, y ¡no voy a permitir que me falten el respeto de esta forma!"
         show don s at left with move
         show gael m meh t at right
         g "Disculpe, ¿Está todo bien aquí?"
         show don t at left
         show gael m meh s at right
         c1 "Su mesera resultó ser muy inútil, deberían ser más exigentes con las personas que contratan aquí."
         show don s at left
         player_name "A ver, yo no he hecho nada. Solo le explicaba el menú."
         show don t at left
         c1 "¡Ah! ¿Entonces me estás diciendo mentiroso?"
         show gael m angry s at right
         c1 "Debí suponer que no debía esperar tanto de una pocilga como está."
         show don s at left
         show gael m angry t at right
         g "Bueno, si no le gusta el menú. Hay bastantes lugares a dos cuadras que puede ir, donde sé que habrá comida más acorde a lo que busca."
         show don nerv s at left
         show gael m meh s at right
         c1 "{b}{size=+10}!!!{/size}{/b}"
         show don nerv t at left
         c1 "Ugh, que pésimo servicio…"
         hide don nerv t with dissolve
         show gael m nervous2 t at center with dissolve
         play music "Cafeteria.mp3"
         g "Ugh, con cosas como estas, entiendo el por que piensas en renunciar."
         show gael m normal t
         g "Pero, por favor no te desanimes. Al final todo se resolverá."
         show gael m blush t
         g "Y si no, vendré ayudarte cuantas veces ocupes"
         show gael m normal s
         n "No entendías por qué, pero sus palabras te ayudaron a tranquilizarte."
         n "Tal vez tenga razón. Nada va a ser tan malo."
         hide gael m normal s with dissolve
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_4

label dia_4:
    scene Cuarto with dissolve
    n "Después de un día complicado como el anterior, hoy habías decidido que este sería tranquilo."
    scene Tienda
    play music "Park.mp3"
    n "Con el dinero que habías ganado en tus primeros días de trabajo, estabas lista para darle un buen uso."
    n "Miraste por cada rincón, tachando cada material que habías anotado para tu proyecto."
    player_name "Uhm… este ya, y este también…"
    n "Pasaron unos minutos para que estuvieras frente al mostrador con todo lo necesario."
    play sound "Cash.mp3"
    n "No esperabas que esta mañana fuera tan eficiente."
    scene Park with dissolve
    n "Solo estabas tú y tus pensamientos. Hasta que una voz entre risas interrumpió tu calma."
    play music "No.mp3"
    d "¡Hey tranquilos!"
    show gael d nervous2 s with dissolve
    player_name "¿Gael?"
    hide gael d nervous2 s with dissolve
    n "No puedes ni confirmar tus sospechas, porque observas a un perro correr hacia ti."
    show momo run with dissolve
    play sound "crash.mp3"
    g "¡Ay no! ¿Estas bien-"
    hide momo run with dissolve
    show gael d shock with dissolve
    g "\¿[player_name]?"
    show gael d sad s
    n "Empiezas a recobrar la visión. Mientras sientes al perro lamiendo tu mejilla."
    g "Gael agarra al perro, separándolo de ti."
    show gael d shock
    g "{i}{size=-10}Chin…{/i}{/size}"
    n "Miras a la dirección que Gael ve."
    n "Todos tus materiales... "
    extend "estan arruinados."
    show gael d sad t at left with move
    show momo sad at right
    g "¡Perdóname!"
    n "Gael te ofrece su mano para ayudarte a levantarte."
    g "¿Costaron mucho?"

    menu:
     "No aceptas su mano":
         show gael d shock at left
         n "Golpeas su mano."
         n "Te levantas, sacudiendote el lodo."
         n "En silencio tomás tus materiales arruinados, con el poco orgullo que te queda."
         show gael d sad s at left
         player_name "No necesito la ayuda de alguien tan torpe."
         n "Lo miras de reojo."
         show gael d shock at left
         player_name "De seguro por eso estás en dos trabajos."
         hide gael d shock with dissolve
         hide momo sad with dissolve
         n "Gael te mira sorprendido, mientras tú te retiras del lugar."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_5_normal

     "Aceptas su mano":
         play music "Happyending.mp3"
         hide momo sad with dissolve
         show gael d sad s at center with move
         n "Gael te ayuda a levantarte con cuidado, se le ve bastante apenado."
         player_name "Pues si costaron un poco, ¡pero no te preocupes!"
         show gael d sad t
         g "No creo que haya sido solo “un poco”..."
         show gael d sad t at left with move
         show momo sad at right with dissolve
         g "De verdad lo siento mucho, Momo es bastante fuerte cuando se emociona."
         g "Y cuando menos me di cuenta, su correa se zafó de mi mano."
         show gael d sad s at left
         n "Momo te ve con ojitos de culpa."
         hide gael d sad s with dissolve
         show momo sad at center with move
         player_name "Está bien, son cosas que a veces pasan."
         show momo happy
         n "Comienzas a acariciar la cabeza de Momo para calmarla."
         player_name "Solo esperó poder rescatar algunos de los materiales."
         hide momo happy with dissolve
         show gael d sad s
         n "Gael te ayuda a levantar los materiales."
         show gael d sad t
         g "De verdad lo siento tanto, esperó poder compensartelo."
         hide gael d sad t with dissolve
         show momo happy with dissolve
         n "Los perritos comienzan a jalar las correas en las manos de Gael."
         n "No puedes enojarte con ellos."
         show momo happy at right with move
         show gael d sad s at left
         player_name "Creo que quieren continuar su paseo. Y yo debo regresar a mi casa."
         show gael d sad t at left
         g "Pero-"
         show gael d sad s at left
         n "Solo pudiste sonreir levemente."
         player_name "Nos vemos mañana"
         n "Te despides con tu mano y te alejas del lugar."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_5_good

label dia_5_good:
    scene Uni In with dissolve
    play music "Uni.mp3"
    n "Otro día, una nueva clase con la profesora Marta."
    show marta normal t with dissolve
    m "Bueno jovenes, ¿les parece si damos un pequeño descanso de 15 minutitos?"
    show marta normal s
    n "Algunos de tus compañeros asienten."
    show marta normal t
    m "Bueno, entonces nos vemos más tarde con sus materiales."
    show marta normal s
    player_name "{i}{size=-10}Chin…{/i}{/size}"
    hide marta normal s with dissolve
    scene Uni Out with dissolve
    play music "Park.mp3"
    n "Con pasos preocupados fuiste a la máquina expendedora."
    n "Aunque trataste toda la noche de recuperar algo de tus materiales, simplemente fue imposible."
    n "Lo único que llevaste era un lienzo cubierto de lodo y patitas, unos pinceles y pinturas dañadas."
    n "Nada iba como el plan."
    n "Pasaron algunos de tus compañeros con sus materiales a sus costados. "
    extend "Estaban en perfecto estado."
    player_name "Ugh…"
    n "Te recargas en la máquina decepcionada."
    player_name "¿Y ahora qué voy a hacer…?"
    n "Mientras te lamentas, escuchas unos pasos apurados acercándose."
    show gael s run with dissolve
    play music "Happyending.mp3"
    n "Se detuvo frente a ti por un momento, agarrando aire."
    hide gael s run
    show gael n normal t
    n "Tan pronto volvió en sí, miró contento."
    g "¡Tatan! ¡He llegado a salvarte!"
    show gael n normal s
    n "No pude evitar mirar curiosa aquella escena."
    n "Gael te muestra una bolsa de compras."
    player_name "{b}{size=+10}!!!{/size}{/b}"
    n "Eran los materiales. Estaban perfectos."
    player_name "¿Pero cómo-"
    show gael n normal t
    g "Digamos que no me gusta quedarme de brazos cruzados."
    show gael n sad t
    g "No es justo que todo tu esfuerzo sea en vano, además que fue mi culpa."
    show gael n normal s
    n "No podías creerlo."
    show gael n normal t
    g "Por favor tomalos."
    show gael n blush s
    player_name "Muchas gracias, de verdad gracias"
    n "Escuchas algunas voces cerca."
    show gael n nervous2 t
    g "Ay, debo regresar a mi clase."
    show gael n normal t
    g "¡Nos vemos en el trabajo!"
    hide gael n normal t with dissolve
    n "Te quedas estatica por unos segundos tratando de entender la situación."
    n "Miraste los materiales con una gran sonrisa."
    scene Uni In with dissolve
    play music "Uni.mp3"
    n "Regresaste al salón, esta vez más segura."
    show marta normal s
    n "La profesora se acerca a cada uno. Cuando llega contigo su rostro se le ve sorprendido."
    show marta normal t
    m "¡Vaya, esa es una muy buena marca! Solo debes dejar un poco más de tiempo secar la primera capa si no se estropea."
    m "Esperó ver sus bocetos pronto."
    hide marta normal s with dissolve
    n "La profesora se fue con otro alumno."
    n "El día realmente se arregló. Continuaste tu rutina del día."
    scene Fondita In with dissolve
    play music "happyending.mp3"
    n "Una vez en el trabajo, todos los clientes notaban tu alegría. "
    extend "Fue un buen día de propinas."
    n "Así como no parabas de agradecerle a Gael. Realmente si te salvó de uno."
    scene Cuarto with dissolve
    n "Finalmente, llegaste a tu casa a dormir."
    scene black with dissolve
    stop music fadeout 1.0
    jump dia_6_good

label dia_5_normal:
    scene Uni In with dissolve
    play music "Uni.mp3"
    n "Otro día, una nueva clase con la profesora Marta."
    show marta normal t with dissolve
    m "Bueno jovenes, ¿les parece si damos un pequeño descanso de 15 minutitos?"
    show marta normal s
    n "Algunos de tus compañeros asienten."
    show marta normal t
    m "Bueno, entonces nos vemos más tarde con sus materiales."
    show marta normal s
    player_name "{i}{size=-10}Chin…{/i}{/size}"
    hide marta normal s with dissolve
    scene Uni Out with dissolve
    play music "Park.mp3"
    n "Con pasos preocupados fuiste a la máquina expendedora."
    n "Aunque trataste toda la noche de recuperar algo de tus materiales, simplemente fue imposible."
    n "Lo único que llevaste era un lienzo cubierto de lodo y patitas, unos pinceles y pinturas dañadas."
    n "Nada iba como el plan."
    n "Pero no podías hacer nada más."
    player_name "Ugh… ¿y ahora que voy a hacer? "
    show Uni In with dissolve
    play music "Sadend.mp3"
    n "Resignada regresaste al salón. No iba a ser el mejor proyecto, pero algo era mejor que nada."
    n "Cuando llegas a la clase, miras a los demás con sus materiales en perfecto estado."
    n "Qué vergüenza…"
    show marta question with dissolve
    n "La profesora se acerca a cada uno. Cuando llega contigo su rostro amable muestra desaprobación."
    show marta angry t
    m "[player_name], si no está interesada en la clase puede retirarse."
    show marta angry s
    n "Escuchaste algunas risas y susurros de los demás."
    n "Solo tomas tus cosas y sales de lugar."
    scene Uni Out with dissolve
    player_name "¡Agh! ¡Todo es su culpa!"
    scene Fondita In with dissolve
    n "Continuaste tu rutina del día. Una vez en el trabajo, sentiste las horas interminables."
    n "Cada vez que Gael trataba de acercarse a decir algo solo lo ignorabas."
    n "Los clientes percibieron tu mal humor."
    n "No fue para nada un muy buen día."
    scene Cuarto with dissolve
    n "Finalmente, llegaste a tu casa a dormir."
    scene black with dissolve
    jump dia_6_normal

label dia_6_good:
    scene Uni Out with dissolve
    play music "Park.mp3"
    n "Un nuevo día empezó."
    n "Mientras caminabas a tu salón, Ana Sofi se acercó a ti."
    show asof normal t with dissolve
    s "\¡[player_name]! \¿Cómo estás? Cuéntame sobre tu ligue, \¿todo ha ido bien?"
    show asof normal s
    player_name "¿Ligue? ¿De qué hablas?"
    show asof happy t
    s "Ay, ya sabes del chico de la fondita."
    show asof happy s
    n "No pudiste evitar sonreír al recordarlo."
    player_name "Bueno, supongo que bien."
    hide asof happy s
    show sof happy t
    s "¡Oh oh! ¿[player_name] sonriendo? Eso sí es noticia."
    show sof happy s
    n "Solo pudiste golpear su hombro suavemente. Pero no lo negabas, realmente es nuevo esto en ti."
    show sof happy t
    s "¡Pero por qué lo cortas! ¡Dime qué ha pasado entre ustedes!"
    show sof happy s
    player_name "Bueno, es que han pasado tantas cosas…"
    show sof nervous t
    s "¿En una semana?"
    hide sof nervous t
    show asof happy s
    player_name "Primero, se presentó un cliente de lo más horrendo en el lugar."
    s "Ajá"
    player_name "Se enojó de repente, y me quería hacer bronca. Pero por suerte Gael estaba ahí para ayudarme. Pareciera qué ya es algo normal entre los dos."
    s "¿Por?"
    player_name "Bueno, es que no se queda ahí. Digamos por su culpa se me estropearon los materiales que compré."
    show asof shock s at jumper
    s "{b}{size=+10}!!!{/size}{/b}"
    player_name "¡Fue totalmente un accidente! Resulta que no solo trabaja en la fondita, si no que también cuida perritos muy bonitos, pero a veces son… bueno un poco intensos."
    show asof happy s
    player_name "Pero, él fue muy gentil. Incluso me compró nuevo material para reponer los otros."
    hide asof happy s
    show sof happy t
    s "¡Ay pero qué divino! Yo sabía que mi presentimiento era correcto a este paso vas a tener novio nuevo."
    show sof happy s
    player_name "No se si novio, pero sin duda me estoy llevando muy bien con él."
    n "Entre risas y cuchicheos van juntas al salón."
    hide sof happy t with dissolve
    scene Uni In with dissolve
    play music "Uni.mp3"
    n "En el salón."
    show marta normal t with dissolve
    m "Bueno chicos, ya tenemos que iniciar el proyecto final, porque la exposición se acerca."
    m "Así que ya es tiempo de empezar a considerar el tema de su pintura."
    m "Recuerden que se va contemplar todo en mi evaluación, así que espero que en esta hora de clase puedan revisar o cuestionar lo que quieren comunicar."
    m "Hagan lo que consideren necesario."
    hide marta normal t with dissolve
    player_name "{i}{size=-10}Uhm… un tema…{/i}{/size}"
    n "La profesora parecía notar la confusión en la cara de algunos de sus estudiantes, incluyéndote."
    show marta normal t with dissolve
    m "Bueno, no había pensado usarlos, pero creo que es lo más conveniente."
    n "Comienza a escribir tres propuestas en el pizzarón."
    m "Si consideran necesario, usenlas sin ningún inconveniente."
    n "No dudaste mucho en mirarlas. Parece ser la mejor forma de elegir en este punto."
    n "Elije sabiamente."
    menu:
     "Prefieres dar tu toque a algo existente":
         n "Satisfecha de tu elección, te retiras a tu casa para comenzar a bocetar."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_7_good_1

     "Prefieres dar a conocer tus emociones":
         n "Satisfecha de tu elección, te retiras a tu casa para comenzar a bocetar."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_7_good_2

label dia_6_normal:
    scene Uni Out with dissolve
    play music "Park.mp3"
    n "Un nuevo día empezó."
    n "Mientras caminabas a tu salón, Ana Sofi se acercó a ti."
    show asof normal t with dissolve
    s "\¡[player_name]! \¿Cómo estás? Cuéntame sobre tu ligue, \¿todo ha ido bien?"
    show asof normal s
    player_name "¿Ligue? ¿De qué hablas?"
    show asof happy t
    s "Ay, ya sabes del chico de la fondita."
    show asof shock s
    player_name "\¡Ugh! \¡Ni me lo menciones!"
    show asof shock t
    s "\¿Uhm? \¿Y eso?"
    show asof shock s
    player_name "\¿Por dónde comienzo?"
    player_name "Por su culpa se me estropearon todos los materiales, la profe me echó de su clase y el trabajo solo ha sido cada vez más incómodo."
    player_name "¡UGH! ¡Me urge renunciar!"
    show asof meh
    s "Ay [player_name]..."
    show asof serious t
    s "¿Y ni siquiera se ha disculpado o algo?"
    show asof serious s
    player_name "Ni le he dejado que lo haga. No quiero oír ni una palabra de él."
    show asof serious t
    s "Qué mal [player_name], y yo que creía que ya hasta novio tendrías."
    show asof serious s
    player_name "¡Primero muerta!"
    hide asof serious s with dissolve
    n "A paso enojado, te vas a tu salón."
    scene Uni In with dissolve
    play music "Uni.mp3"
    n "En el salón."
    show marta normal t with dissolve
    m "Bueno chicos, ya tenemos que iniciar el proyecto final, porque la exposición se acerca."
    m "Así que ya es tiempo de empezar a considerar el tema de su pintura."
    m "Recuerden que se va contemplar todo en mi evaluación, así que espero que en esta hora de clase puedan revisar o cuestionar lo que quieren comunicar."
    m "Hagan lo que consideren necesario."
    hide marta normal t with dissolve
    player_name "{i}{size=-10}Uhm… un tema…{/i}{/size}"
    n "Solo mirabas una y otra vez los pocos lápices rotos que tenias a la mano. Tampoco era como si pudieras hacer algo bueno con esto."
    n "…"
    n "Lo mejor será solo fluir con lo que salga."
    n "Un poco desanimada te retiras del salón."
    scene black with dissolve
    stop music fadeout 1.0
    jump dia_7_bad

label dia_7_bad:
    scene Fondita In with dissolve
    play music "No.mp3"
    n "Hoy como cada tarde te toca trabajar en la fondita."
    n "Sin embargo, hoy ha sido un día bastante ajetreado."
    n "Clientes han llegado, llenando el local desde temprano, haciendo que ya ni recuerdes de que mesa era cada orden."
    show man with dissolve
    c2 "¡¿Qué le pasa?! ¡Le dijimos que sin cacahuate!"
    player_name "Ay lo siento mucho, déjeme cambiarlo"
    c2 "Más le vale, y esperamos que sea gratis."
    hide man with dissolve
    show woman with dissolve
    c3 "Disculpe, nos pasa la salsa de cacahuate que le pedimos hace rato."
    hide woman with dissolve
    n "Este es un día muy pesado"
    show gael m sad t with dissolve
    g "¿Oye ocupas ayuda?"
    show gael m sad s

    menu:
     "Te niegas a su ayuda.":
         show gael m shock
         player_name "Ugh… “más ayuda el que no estorba”."
         hide gael m shock with dissolve
         n "Te das la vuelta, solo puedes confiar en ti."
         n "{b}Horas más tarde.{/b}"
         n "No puedes ni confiar en ti."
         n "Ya van dos clientes que se han quejado del servicio, e incluso puesto malas reseñas en gugule."
         n "No vas a durar mucho aquí…"
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_8_bad

     "Aceptas su ayuda.":
         play music "Cafeteria.mp3"
         n "Solo asientes agotada."
         n "Como si fuera magia, Gael empezó a ir en cada mesa y atendió a todos con una sonrisa."
         n "Realmente se notaba su experiencia."
         n "Seguiste sus indicaciones y en unas horas, la tranquilidad volvió a reinar en la fondita."
         n "Con los dos casi solos, sabías que era buen momento para hablar."
         player_name "Uhm, oye…muchas gracias por lo de antes."
         g "Ah no es nada, sigues aprendiendo, es razonable que aún te cueste en momentos."
         n "No pudiste evitar mostrar una ligera sonrisa."
         player_name "y… ¿Tienes consejos para tratar con clientes…uhm…ya sabes-"
         g "\¿Difíciles?"
         g "Bueno, hay que mantenernos tranquilos aunque el cliente parezca como un loco."
         g "Solo si es {b}muy{/b} necesario, debemos ser firmes y pedir que se retiren."
         player_name "¿Cómo lo hiciste hace unos días?"    
         n "Reiste un poco al recordarlo."
         player_name "Parecías una persona diferente con tu cara toda seria."    
         g "¡Oye! ¿Así agradeces que te salve ese día?"
         n "Después de eso, la conversación dejó de ser tan formal."
         n "¿Quién diría que podrías llegar a llevarte bien con Gael?"
         n "El fin de tu turno llegó y mientras caminabas a casa sentiste que tal vez, si podrías llegar a ser un buen amigo aquel chico."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_8_norm_3

label dia_8_bad:
    scene Uni Out with dissolve
    play music "Park.mp3"
    show asof normal s with dissolve
    n "Caminando por la Universidad, te topaste con Sofí."
    show asof normal t
    s "¿Entonces cómo va tu pintura?"

    show asof shock s
    player_name "Terrible, no tengo mucho y con los materiales que tengo no me llega ni una inspiración."
    show asof meh
    s "Ay [player_name]..."
    hide asof meh with dissolve

    scene Fondita In with dissolve
    play music "Fondita"
    n "Después de clases fuiste a trabajar en la fondita. Esta vez no había tanta gente."
    n "Sin embargo, no parabas de notar la mirada constante de una chica."
    show loca miedo with dissolve
    d "..."
    player_name "{b}{size=+10}???{/size}{/b}"
    n ". "
    extend ". "
    extend "."
    show loca meh t
    d "\¡AY POR FAVOR!"
    show loca diuk
    n "La chica se acerca a ti apresuradamente."
    show loca meh t
    d "No captas indirectas \¿o qué?"
    show loca diuk
    player_name "{i}¿Y esta intensa qué?{/i}"
    player_name "Uh… \¿Se te ofrece algo?"
    show loca meh t
    d "¿El chico que trabaja contigo es tu novio?"
    show loca meh s

    player_name "NO"
    player_name "¿Ese tipo? Nah, solo colegas y eso…"
    show loca smile s
    n "La chica suspira alegre. Parece que se quitó un gran peso de encima."
    show loca blush t
    d "¡Ay que alivio! Entonces…"
    d "No te importaría pasarme su número ¿verdad? Es que es taaan lindoo"
    show loca blush s
    n "DIUK"
    player_name "a"

    menu:
     "Dárselo":
         n "Tomas una servilleta cercana y anotas el número de Gael como si nada."
         n "La chica se veía más que contenta."
         show loca blush t
         d "Ay muchas gracias de veras ¡Eres la mejor!"
         n "La chica te mira por unos segundos."
         show loca miedo
         d "Aún así trata de no acercarte tanto a él, \¿oíste?"
         hide loca miedo with dissolve
         n "Así con el papel en sus manos se empezó a alejar de ti."
         player_name "{i}Vaya rara…{/i}"
         n "Gael salió de la cocina y fue a atender la mesa de la chica."
         show loca blush t at left with dissolve
         show gael m nervous2 s at right with dissolve
         n "Parecía tan contenta, que hasta daba miedo."
         n "Pero bueno, ahora es problema de Gael, que lo solucione como pueda."
         hide loca blush t with dissolve
         hide gael m nervous2 s with dissolve
         n "Así el día pasó rápidamente."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_9_bad

     "No dárselo":
         n "Niegas con tu cabeza."
         show loca meh s at jumper
         player_name "Nah, si lo quieres consíguelo por tu cuenta, niña."
         show loca angry s
         n "La chica se le ve muy enfadada."
         show loca meh t
         d "¡¿Cómo te atreves?! Eres una envidiosa, de seguro te gusta, pero qué crees…"
         d "Él conmigo estará mejor."
         show loca angry s
         n "Así la chica regresa a su mesa. No mentiras, se veía muy graciosa enojada."
         hide loca angry s with dissolve
         player_name "{i}Vaya rara…{/i}"
         n "Gael salió de la cocina y fue a atender la mesa de la chica."
         show loca blush t at left with dissolve
         show gael m nervous2 s at right with dissolve
         n "Parecía tan contenta, que hasta daba miedo."
         n "Pero bueno, ahora es problema de Gael, que lo solucione como pueda."
         hide loca blush t with dissolve
         hide gael m nervous2 s with dissolve
         n "Así el día pasó rápidamente."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_9_bad

label dia_9_bad:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    n "Es un nuevo día."
    n "Mañana es la exposición en la galería, por lo que decidiste tomarte toda la mañana para acabar tu pintura."
    n "A pesar de haber tenido días para hacerlo, apenas lo vas a comenzar."
    n "Decidiste que era mejor culpar a los materiales que a tu poca organización por días."
    n "Pero bueno, aún así debes entregar algo."
    player_name "Que sea lo que dios quiera…"

label game_3:
    play music "Park.mp3"
    $ setup_puzzle3()
    call screen reassemble_puzzle3

label dia_9_bad_p2:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    player_name "Bueno… no es mucho, pero es un trabajo honesto."
    n "Ay ajá."
    player_name "Como sea, es hora de trabajar, ya no queda de otra…"
    scene Fondita Out  with dissolve
    play music "Sadend.mp3"
    n "Al llegar a la fondita te das cuenta que Gael está cerrando."
    show gael n sad s with dissolve
    n "Pero apenas son las 2 de la tarde…"
    player_name "¿Gael? ¿Qué significa esto?"
    show gael n sad t
    g "Oh [player_name], uh… bueno."
    show gael n sad s
    n "Parecía tratar de ordenar sus ideas en su cabeza. Era raro verlo tan agobiado, en vez de su tonta sonrisa."
    show gael n sad t
    g "Creo que tendrás que conseguir otro trabajo después de todo."
    show gael n sad s
    player_name "{b}{size=+10}???{/size}{/b}"
    show gael n sad t
    g "La fondita no ha tenido una muy buena recepción. Las reseñas y la gente parece que solo se quejan del servicio, y pues bueno, no es muy bueno para el local ¿sabes?"
    show gael n sad s
    n "Oh…"
    show gael n nervous2 t
    g "Así que, ¡Hey! al menos ya vas a lograr dejar de trabajar aquí"
    show gael n nervous2 s
    player_name "Ha… si…"
    show gael n sad t
    g "Pero no te preocupes, esto no es tu culpa."
    show gael n sad s
    n "Por unos segundos solo parecía haber un silencio incómodo entre ambos."
    n "..."
    n "Espera…"
    n "Esto se debe a…"
    n "Si es…"
    play music "No.mp3"
    player_name "Tienes razón, esto no es mi culpa…"
    show gael n shock at jumper
    player_name "¡Esto es {b}tú{/b} culpa!"
    g "\¿Qué-"
    player_name "¡Por tu culpa los dos nos quedamos sin nada! De seguro atendiste mal a los clientes y por eso es que está pasando esto."
    show gael n angry t
    g "A ver esperate yo-"
    show gael n angry s
    player_name "¡¿En qué estabas pensando?! ¡No te basta con arruinar mi vida! ¡¿sino que también la de tu familia?!"
    show gael n angry t
    g "\¿De qué estás hablando-"
    show gael n angry s
    player_name "Primero mis materiales, tu actitud, tus odiosos clientes que para colmo están obsesionados contigo."
    show gael n sad t
    g "Espera ¿Qué-"
    player_name "{b}¡No me interrumpas!{/b}"
    show gael n shock
    g "..."
    player_name "¡Es que de verdad! ¡¿Cómo puedes ser tan odioso?!"
    show gael n sad s
    n "Suspiras pesadamente, y te das la media vuelta."
    player_name "No me vuelvas a hablar en la vida."
    player_name "Y más te vale que no te aparezcas frente a mi en la Uni."
    player_name "¡AGH!"
    hide gael n sad s with dissolve
    n "Simplemente sujetas bien tu bolso y te vas lejos de ahí."
    scene black with dissolve
    stop music fadeout 1.0
    jump FinalMalo

label FinalMalo:
    scene Gallery with dissolve
    play music "Gallery.mp3"
    n "Después de unas largas semanas, finalmente llegó el día."
    n "Toda tu clase estaba reunida en la galería con sus trabajos listos para exponer."
    n "La profesora Marta incluso se vistió para la ocasión."
    n "Cada alumno tenía que mostrarle sus trabajos antes de exponerlos, así sabrías tu nota final y solo disfrutarías el evento."

    n "O eso harías si no vieras claramente que tu trabajo era el peor del salón."
    player_name "{i}Bueno, la profa no suele ser tan cruel, o eso dicen…{/i}"
    n "Mientras más te acercabas tu ansiedad crecía, y no ayudaba el hecho que la chica frente a ti tenía un trabajo de museo."
    show marta normal t with dissolve
    m "¡La siguiente persona por favor!"
    show marta normal s
    player_name "{i}Hasta acá llegue en la Uni…{/i}"
    n "Con vergüenza mostraste tu pintura a la profesora."
    show marta annoyed
    play music "Sadend.mp3"
    n "No tenías que ser un genio para adivinar que su rostro alegre se volvería uno incrédulo."
    m "[player_name], ¿es enserio? ¿Este es tu trabajo?"
    player_name "…"
    m "Jovencita, tuvo el mismo tiempo y oportunidades que todos aquí presentes y lo único que se le ocurrió hacer ¿fue esto?"
    n "Sentías las miradas de tus compañeros en ti. Sabías que era mala, pero no era tu culpa ¿verdad?"
    player_name "Profesora, entiendame, mis materiales se arruinaron y esto es lo mejor que podía hacer con ellos-"
    m "No se justifique de esa forma. Usted sabe muy bien que los materiales no definen al artista."
    n "Te quedaste en silencio."
    m "No quería creer lo que sus otros profesores hablan de usted, pero veo que tienen razón."
    m "No debía esperar mucho de usted."
    n "La profesora solo te devolvió tu pintura."
    n "Risas, murmullos y miradas."
    scene black with dissolve
    n "Era de esperarse que te reprobara unos días después."
    n "Todo salió mal."
    n "Estas a una materia reprobada de ser expulsada de la carrera, no tienes ni trabajo para sacar aunque sea un poco de dinero."
    n "Todo genuinamente salió mal."
    n "Y todo…"
    player_name "Fue culpa de ese odioso…"
    scene final 2 with dissolve
    n " "
    n "Has conseguido el final malo."
    stop music fadeout 1.0
    return
    ####Final Malo###

label dia_7_good_1:
    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Hoy como cada tarde en los últimos días, te toca trabajar en la fondita."
    n "A pesar de ser un día ajetreado, Gael te ha hecho compañía."
    n "Clientes han llegado, llenando el local desde temprano. Por suerte todo ha fluido tranquilamente."
    n "Después de atender algunas mesas y clientes complicados, finalmente pudiste tomar un descanso."
    n "Aprovechaste unos asientos vacíos en el fondo."
    show gael m normal t with dissolve
    g "¡Hey, aquí estabas!"
    show gael m normal s
    player_name "¿uh? ¿Llegaron más clientes?"
    show gael m blush2 t
    g "¡Oh no, no! Solo quería hablar contigo."
    show gael m normal t
    g "¿Cómo te has sentido estos días? Sé que no es un trabajo tan fácil como puede parecer."
    show gael m normal s
    player_name "Pues…¿bien supongo? Si ha sido algo agotador pero eso no me va a desanimar."
    player_name "Al fin y al cabo, voy a quedarme aquí un rato, entonces…"
    show gael m normal t
    g "Me alegra escuchar eso"
    show gael m nervous2 t
    g "Por un segundo creí que otra vez ibas a querer renunciar."
    show gael m nervous2 s
    n "No pudiste evitar mostrar una ligera sonrisa, realmente sigue pensando en ello."
    n "A pesar de que el silencio era agradable, era mejor sacar un tema."
    menu:
     "Preguntar sobre el trabajo":
         player_name "y… ¿Tienes consejos para tratar con clientes…uhm…ya sabes-"
         show gael m nervous2 t
         g "¿Difíciles?"
         show gael m nervous2 s
         n "Asientes lentamente."
         show gael m normal t
         g "Bueno, hay que mantenernos tranquilos aunque el cliente parezca como un loco."
         show gael m angry t
         g "Solo si es {b}muy{/b} necesario, debemos ser firmes y pedir que se retiren."
         show gael m meh s
         player_name "¿Cómo lo hiciste hace unos días?"  
         show gael m nervous s
         n "Reiste un poco al recordarlo."
         player_name "Parecías una persona diferente con tu cara toda seria." 
         show gael m blush t
         g "¡Oye! ¿Así agradeces que te salve ese día?"
         show gael m blush s
         n "Después de eso, la conversación dejó de ser tan formal."
         n "¿Quién diría que podrías llegar a llevarte bien con Gael?"
         hide gael m blush s with dissolve
         n "El fin de tu turno llegó y mientras caminabas a casa sentiste que tal vez, si podría llegar a ser un buen amigo aquel chico."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_8_norm_1

     "Preguntar sobre los perritos":
         player_name "y… Tienes dos trabajos ¿verdad?"
         show gael m nervous t
         g "Oh, cierto me viste ese día…"
         show gael m nervous s
         player_name "¿En qué trabajas en sí? ¿Paseas perritos, los cuidas o qué?"
         show gael m normal t
         g "Bueno, digamos que son como prácticas pero no exactamente."
         show gael m normal s
         player_name "{b}{size=+10}???{/size}{/b}"
         show gael m normal t
         g "Conozco a un doctor que tiene su clínica cerca, siempre ha llamado mi atención los animales desde pequeño y él siempre fue muy amable introduciéndome al campo."
         show gael m nervous t
         g "De hecho hasta me echa la mano para estudiar para mis exámenes."
         show gael m blush t
         g "Regresando al trabajo, entre platica y platica sacó el tema de que quería empezar un servicio extra. Una cosa llevó a la otra y ahora paseo perritos entre semana."
         g "Sirve para practicar y el dinero extra siempre es bien recibido."
         show gael m blush s
         n "Era agradable ver a Gael tan emocionado, normalmente solo hablaban de la fondita. Parece que genuinamente disfruta su carrera."
         player_name "Entonces paseas muchos perritos, me pregunto si tendrán uno favorito."
         show gael m nervous2 t
         g "¡Hey, eso es como poner a decidir quién es tu hijo favorito!"
         show gael m nervous2 s
         g "..."
         show gael m normal t
         g "Aunque tal vez sí tenga…"
         show gael m normal s
         player_name "¡Dime, dime!"
         show gael m nervous2 t
         g "Si somos honestos, ya la conoces. Se llama Momo, y bueno, es la perrita que te tiro esa vez."
         show gael m nervous2 s
         player_name "a"
         show gael m nervous2 t
         g "¡Pero te juro que no es así!"
         g "{i}{size=-10}no siempre…{/i}{/size}"
         show gael m nervous2 s
         g "Me gustaría que pudieras conocerla mejor, debe limpiar su nombre contigo. De verdad que es muy linda."
         show gael m blush t
         player_name "Sí me gustaría, pero no quiero molestarte con ello-"
         g "¡No! \¿Sabes qué? Ya está decidido. Buscame al final del turno en el parque, ahí se va a arreglar todo."
         show gael m blush s
         player_name "Espera qué-"
         show gael m blush t
         g "¡Nos vemos allá!"
         hide gael m blush t with dissolve
         n "Tan pronto como acabo de decir aquello, desapareció del lugar."
         n "Bueno, un descanso siempre es útil. Además son perritos ¿Cómo decir no?"
         play music "Park.mp3"
         scene Park with dissolve
         show gael d normal s
         n "Llegaste a la hora citada, y sorprendentemente si estaba Gael con un grupo de 5 perritos."
         show gael d blush s
         n "Tan pronto te miró, sonrió emocionado haciéndote señas para que te acercaras."
         n "Carraspeo por un segundo y como si fuera un papá orgulloso comenzó a hablarte de cada perrito."
         n "Pero claro, que se tomó su tiempo hablando de Momo. Quien no dudo de mostrarte su arrepentimiento."
         n "Realmente fue un rato agradable. Todos los perritos eran muy amorosos y tranquilos, que ni te diste cuenta de cómo pasó el tiempo."
         n "Con pesar, comenzaste a despedirte de todos los perritos. Dándole mimos extra a Momo sin querer. No querías, pero sabías que tenías que irte."
         show gael d blush t
         play music "Happyending.mp3"
         g "Gracias por venir, esperó que te hayas divertido."
         show gael d blush s
         player_name "Si, lo hice"
         show gael d blush t
         g "Supongo que nos vemos mañana."
         show gael d blush s
         n "Ibas a decir algo más pero preferiste no hacerlo."
         hide gael d blush s with dissolve
         n "Te despediste con una ligera sonrisa y empezaste a caminar a tu casa."
         n "Tal vez era momento de aceptar que Gael nunca fue tan malo como pensaste alguna vez."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_8_good_1

label dia_7_good_2:
    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Hoy como cada tarde en los últimos días, te toca trabajar en la fondita."
    n "A pesar de ser un día ajetreado, Gael te ha hecho compañía."
    n "Clientes han llegado, llenando el local desde temprano. Por suerte todo ha fluido tranquilamente."
    n "Después de atender algunas mesas y clientes complicados, finalmente pudiste tomar un descanso."
    n "Aprovechaste unos asientos vacíos en el fondo."
    show gael m normal t with dissolve
    g "¡Hey, aquí estabas!"
    show gael m normal s
    player_name "¿uh? ¿Llegaron más clientes?"
    show gael m blush2 t
    g "¡Oh no, no! Solo quería hablar contigo."
    show gael m normal t
    g "¿Cómo te has sentido estos días? Sé que no es un trabajo tan fácil como puede parecer."
    show gael m normal s
    player_name "Pues…¿bien supongo? Si ha sido algo agotador pero eso no me va a desanimar."
    player_name "Al fin y al cabo, voy a quedarme aquí un rato, entonces…"
    show gael m normal t
    g "Me alegra escuchar eso"
    show gael m nervous2 t
    g "Por un segundo creí que otra vez ibas a querer renunciar."
    show gael m nervous2 s
    n "No pudiste evitar mostrar una ligera sonrisa, realmente sigue pensando en ello."
    n "A pesar de que el silencio era agradable, era mejor sacar un tema."
    menu:
     "Preguntar sobre el trabajo":
         player_name "y… ¿Tienes consejos para tratar con clientes…uhm…ya sabes-"
         show gael m nervous2 t
         g "¿Difíciles?"
         show gael m nervous2 s
         n "Asientes lentamente."
         show gael m normal t
         g "Bueno, hay que mantenernos tranquilos aunque el cliente parezca como un loco."
         show gael m angry t
         g "Solo si es {b}muy{/b} necesario, debemos ser firmes y pedir que se retiren."
         show gael m meh s
         player_name "¿Cómo lo hiciste hace unos días?"  
         show gael m nervous s
         n "Reiste un poco al recordarlo."
         player_name "Parecías una persona diferente con tu cara toda seria." 
         show gael m blush t
         g "¡Oye! ¿Así agradeces que te salve ese día?"
         show gael m blush s
         n "Después de eso, la conversación dejó de ser tan formal."
         n "¿Quién diría que podrías llegar a llevarte bien con Gael?"
         hide gael m blush s with dissolve
         n "El fin de tu turno llegó y mientras caminabas a casa sentiste que tal vez, si podrías llegar a ser un buen amigo aquel chico."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_8_norm_2

     "Preguntar sobre los perritos":
         player_name "y… Tienes dos trabajos ¿verdad?"
         show gael m nervous t
         g "Oh, cierto me viste ese día…"
         show gael m nervous s
         player_name "¿En qué trabajas en sí? ¿Paseas perritos, los cuidas o qué?"
         show gael m normal t
         g "Bueno, digamos que son como prácticas pero no exactamente."
         show gael m normal s
         player_name "{b}{size=+10}???{/size}{/b}"
         show gael m normal t
         g "Conozco a un doctor que tiene su clínica cerca, siempre ha llamado mi atención los animales desde pequeño y él siempre fue muy amable introduciéndome al campo."
         show gael m nervous t
         g "De hecho hasta me echa la mano para estudiar para mis exámenes."
         show gael m blush t
         g "Regresando al trabajo, entre platica y platica sacó el tema de que quería empezar un servicio extra. Una cosa llevó a la otra y ahora paseo perritos entre semana."
         g "Sirve para practicar y el dinero extra siempre es bien recibido."
         show gael m blush s
         n "Era agradable ver a Gael tan emocionado, normalmente solo hablaban de la fondita. Parece que genuinamente disfruta su carrera."
         player_name "Entonces paseas muchos perritos, me pregunto si tendrás uno favorito."
         show gael m nervous2 t
         g "¡Hey, eso es como poner a decidir quién es tu hijo favorito!"
         show gael m nervous2 s
         g "..."
         show gael m normal t
         g "Aunque tal vez sí tenga…"
         show gael m normal s
         player_name "¡Dime, dime!"
         show gael m nervous2 t
         g "Si somos honestos, ya la conoces. Se llama Momo, y bueno, es la perrita que te tiro esa vez."
         show gael m nervous2 s
         player_name "a"
         show gael m nervous2 t
         g "¡Pero te juro que no es así!"
         g "{i}{size=-10}no siempre…{/i}{/size}"
         show gael m nervous2 s
         g "Me gustaría que pudieras conocerla mejor, debe limpiar su nombre contigo. De verdad que es muy linda."
         show gael m blush t
         player_name "Sí me gustaría, pero no quiero molestarte con ello-"
         g "¡No! \¿Sabes qué? Ya está decidido. Buscame al final del turno en el parque, ahí se va a arreglar todo."
         show gael m blush s
         player_name "Espera qué-"
         show gael m blush t
         g "¡Nos vemos allá!"
         hide gael m blush t with dissolve
         n "Tan pronto como acabo de decir aquello, desapareció del lugar."
         n "Bueno, un descanso siempre es útil. Además son perritos ¿Cómo decir no?"
         play music "Park.mp3"
         scene Park with dissolve
         show gael d normal s
         n "Llegaste a la hora citada, y sorprendentemente si estaba Gael con un grupo de 5 perritos."
         show gael d blush s
         n "Tan pronto te miró, sonrió emocionado haciéndote señas para que te acercaras."
         n "Carraspeo por un segundo y como si fuera un papá orgulloso comenzó a hablarte de cada perrito."
         n "Pero claro, que se tomó su tiempo hablando de Momo. Quien no dudo de mostrarte su arrepentimiento."
         n "Realmente fue un rato agradable. Todos los perritos eran muy amorosos y tranquilos, que ni te diste cuenta de cómo pasó el tiempo."
         n "Con pesar, comenzaste a despedirte de todos los perritos. Dándole mimos extra a Momo sin querer. No querías, pero sabías que tenías que irte."
         show gael d blush t
         play music "Happyending.mp3"
         g "Gracias por venir, esperó que te hayas divertido."
         show gael d blush s
         player_name "Si, lo hice"
         show gael d blush t
         g "Supongo que nos vemos mañana."
         show gael d blush s
         n "Ibas a decir algo más pero preferiste no hacerlo."
         hide gael d blush s with dissolve
         n "Te despediste con una ligera sonrisa y empezaste a caminar a tu casa."
         n "Tal vez era momento de aceptar que Gael nunca fue tan malo como pensaste alguna vez."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_8_good_2

label dia_8_norm_1:
    scene Uni Out with dissolve
    play music "Park.mp3"
    show asof normal s with dissolve
    n "Caminando por la Universidad, te topaste con Sofí."
    show asof normal t
    s "¿Entonces cómo va tu pintura?"

    show asof normal s
    player_name "Bastante bien, creo. Ya tengo un boceto y esperó mañana acabarlo."
    show asof normal t
    s "Me alegra escuchar eso [player_name], esperó ser la primera en verlo."
    hide asof normal t with dissolve
    
    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Después de clases fuiste a trabajar en la fondita. Esta vez no había tanta gente."
    n "Sin embargo, no parabas de notar la mirada constante de una chica."
    show loca miedo with dissolve
    d "..."
    player_name "{b}{size=+10}???{/size}{/b}"
    n ". "
    extend ". "
    extend "."
    show loca meh t
    d "\¡AY POR FAVOR!"
    show loca diuk
    n "La chica se acerca a ti apresuradamente."
    show loca meh t
    d "No captas indirectas \¿o qué?"
    show loca diuk
    player_name "{i}¿Y esta intensa qué?{/i}"
    player_name "Uh… \¿Se te ofrece algo?"
    show loca meh t
    d "¿El chico que trabaja contigo es tu novio?"
    show loca meh s

    player_name "¡Oh no! Solo somos amigos."
    show loca smile s
    n "La chica suspira alegre. Parece que se quitó un gran peso de encima."
    d "¡Ay que alivio! Entonces…"
    d "No te importaría pasarme su número ¿verdad? Es que es taaan lindoo"
    n "Reíste por su comentario. Gael si era algo guapo, tiene sentido que alguien lo busque. Pero no sabías que tan correcto es entregar su número a una extraña."

    menu:
     "Dárselo":
         player_name "{i}Bueno, una ayudita no es mala de vez en cuando.{/i}"
         n "Tomas una servilleta cercana y anotas el número de Gael."
         n "La chica se veía más que contenta."
         show loca blush t
         d "Ay muchas gracias de veras ¡Eres la mejor!"
         n "La chica te mira por unos segundos."
         show loca miedo
         d "Aún así trata de no acercarte tanto a él, \¿oíste?"
         hide loca miedo with dissolve
         n "Así con el papel en sus manos se empezó a alejar de ti."
         player_name "{i}Vaya rara…{/i}"
         n "Gael salió de la cocina y fue a atender la mesa de la chica."
         show loca blush t at left with dissolve
         show gael m nervous2 s at right with dissolve
         n "Parecía tan contenta, que hasta daba miedo."
         n "Pero bueno, solo podías esperar a ver como eso resulta"
         n "Tal vez, hasta se hagan pareja. Sería curioso ver eso."
         hide loca blush t with dissolve
         hide gael m nervous2 s with dissolve
         n "Así el día pasó rápidamente."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_9_norm_1

     "No dárselo":
         n "Niegas con tu cabeza."
         show loca meh s at jumper
         player_name "No creo que sea correcto que te de su información, así no más."
         show loca angry s
         n "La chica se le ve muy enfadada."
         show loca meh t
         d "\¡\¿Uh?! Eres una envidiosa, de seguro te gusta, pero qué crees…"
         d "Él conmigo estará mejor."
         show loca angry s
         n "Así la chica regresa a su mesa. No mentiras, se veía muy graciosa enojada."
         hide loca angry s with dissolve
         player_name "{i}Vaya si es algo rara…{/i}"
         n "Gael salió de la cocina y fue a atender la mesa de la chica."
         show loca blush t at left with dissolve
         show gael m nervous2 s at right with dissolve
         n "Parecía tan contenta, que hasta daba miedo."
         n "Pero bueno, solo podías esperar a ver como eso resulta"
         n "Tal vez, hasta se hagan pareja. Sería curioso ver eso."
         hide loca blush t with dissolve
         hide gael m nervous2 s with dissolve
         n "Así el día pasó rápidamente."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_9_norm_1

label dia_8_norm_2:
    scene Uni Out with dissolve
    play music "Park.mp3"
    show asof normal s with dissolve
    n "Caminando por la Universidad, te topaste con Sofí."
    show asof normal t
    s "¿Entonces cómo va tu pintura?"

    show asof normal s
    player_name "Bastante bien, creo. Ya tengo un boceto y esperó mañana acabarlo."
    show asof normal t
    s "Me alegra escuchar eso [player_name], esperó ser la primera en verlo."
    hide asof normal t with dissolve
    
    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Después de clases fuiste a trabajar en la fondita. Esta vez no había tanta gente."
    n "Sin embargo, no parabas de notar la mirada constante de una chica."
    show loca miedo with dissolve
    d "..."
    player_name "{b}{size=+10}???{/size}{/b}"
    n ". "
    extend ". "
    extend "."
    show loca meh t
    d "\¡AY POR FAVOR!"
    show loca diuk
    n "La chica se acerca a ti apresuradamente."
    show loca meh t
    d "No captas indirectas \¿o qué?"
    show loca diuk
    player_name "{i}¿Y esta intensa qué?{/i}"
    player_name "Uh… \¿Se te ofrece algo?"
    show loca meh t
    d "¿El chico que trabaja contigo es tu novio?"
    show loca meh s

    player_name "¡Oh no! Solo somos amigos."
    show loca smile s
    n "La chica suspira alegre. Parece que se quitó un gran peso de encima."
    d "¡Ay que alivio! Entonces…"
    d "No te importaría pasarme su número ¿verdad? Es que es taaan lindoo"
    n "Reíste por su comentario. Gael si era algo guapo, tiene sentido que alguien lo busque. Pero no sabías que tan correcto es entregar su número a una extraña."

    menu:
     "Dárselo":
         player_name "{i}Bueno, una ayudita no es mala de vez en cuando.{/i}"
         n "Tomas una servilleta cercana y anotas el número de Gael."
         n "La chica se veía más que contenta."
         show loca blush t
         d "Ay muchas gracias de veras ¡Eres la mejor!"
         n "La chica te mira por unos segundos."
         show loca miedo
         d "Aún así trata de no acercarte tanto a él, \¿oíste?"
         hide loca miedo with dissolve
         n "Así con el papel en sus manos se empezó a alejar de ti."
         player_name "{i}Vaya rara…{/i}"
         n "Gael salió de la cocina y fue a atender la mesa de la chica."
         show loca blush t at left with dissolve
         show gael m nervous2 s at right with dissolve
         n "Parecía tan contenta, que hasta daba miedo."
         n "Pero bueno, solo podías esperar a ver como eso resulta"
         n "Tal vez, hasta se hagan pareja. Sería curioso ver eso."
         hide loca blush t with dissolve
         hide gael m nervous2 s with dissolve
         n "Así el día pasó rápidamente."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_9_norm_2

     "No dárselo":
         n "Niegas con tu cabeza."
         show loca meh s at jumper
         player_name "No creo que sea correcto que te de su información, así no más."
         show loca angry s
         n "La chica se le ve muy enfadada."
         show loca meh t
         d "\¡\¿Uh?! Eres una envidiosa, de seguro te gusta, pero qué crees…"
         d "Él conmigo estará mejor."
         show loca angry s
         n "Así la chica regresa a su mesa. No mentiras, se veía muy graciosa enojada."
         hide loca angry s with dissolve
         player_name "{i}Vaya si es algo rara…{/i}"
         n "Gael salió de la cocina y fue a atender la mesa de la chica."
         show loca blush t at left with dissolve
         show gael m nervous2 s at right with dissolve
         n "Parecía tan contenta, que hasta daba miedo."
         n "Pero bueno, solo podías esperar a ver como eso resulta"
         n "Tal vez, hasta se hagan pareja. Sería curioso ver eso."
         hide loca blush t with dissolve
         hide gael m nervous2 s with dissolve
         n "Así el día pasó rápidamente."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_9_norm_2

label dia_8_norm_3:
    scene Uni Out with dissolve
    play music "Park.mp3"
    show asof normal s with dissolve
    n "Caminando por la Universidad, te topaste con Sofí."
    show asof normal t
    s "¿Entonces cómo va tu pintura?"

    show asof normal s
    player_name "Bastante bien, creo. Ya tengo un boceto y esperó mañana acabarlo."
    show asof normal t
    s "Me alegra escuchar eso [player_name], esperó ser la primera en verlo."
    hide asof normal t with dissolve
    
    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Después de clases fuiste a trabajar en la fondita. Esta vez no había tanta gente."
    n "Sin embargo, no parabas de notar la mirada constante de una chica."
    show loca miedo with dissolve
    d "..."
    player_name "{b}{size=+10}???{/size}{/b}"
    n ". "
    extend ". "
    extend "."
    show loca meh t
    d "\¡AY POR FAVOR!"
    show loca diuk
    n "La chica se acerca a ti apresuradamente."
    show loca meh t
    d "No captas indirectas \¿o qué?"
    show loca diuk
    player_name "{i}¿Y esta intensa qué?{/i}"
    player_name "Uh… \¿Se te ofrece algo?"
    show loca meh t
    d "¿El chico que trabaja contigo es tu novio?"
    show loca meh s

    player_name "¡Oh no! Solo somos amigos."
    show loca smile s
    n "La chica suspira alegre. Parece que se quitó un gran peso de encima."
    d "¡Ay que alivio! Entonces…"
    d "No te importaría pasarme su número ¿verdad? Es que es taaan lindoo"
    n "Reíste por su comentario. Gael si era algo guapo, tiene sentido que alguien lo busque. Pero no sabías que tan correcto es entregar su número a una extraña."

    menu:
     "Dárselo":
         player_name "{i}Bueno, una ayudita no es mala de vez en cuando.{/i}"
         n "Tomas una servilleta cercana y anotas el número de Gael."
         n "La chica se veía más que contenta."
         show loca blush t
         d "Ay muchas gracias de veras ¡Eres la mejor!"
         n "La chica te mira por unos segundos."
         show loca miedo
         d "Aún así trata de no acercarte tanto a él, \¿oíste?"
         hide loca miedo with dissolve
         n "Así con el papel en sus manos se empezó a alejar de ti."
         player_name "{i}Vaya rara…{/i}"
         n "Gael salió de la cocina y fue a atender la mesa de la chica."
         show loca blush t at left with dissolve
         show gael m nervous2 s at right with dissolve
         n "Parecía tan contenta, que hasta daba miedo."
         n "Pero bueno, solo podías esperar a ver como eso resulta"
         n "Tal vez, hasta se hagan pareja. Sería curioso ver eso."
         hide loca blush t with dissolve
         hide gael m nervous2 s with dissolve
         n "Así el día pasó rápidamente."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_9_norm_3

     "No dárselo":
         n "Niegas con tu cabeza."
         show loca meh s at jumper
         player_name "No creo que sea correcto que te de su información, así no más."
         show loca angry s
         n "La chica se le ve muy enfadada."
         show loca meh t
         d "\¡\¿Uh?! Eres una envidiosa, de seguro te gusta, pero qué crees…"
         d "Él conmigo estará mejor."
         show loca angry s
         n "Así la chica regresa a su mesa. No mentiras, se veía muy graciosa enojada."
         hide loca angry s with dissolve
         player_name "{i}Vaya si es algo rara…{/i}"
         n "Gael salió de la cocina y fue a atender la mesa de la chica."
         show loca blush t at left with dissolve
         show gael m nervous2 s at right with dissolve
         n "Parecía tan contenta, que hasta daba miedo."
         n "Pero bueno, solo podías esperar a ver como eso resulta"
         n "Tal vez, hasta se hagan pareja. Sería curioso ver eso."
         hide loca blush t with dissolve
         hide gael m nervous2 s with dissolve
         n "Así el día pasó rápidamente."
         scene black with dissolve
         stop music fadeout 1.0
         jump dia_9_norm_3

label dia_9_norm_1:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    n "Es un nuevo día."
    n "Mañana es la exposición en la galería, por lo que decidiste tomarte toda la mañana para acabar tu pintura."
    
    n "Trazos, pinceladas y mucha pintura en tus brazos. Sin duda, fue toda una experiencia."
    n "Fue bastante grato ver como tu idea cobraba forma."
    jump game_1_n

label dia_9_norm_2:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    n "Es un nuevo día."
    n "Mañana es la exposición en la galería, por lo que decidiste tomarte toda la mañana para acabar tu pintura."
    
    n "Trazos, pinceladas y mucha pintura en tus brazos. Sin duda, fue toda una experiencia."
    n "Fue bastante grato ver como tu idea cobraba forma."

    jump game_2_n

label game_1_n:
    play music "Park.mp3"
    $ setup_puzzle1()
    call screen reassemble_puzzle1

label game_2_n:
    play music "Park.mp3"
    $ setup_puzzle2()
    call screen reassemble_puzzle2

label dia_9_norm1_p2:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    show p1 with dissolve
    player_name "¡Y listo!"
    n "Después de observar con orgullo tu obra, miraste el desastre que te rodeaba."
    hide p1 with dissolve
    n "Así que solo quedaba aprovechar el día de descanso hasta el final."
    scene black with dissolve
    jump final_norm

label dia_9_norm2_p2:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    show p2 with dissolve
    player_name "¡Y listo!"
    n "Después de observar con orgullo tu obra, miraste el desastre que te rodeaba."
    hide p2 with dissolve
    n "Así que solo quedaba aprovechar el día de descanso hasta el final."
    scene black with dissolve
    jump final_norm

label dia_9_norm_3:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    n "Es un nuevo día."
    n "Mañana es la exposición en la galería, por lo que decidiste tomarte toda la mañana para acabar tu pintura." 
    n "Trazos, pinceladas y mucha pintura en tus brazos. Sin duda, fue toda una experiencia."
    n "A pesar de tus dudas con los materiales que tenías. "
    extend "Fue bastante grato ver como tu idea cobraba forma."
    player_name "¡Y listo!"
    n "Después de observar con orgullo tu obra, miraste el desastre que te rodeaba."
    n "Así que solo quedaba aprovechar el día de descanso hasta el final."
    jump final_norm

label final_norm:
    scene Gallery with dissolve
    play music "Gallery.mp3"
    n "Después de unas largas semanas, finalmente llegó el día."
    n "Toda tu clase estaba reunida en la galería con sus trabajos listos para exponer."
    n "La profesora Marta incluso se vistió para la ocasión."
    n "Cada alumno tenía que mostrarle sus trabajos antes de exponerlos, así sabrías tu nota final y solo disfrutarías el evento."
    n "Aún así, no dejabas de sentir nervios en cada paso que te acercabas a la profesora."
    n "Incluso Sofí te había dicho que estaba bien, además la profesora nunca había sido cruel al revisar."
    n "Sin embargo, una notificación te sacó de tus pensamientos."
    n "Era Gael."
    nvl_narrator "Tienes nuevos mensajes"
    g_nvl "Hoy es tu presentación ¿verdad?"
    g_nvl "Se que puedes, has trabajado mucho. ¡Ánimo!"
    g_nvl "{image=piolin.png}"
    n "Sabías que le tenías que agradecer más tarde, porque sin duda te sacó de la ansiedad."
    n "Lo malo, es que ahora debías evitar reírte en plena galería por sus imágenes de señora."
    show marta normal t with dissolve
    m "¡La siguiente persona por favor!"
    show marta normal s
    n "Era hora. Más relajada, le mostraste tu pintura."
    show marta normal t
    m "¡Vaya! Sabía que no me iba decepcionar jovencita."
    m "No quería creer lo que sus otros profesores hablan de usted, pero veo que tienen razón."
    m "Realmente es muy bueno su trabajo. Se que va a ser uno de los que más luzcan hoy."
    show marta normal s
    n "No podías ocultar tu sonrisa."
    show marta normal s with dissolve
    n "Disfrutaste del evento y toda la noche muchos halagaron tu trabajo."
    scene black with dissolve
    n "Realmente todo salió bien."
    n "El proyecto, el trabajo y ahora hasta un nuevo amigo."
    n "Sin duda, un buen comienzo."
    scene final 3 with dissolve
    n " "
    n "Has conseguido el final neutral."
    stop music fadeout 1.0
    return
    ####Final Neutral###

label dia_8_good_1:
    scene Uni Out with dissolve
    play music "Park.mp3"
    show asof normal s with dissolve
    n "Caminando por la Universidad, te topaste con Sofí."
    show asof normal t
    s "¿Entonces cómo va tu pintura?"
    show asof normal s
    player_name "Bastante bien, creo. Ya tengo un boceto y esperó mañana acabarlo."
    show asof normal t
    s "Me alegra escuchar eso [player_name], esperó ser la primera en verlo."

    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Después de clases fuiste a trabajar en la fondita. Esta vez no había tanta gente."
    n "Sin embargo, no parabas de notar la mirada constante de una chica."
    show loca miedo with dissolve
    d "..."
    player_name "{b}{size=+10}???{/size}{/b}"
    n ". "
    extend ". "
    extend "."
    show loca meh t
    d "\¡AY POR FAVOR!"
    show loca diuk
    n "La chica se acerca a ti apresuradamente."
    show loca meh t
    d "No captas indirectas \¿o qué?"
    show loca diuk
    player_name "{i}¿Y esta intensa qué?{/i}"
    player_name "Uh… \¿Se te ofrece algo?"
    show loca meh t
    d "¿El chico que trabaja contigo es tu novio?"
    show loca meh s
    player_name "Mmm, ¿Por qué preguntas?"
    show loca meh t
    d "Ugh, solo quiero saber ¿si?"
    show loca meh s
    n "La chica suspira y te mira fijamente."
    show loca meh t
    d "Bueno, si no lo es…"
    show loca blush t
    d "…No te importaría pasarme su número ¿verdad? Es que es taaan lindoo"
    show loca blush s
    n "No creías que la conservación fuera ahí. Sabías que Gael era guapo, era de esperarse que alguien se fijará en él."
    n "Pero no entendías el porqué te sentías algo molesta."

    menu:
     "Dárselo":
            play music "Sadend.mp3"
            player_name "{i}Bueno, al final del día no soy nada de él, no debería tomarle importancia.{/i}"
            n "Tomas una servilleta cercana y anotas el número de Gael con cierta duda."
            n "La chica se veía más que contenta."
            show loca blush t
            d "Ay muchas gracias de veras ¡Eres la mejor!"
            n "La chica te mira por unos segundos."
            show loca miedo
            d "En fin, no te acerques tanto a él, \¿oíste?"
            hide loca miedo with dissolve
            n "Así con el papel en sus manos se empezó a alejar de ti."
            player_name "..."
            n "La chica se acercó al mostrador donde Gael se encontraba."
            scene closer with dissolve
            show gael s2 nervous with dissolve
            n "Parecía tan contenta, que hasta daba miedo."
            n "La chica parece tratar de conversar con él."
            player_name "{i}De cierto modo, se ve bien juntos, o bueno, Gael se ve bien en pareja.{/i}"
            player_name "..."
            player_name "{i}Aunque se ve incómodo… Tal vez debería acercarme…{/i}"
            player_name "{i}No, no. Él está bien.{/i}"
            d "Entonces \¿Te gustaría salir después de tu turno?"
            g "Uh…"
            player_name "..."
            player_name "{i}Tal vez soy yo la que se siente mal.{/i}"
            stop music fadeout 1.0
            show gael s2 surpised
            player_name "{b}{size=+10}!!!{/size}{/b}"
            show gael s2 blush 1
            n " "
            show gael s2 blush 2
            g "Cough"
            g "Agradezco tu invitación, pero tendré que negarme."
            d "\¡P-Pero!"
            g "Lo siento."
            scene Fondita In with dissolve
            hide gael s2 blush 2 with dissolve
            play music "Happyending.mp3"
            n "La chica se veía algo herida"
            n "No entendías, pero sentiste un gran alivio cuando cruzó la puerta."
            show gael m nervous2 t with dissolve
            g "Eso fue raro ¿verdad?"
            show gael m nervous2 s
            n "Solo pudiste asentir."
            n "Nunca habías sentido un silencio tan extenso."

            menu:
             "Preguntar":
                    show gael m nervous s
                    player_name "Gael, ¿Por qué te negaste a la cita?"
                    show gael m nervous t
                    g "Ah, este...bueno, verás..."
                    show gael m blush t
                    g "Siento que no es correcto aceptar una cita cuando me gusta alguien más…"
                    player_name "\¿Q-Qué?"
                    show gael m nervous t
                    g "Uhm, ya casi se acaba nuestro turno… así que mejor voy por allá"
                    show gael m nervous s
                    g "{b}{size=-10}Casi la riego abriendo mi bocota{/size}{/b}"
                    hide gael m nervous s with dissolve
                    n "No sabías cómo digerir todo lo que había pasado hoy."
                    n "Sin duda, este día sería uno largo."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump dia_9_good_1

             "Preguntar":
                    show gael m nervous s
                    player_name "Gael, ¿Por qué te negaste a la cita?"
                    show gael m nervous t
                    g "Ah, este...bueno, verás..."
                    show gael m blush t
                    g "Siento que no es correcto aceptar una cita cuando me gusta alguien más…"
                    player_name "\¿Q-Qué?"
                    show gael m nervous t
                    g "Uhm, ya casi se acaba nuestro turno… así que mejor voy por allá"
                    show gael m nervous s
                    g "{b}{size=-10}Casi la riego abriendo mi bocota{/size}{/b}"
                    hide gael m nervous s with dissolve
                    n "No sabías cómo digerir todo lo que había pasado hoy."
                    n "Sin duda, este día sería uno largo."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump dia_9_good_1


     "No dárselo":
            n "Niegas con tu cabeza. No era correcto y honestamente no querías dárselo."
            show loca meh s at jumper
            player_name "No creo que sea correcto que te de su información, así no más."
            show loca angry s
            n "La chica se le ve muy enfadada."
            show loca meh t
            d "\¡\¿Uh?! Eres una envidiosa, es obvio que te gusta, pero qué crees…"
            d "Eso no me va a impedir ir tras él, ¿escuchaste?"
            show loca angry s
            player_name "..."
            hide loca angry s with dissolve
            n "La chica se acercó al mostrador donde Gael se encontraba."
            scene closer with dissolve
            show gael s2 nervous with dissolve
            n "Parecía tan contenta, que hasta daba miedo."
            n "La chica parece tratar de conversar con él."
            player_name "{i}De cierto modo, se ve bien juntos, o bueno, Gael se ve bien en pareja.{/i}"
            player_name "..."
            player_name "{i}Aunque se ve incómodo… Tal vez debería acercarme…{/i}"
            player_name "{i}No, no. Él está bien.{/i}"
            d "Entonces \¿Te gustaría salir después de tu turno?"
            g "Uh…"
            player_name "..."
            player_name "{i}Tal vez soy yo la que se siente mal.{/i}"
            show gael s2 surpised
            player_name "{b}{size=+10}!!!{/size}{/b}"
            show gael s2 blush 1
            n " "
            show gael s2 blush 2
            g "Cough"
            g "Agradezco tu invitación, pero tendré que negarme."
            d "\¡P-Pero!"
            g "Lo siento."
            scene Fondita In with dissolve
            hide gael s2 blush 2 with dissolve
            play music "Happyending.mp3"
            n "La chica se veía algo herida"
            n "No entendías, pero sentiste un gran alivio cuando cruzó la puerta."
            show gael m nervous2 t with dissolve
            g "Eso fue raro ¿verdad?"
            show gael m nervous2 s
            n "Solo pudiste asentir."
            n "Nunca habías sentido un silencio tan extenso."
         
            menu:
             "Preguntar":
                    show gael m nervous s
                    player_name "Gael, ¿Por qué te negaste a la cita?"
                    show gael m nervous t
                    g "Ah, este...bueno, verás..."
                    show gael m blush t
                    g "Siento que no es correcto aceptar una cita cuando me gusta alguien más…"
                    player_name "\¿Q-Qué?"
                    show gael m nervous t
                    g "Uhm, ya casi se acaba nuestro turno… así que mejor voy por allá"
                    show gael m nervous s
                    g "{b}{size=-10}Casi la riego abriendo mi bocota{/size}{/b}"
                    hide gael m nervous s with dissolve
                    n "No sabías cómo digerir todo lo que había pasado hoy."
                    n "Sin duda, este día sería uno largo."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump dia_9_good_1
                
             "Preguntar":
                    show gael m nervous s
                    player_name "Gael, ¿Por qué te negaste a la cita?"
                    show gael m nervous t
                    g "Ah, este...bueno, verás..."
                    show gael m blush t
                    g "Siento que no es correcto aceptar una cita cuando me gusta alguien más…"
                    player_name "\¿Q-Qué?"
                    show gael m nervous t
                    g "Uhm, ya casi se acaba nuestro turno… así que mejor voy por allá"
                    show gael m nervous s
                    g "{b}{size=-10}Casi la riego abriendo mi bocota{/size}{/b}"
                    hide gael m nervous s with dissolve
                    n "No sabías cómo digerir todo lo que había pasado hoy."
                    n "Sin duda, este día sería uno largo."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump dia_9_good_1

label dia_8_good_2:
    scene Uni Out with dissolve
    play music "Park.mp3"
    show asof normal s with dissolve
    n "Caminando por la Universidad, te topaste con Sofí."
    show asof normal t
    s "¿Entonces cómo va tu pintura?"
    show asof normal s
    player_name "Bastante bien, creo. Ya tengo un boceto y esperó mañana acabarlo."
    show asof normal t
    s "Me alegra escuchar eso [player_name], esperó ser la primera en verlo."

    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Después de clases fuiste a trabajar en la fondita. Esta vez no había tanta gente."
    n "Sin embargo, no parabas de notar la mirada constante de una chica."
    show loca miedo with dissolve
    d "..."
    player_name "{b}{size=+10}???{/size}{/b}"
    n ". "
    extend ". "
    extend "."
    show loca meh t
    d "\¡AY POR FAVOR!"
    show loca diuk
    n "La chica se acerca a ti apresuradamente."
    show loca meh t
    d "No captas indirectas \¿o qué?"
    show loca diuk
    player_name "{i}¿Y esta intensa qué?{/i}"
    player_name "Uh… \¿Se te ofrece algo?"
    show loca meh t
    d "¿El chico que trabaja contigo es tu novio?"
    show loca meh s
    player_name "Mmm, ¿Por qué preguntas?"
    show loca meh t
    d "Ugh, solo quiero saber ¿si?"
    show loca meh s
    n "La chica suspira y te mira fijamente."
    show loca meh t
    d "Bueno, si no lo es…"
    show loca blush t
    d "…No te importaría pasarme su número ¿verdad? Es que es taaan lindoo"
    show loca blush s
    n "No creías que la conservación fuera ahí. Sabías que Gael era guapo, era de esperarse que alguien se fijará en él."
    n "Pero no entendías el porqué te sentías algo molesta."

    menu:
     "Dárselo":
            player_name "{i}Bueno, al final del día no soy nada de él, no debería tomarle importancia.{/i}"
            n "Tomas una servilleta cercana y anotas el número de Gael con cierta duda."
            n "La chica se veía más que contenta."
            show loca blush t
            d "Ay muchas gracias de veras ¡Eres la mejor!"
            n "La chica te mira por unos segundos."
            show loca miedo
            d "En fin, no te acerques tanto a él, \¿oíste?"
            hide loca miedo with dissolve
            n "Así con el papel en sus manos se empezó a alejar de ti."
            player_name "..."
            n "La chica se acercó al mostrador donde Gael se encontraba."
            scene closer with dissolve
            show gael s2 nervous with dissolve
            n "Parecía tan contenta, que hasta daba miedo."
            n "La chica parece tratar de conversar con él."
            player_name "{i}De cierto modo, se ve bien juntos, o bueno, Gael se ve bien en pareja.{/i}"
            player_name "..."
            player_name "{i}Aunque se ve incómodo… Tal vez debería acercarme…{/i}"
            player_name "{i}No, no. Él está bien.{/i}"
            d "Entonces \¿Te gustaría salir después de tu turno?"
            g "Uh…"
            player_name "..."
            player_name "{i}Tal vez soy yo la que se siente mal.{/i}"
            show gael s2 surpised
            player_name "{b}{size=+10}!!!{/size}{/b}"
            show gael s2 blush 1
            n " "
            show gael s2 blush 2
            g "Cough"
            g "Agradezco tu invitación, pero tendré que negarme."
            d "\¡P-Pero!"
            g "Lo siento."
            scene Fondita In with dissolve
            hide gael s2 blush 2 with dissolve
            play music "Happyending.mp3"
            n "La chica se veía algo herida"
            n "No entendías, pero sentiste un gran alivio cuando cruzó la puerta."
            show gael m nervous2 t with dissolve
            g "Eso fue raro ¿verdad?"
            show gael m nervous2 s
            n "Solo pudiste asentir."
            n "Nunca habías sentido un silencio tan extenso."

            menu:
             "Preguntar":
                    show gael m nervous s
                    player_name "Gael, ¿Por qué te negaste a la cita?"
                    show gael m nervous t
                    g "Ah, este...bueno, verás..."
                    show gael m blush t
                    g "Siento que no es correcto aceptar una cita cuando me gusta alguien más…"
                    player_name "\¿Q-Qué?"
                    show gael m nervous t
                    g "Uhm, ya casi se acaba nuestro turno… así que mejor voy por allá"
                    show gael m nervous s
                    g "{b}{size=-10}Casi la riego abriendo mi bocota{/size}{/b}"
                    hide gael m nervous s with dissolve
                    n "No sabías cómo digerir todo lo que había pasado hoy."
                    n "Sin duda, este día sería uno largo."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump dia_9_good_2

             "Preguntar":
                    show gael m nervous s
                    player_name "Gael, ¿Por qué te negaste a la cita?"
                    show gael m nervous t
                    g "Ah, este...bueno, verás..."
                    show gael m blush t
                    g "Siento que no es correcto aceptar una cita cuando me gusta alguien más…"
                    player_name "\¿Q-Qué?"
                    show gael m nervous t
                    g "Uhm, ya casi se acaba nuestro turno… así que mejor voy por allá"
                    show gael m nervous s
                    g "{b}{size=-10}Casi la riego abriendo mi bocota{/size}{/b}"
                    hide gael m nervous s with dissolve
                    n "No sabías cómo digerir todo lo que había pasado hoy."
                    n "Sin duda, este día sería uno largo."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump dia_9_good_2


     "No dárselo":
            n "Niegas con tu cabeza. No era correcto y honestamente no querías dárselo."
            show loca meh s at jumper
            player_name "No creo que sea correcto que te de su información, así no más."
            show loca angry s
            n "La chica se le ve muy enfadada."
            show loca meh t
            d "\¡\¿Uh?! Eres una envidiosa, es obvio que te gusta, pero qué crees…"
            d "Eso no me va a impedir ir tras él, ¿escuchaste?"
            show loca angry s
            player_name "..."
            hide loca angry s with dissolve
            n "La chica se acercó al mostrador donde Gael se encontraba."
            scene closer with dissolve
            show gael s2 nervous with dissolve
            n "Parecía tan contenta, que hasta daba miedo."
            n "La chica parece tratar de conversar con él."
            player_name "{i}De cierto modo, se ve bien juntos, o bueno, Gael se ve bien en pareja.{/i}"
            player_name "..."
            player_name "{i}Aunque se ve incómodo… Tal vez debería acercarme…{/i}"
            player_name "{i}No, no. Él está bien.{/i}"
            d "Entonces \¿Te gustaría salir después de tu turno?"
            g "Uh…"
            player_name "..."
            player_name "{i}Tal vez soy yo la que se siente mal.{/i}"
            show gael s2 surpised
            player_name "{b}{size=+10}!!!{/size}{/b}"
            show gael s2 blush 1
            n " "
            show gael s2 blush 2
            g "Cough"
            g "Agradezco tu invitación, pero tendré que negarme."
            d "\¡P-Pero!"
            g "Lo siento."
            scene Fondita In with dissolve
            hide gael s2 blush 2 with dissolve
            play music "Happyending.mp3"
            n "La chica se veía algo herida"
            n "No entendías, pero sentiste un gran alivio cuando cruzó la puerta."
            show gael m nervous2 t with dissolve
            g "Eso fue raro ¿verdad?"
            show gael m nervous2 s
            n "Solo pudiste asentir."
            n "Nunca habías sentido un silencio tan extenso."
         
            menu:
             "Preguntar":
                    show gael m nervous s
                    player_name "Gael, ¿Por qué te negaste a la cita?"
                    show gael m nervous t
                    g "Ah, este...bueno, verás..."
                    show gael m blush t
                    g "Siento que no es correcto aceptar una cita cuando me gusta alguien más…"
                    player_name "\¿Q-Qué?"
                    show gael m nervous t
                    g "Uhm, ya casi se acaba nuestro turno… así que mejor voy por allá"
                    show gael m nervous s
                    g "{b}{size=-10}Casi la riego abriendo mi bocota{/size}{/b}"
                    hide gael m nervous s with dissolve
                    n "No sabías cómo digerir todo lo que había pasado hoy."
                    n "Sin duda, este día sería uno largo."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump dia_9_good_2
                
             "Preguntar":
                    show gael m nervous s
                    player_name "Gael, ¿Por qué te negaste a la cita?"
                    show gael m nervous t
                    g "Ah, este...bueno, verás..."
                    show gael m blush t
                    g "Siento que no es correcto aceptar una cita cuando me gusta alguien más…"
                    player_name "\¿Q-Qué?"
                    show gael m nervous t
                    g "Uhm, ya casi se acaba nuestro turno… así que mejor voy por allá"
                    show gael m nervous s
                    g "{b}{size=-10}Casi la riego abriendo mi bocota{/size}{/b}"
                    hide gael m nervous s with dissolve
                    n "No sabías cómo digerir todo lo que había pasado hoy."
                    n "Sin duda, este día sería uno largo."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump dia_9_good_2

label dia_9_good_1:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    n "Es un nuevo día."
    n "Mañana es la exposición en la galería, por lo que decidiste tomarte toda la mañana para acabar tu pintura."
    n "Trazos, pinceladas y mucha pintura en tus brazos. Sin duda, era toda una experiencia."
    n "Siplemente, fue bastante grato ver como tu idea cobraba forma."
    jump game_1

label dia_9_good_2:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    n "Es un nuevo día."
    n "Mañana es la exposición en la galería, por lo que decidiste tomarte toda la mañana para acabar tu pintura."
    n "Trazos, pinceladas y mucha pintura en tus brazos. Sin duda, era toda una experiencia."
    n "Simplemente, fue bastante grato ver como tu idea cobraba forma."
    jump game_2

label  game_1:
    play music "Park.mp3"
    $ setup_puzzle01()
    call screen reassemble_puzzle01

label  game_2:
    play music "Park.mp3"
    $ setup_puzzle02()
    call screen reassemble_puzzle02

label dia_9_good1p2:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    show p1 with dissolve
    player_name "¡Y listo!"
    hide p1 with dissolve
    n "Después de observar con orgullo tu obra, miraste el desastre que te rodeaba."
    n "Cuando estabas lista para limpiar, tu celular te interrumpió."
    nvl_narrator "Tienes un nuevo mensaje"
    g_nvl "Hola! Espero no molestarte, pero hoy vas a trabajar?"
    n "\¿Qué responderle?"

    menu:
     "Si":
            p_nvl "Hola!"
            p_nvl "Si, creo que voy a ir solo un rato..."
            p_nvl "Es que debo ordenar el desastre que hice por mi proyecto :p"
            g_nvl "Proyecto? :0"
            p_nvl "Te explico allá"
            n "Bueno, no podías dejar tu trabajo desatendido, además que era una buena excusa para ver a Gael y tal vez se despejen todas tus dudas."
            
            scene Fondita In  with dissolve
            play music "Cafeteria.mp3"
            n "Al llegar a la fondita, notaste el lugar casi vacío."
            show gael m nervous2 s with dissolve
            n "Gael se encontraba mirando nervioso su celular."
            show gael m normal t at jumper
            g "¡[player_name]!"
            show gael m blush t
            g "Justo te iba a llamar, mis padres decidieron mejor cerrar temprano hoy, para que no vinieras, pero creo que me tarde…"
            show gael m blush s
            player_name "No te preocupes, aún así necesitaba despejarme."
            show gael m normal t
            g "Por tu proyecto, ¿verdad?"
            show gael m normal s
            n "Cierto."
            player_name "Si, mañana voy a presentar una pintura en una galería, es por una clase…"
            n "Por alguna razón no podías ni mirarlo a los ojos."
            n "Todo era culpa de lo que pasó ayer. Si tan solo…"
            player_name "Uhm…"
            show gael m blush2 t
            g "Bueno, esperó que se quede en exposición por un tiempo. Me gustaría poder ver tu trabajo" 
            show gael m blush t
            g "Así podría decir que soy amigo de una gran artista."
            n "Amigo"
            n "{b}Amigo{/b}"
            play music "Sadend.mp3"
            n "No podías ignorar la extraña sensación de tristeza que surgió al escuchar eso."
            n "\¿Qué está haciendo con tu cabeza? Eso es normal, hasta es bueno."
            show gael m normal s
            n "Te considera una amistad."
            extend " Eso es bueno para ti ¿verdad?"

            menu:
             
             "Si":
                    player_name "{b}¡Si!{/b}"
                    show gael m nervous2 s at jumper
                    g "{b}{size=+10}???{/size}{/b}"
                    player_name "Uh..."
                    player_name "Que...¡si va a estar como por un mes allá!"
                    show gael m nervous2 t
                    g "Oh, ¡Qué bien! Entonces esperó ir después."
                    show gael m nervous2 s
                    n "Solo querías irte ya."
                    player_name "Bueno, como ya no hay trabajo creo que será mejor que me vaya."
                    extend " Nos vemos."
                    hide gael m nervous2 s with dissolve
                    n "Esta sería otra noche larga."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump final_norm
             
             "No":
                player_name "{b}No...{/b}"
                show gael m nervous2 t
                g "Oh..."
                g "\¿No quieres qué la vea?"
                show gael m nervous2 s
                player_name "\¡Ay! \¡No es eso! Es que...uh..."

                menu:
                 "Decirle":
                        play music "Happyending.mp3"
                        player_name "Yo..."
                        n "Respiraste y finalmente..."
                        player_name "¡Te quería invitar a verlo conmigo!"
                        show gael m blush s at jumper
                        g "{b}{size=+10}!!!{/size}{/b}"
                        show gael m blush t
                        g "C-Claro! ¡Me encantaría ir!"
                        n "Sin dudarlo, le mandaste toda la información para que llegará."
                        hide gael m blush t with dissolve
                        n "No podías esperar a mañana."
                        scene black with dissolve
                        stop music fadeout 1.0
                        jump final_bueno

                 "No decirle":
                        player_name "Uh, que no va a estar solo mañana, si no como..."
                        player_name "Uh..."
                        show gael m normal s
                        player_name "{b}¡Un mes!{/b}"
                        extend "...si, un mes..."
                        show gael m normal t
                        g "Oh, ¡Qué bien! Entonces esperó ir después."
                        show gael m normal s
                        n "Solo querías irte ya."
                        player_name "Bueno, como ya no hay trabajo creo que será mejor que me vaya. Nos vemos."
                        hide gael m normal s with dissolve
                        n "Esta sería otra noche larga."
                        scene black with dissolve
                        stop music fadeout 1.0
                        jump final_norm
     "No":
            p_nvl "Hola!"
            p_nvl "No, lo siento :( "
            g_nvl "Oh, ok! Ntp, nos vemos después."
            n "Bueno, no podías simplemente dejar todo así y necesitabas descansar."
            n "Así que solo quedaba aprovechar el día de descanso hasta el final."
            scene black with dissolve
            stop music fadeout 1.0
            jump final_norm

label dia_9_good2p2:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    show p2 with dissolve
    player_name "¡Y listo!"
    hide p2 with dissolve
    n "Después de observar con orgullo tu obra, miraste el desastre que te rodeaba."
    n "Cuando estabas lista para limpiar, tu celular te interrumpió."
    nvl_narrator "Tienes un nuevo mensaje"
    g_nvl "Hola! Espero no molestarte, pero hoy vas a trabajar?"
    n "\¿Qué responderle?"

    menu:
     "Si":
            p_nvl "Hola!"
            p_nvl "Si, creo que voy a ir solo un rato..."
            p_nvl "Es que debo ordenar el desastre que hice por mi proyecto :p"
            g_nvl "Proyecto? :0"
            p_nvl "Te explico allá"
            n "Bueno, no podías dejar tu trabajo desatendido, además que era una buena excusa para ver a Gael y tal vez se despejen todas tus dudas."
            
            scene Fondita In  with dissolve
            play music "Cafeteria.mp3"
            n "Al llegar a la fondita, notaste el lugar casi vacío."
            show gael m nervous2 s with dissolve
            n "Gael se encontraba mirando nervioso su celular."
            show gael m normal t at jumper
            g "¡[player_name]!"
            show gael m blush t
            g "Justo te iba a llamar, mis padres decidieron mejor cerrar temprano hoy, para que no vinieras, pero creo que me tarde…"
            show gael m blush s
            player_name "No te preocupes, aún así necesitaba despejarme."
            show gael m normal t
            g "Por tu proyecto, ¿verdad?"
            show gael m normal s
            n "Cierto."
            player_name "Si, mañana voy a presentar una pintura en una galería, es por una clase…"
            n "Por alguna razón no podías ni mirarlo a los ojos."
            n "Todo era culpa de lo que pasó ayer. Si tan solo…"
            player_name "Uhm…"
            show gael m blush2 t
            g "Bueno, esperó que se quede en exposición por un tiempo. Me gustaría poder ver tu trabajo" 
            show gael m blush t
            g "Así podría decir que soy amigo de una gran artista."
            n "Amigo"
            n "{b}Amigo{/b}"
            play music "Sadend.mp3"
            n "No podías ignorar la extraña sensación de tristeza que surgió al escuchar eso."
            n "\¿Qué está haciendo con tu cabeza? Eso es normal, hasta es bueno."
            show gael m normal s
            n "Te considera una amistad."
            extend " Eso es bueno para ti ¿verdad?"

            menu:
             
             "Si":
                    player_name "{b}¡Si!{/b}"
                    show gael m nervous2 s at jumper
                    g "{b}{size=+10}???{/size}{/b}"
                    player_name "Uh..."
                    player_name "Que...¡si va a estar como por un mes allá!"
                    show gael m nervous2 t
                    g "Oh, ¡Qué bien! Entonces esperó ir después."
                    show gael m nervous2 s
                    n "Solo querías irte ya."
                    player_name "Bueno, como ya no hay trabajo creo que será mejor que me vaya."
                    extend " Nos vemos."
                    hide gael m nervous2 s with dissolve
                    n "Esta sería otra noche larga."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump final_norm
             
             "No":
                player_name "{b}No...{/b}"
                show gael m nervous2 t
                g "Oh..."
                g "\¿No quieres qué la vea?"
                show gael m nervous2 s
                player_name "\¡Ay! \¡No es eso! Es que...uh..."

                menu:
                 "Decirle":
                        play music "Happyending.mp3"
                        player_name "Yo..."
                        n "Respiraste y finalmente..."
                        player_name "¡Te quería invitar a verlo conmigo!"
                        show gael m blush s at jumper
                        g "{b}{size=+10}!!!{/size}{/b}"
                        show gael m blush t
                        g "C-Claro! ¡Me encantaría ir!"
                        n "Sin dudarlo, le mandaste toda la información para que llegará."
                        hide gael m blush t with dissolve
                        n "No podías esperar a mañana."
                        scene black with dissolve
                        stop music fadeout 1.0
                        jump final_bueno

                 "No decirle":
                        player_name "Uh, que no va a estar solo mañana, si no como..."
                        player_name "Uh..."
                        show gael m normal s
                        player_name "{b}¡Un mes!{/b}"
                        extend "...si, un mes..."
                        show gael m normal t
                        g "Oh, ¡Qué bien! Entonces esperó ir después."
                        show gael m normal s
                        n "Solo querías irte ya."
                        player_name "Bueno, como ya no hay trabajo creo que será mejor que me vaya. Nos vemos."
                        hide gael m normal s with dissolve
                        n "Esta sería otra noche larga."
                        scene black with dissolve
                        stop music fadeout 1.0
                        jump final_norm
     "No":
            p_nvl "Hola!"
            p_nvl "No, lo siento :( "
            g_nvl "Oh, ok! Ntp, nos vemos después."
            n "Bueno, no podías simplemente dejar todo así y necesitabas descansar."
            n "Así que solo quedaba aprovechar el día de descanso hasta el final."
            scene black with dissolve
            stop music fadeout 1.0
            jump final_norm

label final_bueno:
    scene Gallery with dissolve
    play music "Gallery.mp3"
    n "Después de unas largas semanas, finalmente llegó el día."
    n "Toda tu clase estaba reunida en la galería con sus trabajos listos para exponer."
    n "La profesora Marta incluso se vistió para la ocasión."
    n "Cada alumno tenía que mostrarle sus trabajos antes de exponerlos, así sabrías tu nota final y solo disfrutarías el evento."
    n "Aún así, no dejabas de sentir nervios en cada paso que te acercabas a la profesora."
    n "Incluso Sofí te había dicho que estaba bien, además la profesora nunca había sido cruel al revisar."
    n "Pero sabías en el fondo que tus nervios no eran por el proyecto, si no por que aún no había llegado a quién más esperabas."
    show marta normal t with dissolve
    m "¡La siguiente persona por favor!"
    show marta normal s
    n "Era hora. Respiraste hondo y le mostraste tu pintura."
    show marta normal t
    m "¡Vaya! Sabía que no me iba decepcionar jovencita."
    m "No quería creer lo que sus otros profesores hablan de usted, pero veo que tienen razón."
    m "Realmente es muy bueno su trabajo. Se que va a ser uno de los que más luzcan hoy."
    hide marta normal t with dissolve
    n "Te alegraste un poco al escuchar aquellas palabras, realmente lo habías conseguido."
    n "Al poco tiempo tu cuadro fue expuesto. Veías a varias personas que se detenían a verlo."
    n "Era un sentimiento muy grato."
    n "Cuando te encontrabas más perdida en tus pensamientos sentiste un pequeño golpe en tu hombro."
    n "No podías ocultar tu sonrisa."
    n "Era Gael."
    play music "Happyending.mp3"
    show gael s3 normal l with dissolve
    g "¿Ese es tu trabajo? Vaya que es bueno y eso que no se mucho de arte."
    show gael s3 normal c
    g "Valió la pena venir a verte-"
    show gael s3 surprised t at jumper
    g "uhhhhh"
    show gael s3 haha
    g "¡A ver tu {b}trabajo{/b}!"
    g "¡Si! Eso...Quise decir"
    show gael s3 surprised s
    player_name "{i}¿Cómo puede decir cosas así?{/i}"
    show gael s3 uh
    player_name "{i}Primero mi molestia al verlo con esa chica, luego ayer invitandolo de golpe.{/i}"
    show gael s3 sad
    player_name "{i}¡\¿Pero qué me está pasando?!{/i}"
    show gael s3 uh
    g "Uhm, ¿[player_name]? ¿Todo bien?"
    g "Perdón si dije algo que te incomodó, lo dije sin pensar y yo-"
    player_name "..."

    menu:
        "Decirle la verdad":
            player_name "Gael..."
            extend "creo que me gustas."
            show gael s3 wow
            g "{b}{size=+10}!!!{/size}{/b}"
            show gael s3 haha at jumper
            g "Y-Yo, que? "
            g "Digo uh..."
            show gael s3 surprised s
            g "..."
            show gael s3 blushl t
            g "Bueno, eso explica muchas cosas"
            show gael s3 blushl s
            player_name "¡Lo dices como si no estuvieras igual de rojo que yo!"
            show gael s3 blush
            g "E-Es diferente ¿Ok?"
            hide gael s3 blush with dissolve

    scene black with dissolve
    n "Este es..."
    extend "Un brillante futuro."
    stop music fadeout 1.0
    scene final 4 with dissolve
    n " "
    n "Has conseguido el final Bueno."
    return
    ####Final Bueno###


label hdia_1:
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
    r "\¿[player_name], eres tú?"

    show rogelio happy s
    n "Con una sonrisa incómoda te sientas de nuevo."
    n "Rogelio se sienta y empieza a llamar la atención del mesero."

    show rogelio happy t at left with move
    show mesero happy at right with dissolve
    w "¿Qué van a-"
    show mesero s at right
    r "Dame un pastel de chocolate y un café semidescremado con espuma a 156°F"
    show rogelio happy s at left
    n "El mesero se nota fastidiado por su actitud, pero trata de ser amable contigo."
    show mesero happy at right
    w "Y ¿Para usted?"
    player_name "Para mi-"
    show rogelio annoyed t at left
    show mesero s at right
    r "A él dale una ensalada."
    show rogelio annoyed s at left
    player_name "Pero-"
    show rogelio annoyed t at left
    r "Que se ve que le hace falta…"
    show rogelio annoyed s at left
    show mesero uncomfy at right
    w "¿Ok?"
    hide mesero uncomfy with dissolve
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
         r "Cuando seas mi novio, me iré lindo."

    show rogelio happyp s at center
    n "Qué incómodo…"
    show rogelio happyp s at left with move
    show mesero s at right with dissolve
    n "Por suerte llegó el mesero con los pedidos."
    n "..."
    hide mesero s with dissolve
    show rogelio happyp s at center with move
    n "Estabas convencido que jamás habías visto una ensalada tan insípida en tu vida."
    player_name "…"
    show rogelio annoyed t
    r "Seamos claros. Se como son los de tu tipo."
    n "{b}{size=+10}???{/size}{/b}"
    show rogelio happyp t
    r "Ana Sofi me contó de tu situación económica así que podemos solucionar nuestros problemas. "
    show rogelio happy t
    extend "¿Me entiendes?"
    show rogelio happyp s

    menu:

     "Huir":
         n "Pero antes de poder hacer algo, escuchas un grito frente a ti."
         scene Coffee with vpunch
         play sound "hit.mp3"

     "Huir":
         n "Pero antes de poder hacer algo, escuchas un grito frente a ti."
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
    d "Ay, perdona fue un accidente"
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
    n "No sabes como reaccionar ante tales palabras, mientras lo ves tomar sus cosas al irse del café."
    n "Vaya lío."
    show gael n meh s with dissolve
    player_name "Oye ¿Estas bien?"
    show gael n sad t
    d "No te preocupes por mí, mejor dime ¿tú estás bien?"
    show gael n angry t
    d "Qué ese tipo era todo un personaje ¡eh!"
    show gael n angry s
    player_name "Si, ni que lo digas…"
    show gael n meh t
    d "Bueno… digamos que el \“accidente”, no fue tan así."
    show gael n normal t
    d "Verás yo quería ayudarte un poco, ya que te veías muy incomodo."
    show gael n normal s
    n "Que agradable sujeto."
    player_name "Ay muchas gracias, ¿puedo pagarte tu café o algo?"
    show gael n nervous t
    d "Pues… con una cita sería suficiente"
    show gael n nervous s
    n "Si, sabías que no podías confiar en la buena fé de la gente ¿Pero qué responderle?"
    menu:

     "Si, ¿por qué no?":
         show gael n blush s
         d "{i}{size=-10}Wow, no pensé que funcionaría…{/i}{/size}"
         show gael n blush t
         d "¡Bien! Uhm, entonces te entrego mi número, ¿va?"
         show gael n blush s
         n "El chico comienza a escribirlo en una servilleta. Se le ve contento."
         show gael n blush t
         d "Ok, entonces ¡te veo luego!"
         hide gael n blush t with dissolve
         n "Ves al chico irse tan rápido como apareció."
         #show mesero s at dissolve
         n "Después de aquella escena, el mesero se acerca con la cuenta."
         player_name "Ay, ¿por qué me metiste en esto Sofi?"
         #hide mesero s at dissolve
         stop music fadeout 1.0
         scene Cuarto with dissolve
         play music "Cuarto.mp3"
         n "Unas horas más tarde, estás en tu habitación jugando con los bordes de la servilleta."
         n "¿Sería muy pronto para llamar? "
         extend "Nah"
         play sound "ReceiveText.ogg"
         d "¿hola?"
         n "Escuchas del otro lado de la línea la voz de una señora."
         d "Buenos días, ¿vas a pedir algo a domicilio?"
         n "Rápidamente colgaste. Qué vergüenza…"
         player_name "Ni una cita ni otra"
         player_name "Ugh…"
         n "Decepcionado del día, decides mejor dormir y tratar de olvidar todo."
         scene black with dissolve
         jump hdia_2_good


     "No, así estoy bien":
         show gael n nervous2 t
         d "Ah, bueno… si, creo que me lo busque"
         show gael n normal t
         d "Disfruta tu comida"
         show gael n nervous2 s
         n "El chico se va incómodo."
         hide gael n nervous s with dissolve
         player_name "Pero que chicos que me tope hoy…"
         #show mesero s at dissolve
         n "Después de aquella escena, un mesero se acerca con la cuenta."
         player_name "Ay, ¿por qué me metiste en esto Sofi?"
         #hide mesero s at dissolve
         scene Cuarto with dissolve
         play music "Cuarto.mp3"
         n "Unas horas más tarde, estás en tu habitación"
         n "Decepcionado del día, decides mejor dormir y tratar de olvidar todo."
         scene black with dissolve
         jump hdia_2_normal

label hdia_2_good:
    scene Cuarto with dissolve
    n "Después de un merecido descanso, te alistas para ir a la Universidad."
    scene Uni In with dissolve
    play music "Uni.mp3"
    n "La clase de la profesora Marta comenzó. Explicando todo acerca de la presentación de final de semestre, que sería en un par de semanas."
    show marta normal t with dissolve
    m "¡Chicos! ¡Logré que nos prestarán uno de los auditorios del museo de la ciudad para nuestra exposición!"
    show marta normal s
    n "Algunos alumnos se alegraron mientras otros les daba igual."
    show marta normal t
    m "Entonces procuren entregar una pintura digna del espacio ¡Así que esfuércense!"
    hide marta normal s with dissolve
    n "Sabías bien que no solo se refería a la técnica, si no a tener buenos materiales."
    n "Igual a…"
    extend" necesitas dinero."
    n "Dinero que te gastaste ayer por culpa de ese tonto."
    n "Dinero que no tienes…"
    player_name "Ughhhhhhh"
    scene Uni Out with dissolve
    play music "Park.mp3"
    n "Sales de la clase, aún pensando que puedes hacer. No es como si las oportunidades cayeran del cielo."
    scene Uni Out with vpunch
    play sound "hit.mp3"
    n "Por estar dando vueltas al asunto, chocaste con el tablón de anuncios. Haciendo que uno de los panfletos cayera a tus manos."
    n "{size=+10}SE BUSCA AYUDANTE{/size}"
    player_name "¿Quién lo diría?"
    extend " Si caen del cielo."
    n "No perdías nada al intentar ir a preguntar ¿verdad?"

    scene Fondita Out with dissolve
    n "Caminaste por unos minutos. El lugar no era tan lejano como creías, eso era un punto a favor."
    scene Fondita In with dissolve
    play sound "shop bell.mp3"
    play music "Cafeteria.mp3"
    n "La fondita parecía espaciosa y un poco concurrida. La decoración y ambiente hogareño se sentía como un abrazo cálido."
    n "Definitivamente el lugar tenía su encanto."
    show gael m normal s with dissolve
    n "Mientras más te acercabas a la barra principal, notabas un rostro familiar."
    show gael m shock at jumper
    n "{b}{size=+10}!!!{/size}{/b}"
    n "Bueno, esto empieza a explicar muchas cosas."
    show gael m nervous s
    d "…"
    player_name "Oh"
    show gael m nervous t
    a "¡H-Hola!"
    show gael m nervous s
    n "No puedes evitar sonreír un poco al verlo tan avergonzado."
    player_name "No creí que volvería a verte tan pronto."
    extend " Aunque ahora entiendo el por que cuando llamé me preguntaron si quería pedir algo."
    show gael m sad t
    a "{i}{size=-10}Chale, si eras tú.{/i}{/size}"
    show gael m nervous t
    a "Qué vergüenza, de verdad lo siento."
    a "Es que ya se me hace costumbre que pidan el número del lugar y no esperaba que dijeras que si ayer, entonces los cables se me cruzaron y solo escribí el primer número que pasó por mi mente. Ya después me di cuenta, pero no sabía cómo encontrarte y-"
    show gael m sad s
    n "No pudiste soportarlo más y una risita escapó de tus labios."
    player_name "Perdón, es solo que me alegra saber que tenía una explicación. Ya me estaba montando teorías en la cabeza."
    show gael m nervous t
    a "Bueno… uhm "
    extend "¿y qué te trae aquí?"
    show gael m nervous s

    n "Sacaste de tus bolsillos el panfleto."
    player_name "Vi esto en la universidad, y estaba pensando en postularme para el trabajo de mesero."
    player_name "Pero no sabía que tú trabajabas aquí…"

    menu:

     "Te vas por la vergüenza":
         show gael m nervous2 s
         player_name "Ay, como que acabo de recordar que debo hacer algo"
         player_name "Adiós"
         hide gael m nervous s with dissolve
         stop music fadeout 1.0
         scene Fondita Out with dissolve
         n "Qué horror. No esperabas encontrarlo y podrás necesitar dinero pero para nada te quedarás unos segundos más."
         play sound "bicycle.mp3"
         d "¡Oye! ¡Muévete!"
         n "Oh no..."
         scene Fondita Out with vpunch
         play sound "crash.mp3"
         scene black with dissolve
         n "..."
         scene final 0 with dissolve
         n " "
         n "Has conseguido el final 0."
         return
         ####Final 0###


     "Te quedas":
         player_name "Pero no importa, necesito el trabajo"
         player_name "Así que, ¿qué debo hacer?"
         show gael m normal t
         a "Bueno… antes que nada necesitamos saber que tienes lo necesario para trabajar aquí."
         show gael m blush t
         a "¡Pero no te preocupes! El día de prueba va a ser remunerado"
         hide gael m blush t with dissolve
         n "Después de unas horas trabajando en la fondita, emepezaste a familiarizarte con tu alrededor."
         n "Cuando menos lo notaste, Gael se acerca."
         show gael m normal t with dissolve
         a "Creo que podrías afinar algunas cosas, pero tienes las habilidades necesarias para trabajar aquí."
         a "¡Así que bienvenida!"
         hide gael m normal s with dissolve
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_3_good

label hdia_2_normal:
    scene Cuarto with dissolve
    n "Después de un merecido descanso, te alistas para ir a la Universidad."
    scene Uni In with dissolve
    play music "Uni.mp3"
    n "La clase de la profesora Marta comenzó. Explicando todo acerca de la presentación de final de semestre, que sería en un par de semanas."
    show marta normal t with dissolve
    m "¡Chicos! ¡Logré que nos prestarán uno de los auditorios del museo de la ciudad para nuestra exposición!"
    show marta normal s
    n "Algunos alumnos se alegraron mientras otros les daba igual."
    show marta normal t
    m "Entonces procuren entregar una pintura digna del espacio ¡Así que esfuércense!"
    hide marta normal s with dissolve
    n "Sabías bien que no solo se refería a la técnica, si no a tener buenos materiales."
    n "Igual a…"
    extend " necesitas dinero."
    n "Dinero que te gastaste ayer por culpa de ese tonto."
    n "Dinero que no tienes…"
    player_name "Ughhhhhhh"
    scene Uni Out with dissolve
    play music "Park.mp3"
    n "Sales de la clase, aún pensando que puedes hacer. No es como si las oportunidades cayeran del cielo."
    scene Uni Out with vpunch
    play sound "hit.mp3"
    n "Por estar dando vueltas al asunto, chocaste con el tablón de anuncios. Haciendo que uno de los panfletos cayera a tus manos."
    n "{size=+10}SE BUSCA AYUDANTE{/size}"
    player_name "¿Quién lo diría?"
    extend " Si caen del cielo."
    n "No perdías nada al intentar ir a preguntar ¿verdad?"

    scene Fondita Out with dissolve
    n "Caminaste por unos minutos. El lugar no era tan lejano como creías, eso era un punto a favor."
    scene Fondita In with dissolve
    play sound "shop bell.mp3"
    play music "Cafeteria.mp3"
    n "La fondita parecía espaciosa y un poco concurrida. La decoración y ambiente hogareño se sentía como un abrazo cálido."
    n "Definitivamente el lugar tenía su encanto."
    show gael m normal s with dissolve
    n "Mientras más te acercabas a la barra principal, notabas un rostro familiar."
    show gael m shock at jumper
    n "{b}{size=+10}!!!{/size}{/b}"
    show gael m sad s
    n "No puede ser."
    show gael m nervous2 t
    n "Oh…"
    player_name "..."
    show gael m nervous2 s
    n "De todas las personas que existen, tenía que ser ese chico quién trabajará aquí."
    show gael m nervous2 t
    a "Uhm, ¿Qué te trae aquí?"
    show gael m nervous2 s

    n "Sacaste de tus bolsillos el panfleto."
    player_name "Vi esto en la universidad, y estaba pensando en postularme para el trabajo de mesero."
    player_name "Pero no sabía que tú trabajabas aquí…"

    menu:

     "Te vas":
         show gael m nervous2 s
         player_name "Ay, como que acabo de recordar que debo hacer algo"
         player_name "Adiós"
         hide gael m nervous s with dissolve
         stop music fadeout 1.0
         scene Fondita Out with dissolve
         n "Qué horror. No esperabas encontrarlo y podrás necesitar dinero pero para nada te quedarás unos segundos más."
         play sound "bicycle.mp3"
         d "¡Oye! ¡Muévete!"
         n "Oh no..."
         scene Fondita Out with vpunch
         play sound "crash.mp3"
         scene black with dissolve
         n "..."
         scene final 0 with dissolve
         n " "
         n "Has conseguido el final 0."
         return
         ####Final 0###

     "Te quedas":
         player_name "Pero no importa, necesito el trabajo"
         player_name "Así que, ¿qué debo hacer?"
         show gael m normal t
         a "Bueno… antes que nada necesitamos saber que tienes lo necesario para trabajar aquí."
         show gael m blush t
         a "¡Pero no te preocupes! El día de prueba va a ser remunerado"
         hide gael m blush t with dissolve
         n "Después de unas horas trabajando en la fondita, emepezaste a familiarizarte con tu alrededor."
         n "Cuando menos lo notaste, Gael se acerca."
         show gael m normal t with dissolve
         a "Creo que podrías afinar algunas cosas, pero tienes las habilidades necesarias para trabajar aquí."
         a "¡Así que bienvenida!"
         hide gael m normal s with dissolve
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_3_normal

label hdia_3_good:
    scene Uni Out with dissolve
    play music "Park.mp3"
    n "Al día siguiente continuaste con tus actividades con normalidad."
    n "Después de una larga clase, llegó el descanso..."
    extend "que tu amiga aprovecho como excusa para hablar."
    show asof nervous s with dissolve
    player_name "No entiendo cómo pudiste hacerme esto…"
    show asof nervous t
    s "¡Ya me disculpé muchas veces hoy [player_name]!"
    show asof nervous s
    player_name "No es suficiente…"
    show asof shock t
    s "¡¿Qué iba a saber yo que ese wey era un patán?!"
    hide asof shock t
    show sof nervous t
    s "Solo lo veo en Navidad y ni le hablo, pero se me hacía guapo y dije "
    extend "\“¡ah! tal vez le sirva a mi bestie\”"
    hide sof nervous t
    show asof nervous s
    player_name "ugh…"
    show asof meh
    s "Ya perdoname, te prometo que no vuelvo a hacer algo así."
    show asof close2
    player_name "Es la tercera vez…"
    hide asof close2
    show sof nervous t
    s "Lo se pero ya no va haber cuarta."
    show sof nervous s
    player_name "Y lo peor de todo, es que tuve que pagar su cuenta."
    hide sof nervous s
    show asof shock s
    s "{b}{size=+10}!!!{/size}{/b}"
    player_name "Y no pidió poquito…"
    show asof serious t
    s "Ay supongo que me lo debí imaginar, por eso mi tío lo quiere desheredar."
    show asof close2
    s "..."
    hide asof close2
    show sof shock t
    s "Oye pero ¿Cómo vas a pagar tus materiales para el proyecto final?"
    player_name "De hecho, justo ayer conseguí trabajo."
    hide sof shock t
    show asof shock s
    player_name "Y eso es otro problema."
    hide asof shock s
    show sof shock t 
    s "¿Qué? ¿Por qué?"
    show sof shock s
    player_name "Por que la cita no acabo con que Rogelio me dejo, si no que otro chavo se metió en el asunto."
    show sof shock s at jumper
    s "{b}{size=+10}???{/size}{/b}"
    player_name "Él tiró todo su café en Rogelio para sacarme de ahí."
    show sof nervous t
    s "Eso es bueno ¿no?"
    hide sof nervous t
    show asof nervous s
    player_name "Pues…"

    menu:

     "Hablar bien":
         player_name "No te voy a mentir, era mi tipo."
         show asof happy s
         player_name "Hasta su número me dio y todo."
         hide asof happy s
         show sof happy t
         s "Boy, ¿ya ves que mis planes no son tan malos? Puedes juzgar mis métodos pero no mis resultados."
         hide sof happy t
         show asof nervous s
         player_name "Pero se confundió y anotó otra cosa."
         hide asof nervous s
         show sof normal t
         jump hdia_3_pt2_good

     "Hablar mal":
         player_name "Resultó que tenía otras intenciones…"
         show asof shock t
         s "Ay, ¿Pues qué pasó?"
         show asof serious s
         player_name "Fue demasiado directo, ¡ni su nombre sé y me pidió una cita!"
         hide asof serious s
         show sof happy t
         s "Ay, pues hubieras aprovechado"
         show sof happy s
         player_name "¡Ni loco!"
         show sof happy t
         s "Si dios quita, dios da"
         show sof happy s
         player_name "Ugh…"
         show sof normal t
         jump hdia_3_pt2_normal

label hdia_3_normal:
    scene Uni Out with dissolve
    play music "Park.mp3"
    n "Al día siguiente continuaste con tus actividades con normalidad."
    n "Después de una larga clase, llegó el descanso..."
    extend "que tu amiga aprovecho como excusa para hablar."
    show asof nervous s with dissolve
    player_name "No entiendo cómo pudiste hacerme esto…"
    show asof nervous t
    s "¡Ya me disculpé muchas veces hoy [player_name]!"
    show asof nervous s
    player_name "No es suficiente…"
    show asof shock t
    s "¡¿Qué iba a saber yo que ese wey era un patán?!"
    hide asof shock t
    show sof nervous t
    s "Solo lo veo en Navidad y ni le hablo, pero se me hacía guapo y dije "
    extend "\“¡ah! tal vez le sirva a mi bestie\”"
    hide sof nervous t
    show asof nervous s
    player_name "ugh…"
    show asof meh
    s "Ya perdoname, te prometo que no vuelvo a hacer algo así."
    show asof close2
    player_name "Es la tercera vez…"
    hide asof close2
    show sof nervous t
    s "Lo se pero ya no va haber cuarta."
    show sof nervous s
    player_name "Y lo peor de todo, es que tuve que pagar su cuenta."
    hide sof nervous s
    show asof shock s
    s "{b}{size=+10}!!!{/size}{/b}"
    player_name "Y no pidió poquito…"
    show asof serious t
    s "Ay supongo que me lo debí imaginar, por eso mi tío lo quiere desheredar."
    show asof close2
    s "..."
    hide asof close2
    show sof shock t
    s "Oye pero ¿Cómo vas a pagar tus materiales para el proyecto final?"
    player_name "De hecho, justo ayer conseguí trabajo."
    hide sof shock t
    show asof shock s
    player_name "Y eso es otro problema."
    hide asof shock s
    show sof shock t 
    s "¿Qué? ¿Por qué?"
    show sof shock s
    player_name "Por que la cita no acabo con que Rogelio me dejo, si no que otro chavo se metió en el asunto."
    show sof shock s at jumper
    s "{b}{size=+10}???{/size}{/b}"
    player_name "Él tiró todo su café en Rogelio para sacarme de ahí."
    show sof nervous t
    s "Eso es bueno ¿no?"
    hide sof nervous t
    show asof nervous s
    player_name "Pues…"


    menu:

     "Hablar bien":
         player_name "No te voy a mentir, era lindo."
         hide asof nervous s
         show sof happy t
         s "Boy, ¿ya ves que mis planes no son tan malos? Puedes juzgar mis métodos pero no mis resultados."
         hide sof happy t
         show asof nervous s
         player_name "Pero fue muy directo de repente y mejor lo deje."
         hide asof nervous s
         show sof normal t
         jump hdia_3_pt2_good

     "Hablar mal":
         player_name "Resultó que tenía otras intenciones…"
         hide asof nervous s
         show sof shock t
         s "Ay, ¿Pues qué pasó?"
         hide sof shock t
         show asof serious s
         player_name "Fue demasiado directo, ¡ni su nombre sé y me pidió una cita!"
         hide asof serious s
         show sof happy t
         s "Ay, pues hubieras aprovechado"
         show sof happy s
         player_name "¡Ni loco!"
         show sof happy t
         s "Si dios quita, dios da"
         show sof happy s
         player_name "Ugh…"
         show sof normal t
         jump hdia_3_pt2_normal

label hdia_3_pt2_good:
    s "Ok ¿Y qué tiene que ver con tu trabajo?"
    hide sof normal t
    show asof normal s
    player_name "Pues resulta que es mi compañero de trabajo…"
    show asof shock t
    s "Ay no amix, esto ya parece Wittpad"
    show asof shock s
    player_name "No empieces Ana Sofí"
    hide asof shock s
    show sof shock t
    s "Es que, o sea"
    s "¿Qué probabilidad hay de que eso te pase?"
    hide sof shock t
    show asof shock s
    player_name "La verdad ni se si me voy a quedar ahí por mucho tiempo."
    player_name "Tal vez hasta renuncie cuando junte para los materiales."
    show asof meh
    s "Ay [player_name], tu siempre tan \“positivo\”"
    show asof close2
    player_name "Es que no entiendes Sofí, es algo raro."
    show asof meh
    s "Si tu lo dices..."
    hide asof meh with dissolve
    n "Mientras regresabas al salón, observaste a alguien caminando del lado contrario."
    show gael n normal s with dissolve
    player_name "{i}{size=-10}¿Acaso es?{/size}{/i}"
    hide gael n normal s with dissolve
    player_name "{i}{size=-10}Creo que ya estoy alucinando cosas...{/size}{/i}"

    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Horas más tarde"
    n "Después de unas horas trabajando, finalmente encuentras un momento de descanso."
    d "Día pesado ¿eh?"
    n "Volteas a la dirección de la voz."
    show gael m normal s with dissolve
    player_name "…"
    show gael m nervous2 t
    a "{i}{size=-10}Público pesado…{/size}{/i}"
    show gael m nervous2 s
    a "{i}{size=-10}Cofcof{/size}{/i}"
    show gael m normal t
    a "Uhm…ahora que lo pienso, ni siquiera conozco tu nombre."
    show gael m normal s
    player_name "[player_name]. Mi nombre es [player_name]."
    n "..."
    show gael m normal t
    g "Bueno... el mio es Gael, um...mucho gusto"
    player_name "Ah, un gusto."
    show gael m normal s
    n "..."
    show gael m meh s
    n "Qué incómodo."
    n "Supones que es mejor romper el hielo que seguir fingiendo limpiar la barra en silencio."
    show gael m normal s

    menu:
      "Preguntar sobre el trabajo":
            player_name "Uhm, y entonces ¿desde cuando trabajas acá?"
            show gael m normal t
            g "De hecho, es negocio de mi familia. Así que desde hace tiempo supongo. Aunque ahorita estoy estudiando entonces ha sido un poco complicado el manejo."
            show gael m normal s

            menu:
                "Preguntar sobre su carrera":
                    player_name "Oh, y ¿qué estudias?"
                    show gael m normal t
                    g "Veterinaria. "
                    extend "En la Universidad de Miralta."
                    show gael m nervous2 t
                    g "...y creo que descubrí hoy que tú también estudias ahí, ¿verdad?"
                    show gael m normal s
                    player_name "Ah sí, estudió artes plásticas..."
                    n "Paraste en seco."
                    player_name "Aguanta…"
                    n "..."
                    n "..."
                    n "{b}{size=+10}!!!{/size}{/b}"
                    player_name "¡Así que si eras tú!"
                    show gael m nervous2 s at jumper
                    g "{b}{size=+10}!!!{/size}{/b}"
                    show gael m nervous2 t
                    g "Supongo que no soy un bueno ocultando cosas…"
                    extend "ja…"
                    show gael m nervous2 s
                    n "..."

                    menu:
                      "Y… ¿Qué tanto escuchaste?":
                            show gael m normal t
                            g "Bueno, no es como si te estuviera espiando ¿si?, solo estaba ahí pegando volantes y una cosa llevo a otra."
                            show gael m nervous t
                            g "Además que me halago saber que soy tu tipo"
                            show gael m nervous s

      "Preguntar sobre su carrera":
            player_name "Oh, y ¿qué estudias?"
            show gael m normal t
            g "Veterinaria. "
            extend "En la Universidad de Miralta."
            show gael m nervous2 t
            g "...y creo que descubrí hoy que tú también estudias ahí, ¿verdad?"
            show gael m normal s
            player_name "Ah sí, estudió artes plásticas..."
            n "Paraste en seco."
            player_name "Aguanta…"
            n "..."
            n "..."
            n "{b}{size=+10}!!!{/size}{/b}"
            player_name "¡Así que si eras tú!"
            show gael m nervous2 s at jumper
            g "{b}{size=+10}!!!{/size}{/b}"
            show gael m nervous2 t
            g "Supongo que no soy un bueno ocultando cosas…"
            extend "ja…"
            show gael m nervous2 s
            n "..."

            menu:
                      "Y… ¿Qué tanto escuchaste?":
                            show gael m normal t
                            g "Bueno, no es como si te estuviera espiando ¿si?, solo estaba ahí pegando volantes y una cosa llevo a otra."
                            show gael m nervous t
                            g "Además que me halago saber que soy tu tipo"
                            show gael m nervous s

    n "Gael se acerca a ti y te ofrece tu pago del día."
    show gael m normal t
    g "El punto es que... "
    g "Entiendo que este sea un trabajo rápido para tí, pero realmente creo que lo estás haciendo bien. Capaz y hasta ayudes a que este lugar sea más interesante."
    g "Así que…¿qué dices?"
    show gael m normal s
 
    menu:
     "Que verguenza, mejor renuncias":
         player_name "Lo siento, creo que será mejor hasta aquí."
         show gael m sad s
         n "Tomas las propinas de tu bolsillo."
         player_name "Aún así gracias."
         n "Dejas tu mandil en la barra, y te retiras avergonzado de la fonda."
         n "No puedes creer que te escuchó diciendo eso acerca de él."
         hide gael m sad s with dissolve
         scene Tienda with dissolve
         stop music fadeout 1.0
         n "Caminas por un rato, llegando a una gran papelería."
         n "Tomas de los pasillos algunos materiales para tu proyecto."
         n "Al llegar al cajero, mientras más artículos pasan, te das cuenta que el número de la cuenta incrementa más"
         extend "…y más."
         c "Bueno, va a ser $1550 pesos."
         n "{b}{size=+10}!!!{/size}{/b}"
         n "Tuviste que regresar más de la mitad de las cosas."
         n "No sabes como vas a poder entregar tu proyecto ahora."
         scene black with dissolve
         n "..."
         scene final 1 with dissolve
         n " "
         n "Has conseguido el final 1."
         return
         ####Final 1###

     "Te quedas":
         n "Sonreíste al escuchar sus palabras."
         player_name "Gracias, eres muy convincente ¿lo sabes?"
         hide gael m normal s with dissolve
         n "Continuas trabajando por un rato más. Clientes vienen y van. Parecía que el día sería bueno."
         n "Hasta que todo se arruinó."
         n "Un señor entra y se sienta enojado en una de las mesas de atrás."
         n "Tomas un respiro y te acercas. Sabías que este no sería como los otros clientes."
         show don s with dissolve
         player_name "Buenas tardes. Le entregó el menú-"
         show don t
         c1 "No, no. Dígame cuál es el especial."
         show don s
         player_name "A-Ah, bueno es una ensalada César."
         show don t
         c1 "¿César? ¿Quién es ese tal César?"
         show don s
         player_name "No, no. Así se llama la ensalada que tiene pollo y-"
         show don t
         c1 "¿Ensalada? ¿Acaso me dices gordo?"
         show don s
         play music "No.mp3"
         player_name "Ay, no. Espere, no me referia a eso. Es que ese es nuestro especial del día."
         show don t
         c1 "Creo que se muy bien lo que entendí, y ¡no voy a permitir que me falten el respeto de esta forma!"
         show don s at left with move
         show gael m meh t at right
         g "Disculpe, ¿Está todo bien aquí?"
         show don t at left
         show gael m meh s at right
         c1 "Su mesero resultó ser muy inútil, deberían ser más exigentes con las personas que contratan aquí."
         show don s at left
         player_name "A ver, yo no he hecho nada. Solo le explicaba el menú."
         show don t at left
         c1 "¡Ah! ¿Entonces me estás diciendo mentiroso?"
         show gael m angry s at right
         c1 "Debí suponer que no debía esperar tanto de una pocilga como está."
         show don s at left
         show gael m angry t at right
         g "Bueno, si no le gusta el menú. Hay bastantes lugares a dos cuadras que puede ir, donde sé que habrá comida más acorde a lo que busca."
         show don nerv s at left
         show gael m meh s at right
         c1 "{b}{size=+10}!!!{/size}{/b}"
         show don nerv t at left
         c1 "Ugh, que pésimo servicio…"
         hide don nerv t with dissolve
         play music "Cafeteria.mp3"
         show gael m nervous2 t at center with dissolve
         g "Ugh, con cosas como estas, entiendo el por que piensas en renunciar."
         show gael m normal t
         g "Pero, por favor no te desanimes. Al final todo se resolverá."
         show gael m blush t
         g "Y si no, vendré ayudarte cuantas veces ocupes"
         show gael m normal s
         n "No entendías por qué, pero sus palabras te ayudaron a tranquilizarte."
         n "Tal vez tenga razón. Nada va a ser tan malo."
         hide gael m normal s with dissolve
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_4

label hdia_3_pt2_normal:
    s "Ok \¿Y qué tiene que ver con tu trabajo?"
    hide sof normal t
    show asof normal s
    player_name "Pues resulta que es mi compañero de trabajo…"
    show asof shock t
    s "Ay no amix, esto ya parece Wittpad"
    show asof shock s
    player_name "No empieces Ana Sofí"
    hide asof shock s
    show sof shock t
    s "Es que, o sea"
    s "\¿Qué probabilidad hay de que eso te pase?"
    hide sof shock t
    show asof shock s
    player_name "La verdad ni se si me voy a quedar ahí por mucho tiempo."
    player_name "Tal vez hasta renuncie cuando junte para los materiales."
    show asof meh
    s "Ay [player_name], tu siempre tan \“positivo\”"
    show asof close2
    player_name "Es que no entiendes Sofí, es algo raro."
    show asof meh
    s "Si tu lo dices..."
    hide asof meh with dissolve
    n "Mientras regresabas al salón, observaste a alguien caminando del lado contrario."
    show gael n normal s with dissolve
    player_name "{i}{size=-10}¿Acaso es?{/size}{/i}"
    hide gael n normal s with dissolve
    player_name "{i}{size=-10}Creo que ya estoy alucinando cosas...{/size}{/i}"

    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Horas más tarde"
    n "Después de unas horas trabajando, finalmente encuentras un momento de descanso."
    d "Día pesado ¿eh?"
    n "Volteas a la dirección de la voz."
    show gael m normal s with dissolve
    player_name "…"
    show gael m nervous2 t
    a "{i}{size=-10}Público pesado…{/size}{/i}"
    show gael m nervous2 s
    a "{i}{size=-10}Cofcof{/size}{/i}"
    show gael m normal t
    a "Uhm…ahora que lo pienso, ni siquiera conozco tu nombre."
    show gael m normal s
    player_name "[player_name]. Mi nombre es [player_name]."
    n "..."
    show gael m normal t
    g "Bueno... el mio es Gael, um...mucho gusto"
    player_name "Ah, un gusto."
    show gael m normal s
    n "..."
    show gael m meh s
    n "Qué incómodo."
    n "Supones que es mejor romper el hielo que seguir fingiendo limpiar la barra en silencio."
    menu:
      "Preguntar sobre el trabajo":
            player_name "Uhm, y entonces ¿desde cuando trabajas acá?"
            show gael m normal t
            g "De hecho, es negocio de mi familia. Así que desde hace tiempo supongo. Aunque ahorita estoy estudiando entonces ha sido un poco complicado el manejo."
            show gael m normal s

            menu:
                "Preguntar sobre su carrera":
                    player_name "Oh, y ¿qué estudias?"
                    show gael m normal t
                    g "Veterinaria. "
                    extend "En la Universidad de Miralta."
                    show gael m nervous2 t
                    g "...y creo que descubrí hoy que tú también estudias ahí, ¿verdad?"
                    show gael m normal s
                    player_name "Ah sí, estudió artes plásticas..."
                    n "Paraste en seco."
                    player_name "Aguanta…"
                    n "..."
                    n "..."
                    n "{b}{size=+10}!!!{/size}{/b}"
                    player_name "¡Así que si eras tú!"
                    show gael m nervous2 s at jumper
                    g "{b}{size=+10}!!!{/size}{/b}"
                    show gael m nervous2 t
                    g "Supongo que no soy un bueno ocultando cosas…"
                    extend "ja…"
                    show gael m nervous2 s
                    n "..."

                    menu:
                      "Y… ¿Qué tanto escuchaste?":
                            show gael m normal t
                            g "Bueno, no es como si te estuviera espiando ¿si?, solo estaba ahí pegando volantes y una cosa llevo a otra."
                            show gael m nervous t
                            g "Además que me halago saber que soy tu tipo"
                            show gael m nervous s

      "Preguntar sobre su carrera":
            player_name "Oh, y ¿qué estudias?"
            show gael m normal t
            g "Veterinaria. "
            extend "En la Universidad de Miralta."
            show gael m nervous2 t
            g "...y creo que descubrí hoy que tú también estudias ahí, ¿verdad?"
            show gael m normal s
            player_name "Ah sí, estudió artes plásticas..."
            n "Paraste en seco."
            player_name "Aguanta…"
            n "..."
            n "..."
            n "{b}{size=+10}!!!{/size}{/b}"
            player_name "¡Así que si eras tú!"
            show gael m nervous2 s at jumper
            g "{b}{size=+10}!!!{/size}{/b}"
            show gael m nervous2 t
            g "Supongo que no soy un bueno ocultando cosas…"
            extend "ja…"
            show gael m nervous2 s
            n "..."

            menu:
                      "Y… ¿Qué tanto escuchaste?":
                            show gael m normal t
                            g "Bueno, no es como si te estuviera espiando ¿si?, solo estaba ahí pegando volantes y una cosa llevo a otra."
                            show gael m nervous t
                            g "Además que me halago saber que soy tu tipo"
                            show gael m nervous s

    n "Gael se acerca a ti y te ofrece tu pago del día."
    show gael m normal t
    g "El punto es que... "
    g "Entiendo que este sea un trabajo rápido para tí, pero realmente creo que lo estás haciendo bien. Capaz y hasta ayudes a que este lugar sea más interesante."
    g "Así que…¿qué dices?"
    show gael m normal s

    menu:

     "Mejor renuncias":
         player_name "Lo siento, creo que será mejor hasta aquí."
         show gael m sad s
         n "Tomas las propinas de tu bolsillo."
         player_name "Aún así gracias."
         n "Dejas tu mandil en la barra, y te retiras tranquilamente de la fonda"
         hide gael m sad s with dissolve
         scene Tienda with dissolve
         stop music fadeout 1.0
         n "Caminas por un rato, llegando a una gran papelería."
         n "Tomas de los pasillos algunos materiales para tu proyecto."
         n "Al llegar al cajero, mientras más artículos pasan, te das cuenta que el número de la cuenta incrementa más"
         extend "…y más."
         c "Bueno, va a ser $1550 pesos."
         n "{b}{size=+10}!!!{/size}{/b}"
         n "Tuviste que regresar más de la mitad de las cosas."
         n "No sabes como vas a poder entregar tu proyecto ahora."
         scene black with dissolve
         n "..."
         scene final 1 with dissolve
         n " "
         n "Has conseguido el final 1."
         return
         ####Final 1###

     "Te quedas":
         n "Sonreíste al escuchar sus palabras."
         player_name "Gracias, eres muy convincente ¿lo sabes?"
         hide gael m normal s with dissolve
         n "Continuas trabajando por un rato más. Clientes vienen y van. Parecía que el día sería bueno."
         n "Hasta que todo se arruinó."
         n "Un señor entra y se sienta enojado en una de las mesas de atrás."
         n "Tomas un respiro y te acercas. Sabías que este no sería como los otros clientes."
         show don s with dissolve
         player_name "Buenas tardes. Le entregó el menú-"
         show don t
         c1 "No, no. Dígame cuál es el especial."
         show don s
         player_name "A-Ah, bueno es una ensalada César."
         show don t
         c1 "¿César? ¿Quién es ese tal César?"
         show don s
         player_name "No, no. Así se llama la ensalada que tiene pollo y-"
         show don t
         c1 "¿Ensalada? ¿Acaso me dices gordo?"
         play music "No.mp3"
         show don s
         player_name "Ay, no. Espere, no me referia a eso. Es que ese es nuestro especial del día."
         show don t
         c1 "Creo que se muy bien lo que entendí, y ¡no voy a permitir que me falten el respeto de esta forma!"
         show don s at left with move
         show gael m meh t at right
         g "Disculpe, ¿Está todo bien aquí?"
         show don t at left
         show gael m meh s at right
         c1 "Su mesero resultó ser muy inútil, deberían ser más exigentes con las personas que contratan aquí."
         show don s at left
         player_name "A ver, yo no he hecho nada. Solo le explicaba el menú."
         show don t at left
         c1 "¡Ah! ¿Entonces me estás diciendo mentiroso?"
         show gael m angry s at right
         c1 "Debí suponer que no debía esperar tanto de una pocilga como está."
         show don s at left
         show gael m angry t at right
         g "Bueno, si no le gusta el menú. Hay bastantes lugares a dos cuadras que puede ir, donde sé que habrá comida más acorde a lo que busca."
         show don nerv s at left
         show gael m meh s at right
         c1 "{b}{size=+10}!!!{/size}{/b}"
         show don nerv t at left
         c1 "Ugh, que pésimo servicio…"
         hide don nerv t with dissolve
         show gael m nervous2 t at center with dissolve
         play music "Cafeteria.mp3"
         g "Ugh, con cosas como estas, entiendo el por que piensas en renunciar."
         show gael m normal t
         g "Pero, por favor no te desanimes. Al final todo se resolverá."
         show gael m blush t
         g "Y si no, vendré ayudarte cuantas veces ocupes"
         show gael m normal s
         n "No entendías por qué, pero sus palabras te ayudaron a tranquilizarte."
         n "Tal vez tenga razón. Nada va a ser tan malo."
         hide gael m normal s with dissolve
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_4

label hdia_4:
    scene Cuarto with dissolve
    n "Después de un día complicado como el anterior, hoy habías decidido que este sería tranquilo."
    scene Tienda
    play music "Park.mp3"
    n "Con el dinero que habías ganado en tus primeros días de trabajo, estabas listo para darle un buen uso."
    n "Miraste por cada rincón, tachando cada material que habías anotado para tu proyecto."
    player_name "Uhm… este ya, y este también…"
    n "Pasaron unos minutos para que estuvieras frente al mostrador con todo lo necesario."
    play sound "Cash.mp3"
    n "No esperabas que esta mañana fuera tan eficiente."
    scene Park with dissolve
    n "Solo estabas tú y tus pensamientos. Hasta que una voz entre risas interrumpió tu calma."
    play music "No.mp3"
    d "¡Hey tranquilos!"
    show gael d nervous2 s with dissolve
    player_name "¿Gael?"
    hide gael d nervous2 s with dissolve
    n "No puedes ni confirmar tus sospechas, porque observas a un perro correr hacia ti."
    show momo run with dissolve
    play sound "crash.mp3"
    g "¡Ay no! ¿Estas bien-"
    hide momo run with dissolve
    show gael d shock with dissolve
    g "\¿[player_name]?"
    show gael d sad s
    n "Empiezas a recobrar la visión. Mientras sientes al perro lamiendo tu mejilla."
    g "Gael agarra al perro, separándolo de ti."
    show gael d shock
    g "{i}{size=-10}Chin…{/i}{/size}"
    n "Miras a la dirección que Gael ve."
    n "Todos tus materiales... "
    extend "estan arruinados."
    show gael d sad t at left with move
    show momo sad at right
    g "¡Perdóname!"
    n "Gael te ofrece su mano para ayudarte a levantarte."
    g "¿Costaron mucho?"

    menu:
     "No aceptas su mano":
         show gael d shock at left
         n "Golpeas su mano."
         n "Te levantas, sacudiendote el lodo."
         n "En silencio tomás tus materiales arruinados, con el poco orgullo que te queda."
         show gael d sad s at left
         player_name "No necesito la ayuda de alguien tan torpe."
         n "Lo miras de reojo."
         show gael d shock at left
         player_name "De seguro por eso estás en dos trabajos."
         hide gael d shock with dissolve
         hide momo sad with dissolve
         n "Gael te mira sorprendido, mientras te retiras del lugar."
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_5_normal

     "Aceptas su mano":
         play music "Happyending.mp3"
         hide momo sad with dissolve
         show gael d sad s at center with move
         n "Gael te ayuda a levantarte con cuidado, se le ve bastante apenado."
         player_name "Pues si costaron un poco, ¡pero no te preocupes!"
         show gael d sad t
         g "No creo que haya sido solo “un poco”..."
         show gael d sad t at left with move
         show momo sad at right with dissolve
         g "De verdad lo siento mucho, Momo es bastante fuerte cuando se emociona."
         g "Y cuando menos me di cuenta, su correa se zafó de mi mano."
         show gael d sad s at left
         n "Momo te ve con ojitos de culpa."
         hide gael d sad s with dissolve
         show momo sad at center with move
         player_name "Está bien, son cosas que a veces pasan."
         show momo happy
         n "Comienzas a acariciar la cabeza de Momo para calmarla."
         player_name "Solo esperó poder rescatar algunos de los materiales."
         hide momo happy with dissolve
         show gael d sad s
         n "Gael te ayuda a levantar los materiales."
         show gael d sad t
         g "De verdad lo siento tanto, esperó poder compensartelo."
         hide gael d sad t with dissolve
         show momo happy with dissolve
         n "Los perritos comienzan a jalar las correas en las manos de Gael."
         n "No puedes enojarte con ellos."
         show momo happy at right with move
         show gael d sad s at left
         player_name "Creo que quieren continuar su paseo. Y yo debo regresar a mi casa."
         show gael d sad t at left
         g "Pero-"
         show gael d sad s at left
         n "Solo pudiste sonreir levemente."
         player_name "Nos vemos mañana"
         n "Te despides con tu mano y te alejas del lugar."
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_5_good

label hdia_5_good:
    scene Uni In with dissolve
    play music "Uni.mp3"
    n "Otro día, una nueva clase con la profesora Marta."
    show marta normal t with dissolve
    m "Bueno jovenes, ¿les parece si damos un pequeño descanso de 15 minutitos?"
    show marta normal s
    n "Algunos de tus compañeros asienten."
    show marta normal t
    m "Bueno, entonces nos vemos más tarde con sus materiales."
    show marta normal s
    player_name "{i}{size=-10}Chin…{/i}{/size}"
    hide marta normal s with dissolve
    scene Uni Out with dissolve
    play music "Park.mp3"
    n "Con pasos preocupados fuiste a la máquina expendedora."
    n "Aunque trataste toda la noche de recuperar algo de tus materiales, simplemente fue imposible."
    n "Lo único que llevaste era un lienzo cubierto de lodo y patitas, unos pinceles y pinturas dañadas."
    n "Nada iba como el plan."
    n "Pasaron algunos de tus compañeros con sus materiales a sus costados. "
    extend "Estaban en perfecto estado."
    player_name "Ugh…"
    n "Te recargas en la máquina decepcionada."
    player_name "¿Y ahora qué voy a hacer…?"
    n "Mientras te lamentas, escuchas unos pasos apurados acercándose."
    show gael s run with dissolve
    play music "Happyending.mp3"
    n "Se detuvo frente a ti por un momento, agarrando aire."
    hide gael s run
    show gael n normal t
    n "Tan pronto volvió en sí, miró contento."
    g "¡Tatan! ¡He llegado a salvarte!"
    show gael n normal s
    n "No pude evitar mirar curiosa aquella escena."
    n "Gael te muestra una bolsa de compras."
    player_name "{b}{size=+10}!!!{/size}{/b}"
    n "Eran los materiales. Estaban perfectos."
    player_name "¿Pero cómo-"
    show gael n normal t
    g "Digamos que no me gusta quedarme de brazos cruzados."
    show gael n sad t
    g "No es justo que todo tu esfuerzo sea en vano, además que fue mi culpa."
    show gael n normal s
    n "No podías creerlo."
    show gael n normal t
    g "Por favor tomalos."
    show gael n blush s
    player_name "Muchas gracias, de verdad gracias"
    n "Escuchas algunas voces cerca."
    show gael n nervous2 t
    g "Ay, debo regresar a mi clase."
    show gael n normal t
    g "¡Nos vemos en el trabajo!"
    hide gael n normal t with dissolve
    n "Te quedas estatico por unos segundos tratando de entender la situación."
    n "Miraste los materiales con una gran sonrisa."
    scene Uni In with dissolve
    play music "Uni.mp3"
    n "Regresaste al salón, esta vez más seguro."
    show marta normal s
    n "La profesora se acerca a cada uno. Cuando llega contigo su rostro se le ve sorprendido."
    show marta normal t
    m "¡Vaya, esa es una muy buena marca! Solo debes dejar un poco más de tiempo secar la primera capa si no se estropea."
    m "Esperó ver sus bocetos pronto."
    hide marta normal s with dissolve
    n "La profesora se fue con otro alumno."
    n "El día realmente se arregló. Continuaste tu rutina del día."
    scene Fondita In with dissolve
    play music "happyending.mp3"
    n "Una vez en el trabajo, todos los clientes notaban tu alegría. "
    extend "Fue un buen día de propinas."
    n "Así como no parabas de agradecerle a Gael, por su ayuda. Realmente si te había salvado."
    scene Cuarto with dissolve
    n "Finalmente, llegaste a tu casa a dormir."
    scene black with dissolve
    stop music fadeout 1.0
    jump hdia_6_good

label hdia_5_normal:
    scene Uni In with dissolve
    play music "Uni.mp3"
    n "Otro día, una nueva clase con la profesora Marta."
    show marta normal t with dissolve
    m "Bueno jovenes, ¿les parece si damos un pequeño descanso de 15 minutitos?"
    show marta normal s
    n "Algunos de tus compañeros asienten."
    show marta normal t
    m "Bueno, entonces nos vemos más tarde con sus materiales."
    show marta normal s
    player_name "{i}{size=-10}Chin…{/i}{/size}"
    hide marta normal s with dissolve
    scene Uni Out with dissolve
    play music "Park.mp3"
    n "Con pasos preocupados fuiste a la máquina expendedora."
    n "Aunque trataste toda la noche de recuperar algo de tus materiales, simplemente fue imposible."
    n "Lo único que llevaste era un lienzo cubierto de lodo y patitas, unos pinceles y pinturas dañadas."
    n "Nada iba como el plan."
    n "Pero no podías hacer nada más."
    player_name "Ugh… ¿y ahora que voy a hacer? "
    show Uni In with dissolve
    play music "Sadend.mp3"
    n "Resignado regresaste al salón. No iba a ser el mejor proyecto, pero algo era mejor que nada."
    n "Cuando llegas a la clase, miras a los demás con sus materiales en perfecto estado."
    n "Qué vergüenza…"
    show marta question with dissolve
    n "La profesora se acerca a cada uno. Cuando llega contigo su rostro amable muestra desaprobación."
    show marta angry t
    m "[player_name], si no está interesado en la clase puede retirarse."
    show marta angry s
    n "Escuchaste algunas risas y susurros de los demás."
    n "Solo tomas tus cosas y sales de lugar."
    scene Uni Out with dissolve
    player_name "¡Agh! ¡Todo es su culpa!"
    scene Fondita In with dissolve
    n "Continuaste tu rutina del día. Una vez en el trabajo, sentiste las horas interminables."
    n "Cada vez que Gael trataba de acercarse a decir algo solo lo ignorabas."
    n "Los clientes percibieron tu mal humor."
    n "No fue para nada un muy buen día."
    scene Cuarto with dissolve
    n "Finalmente, llegaste a tu casa a dormir."
    scene black with dissolve
    jump hdia_6_normal

label hdia_6_good:
    scene Uni Out with dissolve
    play music "Park.mp3"
    n "Un nuevo día empezó."
    n "Mientras caminabas a tu salón, Ana Sofi se acercó a ti."
    show asof normal t with dissolve
    s "\¡[player_name]! \¿Cómo estás? Cuéntame sobre tu ligue, \¿todo ha ido bien?"
    show asof normal s
    player_name "¿Ligue? ¿De qué hablas?"
    show asof happy t
    s "Ay, ya sabes del chico de la fondita."
    show asof happy s
    n "No pudiste evitar sonreír al recordarlo."
    player_name "Bueno, supongo que bien."
    hide asof happy s
    show sof happy t
    s "¡Oh oh! ¿[player_name] sonriendo? Eso sí es noticia."
    show sof happy s
    n "Solo pudiste golpear su hombro suavemente. Pero no lo negabas, realmente es nuevo esto en ti."
    show sof happy t
    s "¡Pero por qué lo cortas! ¡Dime qué ha pasado entre ustedes!"
    show sof happy s
    player_name "Bueno, es que han pasado tantas cosas…"
    show sof nervous t
    s "¿En una semana?"
    hide sof nervous t
    show asof happy s
    player_name "Primero, se presentó un cliente de lo más horrendo en el lugar."
    s "Ajá"
    player_name "Se enojó de repente, y me quería hacer bronca. Pero por suerte Gael estaba ahí para ayudarme. Pareciera qué ya es algo normal entre los dos."
    s "¿Por?"
    player_name "Bueno, es que no se queda ahí. Digamos por su culpa se me estropearon los materiales que compré."
    show asof shock s at jumper
    s "{b}{size=+10}!!!{/size}{/b}"
    player_name "¡Fue totalmente un accidente! Resulta que no solo trabaja en la fondita, si no que también cuida perritos muy bonitos, pero a veces son… bueno un poco intensos."
    show asof happy s
    player_name "Pero, él fue muy gentil. Incluso me compró nuevo material para reponer los otros."
    hide asof happy s
    show sof happy t
    s "¡Ay pero qué divino! Yo sabía que mi presentimiento era correcto, a este paso vas a tener novio nuevo."
    show sof happy s
    player_name "No se si novio, pero sin duda me estoy llevando muy bien con él."
    n "Entre risas y cuchicheos van juntos al salón."
    hide sof happy t with dissolve
    scene Uni In with dissolve
    play music "Uni.mp3"
    n "En el salón."
    show marta normal t with dissolve
    m "Bueno chicos, ya tenemos que iniciar el proyecto final, porque la exposición se acerca."
    m "Así que ya es tiempo de empezar a considerar el tema de su pintura."
    m "Recuerden que se va contemplar todo en mi evaluación, así que espero que en esta hora de clase puedan revisar o cuestionar lo que quieren comunicar."
    m "Hagan lo que consideren necesario."
    hide marta normal t with dissolve
    player_name "{i}{size=-10}Uhm… un tema…{/i}{/size}"
    n "La profesora parecía notar la confusión en la cara de algunos de sus estudiantes, incluyéndote."
    show marta normal t with dissolve
    m "Bueno, no había pensado usarlos, pero creo que es lo más conveniente."
    n "Comienza a escribir dos propuestas en el pizzarón."
    m "Si consideran necesario, usenlas sin ningún inconveniente."
    n "No dudaste mucho en mirarlas. Parece ser la mejor forma de elegir en este punto."
    n "Elije sabiamente."
    menu:
     "Prefieres dar tu toque a algo existente":
         n "Satisfecho de tu elección, te retiras a tu casa para comenzar a bocetar."
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_7_good_1

     "Prefieres dar a conocer tus emociones":
         n "Satisfecho de tu elección, te retiras a tu casa para comenzar a bocetar."
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_7_good_2

label hdia_6_normal:
    scene Uni Out with dissolve
    play music "Park.mp3"
    n "Un nuevo día empezó."
    n "Mientras caminabas a tu salón, Ana Sofi se acercó a ti."
    show asof normal t with dissolve
    s "\¡[player_name]! \¿Cómo estás? Cuéntame sobre tu ligue, \¿todo ha ido bien?"
    show asof normal s
    player_name "¿Ligue? ¿De qué hablas?"
    show asof happy t
    s "Ay, ya sabes del chico de la fondita."
    show asof shock s
    player_name "\¡Ugh! \¡Ni me lo menciones!"
    show asof shock t
    s "\¿Uhm? \¿Y eso?"
    show asof shock s
    player_name "\¿Por dónde comienzo?"
    player_name "Por su culpa se me estropearon todos los materiales, la profe me echó de su clase y el trabajo solo ha sido cada vez más incómodo."
    player_name "¡UGH! ¡Me urge renunciar!"
    show asof meh
    s "Ay [player_name]..."
    show asof serious t
    s "¿Y ni siquiera se ha disculpado o algo?"
    show asof serious s
    player_name "Ni le he dejado que lo haga. No quiero oír ni una palabra de él."
    show asof serious t
    s "Qué mal [player_name], y yo que creía que ya hasta novio tendrías."
    show asof serious s
    player_name "¡Primero muerto!"
    hide asof serious s with dissolve
    n "A paso enojado, te vas a tu salón."
    scene Uni In with dissolve
    play music "Uni.mp3"
    n "En el salón."
    show marta normal t with dissolve
    m "Bueno chicos, ya tenemos que iniciar el proyecto final, porque la exposición se acerca."
    m "Así que ya es tiempo de empezar a considerar el tema de su pintura."
    m "Recuerden que se va contemplar todo en mi evaluación, así que espero que en esta hora de clase puedan revisar o cuestionar lo que quieren comunicar."
    m "Hagan lo que consideren necesario."
    hide marta normal t with dissolve
    player_name "{i}{size=-10}Uhm… un tema…{/i}{/size}"
    n "Solo mirabas una y otra vez los pocos lápices rotos que tenias a la mano. Tampoco era como si pudieras hacer algo bueno con esto."
    n "…"
    n "Lo mejor será solo fluir con lo que salga."
    n "Un poco desanimado te retiras del salón."
    scene black with dissolve
    stop music fadeout 1.0
    jump hdia_7_bad

label hdia_7_bad:
    scene Fondita In with dissolve
    play music "No.mp3"
    n "Hoy como cada tarde te toca trabajar en la fondita."
    n "Sin embargo, hoy ha sido un día bastante ajetreado."
    n "Clientes han llegado, llenando el local desde temprano, haciendo que ya ni recuerdes de que mesa era cada orden."
    show man with dissolve
    c2 "¡¿Qué le pasa?! ¡Le dijimos que sin cacahuate!"
    player_name "Ay lo siento mucho, déjeme cambiarlo"
    c2 "Más le vale, y esperamos que sea gratis."
    hide man with dissolve
    show woman with dissolve
    c3 "Disculpe, nos pasa la salsa de cacahuate que le pedimos hace rato."
    hide woman with dissolve
    n "Este es un día muy pesado"
    show gael m sad t with dissolve
    g "¿Oye ocupas ayuda?"
    show gael m sad s

    menu:
     "Te niegas a su ayuda.":
         show gael m shock
         player_name "Ugh… \“más ayuda el que no estorba”."
         hide gael m shock with dissolve
         n "Te das la vuelta, solo puedes confiar en ti."
         n "{b}Horas más tarde.{/b}"
         n "No puedes ni confiar en ti."
         n "Ya van dos clientes que se han quejado del servicio, e incluso han puesto malas reseñas en gugule."
         n "No vas a durar mucho aquí…"
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_8_bad

     "Aceptas su ayuda.":
         play music "Cafeteria.mp3"
         n "Solo asientes agotado."
         n "Como si fuera magia, Gael empezó a ir en cada mesa y atendió a todos con una sonrisa."
         n "Realmente se notaba su experiencia."
         n "Seguiste sus indicaciones y en unas horas, la tranquilidad volvió a reinar en la fondita."
         n "Con los dos casi solos, sabías que era buen momento para hablar."
         player_name "Uhm, oye…muchas gracias por lo de antes."
         g "Ah no es nada, sigues aprendiendo, es razonable que aún te cueste en momentos."
         n "No pudiste evitar mostrar una ligera sonrisa."
         player_name "y… ¿Tienes consejos para tratar con clientes…uhm…ya sabes-"
         g "\¿Difíciles?"
         g "Bueno, hay que mantenernos tranquilos aunque el cliente parezca como un loco."
         g "Solo si es {b}muy{/b} necesario, debemos ser firmes y pedir que se retiren."
         player_name "¿Cómo lo hiciste hace unos días?"    
         n "Reiste un poco al recordarlo."
         player_name "Parecías una persona diferente con tu cara toda seria."    
         g "¡Oye! ¿Así agradeces que te salve ese día?"
         n "Después de eso, la conversación dejó de ser tan formal."
         n "¿Quién diría que podrías llegar a llevarte bien con Gael?"
         n "El fin de tu turno llegó y mientras caminabas a casa sentiste que tal vez, si podrías llegar a ser un buen amigo aquel chico."
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_8_norm_3

label hdia_8_bad:
    scene Uni Out with dissolve
    play music "Park.mp3"
    show asof normal s with dissolve
    n "Caminando por la Universidad, te topaste con Sofí."
    show asof normal t
    s "¿Entonces cómo va tu pintura?"

    show asof shock s
    player_name "Terrible, no tengo mucho y con los materiales que tengo no me llega ni una inspiración."
    show asof meh
    s "Ay [player_name]..."
    hide asof meh with dissolve

    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Después de clases fuiste a trabajar en la fondita. Esta vez no había tanta gente."
    n "Sin embargo, no parabas de notar la mirada constante de una chica."
    show loca miedo with dissolve
    d "..."
    player_name "{b}{size=+10}???{/size}{/b}"
    n ". "
    extend ". "
    extend "."
    show loca meh t
    d "\¡AY POR FAVOR!"
    show loca diuk
    n "La chica se acerca a ti apresuradamente."
    show loca meh t
    d "No captas indirectas \¿o qué?"
    show loca diuk
    player_name "{i}¿Y esta intensa qué?{/i}"
    player_name "Uh… \¿Se te ofrece algo?"
    show loca meh t
    d "¿El chico que trabaja contigo es tu novio?"
    show loca meh s

    player_name "NO"
    player_name "¿Ese tipo? Nah, solo colegas y eso…"
    show loca smile s
    n "La chica suspira alegre. Parece que se quitó un gran peso de encima."
    show loca blush t
    d "¡Ay que alivio! Entonces…"
    d "No te importaría pasarme su número ¿verdad? Es que es taaan lindoo"
    show loca blush s
    n "DIUK"
    player_name "a"

    menu:
     "Dárselo":
         n "Tomas una servilleta cercana y anotas el número de Gael como si nada."
         n "La chica se veía más que contenta."
         show loca blush t
         d "Ay muchas gracias de veras ¡Eres el mejor!"
         n "La chica te mira por unos segundos."
         show loca miedo
         d "Aún así trata de no acercarte tanto a él, \¿oíste?"
         hide loca miedo with dissolve
         n "Así con el papel en sus manos se empezó a alejar de ti."
         player_name "{i}Vaya rara…{/i}"
         n "Gael salió de la cocina y fue a atender la mesa de la chica."
         show loca blush t at left with dissolve
         show gael m nervous2 s at right with dissolve
         n "Parecía tan contenta, que hasta daba miedo."
         n "Pero bueno, ahora es problema de Gael, que lo solucione como pueda."
         hide loca blush t with dissolve
         hide gael m nervous2 s with dissolve
         n "Así el día pasó rápidamente."
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_9_bad

     "No dárselo":
         n "Niegas con tu cabeza."
         show loca meh s at jumper
         player_name "Nah, si lo quieres consíguelo por tu cuenta, niña."
         show loca angry s
         n "La chica se le ve muy enfadada."
         show loca meh t
         d "¡¿Cómo te atreves?! Eres un envidioso, de seguro te gusta, pero qué crees…"
         d "Él conmigo estará mejor."
         show loca angry s
         n "Así la chica regresa a su mesa. No mentiras, se veía muy graciosa enojada."
         hide loca angry s with dissolve
         player_name "{i}Vaya rara…{/i}"
         n "Gael salió de la cocina y fue a atender la mesa de la chica."
         show loca blush t at left with dissolve
         show gael m nervous2 s at right with dissolve
         n "Parecía tan contenta, que hasta daba miedo."
         n "Pero bueno, ahora es problema de Gael, que lo solucione como pueda."
         hide loca blush t with dissolve
         hide gael m nervous2 s with dissolve
         n "Así el día pasó rápidamente."
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_9_bad

label hdia_9_bad:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    n "Es un nuevo día."
    n "Mañana es la exposición en la galería, por lo que decidiste tomarte toda la mañana para acabar tu pintura."
    n "A pesar de haber tenido días para hacerlo, apenas lo vas a comenzar."
    n "Decidiste que era mejor culpar a los materiales que a tu poca organización por días."
    n "Pero bueno, aún así debes entregar algo."
    player_name "Que sea lo que dios quiera…"
    jump hgame_3

label hgame_3:
    play music "Park.mp3"
    $ hsetup_puzzle3()
    call screen hreassemble_puzzle3

label hdia_9_bad_p2:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    show p3 with dissolve
    player_name "Bueno… no es mucho, pero es un trabajo honesto."
    n "Ay ajá."
    hide p3 with dissolve
    player_name "Como sea, es hora de trabajar, ya no queda de otra…"
    scene Fondita Out  with dissolve
    play music "Sadend.mp3"
    n "Al llegar a la fondita te das cuenta que Gael está cerrando."
    show gael n sad s with dissolve
    n "Pero apenas son las 2 de la tarde…"
    player_name "¿Gael? ¿Qué significa esto?"
    show gael n sad t
    g "Oh [player_name], uh… bueno."
    show gael n sad s
    n "Parecía tratar de ordenar sus ideas en su cabeza. Era raro verlo tan agobiado, en vez de su tonta sonrisa."
    show gael n sad t
    g "Creo que tendrás que conseguir otro trabajo después de todo."
    show gael n sad s
    player_name "{b}{size=+10}???{/size}{/b}"
    show gael n sad t
    g "La fondita no ha tenido una muy buena recepción. Las reseñas y la gente parece que solo se quejan del servicio, y pues bueno, no es muy bueno para el local ¿sabes?"
    show gael n sad s
    n "Oh…"
    show gael n nervous2 t
    g "Así que, ¡Hey! al menos ya vas a lograr dejar de trabajar aquí"
    show gael n nervous2 s
    player_name "Ha… si…"
    show gael n sad t
    g "Pero no te preocupes, esto no es tu culpa."
    show gael n sad s
    n "Por unos segundos solo parecía haber un silencio incómodo entre ambos."
    n "..."
    n "Espera…"
    n "Esto se debe a…"
    n "Si es…"
    play music "No.mp3"
    player_name "Tienes razón, esto no es mi culpa…"
    show gael n shock at jumper
    player_name "¡Esto es {b}tú{/b} culpa!"
    g "\¿Qué-"
    player_name "¡Por tu culpa los dos nos quedamos sin nada! De seguro atendiste mal a los clientes y por eso es que está pasando esto."
    show gael n angry t
    g "A ver esperate yo-"
    show gael n angry s
    player_name "¡¿En qué estabas pensando?! ¡No te basta con arruinar mi vida! ¡¿sino que también la de tu familia?!"
    show gael n angry t
    g "\¿De qué estás hablando-"
    show gael n angry s
    player_name "Primero mis materiales, tu actitud, tus odiosos clientes que para colmo están obsesionados contigo."
    show gael n sad t
    g "Espera ¿Qué-"
    player_name "{b}¡No me interrumpas!{/b}"
    show gael n shock
    g "..."
    player_name "¡Es que de verdad! ¡¿Cómo puedes ser tan odioso?!"
    show gael n sad s
    n "Suspiras pesadamente, y te das la media vuelta."
    player_name "No me vuelvas a hablar en la vida."
    player_name "Y más te vale que no te aparezcas frente a mi en la Uni."
    player_name "¡AGH!"
    hide gael n sad s with dissolve
    n "Simplemente sujetas bien tu mochila y te vas lejos de ahí."
    scene black with dissolve
    stop music fadeout 1.0
    jump hFinalMalo

label hFinalMalo:
    scene Gallery with dissolve
    play music "Gallery.mp3"
    n "Después de unas largas semanas, finalmente llegó el día."
    n "Toda tu clase estaba reunida en la galería con sus trabajos listos para exponer."
    n "La profesora Marta incluso se vistió para la ocasión."
    n "Cada alumno tenía que mostrarle sus trabajos antes de exponerlos, así sabrías tu nota final y solo disfrutarías el evento."

    n "O eso harías si no vieras claramente que tu trabajo era el peor del salón."
    player_name "{i}Bueno, la profa no suele ser tan cruel, o eso dicen…{/i}"
    n "Mientras más te acercabas tu ansiedad crecía, y no ayudaba el hecho que la chica frente a ti tenía un trabajo de museo."
    show marta normal t with dissolve
    m "¡La siguiente persona por favor!"
    show marta normal s
    player_name "{i}Hasta acá llegue en la Uni…{/i}"
    n "Con vergüenza mostraste tu pintura a la profesora."
    show marta annoyed
    play music "Sadend.mp3"
    n "No tenías que ser un genio para adivinar que su rostro alegre se volvería uno incrédulo."
    m "[player_name], ¿es enserio? ¿Este es tu trabajo?"
    player_name "…"
    m "Jovencito, tuvo el mismo tiempo y oportunidades que todos aquí presentes y lo único que se le ocurrió hacer ¿fue esto?"
    n "Sentías las miradas de tus compañeros en ti. Sabías que era mala, pero no era tu culpa ¿verdad?"
    player_name "Profesora, entiendame, mis materiales se arruinaron y esto es lo mejor que podía hacer con ellos-"
    m "No se justifique de esa forma. Usted sabe muy bien que los materiales no definen al artista."
    n "Te quedaste en silencio."
    m "No quería creer lo que sus otros profesores hablan de usted, pero veo que tienen razón."
    m "No debía esperar mucho de usted."
    n "La profesora solo te devolvió tu pintura."
    n "Risas, murmullos y miradas."
    scene black with dissolve
    n "Era de esperarse que te reprobara unos días después."
    n "Todo salió mal."
    n "Estas a una materia reprobada de ser expulsado de la carrera, no tienes ni trabajo para sacar aunque sea un poco de dinero."
    n "Todo genuinamente salió mal."
    n "Y todo…"
    player_name "Fue culpa de ese odioso…"
    scene final 2 with dissolve
    n " "
    n "Has conseguido el final malo."
    stop music fadeout 1.0
    return
    ####Final Malo###

label hdia_7_good_1:
    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Hoy como cada tarde en los últimos días, te toca trabajar en la fondita."
    n "A pesar de ser un día ajetreado, Gael te ha hecho compañía."
    n "Clientes han llegado, llenando el local desde temprano. Por suerte todo ha fluido tranquilamente."
    n "Después de atender algunas mesas y clientes complicados, finalmente pudiste tomar un descanso."
    n "Aprovechaste unos asientos vacíos en el fondo."
    show gael m normal t with dissolve
    g "¡Hey, aquí estabas!"
    show gael m normal s
    player_name "¿uh? ¿Llegaron más clientes?"
    show gael m blush2 t
    g "¡Oh no, no! Solo quería hablar contigo."
    show gael m normal t
    g "¿Cómo te has sentido estos días? Sé que no es un trabajo tan fácil como puede parecer."
    show gael m normal s
    player_name "Pues…¿bien supongo? Si ha sido algo agotador pero eso no me va a desanimar."
    player_name "Al fin y al cabo, voy a quedarme aquí un rato, entonces…"
    show gael m normal t
    g "Me alegra escuchar eso"
    show gael m nervous2 t
    g "Por un segundo creí que otra vez ibas a querer renunciar."
    show gael m nervous2 s
    n "No pudiste evitar mostrar una ligera sonrisa, realmente sigue pensando en ello."
    n "A pesar de que el silencio era agradable, era mejor sacar un tema."
    menu:
     "Preguntar sobre el trabajo":
         player_name "y… ¿Tienes consejos para tratar con clientes…uhm…ya sabes-"
         show gael m nervous2 t
         g "¿Difíciles?"
         show gael m nervous2 s
         n "Asientes lentamente."
         show gael m normal t
         g "Bueno, hay que mantenernos tranquilos aunque el cliente parezca como un loco."
         show gael m angry t
         g "Solo si es {b}muy{/b} necesario, debemos ser firmes y pedir que se retiren."
         show gael m meh s
         player_name "¿Cómo lo hiciste hace unos días?"  
         show gael m nervous s
         n "Reiste un poco al recordarlo."
         player_name "Parecías una persona diferente con tu cara toda seria." 
         show gael m blush t
         g "¡Oye! ¿Así agradeces que te salve ese día?"
         show gael m blush s
         n "Después de eso, la conversación dejó de ser tan formal."
         n "¿Quién diría que podrías llegar a llevarte bien con Gael?"
         hide gael m blush s with dissolve
         n "El fin de tu turno llegó y mientras caminabas a casa sentiste que tal vez, si podría llegar a ser un buen amigo aquel chico."
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_8_norm_1

     "Preguntar sobre los perritos":
         player_name "y… Tienes dos trabajos ¿verdad?"
         show gael m nervous t
         g "Oh, cierto me viste ese día…"
         show gael m nervous s
         player_name "¿En qué trabajas en sí? ¿Paseas perritos, los cuidas o qué?"
         show gael m normal t
         g "Bueno, digamos que son como prácticas pero no exactamente."
         show gael m normal s
         player_name "{b}{size=+10}???{/size}{/b}"
         show gael m normal t
         g "Conozco a un doctor que tiene su clínica cerca, siempre ha llamado mi atención los animales desde pequeño y él siempre fue muy amable introduciéndome al campo."
         show gael m nervous t
         g "De hecho hasta me echa la mano para estudiar para mis exámenes."
         show gael m blush t
         g "Regresando al trabajo, entre platica y platica sacó el tema de que quería empezar un servicio extra. Una cosa llevó a la otra y ahora paseo perritos entre semana."
         g "Sirve para practicar y el dinero extra siempre es bien recibido."
         show gael m blush s
         n "Era agradable ver a Gael tan emocionado, normalmente solo hablaban de la fondita. Parece que genuinamente disfruta su carrera."
         player_name "Entonces paseas muchos perritos, me pregunto si tendrás uno favorito."
         show gael m nervous2 t
         g "¡Hey, eso es como poner a decidir quién es tu hijo favorito!"
         show gael m nervous2 s
         g "..."
         show gael m normal t
         g "Aunque tal vez sí tenga…"
         show gael m normal s
         player_name "¡Dime, dime!"
         show gael m nervous2 t
         g "Si somos honestos, ya la conoces. Se llama Momo, y bueno, es la perrita que te tiro esa vez."
         show gael m nervous2 s
         player_name "a"
         show gael m nervous2 t
         g "¡Pero te juro que no es así!"
         g "{i}{size=-10}no siempre…{/i}{/size}"
         show gael m nervous2 s
         g "Me gustaría que pudieras conocerla mejor, debe limpiar su nombre contigo. De verdad que es muy linda."
         show gael m blush t
         player_name "Sí me gustaría, pero no quiero molestarte con ello-"
         g "¡No! \¿Sabes qué? Ya está decidido. Buscame al final del turno en el parque, ahí se va a arreglar todo."
         show gael m blush s
         player_name "Espera qué-"
         show gael m blush t
         g "¡Nos vemos allá!"
         hide gael m blush t with dissolve
         n "Tan pronto como acabo de decir aquello, desapareció del lugar."
         n "Bueno, un descanso siempre es útil. Además son perritos ¿Cómo decir no?"
         play music "Park.mp3"
         scene Park with dissolve
         show gael d normal s
         n "Llegaste a la hora citada, y sorprendentemente si estaba Gael con un grupo de 5 perritos."
         show gael d blush s
         n "Tan pronto te miró, sonrió emocionado haciéndote señas para que te acercaras."
         n "Carraspeo por un segundo y como si fuera un papá orgulloso comenzó a hablarte de cada perrito."
         n "Pero claro, que se tomó su tiempo hablando de Momo. Quien no dudo de mostrarte su arrepentimiento."
         n "Realmente fue un rato agradable. Todos los perritos eran muy amorosos y tranquilos, que ni te diste cuenta de cómo pasó el tiempo."
         n "Con pesar, comenzaste a despedirte de todos los perritos. Dándole mimos extra a Momo sin querer. No querías, pero sabías que tenías que irte."
         show gael d blush t
         play music "Happyending.mp3"
         g "Gracias por venir, esperó que te hayas divertido."
         show gael d blush s
         player_name "Si, lo hice"
         show gael d blush t
         g "Supongo que nos vemos mañana."
         show gael d blush s
         n "Ibas a decir algo más pero preferiste no hacerlo."
         hide gael d blush s with dissolve
         n "Te despediste con una ligera sonrisa y empezaste a caminar a tu casa."
         n "Tal vez era momento de aceptar que Gael nunca fue tan malo como pensaste alguna vez."
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_8_good_1

label hdia_7_good_2:
    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Hoy como cada tarde en los últimos días, te toca trabajar en la fondita."
    n "A pesar de ser un día ajetreado, Gael te ha hecho compañía."
    n "Clientes han llegado, llenando el local desde temprano. Por suerte todo ha fluido tranquilamente."
    n "Después de atender algunas mesas y clientes complicados, finalmente pudiste tomar un descanso."
    n "Aprovechaste unos asientos vacíos en el fondo."
    show gael m normal t with dissolve
    g "¡Hey, aquí estabas!"
    show gael m normal s
    player_name "¿uh? ¿Llegaron más clientes?"
    show gael m blush2 t
    g "¡Oh no, no! Solo quería hablar contigo."
    show gael m normal t
    g "¿Cómo te has sentido estos días? Sé que no es un trabajo tan fácil como puede parecer."
    show gael m normal s
    player_name "Pues…¿bien supongo? Si ha sido algo agotador pero eso no me va a desanimar."
    player_name "Al fin y al cabo, voy a quedarme aquí un rato, entonces…"
    show gael m normal t
    g "Me alegra escuchar eso"
    show gael m nervous2 t
    g "Por un segundo creí que otra vez ibas a querer renunciar."
    show gael m nervous2 s
    n "No pudiste evitar mostrar una ligera sonrisa, realmente sigue pensando en ello."
    n "A pesar de que el silencio era agradable, era mejor sacar un tema."
    menu:
     "Preguntar sobre el trabajo":
         player_name "y… ¿Tienes consejos para tratar con clientes…uhm…ya sabes-"
         show gael m nervous2 t
         g "¿Difíciles?"
         show gael m nervous2 s
         n "Asientes lentamente."
         show gael m normal t
         g "Bueno, hay que mantenernos tranquilos aunque el cliente parezca como un loco."
         show gael m angry t
         g "Solo si es {b}muy{/b} necesario, debemos ser firmes y pedir que se retiren."
         show gael m meh s
         player_name "¿Cómo lo hiciste hace unos días?"  
         show gael m nervous s
         n "Reiste un poco al recordarlo."
         player_name "Parecías una persona diferente con tu cara toda seria." 
         show gael m blush t
         g "¡Oye! ¿Así agradeces que te salve ese día?"
         show gael m blush s
         n "Después de eso, la conversación dejó de ser tan formal."
         n "¿Quién diría que podrías llegar a llevarte bien con Gael?"
         hide gael m blush s with dissolve
         n "El fin de tu turno llegó y mientras caminabas a casa sentiste que tal vez, si podrías llegar a ser un buen amigo aquel chico."
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_8_norm_2

     "Preguntar sobre los perritos":
         player_name "y… Tienes dos trabajos ¿verdad?"
         show gael m nervous t
         g "Oh, cierto me viste ese día…"
         show gael m nervous s
         player_name "¿En qué trabajas en sí? ¿Paseas perritos, los cuidas o qué?"
         show gael m normal t
         g "Bueno, digamos que son como prácticas pero no exactamente."
         show gael m normal s
         player_name "{b}{size=+10}???{/size}{/b}"
         show gael m normal t
         g "Conozco a un doctor que tiene su clínica cerca, siempre ha llamado mi atención los animales desde pequeño y él siempre fue muy amable introduciéndome al campo."
         show gael m nervous t
         g "De hecho hasta me echa la mano para estudiar para mis exámenes."
         show gael m blush t
         g "Regresando al trabajo, entre platica y platica sacó el tema de que quería empezar un servicio extra. Una cosa llevó a la otra y ahora paseo perritos entre semana."
         g "Sirve para practicar y el dinero extra siempre es bien recibido."
         show gael m blush s
         n "Era agradable ver a Gael tan emocionado, normalmente solo hablaban de la fondita. Parece que genuinamente disfruta su carrera."
         player_name "Entonces paseas muchos perritos, me pregunto si tendrán uno favorito."
         show gael m nervous2 t
         g "¡Hey, eso es como poner a decidir quién es tu hijo favorito!"
         show gael m nervous2 s
         g "..."
         show gael m normal t
         g "Aunque tal vez sí tenga…"
         show gael m normal s
         player_name "¡Dime, dime!"
         show gael m nervous2 t
         g "Si somos honestos, ya la conoces. Se llama Momo, y bueno, es la perrita que te tiro esa vez."
         show gael m nervous2 s
         player_name "a"
         show gael m nervous2 t
         g "¡Pero te juro que no es así!"
         g "{i}{size=-10}no siempre…{/i}{/size}"
         show gael m nervous2 s
         g "Me gustaría que pudieras conocerla mejor, debe limpiar su nombre contigo. De verdad que es muy linda."
         show gael m blush t
         player_name "Sí me gustaría, pero no quiero molestarte con ello-"
         g "¡No! \¿Sabes qué? Ya está decidido. Buscame al final del turno en el parque, ahí se va a arreglar todo."
         show gael m blush s
         player_name "Espera qué-"
         show gael m blush t
         g "¡Nos vemos allá!"
         hide gael m blush t with dissolve
         n "Tan pronto como acabo de decir aquello, desapareció del lugar."
         n "Bueno, un descanso siempre es útil. Además son perritos ¿Cómo decir no?"
         play music "Park.mp3"
         scene Park with dissolve
         show gael d normal s
         n "Llegaste a la hora citada, y sorprendentemente si estaba Gael con un grupo de 5 perritos."
         show gael d blush s
         n "Tan pronto te miró, sonrió emocionado haciéndote señas para que te acercaras."
         n "Carraspeo por un segundo y como si fuera un papá orgulloso comenzó a hablarte de cada perrito."
         n "Pero claro, que se tomó su tiempo hablando de Momo. Quien no dudo de mostrarte su arrepentimiento."
         n "Realmente fue un rato agradable. Todos los perritos eran muy amorosos y tranquilos, que ni te diste cuenta de cómo pasó el tiempo."
         n "Con pesar, comenzaste a despedirte de todos los perritos. Dándole mimos extra a Momo sin querer. No querías, pero sabías que tenías que irte."
         show gael d blush t
         play music "Happyending.mp3"
         g "Gracias por venir, esperó que te hayas divertido."
         show gael d blush s
         player_name "Si, lo hice"
         show gael d blush t
         g "Supongo que nos vemos mañana."
         show gael d blush s
         n "Ibas a decir algo más pero preferiste no hacerlo."
         hide gael d blush s with dissolve
         n "Te despediste con una ligera sonrisa y empezaste a caminar a tu casa."
         n "Tal vez era momento de aceptar que Gael nunca fue tan malo como pensaste alguna vez."
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_8_good_2

label hdia_8_norm_1:
    scene Uni Out with dissolve
    play music "Park.mp3"
    show asof normal s with dissolve
    n "Caminando por la Universidad, te topaste con Sofí."
    show asof normal t
    s "¿Entonces cómo va tu pintura?"

    show asof normal s
    player_name "Bastante bien, creo. Ya tengo un boceto y esperó mañana acabarlo."
    show asof normal t
    s "Me alegra escuchar eso [player_name], esperó ser la primera en verlo."
    hide asof normal t with dissolve
    
    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Después de clases fuiste a trabajar en la fondita. Esta vez no había tanta gente."
    n "Sin embargo, no parabas de notar la mirada constante de una chica."
    show loca miedo with dissolve
    d "..."
    player_name "{b}{size=+10}???{/size}{/b}"
    n ". "
    extend ". "
    extend "."
    show loca meh t
    d "\¡AY POR FAVOR!"
    show loca diuk
    n "La chica se acerca a ti apresuradamente."
    show loca meh t
    d "No captas indirectas \¿o qué?"
    show loca diuk
    player_name "{i}¿Y esta intensa qué?{/i}"
    player_name "Uh… \¿Se te ofrece algo?"
    show loca meh t
    d "¿El chico que trabaja contigo es tu novio?"
    show loca meh s

    player_name "¡Oh no! Solo somos amigos."
    show loca smile s
    n "La chica suspira alegre. Parece que se quitó un gran peso de encima."
    d "¡Ay que alivio! Entonces…"
    d "No te importaría pasarme su número ¿verdad? Es que es taaan lindoo"
    n "Reíste por su comentario. Gael si era algo guapo, tiene sentido que alguien lo busque. Pero no sabías que tan correcto es entregar su número a una extraña."

    menu:
     "Dárselo":
         player_name "{i}Bueno, una ayudita no es mala de vez en cuando.{/i}"
         n "Tomas una servilleta cercana y anotas el número de Gael."
         n "La chica se veía más que contenta."
         show loca blush t
         d "Ay muchas gracias de veras ¡Eres el mejor!"
         n "La chica te mira por unos segundos."
         show loca miedo
         d "Aún así trata de no acercarte tanto a él, \¿oíste?"
         hide loca miedo with dissolve
         n "Así con el papel en sus manos se empezó a alejar de ti."
         player_name "{i}Vaya rara…{/i}"
         n "Gael salió de la cocina y fue a atender la mesa de la chica."
         show loca blush t at left with dissolve
         show gael m nervous2 s at right with dissolve
         n "Parecía tan contenta, que hasta daba miedo."
         n "Pero bueno, solo podías esperar a ver como eso resulta"
         n "Tal vez, hasta se hagan pareja. Sería curioso ver eso."
         hide loca blush t with dissolve
         hide gael m nervous2 s with dissolve
         n "Así el día pasó rápidamente."
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_9_norm_1

     "No dárselo":
         n "Niegas con tu cabeza."
         show loca meh s at jumper
         player_name "No creo que sea correcto que te de su información, así no más."
         show loca angry s
         n "La chica se le ve muy enfadada."
         show loca meh t
         d "\¡\¿Uh?! Eres un envidioso, de seguro te gusta, pero qué crees…"
         d "Él conmigo estará mejor."
         show loca angry s
         n "Así la chica regresa a su mesa. No mentiras, se veía muy graciosa enojada."
         hide loca angry s with dissolve
         player_name "{i}Vaya si es algo rara…{/i}"
         n "Gael salió de la cocina y fue a atender la mesa de la chica."
         show loca blush t at left with dissolve
         show gael m nervous2 s at right with dissolve
         n "Parecía tan contenta, que hasta daba miedo."
         n "Pero bueno, solo podías esperar a ver como eso resulta"
         n "Tal vez, hasta se hagan pareja. Sería curioso ver eso."
         hide loca blush t with dissolve
         hide gael m nervous2 s with dissolve
         n "Así el día pasó rápidamente."
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_9_norm_1

label hdia_8_norm_2:
    scene Uni Out with dissolve
    play music "Park.mp3"
    show asof normal s with dissolve
    n "Caminando por la Universidad, te topaste con Sofí."
    show asof normal t
    s "¿Entonces cómo va tu pintura?"

    show asof normal s
    player_name "Bastante bien, creo. Ya tengo un boceto y esperó mañana acabarlo."
    show asof normal t
    s "Me alegra escuchar eso [player_name], esperó ser la primera en verlo."
    hide asof normal t with dissolve
    
    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Después de clases fuiste a trabajar en la fondita. Esta vez no había tanta gente."
    n "Sin embargo, no parabas de notar la mirada constante de una chica."
    show loca miedo with dissolve
    d "..."
    player_name "{b}{size=+10}???{/size}{/b}"
    n ". "
    extend ". "
    extend "."
    show loca meh t
    d "\¡AY POR FAVOR!"
    show loca diuk
    n "La chica se acerca a ti apresuradamente."
    show loca meh t
    d "No captas indirectas \¿o qué?"
    show loca diuk
    player_name "{i}¿Y esta intensa qué?{/i}"
    player_name "Uh… \¿Se te ofrece algo?"
    show loca meh t
    d "¿El chico que trabaja contigo es tu novio?"
    show loca meh s

    player_name "¡Oh no! Solo somos amigos."
    show loca smile s
    n "La chica suspira alegre. Parece que se quitó un gran peso de encima."
    d "¡Ay que alivio! Entonces…"
    d "No te importaría pasarme su número ¿verdad? Es que es taaan lindoo"
    n "Reíste por su comentario. Gael si era algo guapo, tiene sentido que alguien lo busque. Pero no sabías que tan correcto es entregar su número a una extraña."

    menu:
     "Dárselo":
         player_name "{i}Bueno, una ayudita no es mala de vez en cuando.{/i}"
         n "Tomas una servilleta cercana y anotas el número de Gael."
         n "La chica se veía más que contenta."
         show loca blush t
         d "Ay muchas gracias de veras ¡Eres el mejor!"
         n "La chica te mira por unos segundos."
         show loca miedo
         d "Aún así trata de no acercarte tanto a él, \¿oíste?"
         hide loca miedo with dissolve
         n "Así con el papel en sus manos se empezó a alejar de ti."
         player_name "{i}Vaya rara…{/i}"
         n "Gael salió de la cocina y fue a atender la mesa de la chica."
         show loca blush t at left with dissolve
         show gael m nervous2 s at right with dissolve
         n "Parecía tan contenta, que hasta daba miedo."
         n "Pero bueno, solo podías esperar a ver como eso resulta"
         n "Tal vez, hasta se hagan pareja. Sería curioso ver eso."
         hide loca blush t with dissolve
         hide gael m nervous2 s with dissolve
         n "Así el día pasó rápidamente."
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_9_norm_2

     "No dárselo":
         n "Niegas con tu cabeza."
         show loca meh s at jumper
         player_name "No creo que sea correcto que te de su información, así no más."
         show loca angry s
         n "La chica se le ve muy enfadada."
         show loca meh t
         d "\¡\¿Uh?! Eres un envidioso, de seguro te gusta, pero qué crees…"
         d "Él conmigo estará mejor."
         show loca angry s
         n "Así la chica regresa a su mesa. No mentiras, se veía muy graciosa enojada."
         hide loca angry s with dissolve
         player_name "{i}Vaya si es algo rara…{/i}"
         n "Gael salió de la cocina y fue a atender la mesa de la chica."
         show loca blush t at left with dissolve
         show gael m nervous2 s at right with dissolve
         n "Parecía tan contenta, que hasta daba miedo."
         n "Pero bueno, solo podías esperar a ver como eso resulta"
         n "Tal vez, hasta se hagan pareja. Sería curioso ver eso."
         hide loca blush t with dissolve
         hide gael m nervous2 s with dissolve
         n "Así el día pasó rápidamente."
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_9_norm_2

label hdia_8_norm_3:
    scene Uni Out with dissolve
    play music "Park.mp3"
    show asof normal s with dissolve
    n "Caminando por la Universidad, te topaste con Sofí."
    show asof normal t
    s "¿Entonces cómo va tu pintura?"

    show asof normal s
    player_name "Bastante bien, creo. Ya tengo un boceto y esperó mañana acabarlo."
    show asof normal t
    s "Me alegra escuchar eso [player_name], esperó ser la primera en verlo."
    hide asof normal t with dissolve
    
    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Después de clases fuiste a trabajar en la fondita. Esta vez no había tanta gente."
    n "Sin embargo, no parabas de notar la mirada constante de una chica."
    show loca miedo with dissolve
    d "..."
    player_name "{b}{size=+10}???{/size}{/b}"
    n ". "
    extend ". "
    extend "."
    show loca meh t
    d "\¡AY POR FAVOR!"
    show loca diuk
    n "La chica se acerca a ti apresuradamente."
    show loca meh t
    d "No captas indirectas \¿o qué?"
    show loca diuk
    player_name "{i}¿Y esta intensa qué?{/i}"
    player_name "Uh… \¿Se te ofrece algo?"
    show loca meh t
    d "¿El chico que trabaja contigo es tu novio?"
    show loca meh s

    player_name "¡Oh no! Solo somos amigos."
    show loca smile s
    n "La chica suspira alegre. Parece que se quitó un gran peso de encima."
    d "¡Ay que alivio! Entonces…"
    d "No te importaría pasarme su número ¿verdad? Es que es taaan lindoo"
    n "Reíste por su comentario. Gael si era algo guapo, tiene sentido que alguien lo busque. Pero no sabías que tan correcto es entregar su número a una extraña."

    menu:
     "Dárselo":
         player_name "{i}Bueno, una ayudita no es mala de vez en cuando.{/i}"
         n "Tomas una servilleta cercana y anotas el número de Gael."
         n "La chica se veía más que contenta."
         show loca blush t
         d "Ay muchas gracias de veras ¡Eres el mejor!"
         n "La chica te mira por unos segundos."
         show loca miedo
         d "Aún así trata de no acercarte tanto a él, \¿oíste?"
         hide loca miedo with dissolve
         n "Así con el papel en sus manos se empezó a alejar de ti."
         player_name "{i}Vaya rara…{/i}"
         n "Gael salió de la cocina y fue a atender la mesa de la chica."
         show loca blush t at left with dissolve
         show gael m nervous2 s at right with dissolve
         n "Parecía tan contenta, que hasta daba miedo."
         n "Pero bueno, solo podías esperar a ver como eso resulta"
         n "Tal vez, hasta se hagan pareja. Sería curioso ver eso."
         hide loca blush t with dissolve
         hide gael m nervous2 s with dissolve
         n "Así el día pasó rápidamente."
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_9_norm_3

     "No dárselo":
         n "Niegas con tu cabeza."
         show loca meh s at jumper
         player_name "No creo que sea correcto que te de su información, así no más."
         show loca angry s
         n "La chica se le ve muy enfadada."
         show loca meh t
         d "\¡\¿Uh?! Eres un envidioso, de seguro te gusta, pero qué crees…"
         d "Él conmigo estará mejor."
         show loca angry s
         n "Así la chica regresa a su mesa. No mentiras, se veía muy graciosa enojada."
         hide loca angry s with dissolve
         player_name "{i}Vaya si es algo rara…{/i}"
         n "Gael salió de la cocina y fue a atender la mesa de la chica."
         show loca blush t at left with dissolve
         show gael m nervous2 s at right with dissolve
         n "Parecía tan contenta, que hasta daba miedo."
         n "Pero bueno, solo podías esperar a ver como eso resulta"
         n "Tal vez, hasta se hagan pareja. Sería curioso ver eso."
         hide loca blush t with dissolve
         hide gael m nervous2 s with dissolve
         n "Así el día pasó rápidamente."
         scene black with dissolve
         stop music fadeout 1.0
         jump hdia_9_norm_3

label hdia_9_norm_1:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    n "Es un nuevo día."
    n "Mañana es la exposición en la galería, por lo que decidiste tomarte toda la mañana para acabar tu pintura."
    
    n "Trazos, pinceladas y mucha pintura en tus brazos. Sin duda, fue toda una experiencia."
    n "Fue bastante grato ver como tu idea cobraba forma."
    jump hgame_1_n

label hdia_9_norm_2:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    n "Es un nuevo día."
    n "Mañana es la exposición en la galería, por lo que decidiste tomarte toda la mañana para acabar tu pintura."
    
    n "Trazos, pinceladas y mucha pintura en tus brazos. Sin duda, fue toda una experiencia."
    n "Fue bastante grato ver como tu idea cobraba forma."

    jump hgame_2_n

label hgame_1_n:
    play music "Park.mp3"
    $ hsetup_puzzle1()
    call screen hreassemble_puzzle1

label hgame_2_n:
    play music "Park.mp3"
    $ hsetup_puzzle2()
    call screen hreassemble_puzzle2

label hdia_9_norm1_p2:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    show p1 with dissolve
    player_name "¡Y listo!"
    n "Después de observar con orgullo tu obra, miraste el desastre que te rodeaba."
    hide p1 with dissolve
    n "Así que solo quedaba aprovechar el día de descanso hasta el final."
    scene black with dissolve
    jump hfinal_norm

label hdia_9_norm2_p2:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    show p2 with dissolve
    player_name "¡Y listo!"
    n "Después de observar con orgullo tu obra, miraste el desastre que te rodeaba."
    hide p2 with dissolve
    n "Así que solo quedaba aprovechar el día de descanso hasta el final."
    scene black with dissolve
    jump hfinal_norm

label hdia_9_norm_3:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    n "Es un nuevo día."
    n "Mañana es la exposición en la galería, por lo que decidiste tomarte toda la mañana para acabar tu pintura." 
    n "Trazos, pinceladas y mucha pintura en tus brazos. Sin duda, fue toda una experiencia."
    n "A pesar de tus dudas con los materiales que tenías. "
    extend "Fue bastante grato ver como tu idea cobraba forma."
    player_name "¡Y listo!"
    n "Después de observar con orgullo tu obra, miraste el desastre que te rodeaba."
    n "Así que solo quedaba aprovechar el día de descanso hasta el final."
    jump hfinal_norm

label hfinal_norm:
    scene Gallery with dissolve
    play music "Gallery.mp3"
    n "Después de unas largas semanas, finalmente llegó el día."
    n "Toda tu clase estaba reunida en la galería con sus trabajos listos para exponer."
    n "La profesora Marta incluso se vistió para la ocasión."
    n "Cada alumno tenía que mostrarle sus trabajos antes de exponerlos, así sabrías tu nota final y solo disfrutarías el evento."
    n "Aún así, no dejabas de sentir nervios en cada paso que te acercabas a la profesora."
    n "Incluso Sofí te había dicho que estaba bien, además la profesora nunca había sido cruel al revisar."
    n "Sin embargo, una notificación te sacó de tus pensamientos."
    n "Era Gael."
    nvl_narrator "Tienes nuevos mensajes"
    g_nvl "Hoy es tu presentación ¿verdad?"
    g_nvl "Se que puedes, has trabajado mucho. ¡Ánimo!"
    g_nvl "{image=piolin.png}"
    n "Sabías que le tenías que agradecer más tarde, porque sin duda te sacó de la ansiedad."
    n "Lo malo, es que ahora debías evitar reírte en plena galería por sus imágenes de señora."
    show marta normal t with dissolve
    m "¡La siguiente persona por favor!"
    show marta normal s
    n "Era hora. Más relajado, le mostraste tu pintura."
    show marta normal t
    m "¡Vaya! Sabía que no me iba decepcionar jovencito."
    m "No quería creer lo que sus otros profesores hablan de usted, pero veo que tienen razón."
    m "Realmente es muy bueno su trabajo. Se que va a ser uno de los que más luzcan hoy."
    show marta normal s
    n "No podías ocultar tu sonrisa."
    show marta normal s with dissolve
    n "Disfrutaste del evento y toda la noche muchos halagaron tu trabajo."
    scene black with dissolve
    n "Realmente todo salió bien."
    n "El proyecto, el trabajo y ahora hasta un nuevo amigo."
    n "Sin duda, un buen comienzo."
    scene final 3 with dissolve
    n " "
    n "Has conseguido el final neutral."
    stop music fadeout 1.0
    return
    ####Final Neutral###

label hdia_8_good_1:
    scene Uni Out with dissolve
    play music "Park.mp3"
    show asof normal s with dissolve
    n "Caminando por la Universidad, te topaste con Sofí."
    show asof normal t
    s "¿Entonces cómo va tu pintura?"
    show asof normal s
    player_name "Bastante bien, creo. Ya tengo un boceto y esperó mañana acabarlo."
    show asof normal t
    s "Me alegra escuchar eso [player_name], esperó ser la primera en verlo."

    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Después de clases fuiste a trabajar en la fondita. Esta vez no había tanta gente."
    n "Sin embargo, no parabas de notar la mirada constante de una chica."
    show loca miedo with dissolve
    d "..."
    player_name "{b}{size=+10}???{/size}{/b}"
    n ". "
    extend ". "
    extend "."
    show loca meh t
    d "\¡AY POR FAVOR!"
    show loca diuk
    n "La chica se acerca a ti apresuradamente."
    show loca meh t
    d "No captas indirectas \¿o qué?"
    show loca diuk
    player_name "{i}¿Y esta intensa qué?{/i}"
    player_name "Uh… \¿Se te ofrece algo?"
    show loca meh t
    d "¿El chico que trabaja contigo es tu novio?"
    show loca meh s
    player_name "Mmm, ¿Por qué preguntas?"
    show loca meh t
    d "Ugh, solo quiero saber ¿si?"
    show loca meh s
    n "La chica suspira y te mira fijamente."
    show loca meh t
    d "Bueno, si no lo es…"
    show loca blush t
    d "…No te importaría pasarme su número ¿verdad? Es que es taaan lindoo"
    show loca blush s
    n "No creías que la conservación fuera ahí. Sabías que Gael era guapo, era de esperarse que alguien se fijará en él."
    n "Pero no entendías el porqué te sentías algo molesto."

    menu:
     "Dárselo":
            play music "Sadend.mp3"
            player_name "{i}Bueno, al final del día no soy nada de él, no debería tomarle importancia.{/i}"
            n "Tomas una servilleta cercana y anotas el número de Gael con cierta duda."
            n "La chica se veía más que contenta."
            show loca blush t
            d "Ay muchas gracias de veras ¡Eres el mejor!"
            n "La chica te mira por unos segundos."
            show loca miedo
            d "En fin, no te acerques tanto a él, \¿oíste?"
            hide loca miedo with dissolve
            n "Así con el papel en sus manos se empezó a alejar de ti."
            player_name "..."
            n "La chica se acercó al mostrador donde Gael se encontraba."
            scene closer with dissolve
            show gael s2 nervous with dissolve
            n "Parecía tan contenta, que hasta daba miedo."
            n "La chica parece tratar de conversar con él."
            player_name "{i}De cierto modo, se ve bien juntos, o bueno, Gael se ve bien en pareja.{/i}"
            player_name "..."
            player_name "{i}Aunque se ve incómodo… Tal vez debería acercarme…{/i}"
            player_name "{i}No, no. Él está bien.{/i}"
            d "Entonces \¿Te gustaría salir después de tu turno?"
            g "Uh…"
            player_name "..."
            player_name "{i}Tal vez soy yo el que se siente mal.{/i}"
            stop music fadeout 1.0
            show gael s2 surpised
            player_name "{b}{size=+10}!!!{/size}{/b}"
            show gael s2 blush 1
            n " "
            show gael s2 blush 2
            g "Cough"
            g "Agradezco tu invitación, pero tendré que negarme."
            d "\¡P-Pero!"
            g "Lo siento."
            scene Fondita In with dissolve
            hide gael s2 blush 2 with dissolve
            play music "Happyending.mp3"
            n "La chica se veía algo herida"
            n "No entendías, pero sentiste un gran alivio cuando cruzó la puerta."
            show gael m nervous2 t with dissolve
            g "Eso fue raro ¿verdad?"
            show gael m nervous2 s
            n "Solo pudiste asentir."
            n "Nunca habías sentido un silencio tan extenso."

            menu:
             "Preguntar":
                    show gael m nervous s
                    player_name "Gael, ¿Por qué te negaste a la cita?"
                    show gael m nervous t
                    g "Ah, este...bueno, verás..."
                    show gael m blush t
                    g "Siento que no es correcto aceptar una cita cuando me gusta alguien más…"
                    player_name "\¿Q-Qué?"
                    show gael m nervous t
                    g "Uhm, ya casi se acaba nuestro turno… así que mejor voy por allá"
                    show gael m nervous s
                    g "{i}{size=-10}Casi la riego abriendo mi bocota{/size}{/i}"
                    hide gael m nervous s with dissolve
                    n "No sabías cómo digerir todo lo que había pasado hoy."
                    n "Sin duda, este día sería uno largo."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump hdia_9_good_1

             "Preguntar":
                    show gael m nervous s
                    player_name "Gael, ¿Por qué te negaste a la cita?"
                    show gael m nervous t
                    g "Ah, este...bueno, verás..."
                    show gael m blush t
                    g "Siento que no es correcto aceptar una cita cuando me gusta alguien más…"
                    player_name "\¿Q-Qué?"
                    show gael m nervous t
                    g "Uhm, ya casi se acaba nuestro turno… así que mejor voy por allá"
                    show gael m nervous s
                    g "{i}{size=-10}Casi la riego abriendo mi bocota{/size}{/i}"
                    hide gael m nervous s with dissolve
                    n "No sabías cómo digerir todo lo que había pasado hoy."
                    n "Sin duda, este día sería uno largo."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump hdia_9_good_1


     "No dárselo":
            n "Niegas con tu cabeza. No era correcto y honestamente no querías dárselo."
            show loca meh s at jumper
            player_name "No creo que sea correcto que te de su información, así no más."
            show loca angry s
            n "La chica se le ve muy enfadada."
            show loca meh t
            d "\¡\¿Uh?! Eres un envidioso, es obvio que te gusta, pero qué crees…"
            d "Eso no me va a impedir ir tras él, ¿escuchaste?"
            show loca angry s
            player_name "..."
            hide loca angry s with dissolve
            n "La chica se acercó al mostrador donde Gael se encontraba."
            scene closer with dissolve
            show gael s2 nervous with dissolve
            n "Parecía tan contenta, que hasta daba miedo."
            n "La chica parece tratar de conversar con él."
            player_name "{i}De cierto modo, se ve bien juntos, o bueno, Gael se ve bien en pareja.{/i}"
            player_name "..."
            player_name "{i}Aunque se ve incómodo… Tal vez debería acercarme…{/i}"
            player_name "{i}No, no. Él está bien.{/i}"
            d "Entonces \¿Te gustaría salir después de tu turno?"
            g "Uh…"
            player_name "..."
            player_name "{i}Tal vez soy yo el que se siente mal.{/i}"
            show gael s2 surpised
            player_name "{b}{size=+10}!!!{/size}{/b}"
            show gael s2 blush 1
            n " "
            show gael s2 blush 2
            g "Cough"
            g "Agradezco tu invitación, pero tendré que negarme."
            d "\¡P-Pero!"
            g "Lo siento."
            scene Fondita In with dissolve
            hide gael s2 blush 2 with dissolve
            play music "Happyending.mp3"
            n "La chica se veía algo herida"
            n "No entendías, pero sentiste un gran alivio cuando cruzó la puerta."
            show gael m nervous2 t with dissolve
            g "Eso fue raro ¿verdad?"
            show gael m nervous2 s
            n "Solo pudiste asentir."
            n "Nunca habías sentido un silencio tan extenso."
         
            menu:
             "Preguntar":
                    show gael m nervous s
                    player_name "Gael, ¿Por qué te negaste a la cita?"
                    show gael m nervous t
                    g "Ah, este...bueno, verás..."
                    show gael m blush t
                    g "Siento que no es correcto aceptar una cita cuando me gusta alguien más…"
                    player_name "\¿Q-Qué?"
                    show gael m nervous t
                    g "Uhm, ya casi se acaba nuestro turno… así que mejor voy por allá"
                    show gael m nervous s
                    g "{i}{size=-10}Casi la riego abriendo mi bocota{/size}{/i}"
                    hide gael m nervous s with dissolve
                    n "No sabías cómo digerir todo lo que había pasado hoy."
                    n "Sin duda, este día sería uno largo."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump hdia_9_good_1
                
             "Preguntar":
                    show gael m nervous s
                    player_name "Gael, ¿Por qué te negaste a la cita?"
                    show gael m nervous t
                    g "Ah, este...bueno, verás..."
                    show gael m blush t
                    g "Siento que no es correcto aceptar una cita cuando me gusta alguien más…"
                    player_name "\¿Q-Qué?"
                    show gael m nervous t
                    g "Uhm, ya casi se acaba nuestro turno… así que mejor voy por allá"
                    show gael m nervous s
                    g "{i}{size=-10}Casi la riego abriendo mi bocota{/size}{/i}"
                    hide gael m nervous s with dissolve
                    n "No sabías cómo digerir todo lo que había pasado hoy."
                    n "Sin duda, este día sería uno largo."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump hdia_9_good_1

label hdia_8_good_2:
    scene Uni Out with dissolve
    play music "Park.mp3"
    show asof normal s with dissolve
    n "Caminando por la Universidad, te topaste con Sofí."
    show asof normal t
    s "¿Entonces cómo va tu pintura?"
    show asof normal s
    player_name "Bastante bien, creo. Ya tengo un boceto y esperó mañana acabarlo."
    show asof normal t
    s "Me alegra escuchar eso [player_name], esperó ser la primera en verlo."

    scene Fondita In with dissolve
    play music "Cafeteria.mp3"
    n "Después de clases fuiste a trabajar en la fondita. Esta vez no había tanta gente."
    n "Sin embargo, no parabas de notar la mirada constante de una chica."
    show loca miedo with dissolve
    d "..."
    player_name "{b}{size=+10}???{/size}{/b}"
    n ". "
    extend ". "
    extend "."
    show loca meh t
    d "\¡AY POR FAVOR!"
    show loca diuk
    n "La chica se acerca a ti apresuradamente."
    show loca meh t
    d "No captas indirectas \¿o qué?"
    show loca diuk
    player_name "{i}¿Y esta intensa qué?{/i}"
    player_name "Uh… \¿Se te ofrece algo?"
    show loca meh t
    d "¿El chico que trabaja contigo es tu novio?"
    show loca meh s
    player_name "Mmm, ¿Por qué preguntas?"
    show loca meh t
    d "Ugh, solo quiero saber ¿si?"
    show loca meh s
    n "La chica suspira y te mira fijamente."
    show loca meh t
    d "Bueno, si no lo es…"
    show loca blush t
    d "…No te importaría pasarme su número ¿verdad? Es que es taaan lindoo"
    show loca blush s
    n "No creías que la conservación fuera ahí. Sabías que Gael era guapo, era de esperarse que alguien se fijará en él."
    n "Pero no entendías el porqué te sentías algo molesto."

    menu:
     "Dárselo":
            play music "Sadend.mp3"
            player_name "{i}Bueno, al final del día no soy nada de él, no debería tomarle importancia.{/i}"
            n "Tomas una servilleta cercana y anotas el número de Gael con cierta duda."
            n "La chica se veía más que contenta."
            show loca blush t
            d "Ay muchas gracias de veras ¡Eres el mejor!"
            n "La chica te mira por unos segundos."
            show loca miedo
            d "En fin, no te acerques tanto a él, \¿oíste?"
            hide loca miedo with dissolve
            n "Así con el papel en sus manos se empezó a alejar de ti."
            player_name "..."
            n "La chica se acercó al mostrador donde Gael se encontraba."
            scene closer with dissolve
            show gael s2 nervous with dissolve
            n "Parecía tan contenta, que hasta daba miedo."
            n "La chica parece tratar de conversar con él."
            player_name "{i}De cierto modo, se ve bien juntos, o bueno, Gael se ve bien en pareja.{/i}"
            player_name "..."
            player_name "{i}Aunque se ve incómodo… Tal vez debería acercarme…{/i}"
            player_name "{i}No, no. Él está bien.{/i}"
            d "Entonces \¿Te gustaría salir después de tu turno?"
            g "Uh…"
            player_name "..."
            player_name "{i}Tal vez soy yo el que se siente mal.{/i}"
            stop music fadeout 1.0
            show gael s2 surpised
            player_name "{b}{size=+10}!!!{/size}{/b}"
            show gael s2 blush 1
            n " "
            show gael s2 blush 2
            g "Cough"
            g "Agradezco tu invitación, pero tendré que negarme."
            d "\¡P-Pero!"
            g "Lo siento."
            scene Fondita In with dissolve
            hide gael s2 blush 2 with dissolve
            play music "Happyending.mp3"
            n "La chica se veía algo herida"
            n "No entendías, pero sentiste un gran alivio cuando cruzó la puerta."
            show gael m nervous2 t with dissolve
            g "Eso fue raro ¿verdad?"
            show gael m nervous2 s
            n "Solo pudiste asentir."
            n "Nunca habías sentido un silencio tan extenso."

            menu:
             "Preguntar":
                    show gael m nervous s
                    player_name "Gael, ¿Por qué te negaste a la cita?"
                    show gael m nervous t
                    g "Ah, este...bueno, verás..."
                    show gael m blush t
                    g "Siento que no es correcto aceptar una cita cuando me gusta alguien más…"
                    player_name "\¿Q-Qué?"
                    show gael m nervous t
                    g "Uhm, ya casi se acaba nuestro turno… así que mejor voy por allá"
                    show gael m nervous s
                    g "{i}{size=-10}Casi la riego abriendo mi bocota{/size}{/i}"
                    hide gael m nervous s with dissolve
                    n "No sabías cómo digerir todo lo que había pasado hoy."
                    n "Sin duda, este día sería uno largo."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump hdia_9_good_2

             "Preguntar":
                    show gael m nervous s
                    player_name "Gael, ¿Por qué te negaste a la cita?"
                    show gael m nervous t
                    g "Ah, este...bueno, verás..."
                    show gael m blush t
                    g "Siento que no es correcto aceptar una cita cuando me gusta alguien más…"
                    player_name "\¿Q-Qué?"
                    show gael m nervous t
                    g "Uhm, ya casi se acaba nuestro turno… así que mejor voy por allá"
                    show gael m nervous s
                    g "{i}{size=-10}Casi la riego abriendo mi bocota{/size}{/i}"
                    hide gael m nervous s with dissolve
                    n "No sabías cómo digerir todo lo que había pasado hoy."
                    n "Sin duda, este día sería uno largo."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump hdia_9_good_2


     "No dárselo":
            n "Niegas con tu cabeza. No era correcto y honestamente no querías dárselo."
            show loca meh s at jumper
            player_name "No creo que sea correcto que te de su información, así no más."
            show loca angry s
            n "La chica se le ve muy enfadada."
            show loca meh t
            d "\¡\¿Uh?! Eres un envidioso, es obvio que te gusta, pero qué crees…"
            d "Eso no me va a impedir ir tras él, ¿escuchaste?"
            show loca angry s
            player_name "..."
            hide loca angry s with dissolve
            n "La chica se acercó al mostrador donde Gael se encontraba."
            scene closer with dissolve
            show gael s2 nervous with dissolve
            n "Parecía tan contenta, que hasta daba miedo."
            n "La chica parece tratar de conversar con él."
            player_name "{i}De cierto modo, se ve bien juntos, o bueno, Gael se ve bien en pareja.{/i}"
            player_name "..."
            player_name "{i}Aunque se ve incómodo… Tal vez debería acercarme…{/i}"
            player_name "{i}No, no. Él está bien.{/i}"
            d "Entonces \¿Te gustaría salir después de tu turno?"
            g "Uh…"
            player_name "..."
            player_name "{i}Tal vez soy yo el que se siente mal.{/i}"
            show gael s2 surpised
            player_name "{b}{size=+10}!!!{/size}{/b}"
            show gael s2 blush 1
            n " "
            show gael s2 blush 2
            g "Cough"
            g "Agradezco tu invitación, pero tendré que negarme."
            d "\¡P-Pero!"
            g "Lo siento."
            scene Fondita In with dissolve
            hide gael s2 blush 2 with dissolve
            play music "Happyending.mp3"
            n "La chica se veía algo herida"
            n "No entendías, pero sentiste un gran alivio cuando cruzó la puerta."
            show gael m nervous2 t with dissolve
            g "Eso fue raro ¿verdad?"
            show gael m nervous2 s
            n "Solo pudiste asentir."
            n "Nunca habías sentido un silencio tan extenso."
         
            menu:
             "Preguntar":
                    show gael m nervous s
                    player_name "Gael, ¿Por qué te negaste a la cita?"
                    show gael m nervous t
                    g "Ah, este...bueno, verás..."
                    show gael m blush t
                    g "Siento que no es correcto aceptar una cita cuando me gusta alguien más…"
                    player_name "\¿Q-Qué?"
                    show gael m nervous t
                    g "Uhm, ya casi se acaba nuestro turno… así que mejor voy por allá"
                    show gael m nervous s
                    g "{i}{size=-10}Casi la riego abriendo mi bocota{/size}{/i}"
                    hide gael m nervous s with dissolve
                    n "No sabías cómo digerir todo lo que había pasado hoy."
                    n "Sin duda, este día sería uno largo."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump hdia_9_good_2
                
             "Preguntar":
                    show gael m nervous s
                    player_name "Gael, ¿Por qué te negaste a la cita?"
                    show gael m nervous t
                    g "Ah, este...bueno, verás..."
                    show gael m blush t
                    g "Siento que no es correcto aceptar una cita cuando me gusta alguien más…"
                    player_name "\¿Q-Qué?"
                    show gael m nervous t
                    g "Uhm, ya casi se acaba nuestro turno… así que mejor voy por allá"
                    show gael m nervous s
                    g "{i}{size=-10}Casi la riego abriendo mi bocota{/size}{/i}"
                    hide gael m nervous s with dissolve
                    n "No sabías cómo digerir todo lo que había pasado hoy."
                    n "Sin duda, este día sería uno largo."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump hdia_9_good_2

label hdia_9_good_1:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    n "Es un nuevo día."
    n "Mañana es la exposición en la galería, por lo que decidiste tomarte toda la mañana para acabar tu pintura."
    n "Trazos, pinceladas y mucha pintura en tus brazos. Sin duda, era toda una experiencia."
    n "Simplemente, fue bastante grato ver como tu idea cobraba forma."
    jump hgame_1

label hdia_9_good_2:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    n "Es un nuevo día."
    n "Mañana es la exposición en la galería, por lo que decidiste tomarte toda la mañana para acabar tu pintura."
    n "Trazos, pinceladas y mucha pintura en tus brazos. Sin duda, era toda una experiencia."
    n "Simplemente, fue bastante grato ver como tu idea cobraba forma."
    jump hgame_2

label  hgame_1:
    play music "Park.mp3"
    $ hsetup_puzzle01()
    call screen hreassemble_puzzle01

label  hgame_2:
    play music "Park.mp3"
    $ hsetup_puzzle02()
    call screen hreassemble_puzzle02

label hdia_9_good1p2:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    show p1 with dissolve
    player_name "¡Y listo!"
    hide p1 with dissolve
    n "Después de observar con orgullo tu obra, miraste el desastre que te rodeaba."
    n "Cuando estabas listo para limpiar, tu celular te interrumpió."
    nvl_narrator "Tienes un nuevo mensaje"
    g_nvl "Hola! Espero no molestarte, pero hoy vas a trabajar?"
    n "\¿Qué responderle?"

    menu:
     "Si":
            p_nvl "Hola!"
            p_nvl "Si, creo que voy a ir solo un rato..."
            p_nvl "Es que debo ordenar el desastre que hice por mi proyecto :p"
            g_nvl "Proyecto? :0"
            p_nvl "Te explico allá"
            n "Bueno, no podías dejar tu trabajo desatendido, además que era una buena excusa para ver a Gael y tal vez se despejen todas tus dudas."
            
            scene Fondita In  with dissolve
            play music "Cafeteria.mp3"
            n "Al llegar a la fondita, notaste el lugar casi vacío."
            show gael m nervous2 s with dissolve
            n "Gael se encontraba mirando nervioso su celular."
            show gael m normal t at jumper
            g "¡[player_name]!"
            show gael m blush t
            g "Justo te iba a llamar, mis padres decidieron mejor cerrar temprano hoy, para que no vinieras, pero creo que me tarde…"
            show gael m blush s
            player_name "No te preocupes, aún así necesitaba despejarme."
            show gael m normal t
            g "Por tu proyecto, ¿verdad?"
            show gael m normal s
            n "Cierto."
            player_name "Si, mañana voy a presentar una pintura en una galería, es por una clase…"
            n "Por alguna razón no podías ni mirarlo a los ojos."
            n "Todo era culpa de lo que pasó ayer. Si tan solo…"
            player_name "Uhm…"
            show gael m blush2 t
            g "Bueno, esperó que se quede en exposición por un tiempo. Me gustaría poder ver tu trabajo" 
            show gael m blush t
            g "Así podría decir que soy amigo de una gran artista."
            n "Amigo"
            n "{b}Amigo{/b}"
            play music "Sadend.mp3"
            n "No podías ignorar la extraña sensación de tristeza que surgió al escuchar eso."
            n "\¿Qué está haciendo con tu cabeza? Eso es normal, hasta es bueno."
            show gael m normal s
            n "Te considera una amistad."
            extend " Eso es bueno para ti ¿verdad?"

            menu:
             
             "Si":
                    player_name "{b}¡Si!{/b}"
                    show gael m nervous2 s at jumper
                    g "{b}{size=+10}???{/size}{/b}"
                    player_name "Uh..."
                    player_name "Que...¡si va a estar como por un mes allá!"
                    show gael m nervous2 t
                    g "Oh, ¡Qué bien! Entonces esperó ir después."
                    show gael m nervous2 s
                    n "Solo querías irte ya."
                    player_name "Bueno, como ya no hay trabajo creo que será mejor que me vaya."
                    extend " Nos vemos."
                    hide gael m nervous2 s with dissolve
                    n "Esta sería otra noche larga."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump hfinal_norm
             
             "No":
                player_name "{b}No...{/b}"
                show gael m nervous2 t
                g "Oh..."
                g "\¿No quieres qué la vea?"
                show gael m nervous2 s
                player_name "\¡Ay! \¡No es eso! Es que...uh..."

                menu:
                 "Decirle":
                        play music "Happyending.mp3"
                        player_name "Yo..."
                        n "Respiraste y finalmente..."
                        player_name "¡Te quería invitar a verlo conmigo!"
                        show gael m blush s at jumper
                        g "{b}{size=+10}!!!{/size}{/b}"
                        show gael m blush t
                        g "C-Claro! ¡Me encantaría ir!"
                        n "Sin dudarlo, le mandaste toda la información para que llegará."
                        hide gael m blush t with dissolve
                        n "No podías esperar a mañana."
                        scene black with dissolve
                        stop music fadeout 1.0
                        jump hfinal_bueno

                 "No decirle":
                        player_name "Uh, que no va a estar solo mañana, si no como..."
                        player_name "Uh..."
                        show gael m normal s
                        player_name "{b}¡Un mes!{/b}"
                        extend "...si, un mes..."
                        show gael m normal t
                        g "Oh, ¡Qué bien! Entonces esperó ir después."
                        show gael m normal s
                        n "Solo querías irte ya."
                        player_name "Bueno, como ya no hay trabajo creo que será mejor que me vaya. Nos vemos."
                        hide gael m normal s with dissolve
                        n "Esta sería otra noche larga."
                        scene black with dissolve
                        stop music fadeout 1.0
                        jump hfinal_norm
     "No":
            p_nvl "Hola!"
            p_nvl "No, lo siento :( "
            g_nvl "Oh, ok! Ntp, nos vemos después."
            n "Bueno, no podías simplemente dejar todo así y necesitabas descansar."
            n "Así que solo quedaba aprovechar el día de descanso hasta el final."
            scene black with dissolve
            stop music fadeout 1.0
            jump hfinal_norm

label hdia_9_good2p2:
    scene Cuarto with dissolve
    play music "Cuarto.mp3"
    show p2 with dissolve
    player_name "¡Y listo!"
    hide p2 with dissolve
    n "Después de observar con orgullo tu obra, miraste el desastre que te rodeaba."
    n "Cuando estabas listo para limpiar, tu celular te interrumpió."
    nvl_narrator "Tienes un nuevo mensaje"
    g_nvl "Hola! Espero no molestarte, pero hoy vas a trabajar?"
    n "\¿Qué responderle?"

    menu:
     "Si":
            p_nvl "Hola!"
            p_nvl "Si, creo que voy a ir solo un rato..."
            p_nvl "Es que debo ordenar el desastre que hice por mi proyecto :p"
            g_nvl "Proyecto? :0"
            p_nvl "Te explico allá"
            n "Bueno, no podías dejar tu trabajo desatendido, además que era una buena excusa para ver a Gael y tal vez se despejen todas tus dudas."
            
            scene Fondita In  with dissolve
            play music "Cafeteria.mp3"
            n "Al llegar a la fondita, notaste el lugar casi vacío."
            show gael m nervous2 s with dissolve
            n "Gael se encontraba mirando nervioso su celular."
            show gael m normal t at jumper
            g "¡[player_name]!"
            show gael m blush t
            g "Justo te iba a llamar, mis padres decidieron mejor cerrar temprano hoy, para que no vinieras, pero creo que me tarde…"
            show gael m blush s
            player_name "No te preocupes, aún así necesitaba despejarme."
            show gael m normal t
            g "Por tu proyecto, ¿verdad?"
            show gael m normal s
            n "Cierto."
            player_name "Si, mañana voy a presentar una pintura en una galería, es por una clase…"
            n "Por alguna razón no podías ni mirarlo a los ojos."
            n "Todo era culpa de lo que pasó ayer. Si tan solo…"
            player_name "Uhm…"
            show gael m blush2 t
            g "Bueno, esperó que se quede en exposición por un tiempo. Me gustaría poder ver tu trabajo" 
            show gael m blush t
            g "Así podría decir que soy amigo de una gran artista."
            n "Amigo"
            n "{b}Amigo{/b}"
            play music "Sadend.mp3"
            n "No podías ignorar la extraña sensación de tristeza que surgió al escuchar eso."
            n "\¿Qué está haciendo con tu cabeza? Eso es normal, hasta es bueno."
            show gael m normal s
            n "Te considera una amistad."
            extend " Eso es bueno para ti ¿verdad?"

            menu:
             
             "Si":
                    player_name "{b}¡Si!{/b}"
                    show gael m nervous2 s at jumper
                    g "{b}{size=+10}???{/size}{/b}"
                    player_name "Uh..."
                    player_name "Que...¡si va a estar como por un mes allá!"
                    show gael m nervous2 t
                    g "Oh, ¡Qué bien! Entonces esperó ir después."
                    show gael m nervous2 s
                    n "Solo querías irte ya."
                    player_name "Bueno, como ya no hay trabajo creo que será mejor que me vaya."
                    extend " Nos vemos."
                    hide gael m nervous2 s with dissolve
                    n "Esta sería otra noche larga."
                    scene black with dissolve
                    stop music fadeout 1.0
                    jump hfinal_norm
             
             "No":
                player_name "{b}No...{/b}"
                show gael m nervous2 t
                g "Oh..."
                g "\¿No quieres qué la vea?"
                show gael m nervous2 s
                player_name "\¡Ay! \¡No es eso! Es que...uh..."

                menu:
                 "Decirle":
                        play music "Happyending.mp3"
                        player_name "Yo..."
                        n "Respiraste y finalmente..."
                        player_name "¡Te quería invitar a verlo conmigo!"
                        show gael m blush s at jumper
                        g "{b}{size=+10}!!!{/size}{/b}"
                        show gael m blush t
                        g "C-Claro! ¡Me encantaría ir!"
                        n "Sin dudarlo, le mandaste toda la información para que llegará."
                        hide gael m blush t with dissolve
                        n "No podías esperar a mañana."
                        scene black with dissolve
                        stop music fadeout 1.0
                        jump hfinal_bueno

                 "No decirle":
                        player_name "Uh, que no va a estar solo mañana, si no como..."
                        player_name "Uh..."
                        show gael m normal s
                        player_name "{b}¡Un mes!{/b}"
                        extend "...si, un mes..."
                        show gael m normal t
                        g "Oh, ¡Qué bien! Entonces esperó ir después."
                        show gael m normal s
                        n "Solo querías irte ya."
                        player_name "Bueno, como ya no hay trabajo creo que será mejor que me vaya. Nos vemos."
                        hide gael m normal s with dissolve
                        n "Esta sería otra noche larga."
                        scene black with dissolve
                        stop music fadeout 1.0
                        jump hfinal_norm
     "No":
            p_nvl "Hola!"
            p_nvl "No, lo siento :( "
            g_nvl "Oh, ok! Ntp, nos vemos después."
            n "Bueno, no podías simplemente dejar todo así y necesitabas descansar."
            n "Así que solo quedaba aprovechar el día de descanso hasta el final."
            scene black with dissolve
            stop music fadeout 1.0
            jump hfinal_norm

label hfinal_bueno:
    scene Gallery with dissolve
    play music "Gallery.mp3"
    n "Después de unas largas semanas, finalmente llegó el día."
    n "Toda tu clase estaba reunida en la galería con sus trabajos listos para exponer."
    n "La profesora Marta incluso se vistió para la ocasión."
    n "Cada alumno tenía que mostrarle sus trabajos antes de exponerlos, así sabrías tu nota final y solo disfrutarías el evento."
    n "Aún así, no dejabas de sentir nervios en cada paso que te acercabas a la profesora."
    n "Incluso Sofí te había dicho que estaba bien, además la profesora nunca había sido cruel al revisar."
    n "Pero sabías en el fondo que tus nervios no eran por el proyecto, si no por que aún no había llegado quién más esperabas."
    show marta normal t with dissolve
    m "¡La siguiente persona por favor!"
    show marta normal s
    n "Era hora. Respiraste hondo y le mostraste tu pintura."
    show marta normal t
    m "¡Vaya! Sabía que no me iba decepcionar jovencito."
    m "No quería creer lo que sus otros profesores hablan de usted, pero veo que tienen razón."
    m "Realmente es muy bueno su trabajo. Se que va a ser uno de los que más luzcan hoy."
    hide marta normal t with dissolve
    n "Te alegraste un poco al escuchar aquellas palabras, realmente lo habías conseguido."
    n "Al poco tiempo tu cuadro fue expuesto. Veías a varias personas que se detenían a verlo."
    n "Era un sentimiento muy grato."
    n "Cuando te encontrabas más perdido en tus pensamientos sentiste un pequeño golpe en tu hombro."
    n "No podías ocultar tu sonrisa."
    n "Era Gael."
    play music "Happyending.mp3"
    show gael s3 normal l with dissolve
    g "¿Ese es tu trabajo? Vaya que es bueno y eso que no se mucho de arte."
    show gael s3 normal c
    g "Valió la pena venir a verte-"
    show gael s3 surprised t at jumper
    g "uhhhhh"
    show gael s3 haha
    g "¡A ver tu {b}trabajo{/b}!"
    g "¡Si! Eso...Quise decir"
    show gael s3 surprised s
    player_name "{i}¿Cómo puede decir cosas así?{/i}"
    show gael s3 uh
    player_name "{i}Primero mi molestia al verlo con esa chica, luego ayer invitandolo de golpe.{/i}"
    show gael s3 sad
    player_name "{i}¡\¿Pero qué me está pasando?!{/i}"
    show gael s3 uh
    g "Uhm, ¿[player_name]? ¿Todo bien?"
    g "Perdón si dije algo que te incomodó, lo dije sin pensar y yo-"
    player_name "..."

    menu:
        "Decirle la verdad":
            player_name "Gael..."
            extend "creo que me gustas."
            show gael s3 wow
            g "{b}{size=+10}!!!{/size}{/b}"
            show gael s3 haha at jumper
            g "Y-Yo, que? "
            g "Digo uh..."
            show gael s3 surprised s
            g "..."
            show gael s3 blushl t
            g "Bueno, eso explica muchas cosas"
            show gael s3 blushl s
            player_name "¡Lo dices como si no estuvieras igual de rojo que yo!"
            show gael s3 blush
            g "E-Es diferente ¿Ok?"
            hide gael s3 blush with dissolve

    scene black with dissolve
    n "Este es..."
    extend "Un brillante futuro."
    stop music fadeout 1.0
    scene final 4 with dissolve
    n " "
    n "Has conseguido el final Bueno."
    return
    ####Final Bueno###