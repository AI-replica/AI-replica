#!/usr/bin/env python

""" Avatar generator GUI

    The avatar generator GUI is a tool for the generation of avatars for facial expression and a tool for building the facial dynamics of a chatbot.
    
    __author__ = "Marco Baturan García"
    __copyright__ = "None"
    __credits__ = "None"
    __license__ = "GPL"
    __version__ = "1.0"
    __maintainer__ = "Marco Baturan García"
    __email__ = "marco.baturan@gmail.com"
    __status__ = "Production"
    
"""
import PySimpleGUI as psg
import py_avataaars as pa

def face_generator(Facial_hair_color, Facial_hair_type, Hair_color, Skin_color, Style, Top, accessories_expr,
                   clothe_expr, eye_expr, eyebrow_expr, face_expression, graphic, hatcolor, name):
    """ Face generator.

        Received parameters to generate a new face or modify an existing face.
        In the first case, It's will be used in the configuration module.
        In the second case, It'll be used in the face module to modify eye and mouth expressions.

    """
    avatar = pa.PyAvataaar(
        style=Style,
        skin_color=Skin_color,
        hair_color=Hair_color,
        facial_hair_type=Facial_hair_type,
        facial_hair_color=Facial_hair_color,
        top_type=Top,
        hat_color=hatcolor,
        mouth_type=face_expression,
        eye_type=eye_expr,
        eyebrow_type=eyebrow_expr,
        nose_type=pa.NoseType.DEFAULT,
        accessories_type=accessories_expr,
        clothe_type=clothe_expr,
        clothe_color=hatcolor,
        clothe_graphic_type=graphic)
    # generate
    avatar.render_png_file(f'{name}.png')

def set_variables_configuration():
    """ Set variables configuration.

        I put the set of variables for initial configuration and on-the-fly emotional reconfiguration.
        Because it's too many variables, it's necessary to put in the module functions for the best
        refactor.
        : return variables:

    """
    # variables
    circle = ['CIRCLE', 'TRANSPARENT']
    skin_tones = ['BLACK', 'BROWN', 'DARK_BROWN', 'LIGHT', 'PALE', 'TANNED', 'YELLOW']
    hair_colors = ['AUBURN', 'BLACK', 'BLONDE', 'BLONDE_GOLDEN', 'BROWN', 'BROWN_DARK', 'PASTEL_PINK', 'PLATINUM',
                   'RED', 'SILVER_GRAY']
    beard_styles = ['BEARD_LIGHT', 'BEARD_MAJESTIC', 'BEARD_MEDIUM', 'DEFAULT', 'MOUSTACHE_FANCY', 'MOUSTACHE_MAGNUM']
    facial_hair_colors = ['AUBURN', 'BLACK', 'BLONDE', 'BLONDE_GOLDEN', 'BROWN', 'BROWN_DARK', 'PASTEL_PINK',
                          'PLATINUM', 'RED', 'SILVER_GRAY']
    top_types = ['EYE_PATCH', 'HAT', 'HIJAB', 'LONG_HAIR_BIG_HAIR', 'LONG_HAIR_BOB', 'LONG_HAIR_BUN', 'LONG_HAIR_CURLY',
                 'LONG_HAIR_CURVY', 'LONG_HAIR_DREADS', 'LONG_HAIR_FRIDA', 'LONG_HAIR_FRO', 'LONG_HAIR_FRO_BAND',
                 'LONG_HAIR_MIA_WALLACE', 'LONG_HAIR_NOT_TOO_LONG', 'LONG_HAIR_SHAVED_SIDES', 'LONG_HAIR_STRAIGHT',
                 'LONG_HAIR_STRAIGHT2', 'LONG_HAIR_STRAIGHT_STRAND', 'NO_HAIR', 'SHORT_HAIR_DREADS_01',
                 'SHORT_HAIR_DREADS_02',
                 'SHORT_HAIR_FRIZZLE', 'SHORT_HAIR_SHAGGY_MULLET', 'SHORT_HAIR_SHORT_CURLY', 'SHORT_HAIR_SHORT_FLAT',
                 'SHORT_HAIR_SHORT_ROUND', 'SHORT_HAIR_SHORT_WAVED', 'SHORT_HAIR_SIDES', 'SHORT_HAIR_THE_CAESAR',
                 'SHORT_HAIR_THE_CAESAR_SIDE_PART', 'TURBAN', 'WINTER_HAT1', 'WINTER_HAT2', 'WINTER_HAT3',
                 'WINTER_HAT4']
    colors = ['BLACK', 'BLUE_01', 'BLUE_02', 'BLUE_03', 'GRAY_01', 'GRAY_02', 'HEATHER', 'PASTEL_BLUE', 'PASTEL_GREEN',
              'PASTEL_ORANGE', 'PASTEL_RED', 'PASTEL_YELLOW', 'PINK', 'RED', 'WHITE']
    expressions = ['CONCERNED', 'DEFAULT', 'DISBELIEF', 'EATING', 'GRIMACE', 'SAD', 'SCREAM_OPEN', 'SERIOUS', 'SMILE',
                   'TONGUE',
                   'TWINKLE', 'VOMIT']
    eye_types = ['CLOSE', 'CRY', 'DEFAULT', 'DIZZY', 'EYE_ROLL', 'HAPPY', 'HEARTS', 'SIDE', 'SQUINT', 'SURPRISED',
                 'WINK',
                 'WINK_WACKY']
    eyebrow_types = ['ANGRY', 'ANGRY_NATURAL', 'DEFAULT', 'DEFAULT_NATURAL', 'FLAT_NATURAL', 'FROWN_NATURAL',
                     'RAISED_EXCITED',
                     'RAISED_EXCITED_NATURAL', 'SAD_CONCERNED', 'SAD_CONCERNED_NATURAL', 'UNI_BROW_NATURAL', 'UP_DOWN',
                     'UP_DOWN_NATURAL']
    accessories_types = ['DEFAULT', 'KURT', 'PRESCRIPTION_01', 'PRESCRIPTION_02', 'ROUND', 'SUNGLASSES', 'WAYFARERS']
    clothing_types = ['BLAZER_SHIRT', 'BLAZER_SWEATER', 'COLLAR_SWEATER', 'GRAPHIC_SHIRT', 'HOODIE', 'OVERALL',
                      'SHIRT_CREW_NECK',
                      'SHIRT_SCOOP_NECK', 'SHIRT_V_NECK']
    graphic = ['BAT', 'BEAR', 'CUMBIA', 'DEER', 'DIAMOND', 'HOLA', 'PIZZA', 'RESIST', 'SELENA', 'SKULL',
               'SKULL_OUTLINE']
    emotion = ['neutral','speak','happy','sad','fear','angry','disgust','surprise']
    return accessories_types, beard_styles, circle, clothing_types, colors, expressions, eye_types, eyebrow_types, facial_hair_colors, graphic, hair_colors,  skin_tones, top_types, emotion


def params_on_the_fly(values):
    """ Parameters on-the-fly.

        This function manages the parameters from values get from configuration and
        output speak of the chatbot. And detect the I/O stream for sentimental
        analysis to generate mouth movement and emotional expression.

        : param values:
        : return values:

    """

    # parameters on-the-fly
    if values[0] is None:
        Style = pa.AvatarStyle.CIRCLE

    else:
        if values[0] == 'CIRCLE':
            Style = pa.AvatarStyle.CIRCLE
        else:
            Style = pa.AvatarStyle.TRANSPARENT

    # SkinColor
    if values[1] == 'BLACK':
        Skin_color = pa.SkinColor.BLACK
    elif values[1] == 'BROWN':
        Skin_color = pa.SkinColor.BROWN
    elif values[1] == 'DARK_BROWN':
        Skin_color = pa.SkinColor.DARK_BROWN
    elif values[1] == 'LIGHT':
        Skin_color = pa.SkinColor.LIGHT
    elif values[1] == 'PALE':
        Skin_color = pa.SkinColor.PALE
    elif values[1] == 'TANNED':
        Skin_color = pa.SkinColor.TANNED
    elif values[1] == 'YELLOW':
        Skin_color = pa.SkinColor.YELLOW
    else:
        print("Invalid skin tone.")
    # hair_colors
    if values[2] == 'AUBURN':
        Hair_color = pa.HairColor.AUBURN
    elif values[2] == 'BLACK':
        Hair_color = pa.HairColor.BLACK
    elif values[2] == 'BLONDE':
        Hair_color = pa.HairColor.BLONDE
    elif values[2] == 'BLONDE_GOLDEN':
        Hair_color = pa.HairColor.BLONDE_GOLDEN
    elif values[2] == 'BROWN':
        Hair_color = pa.HairColor.BROWN
    elif values[2] == 'BROWN_DARK':
        Hair_color = pa.HairColor.BROWN_DARK
    elif values[2] == 'PASTEL_PINK':
        Hair_color = pa.HairColor.PASTEL_PINK
    elif values[2] == 'PLATINUM':
        Hair_color = pa.HairColor.PLATINUM
    elif values[2] == 'RED':
        Hair_color = pa.HairColor.RED
    elif values[2] == 'SILVER_GRAY':
        Hair_color = pa.HairColor.SILVER_GRAY
    else:
        print("Invalid hair color.")
    # BEARD
    if values[3] == 'BEARD_LIGHT':
        Facial_hair_type = pa.FacialHairType.BEARD_LIGHT
    elif values[3] == 'BEARD_MAJESTIC':
        Facial_hair_type = pa.FacialHairType.BEARD_MAJESTIC
    elif values[3] == 'BEARD_MEDIUM':
        Facial_hair_type = pa.FacialHairType.BEARD_MEDIUM
    elif values[3] == 'DEFAULT':
        Facial_hair_type = pa.FacialHairType.DEFAULT
    elif values[3] == 'MOUSTACHE_FANCY':
        Facial_hair_type = pa.FacialHairType.MOUSTACHE_FANCY
    elif values[3] == 'MOUSTACHE_MAGNUM':
        Facial_hair_type = pa.FacialHairType.MOUSTACHE_MAGNUM
    else:
        print("Invalid beard style.")
    # facial hair color
    if values[4] == 'AUBURN':
        Facial_hair_color = pa.HairColor.AUBURN
    elif values[4] == 'BLACK':
        Facial_hair_color = pa.HairColor.BLACK
    elif values[4] == 'BLONDE':
        Facial_hair_color = pa.HairColor.BLONDE
    elif values[4] == 'BLONDE_GOLDEN':
        Facial_hair_color = pa.HairColor.BLONDE_GOLDEN
    elif values[4] == 'BROWN':
        Facial_hair_color = pa.HairColor.BROWN
    elif values[4] == 'BROWN_DARK':
        Facial_hair_color = pa.HairColor.BROWN_DARK
    elif values[4] == 'PASTEL_PINK':
        Facial_hair_color = pa.HairColor.PASTEL_PINK
    elif values[4] == 'PLATINUM':
        Facial_hair_color = pa.HairColor.PLATINUM
    elif values[4] == 'RED':
        Facial_hair_color = pa.HairColor.RED
    elif values[4] == 'SILVER_GRAY':
        Facial_hair_color = pa.HairColor.SILVER_GRAY
    else:
        print("Invalid facial hair color.")
    # TopType
    if values[5] == 'EYE_PATCH':
        Top = pa.TopType.EYE_PATCH
    elif values[5] == 'HAT':
        Top = pa.TopType.HAT
    elif values[5] == 'HIJAB':
        Top = pa.TopType.HIJAB
    elif values[5] == 'LONG_HAIR_BIG_HAIR':
        Top = pa.TopType.LONG_HAIR_BIG_HAIR
    elif values[5] == 'LONG_HAIR_BOB':
        Top = pa.TopType.LONG_HAIR_BOB
    elif values[5] == 'LONG_HAIR_BUN':
        Top = pa.TopType.LONG_HAIR_BUN
    elif values[5] == 'LONG_HAIR_CURLY':
        Top = pa.TopType.LONG_HAIR_CURLY
    elif values[5] == 'LONG_HAIR_CURVY':
        Top = pa.TopType.LONG_HAIR_CURVY
    elif values[5] == 'LONG_HAIR_DREADS':
        Top = pa.TopType.LONG_HAIR_DREADS
    elif values[5] == 'LONG_HAIR_FRIDA':
        Top = pa.TopType.LONG_HAIR_FRIDA
    elif values[5] == 'LONG_HAIR_FRO':
        Top = pa.TopType.LONG_HAIR_FRO
    elif values[5] == 'LONG_HAIR_FRO_BAND':
        Top = pa.TopType.LONG_HAIR_FRO_BAND
    elif values[5] == 'LONG_HAIR_MIA_WALLACE':
        Top = pa.TopType.LONG_HAIR_MIA_WALLACE
    elif values[5] == 'LONG_HAIR_NOT_TOO_LONG':
        Top = pa.TopType.LONG_HAIR_NOT_TOO_LONG
    elif values[5] == 'LONG_HAIR_SHAVED_SIDES':
        Top = pa.TopType.LONG_HAIR_SHAVED_SIDES
    elif values[5] == 'LONG_HAIR_STRAIGHT':
        Top = pa.TopType.LONG_HAIR_STRAIGHT
    elif values[5] == 'LONG_HAIR_STRAIGHT2':
        Top = pa.TopType.LONG_HAIR_STRAIGHT2
    elif values[5] == 'LONG_HAIR_STRAIGHT_STRAND':
        Top = pa.TopType.LONG_HAIR_STRAIGHT_STRAND
    elif values[5] == 'NO_HAIR':
        Top = pa.TopType.NO_HAIR
    elif values[5] == 'SHORT_HAIR_DREADS_01':
        Top = pa.TopType.SHORT_HAIR_DREADS_01
    elif values[5] == 'SHORT_HAIR_DREADS_02':
        Top = pa.TopType.SHORT_HAIR_DREADS_02
    elif values[5] == 'SHORT_HAIR_FRIZZLE':
        Top = pa.TopType.SHORT_HAIR_FRIZZLE
    elif values[5] == 'SHORT_HAIR_SHAGGY_MULLET':
        Top = pa.TopType.SHORT_HAIR_SHAGGY_MULLET
    elif values[5] == 'SHORT_HAIR_SHORT_CURLY':
        Top = pa.TopType.SHORT_HAIR_SHORT_CURLY
    elif values[5] == 'SHORT_HAIR_SHORT_FLAT':
        Top = pa.TopType.SHORT_HAIR_SHORT_FLAT
    elif values[5] == 'SHORT_HAIR_SHORT_ROUND':
        Top = pa.TopType.SHORT_HAIR_SHORT_ROUND
    elif values[5] == 'SHORT_HAIR_SHORT_WAVED':
        Top = pa.TopType.SHORT_HAIR_SHORT_WAVED
    elif values[5] == 'SHORT_HAIR_SIDES':
        Top = pa.TopType.SHORT_HAIR_SIDES
    elif values[5] == 'SHORT_HAIR_THE_CAESAR':
        Top = pa.TopType.SHORT_HAIR_THE_CAESAR
    elif values[5] == 'SHORT_HAIR_THE_CAESAR_SIDE_PART':
        Top = pa.TopType.SHORT_HAIR_THE_CAESAR_SIDE_PART
    elif values[5] == 'TURBAN':
        Top = pa.TopType.TURBAN
    elif values[5] == 'WINTER_HAT1':
        Top = pa.TopType.WINTER_HAT1
    elif values[5] == 'WINTER_HAT2':
        Top = pa.TopType.WINTER_HAT2
    elif values[5] == 'WINTER_HAT3':
        Top = pa.TopType.WINTER_HAT3
    elif values[5] == 'WINTER_HAT4':
        Top = pa.TopType.WINTER_HAT4
    else:
        print("Invalid top type.")
    # color hat
    if values[6] == 'BLACK':
        hatcolor = pa.Color.BLACK
    elif values[6] == 'BLUE_01':
        hatcolor = pa.Color.BLUE_01
    elif values[6] == 'BLUE_02':
        hatcolor = pa.Color.BLUE_02
    elif values[6] == 'BLUE_03':
        hatcolor = pa.Color.BLUE_03
    elif values[6] == 'GRAY_01':
        hatcolor = pa.Color.GRAY_01
    elif values[6] == 'GRAY_02':
        hatcolor = pa.Color.GRAY_02
    elif values[6] == 'HEATHER':
        hatcolor = pa.Color.HEATHER
    elif values[6] == 'PASTEL_BLUE':
        hatcolor = pa.Color.PASTEL_BLUE
    elif values[6] == 'PASTEL_GREEN':
        hatcolor = pa.Color.PASTEL_GREEN
    elif values[6] == 'PASTEL_ORANGE':
        hatcolor = pa.Color.PASTEL_ORANGE
    elif values[6] == 'PASTEL_RED':
        hatcolor = pa.Color.PASTEL_RED
    elif values[6] == 'PASTEL_YELLOW':
        hatcolor = pa.Color.PASTEL_YELLOW
    elif values[6] == 'PINK':
        hatcolor = pa.Color.PINK
    elif values[6] == 'RED':
        hatcolor = pa.Color.RED
    elif values[6] == 'WHITE':
        hatcolor = pa.Color.WHITE
    else:
        print("Invalid color.")
    # Mouth Expressions
    if values[7] == 'CONCERNED':
        face_expression = pa.MouthType.CONCERNED
    elif values[7] == 'DEFAULT':
        face_expression = pa.MouthType.DEFAULT
    elif values[7] == 'DISBELIEF':
        face_expression = pa.MouthType.DISBELIEF
    elif values[7] == 'EATING':
        face_expression = pa.MouthType.EATING
    elif values[7] == 'GRIMACE':
        face_expression = pa.MouthType.GRIMACE
    elif values[7] == 'SAD':
        face_expression = pa.MouthType.SAD
    elif values[7] == 'SCREAM_OPEN':
        face_expression = pa.MouthType.SCREAM_OPEN
    elif values[7] == 'SERIOUS':
        face_expression = pa.MouthType.SERIOUS
    elif values[7] == 'SMILE':
        face_expression = pa.MouthType.SMILE
    elif values[7] == 'TONGUE':
        face_expression = pa.MouthType.TONGUE
    elif values[7] == 'TWINKLE':
        face_expression = pa.MouthType.TWINKLE
    elif values[7] == 'VOMIT':
        face_expression = pa.MouthType.VOMIT
    else:
        print("Invalid expression.")
    # eye express
    if values[8] == 'CLOSE':
        eye_expr = pa.EyesType.CLOSE
    elif values[8] == 'CRY':
        eye_expr = pa.EyesType.CRY
    elif values[8] == 'DEFAULT':
        eye_expr = pa.EyesType.DEFAULT
    elif values[8] == 'DIZZY':
        eye_expr = pa.EyesType.DIZZY
    elif values[8] == 'EYE_ROLL':
        eye_expr = pa.EyesType.EYE_ROLL
    elif values[8] == 'HAPPY':
        eye_expr = pa.EyesType.HAPPY
    elif values[8] == 'HEARTS':
        eye_expr = pa.EyesType.HEARTS
    elif values[8] == 'SIDE':
        eye_expr = pa.EyesType.SIDE
    elif values[8] == 'SQUINT':
        eye_expr = pa.EyesType.SQUINT
    elif values[8] == 'SURPRISED':
        eye_expr = pa.EyesType.SURPRISED
    elif values[8] == 'WINK':
        eye_expr = pa.EyesType.WINK
    elif values[8] == 'WINK_WACKY':
        eye_expr = pa.EyesType.WINK_WACKY
    else:
        print(f"Invalid eye type: {values[8]}")
    # Eyebrow types
    if values[9] == 'ANGRY':
        eyebrow_expr = pa.EyebrowType.ANGRY
    elif values[9] == 'ANGRY_NATURAL':
        eyebrow_expr = pa.EyebrowType.ANGRY_NATURAL
    elif values[9] == 'DEFAULT':
        eyebrow_expr = pa.EyebrowType.DEFAULT
    elif values[9] == 'DEFAULT_NATURAL':
        eyebrow_expr = pa.EyebrowType.DEFAULT_NATURAL
    elif values[9] == 'FLAT_NATURAL':
        eyebrow_expr = pa.EyebrowType.FLAT_NATURAL
    elif values[9] == 'FROWN_NATURAL':
        eyebrow_expr = pa.EyebrowType.FROWN_NATURAL
    elif values[9] == 'RAISED_EXCITED':
        eyebrow_expr = pa.EyebrowType.RAISED_EXCITED
    elif values[9] == 'RAISED_EXCITED_NATURAL':
        eyebrow_expr = pa.EyebrowType.RAISED_EXCITED_NATURAL
    elif values[9] == 'SAD_CONCERNED':
        eyebrow_expr = pa.EyebrowType.SAD_CONCERNED
    elif values[9] == 'SAD_CONCERNED_NATURAL':
        eyebrow_expr = pa.EyebrowType.SAD_CONCERNED_NATURAL
    elif values[9] == 'UNI_BROW_NATURAL':
        eyebrow_expr = pa.EyebrowType.UNI_BROW_NATURAL
    elif values[9] == 'UP_DOWN':
        eyebrow_expr = pa.EyebrowType.UP_DOWN
    elif values[9] == 'UP_DOWN_NATURAL':
        eyebrow_expr = pa.EyebrowType.UP_DOWN_NATURAL
    else:
        print(f"Invalid eye type: {values[9]}")
    # accessories type
    if values[10] == 'DEFAULT':
        accessories_expr = pa.AccessoriesType.DEFAULT
    elif values[10] == 'KURT':
        accessories_expr = pa.AccessoriesType.KURT
    elif values[10] == 'PRESCRIPTION_01':
        accessories_expr = pa.AccessoriesType.PRESCRIPTION_01
    elif values[10] == 'PRESCRIPTION_02':
        accessories_expr = pa.AccessoriesType.PRESCRIPTION_02
    elif values[10] == 'ROUND':
        accessories_expr = pa.AccessoriesType.ROUND
    elif values[10] == 'SUNGLASSES':
        accessories_expr = pa.AccessoriesType.SUNGLASSES
    elif values[10] == 'WAYFARERS':
        accessories_expr = pa.AccessoriesType.WAYFARERS
    else:
        print(f"Invalid accessories type: {values[10]}")
    # clothing_types
    if values[11] == 'BLAZER_SHIRT':
        clothe_expr = pa.ClotheType.BLAZER_SHIRT
    elif values[11] == 'BLAZER_SWEATER':
        clothe_expr = pa.ClotheType.BLAZER_SWEATER
    elif values[11] == 'COLLAR_SWEATER':
        clothe_expr = pa.ClotheType.COLLAR_SWEATER
    elif values[11] == 'GRAPHIC_SHIRT':
        clothe_expr = pa.ClotheType.GRAPHIC_SHIRT
    elif values[11] == 'HOODIE':
        clothe_expr = pa.ClotheType.HOODIE
    elif values[11] == 'OVERALL':
        clothe_expr = pa.ClotheType.OVERALL
    elif values[11] == 'SHIRT_CREW_NECK':
        clothe_expr = pa.ClotheType.SHIRT_CREW_NECK
    elif values[11] == 'SHIRT_SCOOP_NECK':
        clothe_expr = pa.ClotheType.SHIRT_SCOOP_NECK
    elif values[11] == 'SHIRT_V_NECK':
        clothe_expr = pa.ClotheType.SHIRT_V_NECK
    else:
        print(f"Invalid clothing type: {values[11]}")
    # clothe graphic
    if values[13] == 'BAT':
        graphic_expr = pa.ClotheGraphicType.BAT
    elif values[13] == 'BEAR':
        graphic_expr = pa.ClotheGraphicType.BEAR
    elif values[13] == 'CUMBIA':
        graphic_expr = pa.ClotheGraphicType.CUMBIA
    elif values[13] == 'DEER':
        graphic_expr = pa.ClotheGraphicType.DEER
    elif values[13] == 'DIAMOND':
        graphic_expr = pa.ClotheGraphicType.DIAMOND
    elif values[13] == 'HOLA':
        graphic_expr = pa.ClotheGraphicType.HOLA
    elif values[13] == 'PIZZA':
        graphic_expr = pa.ClotheGraphicType.PIZZA
    elif values[13] == 'RESIST':
        graphic_expr = pa.ClotheGraphicType.RESIST
    elif values[13] == 'SELENA':
        graphic_expr = pa.ClotheGraphicType.SELENA
    elif values[13] == 'SKULL':
        graphic_expr = pa.ClotheGraphicType.SKULL
    elif values[13] == 'SKULL_OUTLINE':
        graphic_expr = pa.ClotheGraphicType.SKULL_OUTLINE
    else:
        print(f"Invalid graphic type: {values[12]}")

    return Facial_hair_color, Facial_hair_type, Hair_color, Skin_color, Style, Top, accessories_expr, clothe_expr, eye_expr, eyebrow_expr, face_expression, graphic_expr,hatcolor


def configuration():
  """ Configuration.
  
      The function shows GUI for configuring the avatar generator and labelling de facial expression.
      : param none :
      : return png :
  """
    # set variables for face generation
    accessories_types, beard_styles, circle, clothing_types, colors, expressions, eye_types, eyebrow_types, facial_hair_colors, graphic, hair_colors, skin_tones, top_types, emotion = set_variables_configuration()
    # Format window.
    psg.theme('GreenTan')
    psg.set_options(text_justification='right')
    # nested structured list for the format of the configuration window.
    layout = [
        [psg.Text('Select params and generate the face', font=('Helvetica', 16))],
        [psg.Text('Style window'), psg.Drop(values=(circle), expand_x=True)],
        [psg.Text('Skin color'), psg.Drop(values=(skin_tones), expand_x=True)],
        [psg.Text('Hair color'), psg.Drop(values=(hair_colors), expand_x=True)],
        [psg.Text('facial hair type'), psg.Drop(values=(beard_styles), expand_x=True)],
        [psg.Text('facial hair color'), psg.Drop(values=(facial_hair_colors), expand_x=True)],
        [psg.Text('top type'), psg.Drop(values=(top_types), expand_x=True)],
        [psg.Text('top colors'), psg.Drop(values=(colors), expand_x=True)],
        [psg.Text('mouth type'), psg.Drop(values=(expressions), expand_x=True)],
        [psg.Text('eye type'), psg.Drop(values=(eye_types), expand_x=True)],
        [psg.Text('eyebrow type'), psg.Drop(values=(eyebrow_types), expand_x=True)],
        [psg.Text('accessories type'), psg.Drop(values=(accessories_types), expand_x=True)],
        [psg.Text('clothing type'), psg.Drop(values=(clothing_types), expand_x=True)],
        [psg.Text('clothing colors'), psg.Drop(values=(colors), expand_x=True)],
        [psg.Text('clothing graphic type'), psg.Drop(values=(graphic), expand_x=True)],
        [psg.Text('emotions'), psg.Drop(values=(emotion), expand_x=True)],
        [psg.Submit(), psg.Exit()]]
    window = psg.Window('Configurarion', layout, font=("Helvetica", 12))

    while True:  # The Event Loop
        event, values = window.read()

        # Parameters on the fly
        Facial_hair_color, Facial_hair_type, Hair_color, Skin_color, Style, Top, accessories_expr, clothe_expr, eye_expr, eyebrow_expr, face_expression, hatcolor, graphic_expr = params_on_the_fly(
            values)

        face_generator(Facial_hair_color, Facial_hair_type, Hair_color, Skin_color, Style, Top, accessories_expr,
                       clothe_expr, eye_expr, eyebrow_expr, face_expression, graphic, hatcolor, name=values[14])

        with open('configuration.mem', 'wt') as file:
            for value in range(len(values)):
                file.write(values[value] + '\n')
        # print(event, values)
        if event == psg.WIN_CLOSED or event == 'Exit':
            break
            # Write and save the configuration of the face.
    window.close()




configuration()
