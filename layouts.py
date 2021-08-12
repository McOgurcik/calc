import PySimpleGUI as sg #1111111111
import images
def author_layout():
    author_layout = [[sg.T('ку')],[sg.Button(image_data=images.mccree)]]
    return author_layout
def tab2_layout_1():
    tab2_layout_1 = [[sg.Button('Площадь Прямоугольного треугольника S=a*b*0.5')]]
    return  tab2_layout_1
def tab2_layout_2():
    tab2_layout_2 = [[sg.Button('Sin(α+β)'),sg.Button('Sin(α-β)'),sg.Button('sin2α'),sg.Button('Sinα + Sinβ'),sg.Button('Sinα - Sinβ')],[sg.Button('Cos(α+β)'),sg.Button('Cos(α-β)'),sg.Button('cos2α'),sg.Button('Cosα + Cosβ'),sg.Button('Cosα - Cosβ')],[sg.Button('tg(α+β)'),sg.Button('tg(α-β)'),sg.Button('tg2α')]]
    return tab2_layout_2
def tab2_layout_3():
    tab2_layout_3 = [[sg.Button('Диагональ параллелепипеда  d=(a**2+b**2+c**2)**0.5')]]
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
    pr_rash_layout = [[sg.Button('log'),sg.Button('arccos'),sg.Button('arcsin'),sg.Button('arctan')],[sg.Button('cos'),sg.Button('sin'),sg.Button('tan')]
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
    inf_layout = []
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


# ВСТАВЛЯТЬ СЮДА ВСЕ СПИКИ ПО МЕРЕ ОБНОВЛЕНИЯ!!!!!!!!!!!!!!!!!!!!
#
#
#
#
def layout_all():
    layout_all = [tab2_layout_1(), tab2_layout_2(), kv_ur_layout(), s_umn_layout(), tab1_layout(), tab2_layout(), summakvadrata_layout(), raznostkvadrata_layout(), summakuba_layout(), raznostkuba_layout(), raznostkubov_layout (), ploshadtriugolnika_layout (), inf_layout(), fuz_layout(),kv_ur_dis_layout(), layout(), menu_def()]
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
