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
