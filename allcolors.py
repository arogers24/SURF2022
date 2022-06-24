from collections import OrderedDict
import webcolors

colors = {}  # dict of colors

def RGB(red, green, blue):
    return '#{:02X}{:02X}{:02X}'.format(red, green, blue)

def closest_color(requested_colour):
    r, g, b = requested_colour
    min_colours = {}
    for key, name in colors.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - r) ** 2
        gd = (g_c - g) ** 2
        bd = (b_c - b) ** 2
        min_colours[(rd + gd + bd)] = name
    print(min_colours[min(min_colours.keys())])

# Color Contants 551 colors
ALICEBLUE = RGB(240, 248, 255)
ANTIQUEWHITE = RGB(250, 235, 215)
ANTIQUEWHITE1 = RGB(255, 239, 219)
ANTIQUEWHITE2 = RGB(238, 223, 204)
ANTIQUEWHITE3 = RGB(205, 192, 176)
ANTIQUEWHITE4 = RGB(139, 131, 120)
AQUA = RGB(0, 255, 255)
AQUAMARINE1 = RGB(127, 255, 212)
AQUAMARINE2 = RGB(118, 238, 198)
AQUAMARINE3 = RGB(102, 205, 170)
AQUAMARINE4 = RGB(69, 139, 116)
AZURE1 = RGB(240, 255, 255)
AZURE2 = RGB(224, 238, 238)
AZURE3 = RGB(193, 205, 205)
AZURE4 = RGB(131, 139, 139)
BANANA = RGB(227, 207, 87)
BEIGE = RGB(245, 245, 220)
BISQUE1 = RGB(255, 228, 196)
BISQUE2 = RGB(238, 213, 183)
BISQUE3 = RGB(205, 183, 158)
BISQUE4 = RGB(139, 125, 107)
BLACK = RGB(0, 0, 0)
BLANCHEDALMOND = RGB(255, 235, 205)
BLUE = RGB(0, 0, 255)
BLUE2 = RGB(0, 0, 238)
BLUE3 = RGB(0, 0, 205)
BLUE4 = RGB(0, 0, 139)
BLUEVIOLET = RGB(138, 43, 226)
BRICK = RGB(156, 102, 31)
BROWN = RGB(165, 42, 42)
BROWN1 = RGB(255, 64, 64)
BROWN2 = RGB(238, 59, 59)
BROWN3 = RGB(205, 51, 51)
BROWN4 = RGB(139, 35, 35)
BURLYWOOD = RGB(222, 184, 135)
BURLYWOOD1 = RGB(255, 211, 155)
BURLYWOOD2 = RGB(238, 197, 145)
BURLYWOOD3 = RGB(205, 170, 125)
BURLYWOOD4 = RGB(139, 115, 85)
BURNTSIENNA = RGB(138, 54, 15)
BURNTUMBER = RGB(138, 51, 36)
CADETBLUE = RGB(95, 158, 160)
CADETBLUE1 = RGB(152, 245, 255)
CADETBLUE2 = RGB(142, 229, 238)
CADETBLUE3 = RGB(122, 197, 205)
CADETBLUE4 = RGB(83, 134, 139)
CADMIUMORANGE = RGB(255, 97, 3)
CADMIUMYELLOW = RGB(255, 153, 18)
CARROT = RGB(237, 145, 33)
CHARTREUSE1 = RGB(127, 255, 0)
CHARTREUSE2 = RGB(118, 238, 0)
CHARTREUSE3 = RGB(102, 205, 0)
CHARTREUSE4 = RGB(69, 139, 0)
CHOCOLATE = RGB(210, 105, 30)
CHOCOLATE1 = RGB(255, 127, 36)
CHOCOLATE2 = RGB(238, 118, 33)
CHOCOLATE3 = RGB(205, 102, 29)
CHOCOLATE4 = RGB(139, 69, 19)
COBALT = RGB(61, 89, 171)
COBALTGREEN = RGB(61, 145, 64)
COLDGREY = RGB(128, 138, 135)
CORAL = RGB(255, 127, 80)
CORAL1 = RGB(255, 114, 86)
CORAL2 = RGB(238, 106, 80)
CORAL3 = RGB(205, 91, 69)
CORAL4 = RGB(139, 62, 47)
CORNFLOWERBLUE = RGB(100, 149, 237)
CORNSILK1 = RGB(255, 248, 220)
CORNSILK2 = RGB(238, 232, 205)
CORNSILK3 = RGB(205, 200, 177)
CORNSILK4 = RGB(139, 136, 120)
CRIMSON = RGB(220, 20, 60)
CYAN2 = RGB(0, 238, 238)
CYAN3 = RGB(0, 205, 205)
CYAN4 = RGB(0, 139, 139)
DARKGOLDENROD = RGB(184, 134, 11)
DARKGOLDENROD1 = RGB(255, 185, 15)
DARKGOLDENROD2 = RGB(238, 173, 14)
DARKGOLDENROD3 = RGB(205, 149, 12)
DARKGOLDENROD4 = RGB(139, 101, 8)
DARKGRAY = RGB(169, 169, 169)
DARKGREEN = RGB(0, 100, 0)
DARKKHAKI = RGB(189, 183, 107)
DARKOLIVEGREEN = RGB(85, 107, 47)
DARKOLIVEGREEN1 = RGB(202, 255, 112)
DARKOLIVEGREEN2 = RGB(188, 238, 104)
DARKOLIVEGREEN3 = RGB(162, 205, 90)
DARKOLIVEGREEN4 = RGB(110, 139, 61)
DARKORANGE = RGB(255, 140, 0)
DARKORANGE1 = RGB(255, 127, 0)
DARKORANGE2 = RGB(238, 118, 0)
DARKORANGE3 = RGB(205, 102, 0)
DARKORANGE4 = RGB(139, 69, 0)
DARKORCHID = RGB(153, 50, 204)
DARKORCHID1 = RGB(191, 62, 255)
DARKORCHID2 = RGB(178, 58, 238)
DARKORCHID3 = RGB(154, 50, 205)
DARKORCHID4 = RGB(104, 34, 139)
DARKSALMON = RGB(233, 150, 122)
DARKSEAGREEN = RGB(143, 188, 143)
DARKSEAGREEN1 = RGB(193, 255, 193)
DARKSEAGREEN2 = RGB(180, 238, 180)
DARKSEAGREEN3 = RGB(155, 205, 155)
DARKSEAGREEN4 = RGB(105, 139, 105)
DARKSLATEBLUE = RGB(72, 61, 139)
DARKSLATEGRAY = RGB(47, 79, 79)
DARKSLATEGRAY1 = RGB(151, 255, 255)
DARKSLATEGRAY2 = RGB(141, 238, 238)
DARKSLATEGRAY3 = RGB(121, 205, 205)
DARKSLATEGRAY4 = RGB(82, 139, 139)
DARKTURQUOISE = RGB(0, 206, 209)
DARKVIOLET = RGB(148, 0, 211)
DEEPPINK1 = RGB(255, 20, 147)
DEEPPINK2 = RGB(238, 18, 137)
DEEPPINK3 = RGB(205, 16, 118)
DEEPPINK4 = RGB(139, 10, 80)
DEEPSKYBLUE1 = RGB(0, 191, 255)
DEEPSKYBLUE2 = RGB(0, 178, 238)
DEEPSKYBLUE3 = RGB(0, 154, 205)
DEEPSKYBLUE4 = RGB(0, 104, 139)
DIMGRAY = RGB(105, 105, 105)
DODGERBLUE1 = RGB(30, 144, 255)
DODGERBLUE2 = RGB(28, 134, 238)
DODGERBLUE3 = RGB(24, 116, 205)
DODGERBLUE4 = RGB(16, 78, 139)
EGGSHELL = RGB(252, 230, 201)
EMERALDGREEN = RGB(0, 201, 87)
FIREBRICK = RGB(178, 34, 34)
FIREBRICK1 = RGB(255, 48, 48)
FIREBRICK2 = RGB(238, 44, 44)
FIREBRICK3 = RGB(205, 38, 38)
FIREBRICK4 = RGB(139, 26, 26)
FLESH = RGB(255, 125, 64)
FLORALWHITE = RGB(255, 250, 240)
FORESTGREEN = RGB(34, 139, 34)
GAINSBORO = RGB(220, 220, 220)
GHOSTWHITE = RGB(248, 248, 255)
GOLD1 = RGB(255, 215, 0)
GOLD2 = RGB(238, 201, 0)
GOLD3 = RGB(205, 173, 0)
GOLD4 = RGB(139, 117, 0)
GOLDENROD = RGB(218, 165, 32)
GOLDENROD1 = RGB(255, 193, 37)
GOLDENROD2 = RGB(238, 180, 34)
GOLDENROD3 = RGB(205, 155, 29)
GOLDENROD4 = RGB(139, 105, 20)
GRAY = RGB(128, 128, 128)
GRAY1 = RGB(3, 3, 3)
GRAY10 = RGB(26, 26, 26)
GRAY11 = RGB(28, 28, 28)
GRAY12 = RGB(31, 31, 31)
GRAY13 = RGB(33, 33, 33)
GRAY14 = RGB(36, 36, 36)
GRAY15 = RGB(38, 38, 38)
GRAY16 = RGB(41, 41, 41)
GRAY17 = RGB(43, 43, 43)
GRAY18 = RGB(46, 46, 46)
GRAY19 = RGB(48, 48, 48)
GRAY2 = RGB(5, 5, 5)
GRAY20 = RGB(51, 51, 51)
GRAY21 = RGB(54, 54, 54)
GRAY22 = RGB(56, 56, 56)
GRAY23 = RGB(59, 59, 59)
GRAY24 = RGB(61, 61, 61)
GRAY25 = RGB(64, 64, 64)
GRAY26 = RGB(66, 66, 66)
GRAY27 = RGB(69, 69, 69)
GRAY28 = RGB(71, 71, 71)
GRAY29 = RGB(74, 74, 74)
GRAY3 = RGB(8, 8, 8)
GRAY30 = RGB(77, 77, 77)
GRAY31 = RGB(79, 79, 79)
GRAY32 = RGB(82, 82, 82)
GRAY33 = RGB(84, 84, 84)
GRAY34 = RGB(87, 87, 87)
GRAY35 = RGB(89, 89, 89)
GRAY36 = RGB(92, 92, 92)
GRAY37 = RGB(94, 94, 94)
GRAY38 = RGB(97, 97, 97)
GRAY39 = RGB(99, 99, 99)
GRAY4 = RGB(10, 10, 10)
GRAY40 = RGB(102, 102, 102)
GRAY42 = RGB(107, 107, 107)
GRAY43 = RGB(110, 110, 110)
GRAY44 = RGB(112, 112, 112)
GRAY45 = RGB(115, 115, 115)
GRAY46 = RGB(117, 117, 117)
GRAY47 = RGB(120, 120, 120)
GRAY48 = RGB(122, 122, 122)
GRAY49 = RGB(125, 125, 125)
GRAY5 = RGB(13, 13, 13)
GRAY50 = RGB(127, 127, 127)
GRAY51 = RGB(130, 130, 130)
GRAY52 = RGB(133, 133, 133)
GRAY53 = RGB(135, 135, 135)
GRAY54 = RGB(138, 138, 138)
GRAY55 = RGB(140, 140, 140)
GRAY56 = RGB(143, 143, 143)
GRAY57 = RGB(145, 145, 145)
GRAY58 = RGB(148, 148, 148)
GRAY59 = RGB(150, 150, 150)
GRAY6 = RGB(15, 15, 15)
GRAY60 = RGB(153, 153, 153)
GRAY61 = RGB(156, 156, 156)
GRAY62 = RGB(158, 158, 158)
GRAY63 = RGB(161, 161, 161)
GRAY64 = RGB(163, 163, 163)
GRAY65 = RGB(166, 166, 166)
GRAY66 = RGB(168, 168, 168)
GRAY67 = RGB(171, 171, 171)
GRAY68 = RGB(173, 173, 173)
GRAY69 = RGB(176, 176, 176)
GRAY7 = RGB(18, 18, 18)
GRAY70 = RGB(179, 179, 179)
GRAY71 = RGB(181, 181, 181)
GRAY72 = RGB(184, 184, 184)
GRAY73 = RGB(186, 186, 186)
GRAY74 = RGB(189, 189, 189)
GRAY75 = RGB(191, 191, 191)
GRAY76 = RGB(194, 194, 194)
GRAY77 = RGB(196, 196, 196)
GRAY78 = RGB(199, 199, 199)
GRAY79 = RGB(201, 201, 201)
GRAY8 = RGB(20, 20, 20)
GRAY80 = RGB(204, 204, 204)
GRAY81 = RGB(207, 207, 207)
GRAY82 = RGB(209, 209, 209)
GRAY83 = RGB(212, 212, 212)
GRAY84 = RGB(214, 214, 214)
GRAY85 = RGB(217, 217, 217)
GRAY86 = RGB(219, 219, 219)
GRAY87 = RGB(222, 222, 222)
GRAY88 = RGB(224, 224, 224)
GRAY89 = RGB(227, 227, 227)
GRAY9 = RGB(23, 23, 23)
GRAY90 = RGB(229, 229, 229)
GRAY91 = RGB(232, 232, 232)
GRAY92 = RGB(235, 235, 235)
GRAY93 = RGB(237, 237, 237)
GRAY94 = RGB(240, 240, 240)
GRAY95 = RGB(242, 242, 242)
GRAY97 = RGB(247, 247, 247)
GRAY98 = RGB(250, 250, 250)
GRAY99 = RGB(252, 252, 252)
GREEN = RGB(0, 128, 0)
GREEN1 = RGB(0, 255, 0)
GREEN2 = RGB(0, 238, 0)
GREEN3 = RGB(0, 205, 0)
GREEN4 = RGB(0, 139, 0)
GREENYELLOW = RGB(173, 255, 47)
HONEYDEW1 = RGB(240, 255, 240)
HONEYDEW2 = RGB(224, 238, 224)
HONEYDEW3 = RGB(193, 205, 193)
HONEYDEW4 = RGB(131, 139, 131)
HOTPINK = RGB(255, 105, 180)
HOTPINK1 = RGB(255, 110, 180)
HOTPINK2 = RGB(238, 106, 167)
HOTPINK3 = RGB(205, 96, 144)
HOTPINK4 = RGB(139, 58, 98)
INDIANRED = RGB(205, 92, 92)
INDIANRED1 = RGB(255, 106, 106)
INDIANRED2 = RGB(238, 99, 99)
INDIANRED3 = RGB(205, 85, 85)
INDIANRED4 = RGB(139, 58, 58)
INDIGO = RGB(75, 0, 130)
IVORY1 = RGB(255, 255, 240)
IVORY2 = RGB(238, 238, 224)
IVORY3 = RGB(205, 205, 193)
IVORY4 = RGB(139, 139, 131)
IVORYBLACK = RGB(41, 36, 33)
KHAKI = RGB(240, 230, 140)
KHAKI1 = RGB(255, 246, 143)
KHAKI2 = RGB(238, 230, 133)
KHAKI3 = RGB(205, 198, 115)
KHAKI4 = RGB(139, 134, 78)
LAVENDER = RGB(230, 230, 250)
LAVENDERBLUSH1 = RGB(255, 240, 245)
LAVENDERBLUSH2 = RGB(238, 224, 229)
LAVENDERBLUSH3 = RGB(205, 193, 197)
LAVENDERBLUSH4 = RGB(139, 131, 134)
LAWNGREEN = RGB(124, 252, 0)
LEMONCHIFFON1 = RGB(255, 250, 205)
LEMONCHIFFON2 = RGB(238, 233, 191)
LEMONCHIFFON3 = RGB(205, 201, 165)
LEMONCHIFFON4 = RGB(139, 137, 112)
LIGHTBLUE = RGB(173, 216, 230)
LIGHTBLUE1 = RGB(191, 239, 255)
LIGHTBLUE2 = RGB(178, 223, 238)
LIGHTBLUE3 = RGB(154, 192, 205)
LIGHTBLUE4 = RGB(104, 131, 139)
LIGHTCORAL = RGB(240, 128, 128)
LIGHTCYAN1 = RGB(224, 255, 255)
LIGHTCYAN2 = RGB(209, 238, 238)
LIGHTCYAN3 = RGB(180, 205, 205)
LIGHTCYAN4 = RGB(122, 139, 139)
LIGHTGOLDENROD1 = RGB(255, 236, 139)
LIGHTGOLDENROD2 = RGB(238, 220, 130)
LIGHTGOLDENROD3 = RGB(205, 190, 112)
LIGHTGOLDENROD4 = RGB(139, 129, 76)
LIGHTGOLDENRODYELLOW = RGB(250, 250, 210)
LIGHTGREY = RGB(211, 211, 211)
LIGHTPINK = RGB(255, 182, 193)
LIGHTPINK1 = RGB(255, 174, 185)
LIGHTPINK2 = RGB(238, 162, 173)
LIGHTPINK3 = RGB(205, 140, 149)
LIGHTPINK4 = RGB(139, 95, 101)
LIGHTSALMON1 = RGB(255, 160, 122)
LIGHTSALMON2 = RGB(238, 149, 114)
LIGHTSALMON3 = RGB(205, 129, 98)
LIGHTSALMON4 = RGB(139, 87, 66)
LIGHTSEAGREEN = RGB(32, 178, 170)
LIGHTSKYBLUE = RGB(135, 206, 250)
LIGHTSKYBLUE1 = RGB(176, 226, 255)
LIGHTSKYBLUE2 = RGB(164, 211, 238)
LIGHTSKYBLUE3 = RGB(141, 182, 205)
LIGHTSKYBLUE4 = RGB(96, 123, 139)
LIGHTSLATEBLUE = RGB(132, 112, 255)
LIGHTSLATEGRAY = RGB(119, 136, 153)
LIGHTSTEELBLUE = RGB(176, 196, 222)
LIGHTSTEELBLUE1 = RGB(202, 225, 255)
LIGHTSTEELBLUE2 = RGB(188, 210, 238)
LIGHTSTEELBLUE3 = RGB(162, 181, 205)
LIGHTSTEELBLUE4 = RGB(110, 123, 139)
LIGHTYELLOW1 = RGB(255, 255, 224)
LIGHTYELLOW2 = RGB(238, 238, 209)
LIGHTYELLOW3 = RGB(205, 205, 180)
LIGHTYELLOW4 = RGB(139, 139, 122)
LIMEGREEN = RGB(50, 205, 50)
LINEN = RGB(250, 240, 230)
MAGENTA = RGB(255, 0, 255)
MAGENTA2 = RGB(238, 0, 238)
MAGENTA3 = RGB(205, 0, 205)
MAGENTA4 = RGB(139, 0, 139)
MANGANESEBLUE = RGB(3, 168, 158)
MAROON = RGB(128, 0, 0)
MAROON1 = RGB(255, 52, 179)
MAROON2 = RGB(238, 48, 167)
MAROON3 = RGB(205, 41, 144)
MAROON4 = RGB(139, 28, 98)
MEDIUMORCHID = RGB(186, 85, 211)
MEDIUMORCHID1 = RGB(224, 102, 255)
MEDIUMORCHID2 = RGB(209, 95, 238)
MEDIUMORCHID3 = RGB(180, 82, 205)
MEDIUMORCHID4 = RGB(122, 55, 139)
MEDIUMPURPLE = RGB(147, 112, 219)
MEDIUMPURPLE1 = RGB(171, 130, 255)
MEDIUMPURPLE2 = RGB(159, 121, 238)
MEDIUMPURPLE3 = RGB(137, 104, 205)
MEDIUMPURPLE4 = RGB(93, 71, 139)
MEDIUMSEAGREEN = RGB(60, 179, 113)
MEDIUMSLATEBLUE = RGB(123, 104, 238)
MEDIUMSPRINGGREEN = RGB(0, 250, 154)
MEDIUMTURQUOISE = RGB(72, 209, 204)
MEDIUMVIOLETRED = RGB(199, 21, 133)
MELON = RGB(227, 168, 105)
MIDNIGHTBLUE = RGB(25, 25, 112)
MINT = RGB(189, 252, 201)
MINTCREAM = RGB(245, 255, 250)
MISTYROSE1 = RGB(255, 228, 225)
MISTYROSE2 = RGB(238, 213, 210)
MISTYROSE3 = RGB(205, 183, 181)
MISTYROSE4 = RGB(139, 125, 123)
MOCCASIN = RGB(255, 228, 181)
NAVAJOWHITE1 = RGB(255, 222, 173)
NAVAJOWHITE2 = RGB(238, 207, 161)
NAVAJOWHITE3 = RGB(205, 179, 139)
NAVAJOWHITE4 = RGB(139, 121, 94)
NAVY = RGB(0, 0, 128)
OLDLACE = RGB(253, 245, 230)
OLIVE = RGB(128, 128, 0)
OLIVEDRAB = RGB(107, 142, 35)
OLIVEDRAB1 = RGB(192, 255, 62)
OLIVEDRAB2 = RGB(179, 238, 58)
OLIVEDRAB3 = RGB(154, 205, 50)
OLIVEDRAB4 = RGB(105, 139, 34)
ORANGE = RGB(255, 128, 0)
ORANGE1 = RGB(255, 165, 0)
ORANGE2 = RGB(238, 154, 0)
ORANGE3 = RGB(205, 133, 0)
ORANGE4 = RGB(139, 90, 0)
ORANGERED1 = RGB(255, 69, 0)
ORANGERED2 = RGB(238, 64, 0)
ORANGERED3 = RGB(205, 55, 0)
ORANGERED4 = RGB(139, 37, 0)
ORCHID = RGB(218, 112, 214)
ORCHID1 = RGB(255, 131, 250)
ORCHID2 = RGB(238, 122, 233)
ORCHID3 = RGB(205, 105, 201)
ORCHID4 = RGB(139, 71, 137)
PALEGOLDENROD = RGB(238, 232, 170)
PALEGREEN = RGB(152, 251, 152)
PALEGREEN1 = RGB(154, 255, 154)
PALEGREEN2 = RGB(144, 238, 144)
PALEGREEN3 = RGB(124, 205, 124)
PALEGREEN4 = RGB(84, 139, 84)
PALETURQUOISE1 = RGB(187, 255, 255)
PALETURQUOISE2 = RGB(174, 238, 238)
PALETURQUOISE3 = RGB(150, 205, 205)
PALETURQUOISE4 = RGB(102, 139, 139)
PALEVIOLETRED = RGB(219, 112, 147)
PALEVIOLETRED1 = RGB(255, 130, 171)
PALEVIOLETRED2 = RGB(238, 121, 159)
PALEVIOLETRED3 = RGB(205, 104, 137)
PALEVIOLETRED4 = RGB(139, 71, 93)
PAPAYAWHIP = RGB(255, 239, 213)
PEACHPUFF1 = RGB(255, 218, 185)
PEACHPUFF2 = RGB(238, 203, 173)
PEACHPUFF3 = RGB(205, 175, 149)
PEACHPUFF4 = RGB(139, 119, 101)
PEACOCK = RGB(51, 161, 201)
PINK = RGB(255, 192, 203)
PINK1 = RGB(255, 181, 197)
PINK2 = RGB(238, 169, 184)
PINK3 = RGB(205, 145, 158)
PINK4 = RGB(139, 99, 108)
PLUM = RGB(221, 160, 221)
PLUM1 = RGB(255, 187, 255)
PLUM2 = RGB(238, 174, 238)
PLUM3 = RGB(205, 150, 205)
PLUM4 = RGB(139, 102, 139)
POWDERBLUE = RGB(176, 224, 230)
PURPLE = RGB(128, 0, 128)
PURPLE1 = RGB(155, 48, 255)
PURPLE2 = RGB(145, 44, 238)
PURPLE3 = RGB(125, 38, 205)
PURPLE4 = RGB(85, 26, 139)
RASPBERRY = RGB(135, 38, 87)
RAWSIENNA = RGB(199, 97, 20)
RED1 = RGB(255, 0, 0)
RED2 = RGB(238, 0, 0)
RED3 = RGB(205, 0, 0)
RED4 = RGB(139, 0, 0)
ROSYBROWN = RGB(188, 143, 143)
ROSYBROWN1 = RGB(255, 193, 193)
ROSYBROWN2 = RGB(238, 180, 180)
ROSYBROWN3 = RGB(205, 155, 155)
ROSYBROWN4 = RGB(139, 105, 105)
ROYALBLUE = RGB(65, 105, 225)
ROYALBLUE1 = RGB(72, 118, 255)
ROYALBLUE2 = RGB(67, 110, 238)
ROYALBLUE3 = RGB(58, 95, 205)
ROYALBLUE4 = RGB(39, 64, 139)
SALMON = RGB(250, 128, 114)
SALMON1 = RGB(255, 140, 105)
SALMON2 = RGB(238, 130, 98)
SALMON3 = RGB(205, 112, 84)
SALMON4 = RGB(139, 76, 57)
SANDYBROWN = RGB(244, 164, 96)
SAPGREEN = RGB(48, 128, 20)
SEAGREEN1 = RGB(84, 255, 159)
SEAGREEN2 = RGB(78, 238, 148)
SEAGREEN3 = RGB(67, 205, 128)
SEAGREEN4 = RGB(46, 139, 87)
SEASHELL1 = RGB(255, 245, 238)
SEASHELL2 = RGB(238, 229, 222)
SEASHELL3 = RGB(205, 197, 191)
SEASHELL4 = RGB(139, 134, 130)
SEPIA = RGB(94, 38, 18)
SGIBEET = RGB(142, 56, 142)
SGIBRIGHTGRAY = RGB(197, 193, 170)
SGICHARTREUSE = RGB(113, 198, 113)
SGIDARKGRAY = RGB(85, 85, 85)
SGIGRAY12 = RGB(30, 30, 30)
SGIGRAY16 = RGB(40, 40, 40)
SGIGRAY32 = RGB(81, 81, 81)
SGIGRAY36 = RGB(91, 91, 91)
SGIGRAY52 = RGB(132, 132, 132)
SGIGRAY56 = RGB(142, 142, 142)
SGIGRAY72 = RGB(183, 183, 183)
SGIGRAY76 = RGB(193, 193, 193)
SGIGRAY92 = RGB(234, 234, 234)
SGIGRAY96 = RGB(244, 244, 244)
SGILIGHTBLUE = RGB(125, 158, 192)
SGILIGHTGRAY = RGB(170, 170, 170)
SGIOLIVEDRAB = RGB(142, 142, 56)
SGISALMON = RGB(198, 113, 113)
SGISLATEBLUE = RGB(113, 113, 198)
SGITEAL = RGB(56, 142, 142)
SIENNA = RGB(160, 82, 45)
SIENNA1 = RGB(255, 130, 71)
SIENNA2 = RGB(238, 121, 66)
SIENNA3 = RGB(205, 104, 57)
SIENNA4 = RGB(139, 71, 38)
SILVER = RGB(192, 192, 192)
SKYBLUE = RGB(135, 206, 235)
SKYBLUE1 = RGB(135, 206, 255)
SKYBLUE2 = RGB(126, 192, 238)
SKYBLUE3 = RGB(108, 166, 205)
SKYBLUE4 = RGB(74, 112, 139)
SLATEBLUE = RGB(106, 90, 205)
SLATEBLUE1 = RGB(131, 111, 255)
SLATEBLUE2 = RGB(122, 103, 238)
SLATEBLUE3 = RGB(105, 89, 205)
SLATEBLUE4 = RGB(71, 60, 139)
SLATEGRAY = RGB(112, 128, 144)
SLATEGRAY1 = RGB(198, 226, 255)
SLATEGRAY2 = RGB(185, 211, 238)
SLATEGRAY3 = RGB(159, 182, 205)
SLATEGRAY4 = RGB(108, 123, 139)
SNOW1 = RGB(255, 250, 250)
SNOW2 = RGB(238, 233, 233)
SNOW3 = RGB(205, 201, 201)
SNOW4 = RGB(139, 137, 137)
SPRINGGREEN = RGB(0, 255, 127)
SPRINGGREEN1 = RGB(0, 238, 118)
SPRINGGREEN2 = RGB(0, 205, 102)
SPRINGGREEN3 = RGB(0, 139, 69)
STEELBLUE = RGB(70, 130, 180)
STEELBLUE1 = RGB(99, 184, 255)
STEELBLUE2 = RGB(92, 172, 238)
STEELBLUE3 = RGB(79, 148, 205)
STEELBLUE4 = RGB(54, 100, 139)
TAN = RGB(210, 180, 140)
TAN1 = RGB(255, 165, 79)
TAN2 = RGB(238, 154, 73)
TAN3 = RGB(205, 133, 63)
TAN4 = RGB(139, 90, 43)
TEAL = RGB(0, 128, 128)
THISTLE = RGB(216, 191, 216)
THISTLE1 = RGB(255, 225, 255)
THISTLE2 = RGB(238, 210, 238)
THISTLE3 = RGB(205, 181, 205)
THISTLE4 = RGB(139, 123, 139)
TOMATO1 = RGB(255, 99, 71)
TOMATO2 = RGB(238, 92, 66)
TOMATO3 = RGB(205, 79, 57)
TOMATO4 = RGB(139, 54, 38)
TURQUOISE = RGB(64, 224, 208)
TURQUOISE1 = RGB(0, 245, 255)
TURQUOISE2 = RGB(0, 229, 238)
TURQUOISE3 = RGB(0, 197, 205)
TURQUOISE4 = RGB(0, 134, 139)
TURQUOISEBLUE = RGB(0, 199, 140)
VIOLET = RGB(238, 130, 238)
VIOLETRED = RGB(208, 32, 144)
VIOLETRED1 = RGB(255, 62, 150)
VIOLETRED2 = RGB(238, 58, 140)
VIOLETRED3 = RGB(205, 50, 120)
VIOLETRED4 = RGB(139, 34, 82)
WARMGREY = RGB(128, 128, 105)
WHEAT = RGB(245, 222, 179)
WHEAT1 = RGB(255, 231, 186)
WHEAT2 = RGB(238, 216, 174)
WHEAT3 = RGB(205, 186, 150)
WHEAT4 = RGB(139, 126, 102)
WHITE = RGB(255, 255, 255)
WHITESMOKE = RGB(245, 245, 245)
YELLOW1 = RGB(255, 255, 0)
YELLOW2 = RGB(238, 238, 0)
YELLOW3 = RGB(205, 205, 0)
YELLOW4 = RGB(139, 139, 0)

# Add colors to colors dictionary
colors[ALICEBLUE] = 'white'
colors[ANTIQUEWHITE] = 'white'
colors[ANTIQUEWHITE1] = 'white'
colors[ANTIQUEWHITE2] = 'brown'
colors[ANTIQUEWHITE3] = 'brown'
colors[ANTIQUEWHITE4] = 'brown'
colors[AQUA] = 'cyan'
colors[AQUAMARINE1] = 'cyan'
colors[AQUAMARINE2] = 'cyan'
colors[AQUAMARINE3] = 'cyan'
colors[AQUAMARINE4] = 'cyan'
colors[AZURE1] = 'white'
colors[AZURE2] = 'white'
colors[AZURE3] = 'white'
colors[AZURE4] = 'gray'
colors[BANANA] = 'yellow'
colors[BEIGE] = 'white'
colors[BISQUE1] = 'brown'
colors[BISQUE2] = 'brown'
colors[BISQUE3] = 'brown'
colors[BISQUE4] = 'brown'
colors[BLACK] = 'black'
colors[BLANCHEDALMOND] = 'brown'
colors[BLUE] = 'blue'
colors[BLUE2] = 'blue'
colors[BLUE3] = 'blue'
colors[BLUE4] = 'blue'
colors[BLUEVIOLET] = 'purple'
colors[BRICK] = 'brown'
colors[BROWN] = 'brown'
colors[BROWN1] = 'red'
colors[BROWN2] = 'red'
colors[BROWN3] = 'brown'
colors[BROWN4] = 'brown'
colors[BURLYWOOD] = 'brown'
colors[BURLYWOOD1] = 'brown'
colors[BURLYWOOD2] = 'brown'
colors[BURLYWOOD3] = 'brown'
colors[BURLYWOOD4] = 'brown'
colors[BURNTSIENNA] = 'brown'
colors[BURNTUMBER] = 'brown'
colors[CADETBLUE] = 'cyan'
colors[CADETBLUE1] = 'cyan'
colors[CADETBLUE2] = 'cyan'
colors[CADETBLUE3] = 'cyan'
colors[CADETBLUE4] = 'cyan'
colors[CADMIUMORANGE] = 'orange'
colors[CADMIUMYELLOW] = 'orange'
colors[CARROT] = 'orange'
colors[CHARTREUSE1] = 'green'
colors[CHARTREUSE2] = 'green'
colors[CHARTREUSE3] = 'green'
colors[CHARTREUSE4] = 'green'
colors[CHOCOLATE] = 'brown'
colors[CHOCOLATE1] = 'brown'
colors[CHOCOLATE2] = 'brown'
colors[CHOCOLATE3] = 'brown'
colors[CHOCOLATE4] = 'brown'
colors[COBALT] = 'blue'
colors[COBALTGREEN] = 'green'
colors[COLDGREY] = 'gray'
colors[CORAL] = 'orange'
colors[CORAL1] = 'orange'
colors[CORAL2] = 'orange'
colors[CORAL3] = 'orange'
colors[CORAL4] = 'orange'
colors[CORNFLOWERBLUE] = 'blue'
colors[CORNSILK1] = 'brown'
colors[CORNSILK2] = 'brown'
colors[CORNSILK3] = 'brown'
colors[CORNSILK4] = 'brown'
colors[CRIMSON] = 'red'
colors[CYAN2] = 'cyan'
colors[CYAN3] = 'cyan'
colors[CYAN4] = 'cyan'
colors[DARKGOLDENROD] = 'yellow'
colors[DARKGOLDENROD1] = 'yellow'
colors[DARKGOLDENROD2] = 'yellow'
colors[DARKGOLDENROD3] = 'yellow'
colors[DARKGOLDENROD4] = 'yellow'
colors[DARKGRAY] = 'gray'
colors[DARKGREEN] = 'green'
colors[DARKKHAKI] = 'yellow'
colors[DARKOLIVEGREEN] = 'green'
colors[DARKOLIVEGREEN1] = 'green'
colors[DARKOLIVEGREEN2] = 'green'
colors[DARKOLIVEGREEN3] = 'green'
colors[DARKOLIVEGREEN4] = 'green'
colors[DARKORANGE] = 'orange'
colors[DARKORANGE1] = 'orange'
colors[DARKORANGE2] = 'orange'
colors[DARKORANGE3] = 'orange'
colors[DARKORANGE4] = 'orange'
colors[DARKORCHID] = 'purple'
colors[DARKORCHID1] = 'purple'
colors[DARKORCHID2] = 'purple'
colors[DARKORCHID3] = 'purple'
colors[DARKORCHID4] = 'purple'
colors[DARKSALMON] = 'red'
colors[DARKSEAGREEN] = 'green'
colors[DARKSEAGREEN1] = 'green'
colors[DARKSEAGREEN2] = 'green'
colors[DARKSEAGREEN3] = 'green'
colors[DARKSEAGREEN4] = 'green'
colors[DARKSLATEBLUE] = 'purple'
colors[DARKSLATEGRAY] = 'gray'
colors[DARKSLATEGRAY1] = 'cyan'
colors[DARKSLATEGRAY2] = 'cyan'
colors[DARKSLATEGRAY3] = 'cyan'
colors[DARKSLATEGRAY4] = 'cyan'
colors[DARKTURQUOISE] = 'cyan'
colors[DARKVIOLET] = 'purple'
colors[DEEPPINK1] = 'pink'
colors[DEEPPINK2] = 'pink'
colors[DEEPPINK3] = 'pink'
colors[DEEPPINK4] = 'pink'
colors[DEEPSKYBLUE1] = 'blue'
colors[DEEPSKYBLUE2] = 'blue'
colors[DEEPSKYBLUE3] = 'blue'
colors[DEEPSKYBLUE4] = 'blue'
colors[DIMGRAY] = 'gray'
colors[DODGERBLUE1] = 'blue'
colors[DODGERBLUE2] = 'blue'
colors[DODGERBLUE3] = 'blue'
colors[DODGERBLUE4] = 'blue'
colors[EGGSHELL] = 'brown'
colors[EMERALDGREEN] = 'green'
colors[FIREBRICK] = 'red'
colors[FIREBRICK1] = 'red'
colors[FIREBRICK2] = 'red'
colors[FIREBRICK3] = 'red'
colors[FIREBRICK4] = 'red'
colors[FLESH] = 'orange'
colors[FLORALWHITE] = 'white'
colors[FORESTGREEN] = 'green'
colors[GAINSBORO] = 'gray'
colors[GHOSTWHITE] = 'white'
colors[GOLD1] = 'gold'
colors[GOLD2] = 'gold'
colors[GOLD3] = 'gold'
colors[GOLD4] = 'gold'
colors[GOLDENROD] = 'brown'
colors[GOLDENROD1] = 'brown'
colors[GOLDENROD2] = 'brown'
colors[GOLDENROD3] = 'brown'
colors[GOLDENROD4] = 'brown'
colors[GRAY] = 'gray'
colors[GRAY1] = 'black'
colors[GRAY10] = 'black'
colors[GRAY11] = 'black'
colors[GRAY12] = 'black'
colors[GRAY13] = 'black'
colors[GRAY14] = 'black'
colors[GRAY15] = 'black'
colors[GRAY16] = 'gray'
colors[GRAY17] = 'gray'
colors[GRAY18] = 'gray'
colors[GRAY19] = 'gray'
colors[GRAY2] = 'black'
colors[GRAY20] = 'gray'
colors[GRAY21] = 'gray'
colors[GRAY22] = 'gray'
colors[GRAY23] = 'gray'
colors[GRAY24] = 'gray'
colors[GRAY25] = 'gray'
colors[GRAY26] = 'gray'
colors[GRAY27] = 'gray'
colors[GRAY28] = 'gray'
colors[GRAY29] = 'gray'
colors[GRAY3] = 'black'
colors[GRAY30] = 'gray'
colors[GRAY31] = 'gray'
colors[GRAY32] = 'gray'
colors[GRAY33] = 'gray'
colors[GRAY34] = 'gray'
colors[GRAY35] = 'gray'
colors[GRAY36] = 'gray'
colors[GRAY37] = 'gray'
colors[GRAY38] = 'gray'
colors[GRAY39] = 'gray'
colors[GRAY4] = 'black'
colors[GRAY40] = 'gray'
colors[GRAY42] = 'gray'
colors[GRAY43] = 'gray'
colors[GRAY44] = 'gray'
colors[GRAY45] = 'gray'
colors[GRAY46] = 'gray'
colors[GRAY47] = 'gray'
colors[GRAY48] = 'gray'
colors[GRAY49] = 'gray'
colors[GRAY5] = 'black'
colors[GRAY50] = 'gray'
colors[GRAY51] = 'gray'
colors[GRAY52] = 'gray'
colors[GRAY53] = 'gray'
colors[GRAY54] = 'gray'
colors[GRAY55] = 'gray'
colors[GRAY56] = 'gray'
colors[GRAY57] = 'gray'
colors[GRAY58] = 'gray'
colors[GRAY59] = 'gray'
colors[GRAY6] = 'black'
colors[GRAY60] = 'gray'
colors[GRAY61] = 'gray'
colors[GRAY62] = 'gray'
colors[GRAY63] = 'gray'
colors[GRAY64] = 'gray'
colors[GRAY65] = 'gray'
colors[GRAY66] = 'gray'
colors[GRAY67] = 'gray'
colors[GRAY68] = 'gray'
colors[GRAY69] = 'gray'
colors[GRAY7] = 'black'
colors[GRAY70] = 'gray'
colors[GRAY71] = 'gray'
colors[GRAY72] = 'gray'
colors[GRAY73] = 'gray'
colors[GRAY74] = 'gray'
colors[GRAY75] = 'gray'
colors[GRAY76] = 'gray'
colors[GRAY77] = 'gray'
colors[GRAY78] = 'gray'
colors[GRAY79] = 'gray'
colors[GRAY8] = 'black'
colors[GRAY80] = 'gray'
colors[GRAY81] = 'gray'
colors[GRAY82] = 'gray'
colors[GRAY83] = 'gray'
colors[GRAY84] = 'gray'
colors[GRAY85] = 'gray'
colors[GRAY86] = 'gray'
colors[GRAY87] = 'gray'
colors[GRAY88] = 'gray'
colors[GRAY89] = 'gray'
colors[GRAY9] = 'black'
colors[GRAY90] = 'gray'
colors[GRAY91] = 'gray'
colors[GRAY92] = 'gray'
colors[GRAY93] = 'white'
colors[GRAY94] = 'white'
colors[GRAY95] = 'white'
colors[GRAY97] = 'white'
colors[GRAY98] = 'white'
colors[GRAY99] = 'white'
colors[GREEN] = 'green'
colors[GREEN1] = 'green'
colors[GREEN2] = 'green'
colors[GREEN3] = 'green'
colors[GREEN4] = 'green'
colors[GREENYELLOW] = 'green'
colors[HONEYDEW1] = 'white'
colors[HONEYDEW2] = 'white'
colors[HONEYDEW3] = 'gray'
colors[HONEYDEW4] = 'gray'
colors[HOTPINK] = 'pink'
colors[HOTPINK1] = 'pink'
colors[HOTPINK2] = 'pink'
colors[HOTPINK3] = 'pink'
colors[HOTPINK4] = 'pink'
colors[INDIANRED] = 'red'
colors[INDIANRED1] = 'red'
colors[INDIANRED2] = 'red'
colors[INDIANRED3] = 'red'
colors[INDIANRED4] = 'red'
colors[INDIGO] = 'purple'
colors[IVORY1] = 'white'
colors[IVORY2] = 'white'
colors[IVORY3] = 'gray'
colors[IVORY4] = 'gray'
colors[IVORYBLACK] = 'black'
colors[KHAKI] = 'yellow'
colors[KHAKI1] = 'yellow'
colors[KHAKI2] = 'yellow'
colors[KHAKI3] = 'yellow'
colors[KHAKI4] = 'yellow'
colors[LAVENDER] = 'purple'
colors[LAVENDERBLUSH1] = 'white'
colors[LAVENDERBLUSH2] = 'white'
colors[LAVENDERBLUSH3] = 'gray'
colors[LAVENDERBLUSH4] = 'gray'
colors[LAWNGREEN] = 'green'
colors[LEMONCHIFFON1] = 'yellow'
colors[LEMONCHIFFON2] = 'yellow'
colors[LEMONCHIFFON3] = 'yellow'
colors[LEMONCHIFFON4] = 'yellow'
colors[LIGHTBLUE] = 'blue'
colors[LIGHTBLUE1] = 'blue'
colors[LIGHTBLUE2] = 'blue'
colors[LIGHTBLUE3] = 'blue'
colors[LIGHTBLUE4] = 'blue'
colors[LIGHTCORAL] = 'red'
colors[LIGHTCYAN1] = 'cyan'
colors[LIGHTCYAN2] = 'cyan'
colors[LIGHTCYAN3] = 'cyan'
colors[LIGHTCYAN4] = 'cyan'
colors[LIGHTGOLDENROD1] = 'yellow'
colors[LIGHTGOLDENROD2] = 'yellow'
colors[LIGHTGOLDENROD3] = 'yellow'
colors[LIGHTGOLDENROD4] = 'brown'
colors[LIGHTGOLDENRODYELLOW] = 'yellow'
colors[LIGHTGREY] = 'gray'
colors[LIGHTPINK] = 'pink'
colors[LIGHTPINK1] = 'pink'
colors[LIGHTPINK2] = 'pink'
colors[LIGHTPINK3] = 'pink'
colors[LIGHTPINK4] = 'brown'
colors[LIGHTSALMON1] = 'red'
colors[LIGHTSALMON2] = 'red'
colors[LIGHTSALMON3] = 'red'
colors[LIGHTSALMON4] = 'brown'
colors[LIGHTSEAGREEN] = 'cyan'
colors[LIGHTSKYBLUE] = 'blue'
colors[LIGHTSKYBLUE1] = 'blue'
colors[LIGHTSKYBLUE2] = 'blue'
colors[LIGHTSKYBLUE3] = 'blue'
colors[LIGHTSKYBLUE4] = 'blue'
colors[LIGHTSLATEBLUE] = 'purple'
colors[LIGHTSLATEGRAY] = 'gray'
colors[LIGHTSTEELBLUE] = 'blue'
colors[LIGHTSTEELBLUE1] = 'blue'
colors[LIGHTSTEELBLUE2] = 'blue'
colors[LIGHTSTEELBLUE3] = 'blue'
colors[LIGHTSTEELBLUE4] = 'blue'
colors[LIGHTYELLOW1] = 'yellow'
colors[LIGHTYELLOW2] = 'yellow'
colors[LIGHTYELLOW3] = 'yellow'
colors[LIGHTYELLOW4] = 'gray'
colors[LIMEGREEN] = 'green'
colors[LINEN] = 'white'
colors[MAGENTA] = 'purple'
colors[MAGENTA2] = 'purple'
colors[MAGENTA3] = 'purple'
colors[MAGENTA4] = 'purple'
colors[MANGANESEBLUE] = 'cyan'
colors[MAROON] = 'brown'
colors[MAROON1] = 'purple'
colors[MAROON2] = 'purple'
colors[MAROON3] = 'purple'
colors[MAROON4] = 'purple'
colors[MEDIUMORCHID] = 'purple'
colors[MEDIUMORCHID1] = 'purple'
colors[MEDIUMORCHID2] = 'purple'
colors[MEDIUMORCHID3] = 'purple'
colors[MEDIUMORCHID4] = 'purple'
colors[MEDIUMPURPLE] = 'purple'
colors[MEDIUMPURPLE1] = 'purple'
colors[MEDIUMPURPLE2] = 'purple'
colors[MEDIUMPURPLE3] = 'purple'
colors[MEDIUMPURPLE4] = 'purple'
colors[MEDIUMSEAGREEN] = 'green'
colors[MEDIUMSLATEBLUE] = 'purple'
colors[MEDIUMSPRINGGREEN] = 'green'
colors[MEDIUMTURQUOISE] = 'cyan'
colors[MEDIUMVIOLETRED] = 'pink'
colors[MELON] = 'yellow'
colors[MIDNIGHTBLUE] = 'blue'
colors[MINT] = 'green'
colors[MINTCREAM] = 'white'
colors[MISTYROSE1] = 'white'
colors[MISTYROSE2] = 'white'
colors[MISTYROSE3] = 'gray'
colors[MISTYROSE4] = 'gray'
colors[MOCCASIN] = 'yellow'
colors[NAVAJOWHITE1] = 'brown'
colors[NAVAJOWHITE2] = 'brown'
colors[NAVAJOWHITE3] = 'brown'
colors[NAVAJOWHITE4] = 'brown'
colors[NAVY] = 'blue'
colors[OLDLACE] = 'white'
colors[OLIVE] = 'green'
colors[OLIVEDRAB] = 'green'
colors[OLIVEDRAB1] = 'green'
colors[OLIVEDRAB2] = 'green'
colors[OLIVEDRAB3] = 'green'
colors[OLIVEDRAB4] = 'green'
colors[ORANGE] = 'orange'
colors[ORANGE1] = 'orange'
colors[ORANGE2] = 'orange'
colors[ORANGE3] = 'orange'
colors[ORANGE4] = 'orange'
colors[ORANGERED1] = 'orange'
colors[ORANGERED2] = 'orange'
colors[ORANGERED3] = 'red'
colors[ORANGERED4] = 'red'
colors[ORCHID] = 'purple'
colors[ORCHID1] = 'purple'
colors[ORCHID2] = 'purple'
colors[ORCHID3] = 'purple'
colors[ORCHID4] = 'purple'
colors[PALEGOLDENROD] = 'yellow'
colors[PALEGREEN] = 'green'
colors[PALEGREEN1] = 'green'
colors[PALEGREEN2] = 'green'
colors[PALEGREEN3] = 'green'
colors[PALEGREEN4] = 'green'
colors[PALETURQUOISE1] = 'cyan'
colors[PALETURQUOISE2] = 'cyan'
colors[PALETURQUOISE3] = 'cyan'
colors[PALETURQUOISE4] = 'cyan'
colors[PALEVIOLETRED] = 'pink'
colors[PALEVIOLETRED1] = 'pink'
colors[PALEVIOLETRED2] = 'pink'
colors[PALEVIOLETRED3] = 'pink'
colors[PALEVIOLETRED4] = 'pink'
colors[PAPAYAWHIP] = 'yellow'
colors[PEACHPUFF1] = 'yellow'
colors[PEACHPUFF2] = 'yellow'
colors[PEACHPUFF3] = 'brown'
colors[PEACHPUFF4] = 'brown'
colors[PEACOCK] = 'blue'
colors[PINK] = 'pink'
colors[PINK1] = 'pink'
colors[PINK2] = 'pink'
colors[PINK3] = 'pink'
colors[PINK4] = 'pink'
colors[PLUM] = 'purple'
colors[PLUM1] = 'purple'
colors[PLUM2] = 'purple'
colors[PLUM3] = 'purple'
colors[PLUM4] = 'purple'
colors[POWDERBLUE] = 'blue'
colors[PURPLE] = 'purple'
colors[PURPLE1] = 'purple'
colors[PURPLE2] = 'purple'
colors[PURPLE3] = 'purple'
colors[PURPLE4] = 'purple'
colors[RASPBERRY] = 'purple'
colors[RAWSIENNA] = 'brown'
colors[RED1] = 'red'
colors[RED2] = 'red'
colors[RED3] = 'red'
colors[RED4] = 'red'
colors[ROSYBROWN] = 'brown'
colors[ROSYBROWN1] = 'brown'
colors[ROSYBROWN2] = 'brown'
colors[ROSYBROWN3] = 'brown'
colors[ROSYBROWN4] = 'brown'
colors[ROYALBLUE] = 'blue'
colors[ROYALBLUE1] = 'blue'
colors[ROYALBLUE2] = 'blue'
colors[ROYALBLUE3] = 'blue'
colors[ROYALBLUE4] = 'blue'
colors[SALMON] = 'red'
colors[SALMON1] = 'red'
colors[SALMON2] = 'red'
colors[SALMON3] = 'red'
colors[SALMON4] = 'brown'
colors[SANDYBROWN] = 'brown'
colors[SAPGREEN] = 'green'
colors[SEAGREEN1] = 'green'
colors[SEAGREEN2] = 'green'
colors[SEAGREEN3] = 'green'
colors[SEAGREEN4] = 'green'
colors[SEASHELL1] = 'white'
colors[SEASHELL2] = 'white'
colors[SEASHELL3] = 'gray'
colors[SEASHELL4] = 'gray'
colors[SEPIA] = 'brown'
colors[SGIBEET] = 'purple'
colors[SGIBRIGHTGRAY] = 'gray'
colors[SGICHARTREUSE] = 'green'
colors[SGIDARKGRAY] = 'gray'
colors[SGIGRAY12] = 'black'
colors[SGIGRAY16] = 'gray'
colors[SGIGRAY32] = 'gray'
colors[SGIGRAY36] = 'gray'
colors[SGIGRAY52] = 'gray'
colors[SGIGRAY56] = 'gray'
colors[SGIGRAY72] = 'gray'
colors[SGIGRAY76] = 'gray'
colors[SGIGRAY92] = 'gray'
colors[SGIGRAY96] = 'white'
colors[SGILIGHTBLUE] = 'blue'
colors[SGILIGHTGRAY] = 'gray'
colors[SGIOLIVEDRAB] = 'green'
colors[SGISALMON] = 'red'
colors[SGISLATEBLUE] = 'purple'
colors[SGITEAL] = 'cyan'
colors[SIENNA] = 'brown'
colors[SIENNA1] = 'orange'
colors[SIENNA2] = 'orange'
colors[SIENNA3] = 'brown'
colors[SIENNA4] = 'brown'
colors[SILVER] = 'gray'
colors[SKYBLUE] = 'blue'
colors[SKYBLUE1] = 'blue'
colors[SKYBLUE2] = 'blue'
colors[SKYBLUE3] = 'blue'
colors[SKYBLUE4] = 'blue'
colors[SLATEBLUE] = 'purple'
colors[SLATEBLUE1] = 'purple'
colors[SLATEBLUE2] = 'purple'
colors[SLATEBLUE3] = 'purple'
colors[SLATEBLUE4] = 'purple'
colors[SLATEGRAY] = 'gray'
colors[SLATEGRAY1] = 'blue'
colors[SLATEGRAY2] = 'blue'
colors[SLATEGRAY3] = 'blue'
colors[SLATEGRAY4] = 'gray'
colors[SNOW1] = 'white'
colors[SNOW2] = 'white'
colors[SNOW3] = 'gray'
colors[SNOW4] = 'gray'
colors[SPRINGGREEN] = 'green'
colors[SPRINGGREEN1] = 'green'
colors[SPRINGGREEN2] = 'green'
colors[SPRINGGREEN3] = 'green'
colors[STEELBLUE] = 'blue'
colors[STEELBLUE1] = 'blue'
colors[STEELBLUE2] = 'blue'
colors[STEELBLUE3] = 'blue'
colors[STEELBLUE4] = 'blue'
colors[TAN] = 'brown'
colors[TAN1] = 'brown'
colors[TAN2] = 'brown'
colors[TAN3] = 'brown'
colors[TAN4] = 'brown'
colors[TEAL] = 'cyan'
colors[THISTLE] = 'purple'
colors[THISTLE1] = 'purple'
colors[THISTLE2] = 'purple'
colors[THISTLE3] = 'purple'
colors[THISTLE4] = 'purple'
colors[TOMATO1] = 'orange'
colors[TOMATO2] = 'orange'
colors[TOMATO3] = 'red'
colors[TOMATO4] = 'red'
colors[TURQUOISE] = 'cyan'
colors[TURQUOISE1] = 'cyan'
colors[TURQUOISE2] = 'cyan'
colors[TURQUOISE3] = 'cyan'
colors[TURQUOISE4] = 'cyan'
colors[TURQUOISEBLUE] = 'cyan'
colors[VIOLET] = 'purple'
colors[VIOLETRED] = 'pink'
colors[VIOLETRED1] = 'pink'
colors[VIOLETRED2] = 'pink'
colors[VIOLETRED3] = 'pink'
colors[VIOLETRED4] = 'pink'
colors[WARMGREY] = 'gray'
colors[WHEAT] = 'brown'
colors[WHEAT1] = 'brown'
colors[WHEAT2] = 'brown'
colors[WHEAT3] = 'brown'
colors[WHEAT4] = 'brown'
colors[WHITE] = 'white'
colors[WHITESMOKE] = 'white'
colors[YELLOW1] = 'yellow'
colors[YELLOW2] = 'yellow'
colors[YELLOW3] = 'yellow'
colors[YELLOW4] = 'yellow'

colors = OrderedDict(sorted(colors.items(), key=lambda t: t[0]))

requested_colour = (217, 190, 138)

closest_color(requested_colour)
