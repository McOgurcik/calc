try:
    import PySimpleGUI as sg
except:
    print('Пожалуйста установите модуль PySimpleGUI')
import images
def author_layout():
    author_layout = [[sg.T('ку')],[sg.Button(image_data=images.mccree)]]
    return author_layout
def tab2_layout_1():
    tab2_layout_1 = [[sg.Button('Площадь Прямоугольного треугольника S=a*b*0.5'),sg.Button('Площадь Прямоугольника S=ab')],[sg.Button('Площадь Круга S=π*r^2'),sg.Button('Площадь параллелограмма через стороны и угол S=ab*Sinα')],
    [sg.Button('Площадь треугольника по формуле Герона\n S=(p(p-a)(p-b)(p-c))^0.5',size=(35,2)),sg.Button('Площадь трапеции через основания и высоту S=(a+b)/2*h')],[sg.Button('Площадь ромба по стороне и углу a^2*Sinα'),sg.Button('Формула площади правильного многоугольника')]]
    return  tab2_layout_1
def tab2_layout_2():
    tab2_layout_2 = [[sg.Text('Эти формулы принимают только градусные значения!')],[sg.Button('Sin(α+β)'),sg.Button('Sin(α-β)'),sg.Button('sin2α'),sg.Button('Sinα + Sinβ'),sg.Button('Sinα - Sinβ')],[sg.Button('Cos(α+β)'),sg.Button('Cos(α-β)'),sg.Button('cos2α'),sg.Button('Cosα + Cosβ'),sg.Button('Cosα - Cosβ')],[sg.Button('tg(α+β)'),sg.Button('tg(α-β)'),sg.Button('tg2α'),sg.Button('Перевод из градусов в радианы'),sg.Button('Перевод из радиан в градусы')]]
    return tab2_layout_2
def tab2_layout_3():
    tab2_layout_3 = [[sg.Button('Площадь поверхности Куба 6a^2'),sg.Button('Длина диагонали куба')],[sg.Button('Диагональ параллелепипеда  d=(a**2+b**2+c**2)**0.5'),sg.Button('Площадь поверхности параллелепипеда')],[sg.Button('Объём цилиндра πR^2h'),sg.Button('Площадь поверхности цилиндра')],[sg.Button('Объём конуса'),sg.Button('Площадь поверхности конуса')],[sg.Button('Объём шара'),sg.Button('Площадь поверхности шара')]]
    return tab2_layout_3
def kv_ur_layout():
    kv_ur_layout = [[sg.Button('Квадратное уравнение по дискриминанту')], [sg.Button('Квадратное уравнение по теореме Виета')]]
    return kv_ur_layout
def s_umn_layout():
    s_umn_layout =  [[sg.Button('Квадрат суммы (a+b)^2'), sg.Button('Квадрат разности (a-b)^2')],
               [sg.Button('Куб суммы (a+b)^3'), sg.Button('Куб разности (a+b)^3')],
               [sg.Button('Разность кубов a^2-b^2')]

               ]
    return s_umn_layout
def pr_rash_layout():
    pr_rash_layout = [[sg.Text('Тригонометрические формулы принимают только градусные значения!')],[sg.Button('log'),sg.Button('arccos'),sg.Button('arcsin'),sg.Button('arctan')],[sg.Button('cos'),sg.Button('sin'),sg.Button('tan')]
    ]
    return pr_rash_layout
def tab1_layout():
    tab1_layout = [

              [sg.TabGroup([[sg.Tab('Формулы сокращённого умножения', s_umn_layout()), sg.Tab('Квадратные уравнения', kv_ur_layout()), sg.Tab('Расчёты прямых значений', pr_rash_layout())]])] ]
    return tab1_layout
def tab2_layout():
    tab2_layout = [

              [sg.TabGroup([[sg.Tab('Площади', tab2_layout_1()), sg.Tab('Тригонометрия', tab2_layout_2()),sg.Tab('Стереометрия', tab2_layout_3())]])] ]
    return tab2_layout
def summakvadrata_layout():
    summakvadrata_layout = [
            [sg.Text('(a+b)^2')],
            [sg.Text('a'), sg.InputText(0)],
            [sg.Text('b'), sg.InputText(0)],
            [sg.Button('Рассчитать'), sg.Button('Cancel')] ]
    return summakvadrata_layout
def raznostkvadrata_layout():
    raznostkvadrata_layout = [
            [sg.Text('(a-b)^2')],
            [sg.Text('a'), sg.InputText(0)],
            [sg.Text('b'), sg.InputText(0)],
            [sg.Button('Рассчитать'), sg.Button('Cancel')] ]
    return raznostkvadrata_layout
def summakuba_layout():
    summakuba_layout = [
            [sg.Text('(a+b)^3')],
            [sg.Text('a'), sg.InputText(0)],
            [sg.Text('b'), sg.InputText(0)],
            [sg.Button('Рассчитать'), sg.Button('Cancel')] ]
    return summakuba_layout
def raznostkuba_layout():
    raznostkuba_layout = [
            [sg.Text('(a-b)^3')],
            [sg.Text('a'), sg.InputText(0)],
            [sg.Text('b'), sg.InputText(0)],
            [sg.Button('Рассчитать'), sg.Button('Cancel')] ]
    return raznostkuba_layout
def raznostkubov_layout():
    raznostkubov_layout = [
           [sg.Text('a^2-b^2')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Text('b'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return raznostkubov_layout
def ploshadtriugolnika_layout():
    ploshadtriugolnika_layout = [
           [sg.Text('S=a*b*0.5')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Text('b'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return ploshadtriugolnika_layout
def log_layout():
    log_layout = [
            [sg.Text('log')],
            [sg.Text('x'), sg.InputText(0)],
            [sg.Text('Основание логарифма'), sg.InputText(0)],
            [sg.Button('Рассчитать'), sg.Button('Cancel')] ]
    return log_layout
# layout_otvet = [[sg.InputText(a)]]
def inf_layout():
    inf_layout = [[sg.Button('Мощность алфавита N = 2^i'),sg.Button('Кол-во информации I = K * i')],[sg.Button('Кол-во разных сообщений Q = N^L'),sg.Button('Формула Хартли: I = log2 N')],[sg.Button('Перевод любого числа любой системы счисления в любую другую')]]
    return inf_layout
def fuz_layout():
    fuz_layout = []
    return fuz_layout
def kv_ur_dis_layout():
    kv_ur_dis_layout = [
                    [sg.Text('Аргументы Квадратного уравнения')],
                    [sg.Text('a'), sg.InputText(0)],
                    [sg.Text('b'), sg.InputText(0)],
                    [sg.Text('c'), sg.InputText(0)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return kv_ur_dis_layout
def kv_ur_vi_layout():
    kv_ur_vi_layout = [
                    [sg.Text('Аргументы Квадратного уравнения (ТОЛЬКО ЦЕЛОЧИСЛЕННЫЕ!!! )')],
                    [sg.Text('a'), sg.InputText(0)],
                    [sg.Text('b'), sg.InputText(0)],
                    [sg.Text('c'), sg.InputText(0)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return kv_ur_vi_layout
def diag_paralel_layout():
    diag_paralel_layout =  [
                    [sg.Text('Диагональ параллелепипеда  d=(a**2+b**2+c**2)**0.5')],
                    [sg.Text('a'), sg.InputText(0)],
                    [sg.Text('b'), sg.InputText(0)],
                    [sg.Text('c'), sg.InputText(0)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return diag_paralel_layout
def Sin_sum_layout():
    Sin_sum_layout = [
           [sg.Text('Sin(α+β)')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Text('b'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return Sin_sum_layout
def arccos_layout():
    arccos_layout = [
           [sg.Text('arccos')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return arccos_layout
def arcsin_layout():
    arcsin_layout = [
           [sg.Text('arcsin')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return arcsin_layout
def arctan_layout():
    arctan_layout = [
           [sg.Text('arctan')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return arctan_layout
def sin_layout():
    sin_layout = [
           [sg.Text('sin')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return sin_layout
def cos_layout():
    cos_layout = [
           [sg.Text('cos')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return cos_layout
def tan_layout():
    tan_layout = [
           [sg.Text('tan')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return tan_layout
def Sin_razn_layout():
    Sin_razn_layout = [
           [sg.Text('Sin(α-β)')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Text('b'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return Sin_razn_layout
def Cos_sum_layout():
    Cos_sum_layout = [
           [sg.Text('Cos(α+β)')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Text('b'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return Cos_sum_layout
def Cos_razn_layout():
    Cos_razn_layout = [
           [sg.Text('Cos(α-β)')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Text('b'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return Cos_razn_layout
def sin2a_layout():
    sin2a_layout = [
           [sg.Text('Sin2α')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return sin2a_layout
def cos2a_layout():
    cos2a_layout = [
           [sg.Text('Cos2α')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return cos2a_layout
def tg2a_layout():
    tg2a_layout = [
           [sg.Text('tg2α')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return tg2a_layout


def menu_def():
    menu_def_ = [['File', ['Open', 'Save', 'Exit',]],
                 ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
                 ['Help', 'Автор...']]
    return menu_def_
def right_click_menu_layout():
    right_click_menu =  [[], ['Exit']]
    return right_click_menu
def tg_sum_layout():
    tg_sum_layout = [
           [sg.Text('tg(α+β)')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Text('b'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return tg_sum_layout
def tg_razn_layout():
    tg_razn_layout = [
           [sg.Text('tg(α-β)')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Text('b'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return tg_razn_layout
def sins_sum_layout():
    sins_sum_layout = [
           [sg.Text('Sinα + Sinβ')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Text('b'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return sins_sum_layout
def sins_razn_layout():
    sins_razn_layout = [
           [sg.Text('Sinα - Sinβ')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Text('b'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return sins_razn_layout
def coss_sum_layout():
    coss_sum_layout = [
           [sg.Text('Cosα + Cosβ')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Text('b'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return coss_sum_layout
def coss_razn_layout():
    coss_razn_layout = [
           [sg.Text('Cosα - Cosβ')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Text('b'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return coss_razn_layout
def plodhadkruga_layout():
    plodhadkruga_layout = [
           [sg.Text('Площадь Круга S=π*r^2')],
           [sg.Text('r-радиус'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return plodhadkruga_layout
def plodhadgerron_layout():
    plodhadgerron_layout =  [
                    [sg.Text('Площадь треугольника по формуле Герона\n S=(p(p-a)(p-b)(p-c))^0.5')],
                    [sg.Text('a'), sg.InputText(0)],
                    [sg.Text('b'), sg.InputText(0)],
                    [sg.Text('c'), sg.InputText(0)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return plodhadgerron_layout
def plodhadprugol_layout():
    plodhadprugol_layout = [
           [sg.Text('Площадь Прямоугольника S=ab')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Text('b'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return plodhadprugol_layout
def plodhadparugol_layout():
    plodhadparugol_layout =  [
                    [sg.Text('Площадь параллелограмма через стороны и угол S=ab*Sinα')],
                    [sg.Text('a'), sg.InputText(0)],
                    [sg.Text('b'), sg.InputText(0)],
                    [sg.Text('Уголα'), sg.InputText(0)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return plodhadparugol_layout
def plodhadtrap_layout():
    plodhadtrap_layout =  [
                    [sg.Text('Площадь трапеции через основания и высоту S=(a+b)/2*h')],
                    [sg.Text('a'), sg.InputText(0)],
                    [sg.Text('b'), sg.InputText(0)],
                    [sg.Text('h'), sg.InputText(0)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return plodhadtrap_layout
def plodhadromb_layout():
    plodhadromb_layout = [
           [sg.Text('Площадь ромба по стороне и углу a^2*Sinα')],
           [sg.Text('a'), sg.InputText(0)],
           [sg.Text('Уголα'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return plodhadromb_layout
def plodhadmnugol_layout():
    plodhadmnugol_layout = [
           [sg.Text('Формула площади правильного многоугольника')],
           [sg.Text('Сторона a'), sg.InputText(0)],
           [sg.Text('Кол-во сторон'), sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return plodhadmnugol_layout
def radians_layout():
    radians_layout = [
           [sg.Text('Перевод из градусов в радианы')],
           [sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return radians_layout
def degrees_layout():
    degrees_layout = [
           [sg.Text('Перевод из радиан в градусы')],
           [sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return degrees_layout
def plpovkuba_layout():
    plpovkuba_layout = [
           [sg.Text('Площадь поверхности Куба 6a^2')],
           [sg.Text('Ребро a'),sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return plpovkuba_layout
def diagkuba_layout():
    diagkuba_layout = [
           [sg.Text('Длина диагонали куба')],
           [sg.Text('Ребро a'),sg.InputText(0)],
           [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return diagkuba_layout
def plpovpar_layout():
    plpovpar_layout =  [
                    [sg.Text('Площадь поверхности параллелепипеда')],
                    [sg.Text('a'), sg.InputText(0)],
                    [sg.Text('b'), sg.InputText(0)],
                    [sg.Text('c'), sg.InputText(0)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return plpovpar_layout
def obcil_layout():
    obcil_layout =  [
                    [sg.Text('Объём цилиндра πR^2h')],
                    [sg.Text('R-радиус основания'), sg.InputText(0)],
                    [sg.Text('h-высота'), sg.InputText(0)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return obcil_layout
def plpovcil_layout():
    plpovcil_layout =  [
                    [sg.Text('Площадь поверхности цилиндра')],
                    [sg.Text('R-радиус основания'), sg.InputText(0)],
                    [sg.Text('h-высота'), sg.InputText(0)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return plpovcil_layout
def obkon_layout():
    obkon_layout =  [
                    [sg.Text('Объём конуса')],
                    [sg.Text('R-радиус основания'), sg.InputText(0)],
                    [sg.Text('h-высота'), sg.InputText(0)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return obkon_layout
def plpovkon_layout():
    plpovkon_layout =  [
                    [sg.Text('Площадь поверхности конуса')],
                    [sg.Text('R-радиус основания'), sg.InputText(0)],
                    [sg.Text('h-высота'), sg.InputText(0)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return plpovkon_layout
def obshar_layout():
    obshar_layout =  [
                    [sg.Text('Объём шара')],
                    [sg.Text('R'), sg.InputText(0)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return obshar_layout
def plpovshar_layout():
    plpovshar_layout =  [
                    [sg.Text('Площадь поверхности шара')],
                    [sg.Text('R'), sg.InputText(0)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return plpovshar_layout
def alfabet_layout():
    alfabet_layout =  [
                    [sg.Text('Мощность алфавита N = 2^i')],
                    [sg.Text('i'), sg.InputText(0)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return alfabet_layout
def kolinfo_layout():
    kolinfo_layout =  [
                    [sg.Text('Кол-во информации I = K * i')],
                    [sg.Text('K - число символов в сообщении'), sg.InputText(0)],
                    [sg.Text('i - информационный вес символа'), sg.InputText(0)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return kolinfo_layout
def kolsoob_layout():
    kolsoob_layout =  [
                    [sg.Text('Кол-во разных сообщений Q = N^L')],
                    [sg.Text('N - количество символов'), sg.InputText(0)],
                    [sg.Text('L - длина сообщения'), sg.InputText(0)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return kolsoob_layout
def hartl_layout():
    hartl_layout =  [
                    [sg.Text('Формула Хартли: I = log2 N')],
                    [sg.Text('N'), sg.InputText(0)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return hartl_layout
def convert_base_layout():
    convert_base_layout =  [
                    [sg.Text('Перевод любого числа любой системы счисления в любую другую')],
                    [sg.Text('Число'), sg.InputText(0)],
                    [sg.Text('Исходная система счисления'), sg.InputText(10)],
                    [sg.Text('Конечная система счисления'), sg.InputText(10)],
                    [sg.Button('Рассчитать'), sg.Button('Cancel')]]
    return convert_base_layout
# ВСТАВЛЯТЬ СЮДА ВСЕ СПИКИ ПО МЕРЕ ОБНОВЛЕНИЯ!!!!!!!!!!!!!!!!!!!!
#
#
#
#
def layout_all():
    layout_all = [tab2_layout_1(), tab2_layout_2(), kv_ur_layout(), s_umn_layout(), tab1_layout(), tab2_layout(), summakvadrata_layout(), raznostkvadrata_layout(), summakuba_layout(), raznostkuba_layout(), raznostkubov_layout (), ploshadtriugolnika_layout (), inf_layout(), fuz_layout(),kv_ur_dis_layout(), menu_def()]
    return layout_all
def layout123():
    layout123 = [[sg.Button('Print')],
             [sg.Button('Exit')]  ]
    return layout123

#layout = [ [sg.TabGroup([[sg.Tab('Алгебра', tab1_layout()), sg.Tab('Геометрия', tab2_layout()) , sg.Tab('Информатика', inf_layout()) , sg.Tab('Физика', fuz_layout())]])],
#
#              [sg.Button('Exit'), sg.Button('debug')],
#
#             [[sg.Menu(menu_def)]]]
# Create the Window
if __name__ == '__main__':
    print('Пожалуйста запустите исполнительный файл')
