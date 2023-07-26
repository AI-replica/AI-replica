#!/usr/bin/env python

""" Avatar generator GUI

    The avatar generator GUI is a tool for the generation of avatars for facial expression and a tool for building the
    facial dynamics of a chatbot.
    
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
    avatar.render_png_file(f'expressions/{name}.png')


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
    emotion = ['neutral', 'speak', 'happy', 'sad', 'fear', 'angry', 'disgust', 'surprise']
    return accessories_types, beard_styles, circle, clothing_types, colors, expressions, eye_types, eyebrow_types, facial_hair_colors, graphic, hair_colors, skin_tones, top_types, emotion


def params_on_the_fly(values):
    """ Parameters on-the-fly.

        This function manages the parameters from values get from configuration and
        output speak of the chatbot. And detect the I/O stream for sentimental
        analysis to generate mouth movement and emotional expression.

        : param values:
        : return values:

    """

    #  AvatarStyle
    AvatarStyle_id = values[0]
    Style = getattr(pa.AvatarStyle, AvatarStyle_id)

    # SkinColor
    skin_color_id = values[1]
    Skin_color = getattr(pa.SkinColor, skin_color_id)

    # hair_colors
    hair_color_id = values[2]
    Hair_color = getattr(pa.HairColor, hair_color_id)

    # BEARD
    facial_hair_type_id = values[3]
    Facial_hair_type = getattr(pa.FacialHairType, facial_hair_type_id)

    # facial hair color
    facial_hair_color_id = values[4]
    Facial_hair_color = getattr(pa.HairColor, facial_hair_color_id)

    # TopType
    top_id = values[5]
    Top = getattr(pa.TopType, top_id)

    # color hat
    hatcolor_id = values[6]
    hatcolor = getattr(pa.Color, hatcolor_id)

    # Mouth Expressions
    face_expression_id = values[7]
    face_expression = getattr(pa.MouthType, face_expression_id)

    # eye express
    eye_expr_id = values[8]
    eye_expr = getattr(pa.EyesType, eye_expr_id)

    # Eyebrow types
    eyebrow_expr_id = values[9]
    eyebrow_expr = getattr(pa.EyebrowType, eyebrow_expr_id)

    # accessories type
    accessories_expr_id = values[10]
    accessories_expr = getattr(pa.AccessoriesType, accessories_expr_id)

    # clothing_types
    clothe_expr_id = values[11]
    clothe_expr = getattr(pa.ClotheType, clothe_expr_id)

    # clothe graphic
    graphic_expr_id = values[13]
    graphic_expr = getattr(pa.ClotheGraphicType, graphic_expr_id)

    return Facial_hair_color, Facial_hair_type, Hair_color, Skin_color, Style, Top, accessories_expr, clothe_expr, eye_expr, eyebrow_expr, face_expression, graphic_expr, hatcolor


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
