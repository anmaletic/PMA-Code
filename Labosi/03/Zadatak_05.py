
class Boja(object):
    def __init__(self, p_ime:str, p_rgb:list, p_hex:str) -> None:
        self.ime = p_ime
        self.rgb = p_rgb
        self.hex = p_hex


def GetBojaFromHex(p_boje:list, p_hex:str):    
    for _boja in p_boje:
        _boja:Boja
        if _boja.hex == p_hex:
            print(_boja.ime)


def GetBojaFromRGB(p_boje:list, p_rgb:list):    
    for _boja in p_boje:
        _boja:Boja
        if _boja.rgb == p_rgb:
            print(_boja.ime)


def FillBojaData(p_boje:list):
    p_boje.append(Boja("Black",     [0, 0, 0],          "#000000"))
    p_boje.append(Boja("White",     [255, 255, 255],    "#FFFFFF"))
    p_boje.append(Boja("Red",       [255, 0, 0],        "#FF0000"))
    p_boje.append(Boja("Lime",      [0, 255, 0],        "#00FF00"))
    p_boje.append(Boja("Blue",      [0, 0, 255],        "#0000FF"))
    p_boje.append(Boja("Yellow",    [255, 255, 0],      "#FFFF00"))
    p_boje.append(Boja("Cyan",      [0, 255, 255],      "#00FFFF"))
    p_boje.append(Boja("Magenta",   [255, 0, 255],      "#FF00FF"))
    p_boje.append(Boja("Silver",    [192, 192, 192],    "#C0C0C0"))
    p_boje.append(Boja("Gray",      [128, 128, 128],    "#808080"))
    p_boje.append(Boja("Maroon",    [128, 0, 0],        "#800000"))
    p_boje.append(Boja("Olive",     [128, 128, 0],      "#808000"))
    p_boje.append(Boja("Green",     [0, 128, 0],        "#008000"))
    p_boje.append(Boja("Purple",    [128, 0, 128],      "#800080"))
    p_boje.append(Boja("Teal",      [0, 128, 128],      "#008080"))
    p_boje.append(Boja("Navy",      [0, 0, 128],        "#000080"))


def main():
    listaBoja = []
    FillBojaData(listaBoja)

    GetBojaFromHex(listaBoja, "#C0C0C0")
    GetBojaFromRGB(listaBoja, [255, 255, 0])


main()
    



