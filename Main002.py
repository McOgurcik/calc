import PySimpleGUI as sg
import os
import sys
# import imp
#import supervisor
import math
import winsound
import images
# import webbrowser ля интеграции веб ссылок  [sg.Text('www.PySimpleGUI.org', font='default 12 underline', text_color='blue', enable_events=True, key='-LINK-')],
#elif event == '-LINK-':
        # if the text was clicked, open a browser using the text as the address
       # webbrowser.open(window['-LINK-'].DisplayText)   # accessing DisplayText isn't something you'll see often

# тест на плагин атома вроде говно, а вроде и робит
x = 0

a = 1
main_exit = None
cursors = ('X_cursor', 'no', 'arrow','based_arrow_down','based_arrow_up','boat','bogosity','bottom_left_corner','bottom_right_corner','bottom_side','bottom_tee','box_spiral','center_ptr','circle','clock','coffee_mug','cross','cross_reverse','crosshair','diamond_cross','dot','dotbox','double_arrow','draft_large','draft_small','draped_box','exchange','fleur','gobbler','gumby','hand1','hand2','heart','icon','iron_cross','left_ptr','left_side','left_tee','leftbutton','ll_angle','lr_angle','man','middlebutton','mouse','no','pencil','pirate','plus','question_arrow','right_ptr','right_side','right_tee','rightbutton','rtl_logo','sailboat','sb_down_arrow','sb_h_double_arrow','sb_left_arrow','sb_right_arrow','sb_up_arrow','sb_v_double_arrow','shuttle','sizing','spider','spraycan','star','target','tcross','top_left_arrow','top_left_corner','top_right_corner','top_side','top_tee','trek','ul_angle','umbrella','ur_angle','watch','xterm','arrow','center_ptr','crosshair','fleur','ibeam','icon','sb_h_double_arrow','sb_v_double_arrow','watch','xterm','no','starting','size','size_ne_sw','size_ns','size_nw_se','size_we','uparrow','wait','arrow','cross','crosshair','ibeam','plus','watch','xterm')

event, values = 0, 0

print = sg.Print
# sg.theme('Black')
# event, values = sg.Window('Где файл сука?', [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).read(close=True)
sg.theme('DefaultNoMoreNagging')   # Add a touch of color
# All the stuff inside your window.


def tab2_layout_1():
    tab2_layout_1 = [[sg.Button('Площадь Прямоугольного треугольника S=a*b*0.5')]]
    return  tab2_layout_1
def tab2_layout_2():
    tab2_layout_2 = [[sg.Button('Sin(α+β)'),sg.Button('Sin(α-β)'),sg.Button('sin2α')],[sg.Button('Cos(α+β)'),sg.Button('Cos(α-β)'),sg.Button('cos2α')],[sg.Button('tg(α+β)'),sg.Button('tg(α-β)'),sg.Button('tg2α')]]
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
def otvet_layout():
    otvet_layout = [[sg.Multiline('  '+a+'  ')],[sg.Button('Exit')]]
    return otvet_layout
def otvet(otvet):
    global a
    a = otvet
    a = str(a)
    window_o = sg.Window('otvet',otvet_layout(),icon='name.ico')
    while True:
        event, values = window_o.read()
        # print(event, values)
        if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

           window_o.close()
           break


def debug():
    while True:
       window = sg.Window('debug123', layout123(),icon='name.ico')
       event, values = window.read()
       print(event, values)
       if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
           return('Отменено')
           window.close()
           break
       if event == 'Print':
           print(layout_all())
           window.close()
           break


def defsummakvadrata(a,b):
    x = float(a)**2 + 2 * float(a)*float(b) + float(b)**2
    return x
def summakvadrata():
   while True:
     window = sg.Window('Квадрат суммы (a+b)^2', summakvadrata_layout())
     event, values = window.read()
     print(event, values)
     if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
         # os.execl(sys.executable, sys.executable, *sys.argv)

         window.close()
         return('Отменено')
         break


     if event == 'Рассчитать':

         if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

             # os.execl(sys.executable, sys.executable, *sys.argv)
             window.close()
             return('Отменено')

             break




         a = values[0]
         b = values[1]
         try:
                 window.close()
                 return (defsummakvadrata(a,b))
         except:
             window.close()
             return('Ошибка')
         window.close()
         break

def defraznostkvadrata(a,b):
    x = float(a)**2 - 2 * float(a)*float(b) + float(b)**2
    return x
def raznostkvadrata():
    while True:
      window = sg.Window('Квадрат разности (a-b)^2', raznostkvadrata_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')

          break


      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')

              break




          a = values[0]
          b = values[1]
          try:
              window.close()
              return (defraznostkvadrata(a,b))
          except:
             window.close()
             return('Ошибка')


def defsummakuba(a,b):
    x = float(a)**3 + 3*(float(a)**2)*float(b) + 3*float(a)*(float(b)**2) + float(b)**3
    return x
def summakuba():
    while True:
      window = sg.Window('Сумма куба (a-b)^3', summakuba_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')
          break


      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')
              break




          a = values[0]
          b = values[1]
          try:
              window.close()
              return (defsummakuba(a,b))
          except:
             window.close()
             return('Ошибка')
          window.close()
          break


def defraznostkuba(a,b):
    x = float(a)**3 - 3*(float(a)**2)*float(b) + 3*float(a)*(float(b)**2) - float(b)**3
    return x

def raznostkuba():
    while True:
      window = sg.Window('Разность куба (a-b)^3', raznostkuba_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')
          break



      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')
              break




          a = values[0]
          b = values[1]
          try:
              window.close()
              return defraznostkuba(a,b)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break

def defraznostkubov(a,b):
    x = (float(a)-float(b))*(float(a)+float(b))
    return(x)
def raznostkubov():
    while True:
      window = sg.Window('Разность кубов a^2-b^2', raznostkubov_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')
          break



      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')
              break




          a = values[0]
          b = values[1]
          try:
              window.close()
              return defraznostkubov(a,b)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break



def ploshadtriugolnika():
    while True:
      window = sg.Window('Площадь Прямоугольного треугольника S=a*b*0.5', ploshadtriugolnika_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')
          break


      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')
              break




          a = values[0]
          b = values[1]
          try:
              window.close()
              return defploshadtriugolnika(a,b)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break

def defploshadtriugolnika(a,b):
    x = (float(a)*float(b)*0.5)
    return(x)
def def_kv_ur_dis(a,b,c):
    d = float(b)**2 - (4*float(a)*float(c))
    if d > 0:
        y = (-(float(b))+(float(d)**0.5))/(2*float(a))
        z = (-(float(b))-(float(d)**0.5))/(2*float(a))
        y = str(y)
        z = str(z)
        x = 'Первый корень '+z+'Второй корень '+y
        return(x)
    if d == 0:
        x = (-(float(b)))/(2*float(a))
        return(x)
    if d < 0:
        x = 'Не имеет корней'
        return(x)
def kv_ur_dis():
    while True:
      window = sg.Window('Квадратное уравнение по дискриминанту', kv_ur_dis_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')

          break



      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')
              break




          a = values[0]
          b = values[1]
          c = values[2]
          try:
              window.close()
              return def_kv_ur_dis(a,b,c)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break

def drange(x, y, jump) -> float:
# Генератор чисел float
    import decimal
    while x < y:
        yield float(x)
        x += decimal.Decimal(jump)

def def_kv_ur_vi(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)
    x1 = x2 = 0
    x = 'Корень не существует'
    points = [i for i in range(-1000, 1000)]
    for i in points:
        x1 = i
        for j in points:
            x2 = j
            if x1 + x2 == -b / a and x1 * x2 == c / a:
                x = 'x1='+str(x1)+'  '+'x2='+str(x2)
                return(x)
    return(x)



def kv_ur_vi():
    while True:
      window = sg.Window('Квадратное уравнение по теореме Виета', kv_ur_vi_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')

          break



      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')
              break




          a = values[0]
          b = values[1]
          c = values[2]
          try:
              window.close()
              return def_kv_ur_vi(a,b,c)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break

def def_diag_paralel(a,b,c):
    d=(float(a)**2+float(b)**2+float(c)**2)**0.5
    return(d)
def diag_paralel():
    while True:
      window = sg.Window('Диагональ параллелепипеда  d=(a**2+b**2+c**2)**0.5', diag_paralel_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')

          break



      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')

              break




          a = values[0]
          b = values[1]
          c = values[2]
          try:
              window.close()
              return def_diag_paralel(a,b,c)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break

def def_log(a,b):
     try:
         return math.log(float(a),float(b))
     except:
         return('Ошибка')

def log():
    while True:
      window = sg.Window('log', log_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')




      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')




          a = values[0]
          b = values[1]

          try:
              window.close()
              return def_log(a,b)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break
def def_Sin_sum(a,b):
    try:
        x = (math.sin(float(a))*math.cos(float(b)))+((math.cos(float(a))*math.sin(float(b))))
        return (x)
    except:
         return('Ошибка')

def Sin_sum():
     while True:
      window = sg.Window('Sin(α+β)', Sin_sum_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')




      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')




          a = values[0]
          b = values[1]

          try:
              window.close()
              return def_Sin_sum(a,b)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break
def def_arccos(a):
    try:
        return (math.acos(float(a)))
    except:
         return('Ошибка')

def arccos():
    while True:
      window = sg.Window('arccos', arccos_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')




      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')




          a = values[0]

          try:
              window.close()
              return def_arccos(a)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break
def def_arcsin(a):
    try:
        return (math.asin(float(a)))
    except:
         return('Ошибка')
def arcsin():
    while True:
      window = sg.Window('arcsin', arcsin_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')




      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')




          a = values[0]

          try:
              window.close()
              return def_arcsin(a)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break
def def_arctan(a):
    try:
        return (math.atan(float(a)))
    except:
         return('Ошибка')
def arctan():
    while True:
      window = sg.Window('arctan', arctan_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')




      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')




          a = values[0]

          try:
              window.close()
              return def_arctan(a)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break

def def_sin(a):
    try:
        return (math.sin(float(a)))
    except:
         return('Ошибка')
def sin():
    while True:
      window = sg.Window('sin', sin_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')




      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')




          a = values[0]

          try:
              window.close()
              return def_sin(a)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break

def def_cos(a):
    try:
        return (math.cos(float(a)))
    except:
         return('Ошибка')
def cos():
    while True:
      window = sg.Window('cos', cos_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')




      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')




          a = values[0]

          try:
              window.close()
              return def_cos(a)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break

def def_tan(a):
    try:
        return (math.tan(float(a)))
    except:
         return('Ошибка')
def tan():
    while True:
      window = sg.Window('tan', tan_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')




      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')




          a = values[0]

          try:
              window.close()
              return def_tan(a)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break



def def_Sin_razn(a,b):
    try:
        x = (math.sin(float(a))*math.cos(float(b)))-((math.cos(float(a))*math.sin(float(b))))
        return (x)
    except:
         return('Ошибка')

def Sin_razn():
     while True:
      window = sg.Window('Sin(α-β)', Sin_razn_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')




      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')




          a = values[0]
          b = values[1]

          try:
              window.close()
              return def_Sin_razn(a,b)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break



def def_Cos_sum(a,b):
    try:
        x = (math.cos(float(a))*math.cos(float(b)))-(math.cos(float(a))*math.cos(float(b)))
        return (x)
    except:
         return('Ошибка')

def Cos_sum():
     while True:
      window = sg.Window('Cos(α+β)', Cos_sum_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')




      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')




          a = values[0]
          b = values[1]

          try:
              window.close()
              return def_Cos_sum(a,b)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break

def def_Cos_razn(a,b):
    try:
        x = (math.cos(float(a))*math.cos(float(b)))+(math.cos(float(a))*math.cos(float(b)))
        return (x)
    except:
         return('Ошибка')

def Cos_razn():
     while True:
      window = sg.Window('Cos(α-β)', Cos_razn_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')




      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')




          a = values[0]
          b = values[1]

          try:
              window.close()
              return def_Cos_razn(a,b)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break

def def_tg_sum(a,b):
    x = (math.tan(float(a))+math.tan(float(b)))/(1-(math.tan(float(a))*math.tan(float(b))))
    return x
def tg_sum():
     while True:
      window = sg.Window('tg(α+β)', tg_sum_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')




      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')




          a = values[0]
          b = values[1]

          try:
              window.close()
              return def_tg_sum(a,b)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break

def def_tg_razn(a,b):
    x = (math.tan(float(a))-math.tan(float(b)))/(1+(math.tan(float(a))*math.tan(float(b))))
    return x

def tg_razn():
     while True:
      window = sg.Window('tg(α-β)', tg_razn_layout())
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          return('Отменено')




      if event == 'Рассчитать':

          if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

              # os.execl(sys.executable, sys.executable, *sys.argv)
              window.close()
              return('Отменено')




          a = values[0]
          b = values[1]

          try:
              window.close()
              return def_tg_razn(a,b)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break
def def_sin2a(a):
    x = (2*math.sin(float(a)))*math.cos(float(a))
    return x
def sin2a():
    while True:
     window = sg.Window('sin2α', sin2a_layout())
     event, values = window.read()
     print(event, values)
     if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
         # os.execl(sys.executable, sys.executable, *sys.argv)
         window.close()
         return('Отменено')




     if event == 'Рассчитать':

         if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

             # os.execl(sys.executable, sys.executable, *sys.argv)
             window.close()
             return('Отменено')




         a = values[0]

         a = float(a)

         try:
             window.close()
             return def_sin2a(a)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_cos2a(a):
    x = (math.cos(a)**2)-(math.sin(a)**2)
    return x
def cos2a():
    while True:
     window = sg.Window('cos2α', cos2a_layout())
     event, values = window.read()
     print(event, values)
     if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
         # os.execl(sys.executable, sys.executable, *sys.argv)
         window.close()
         return('Отменено')




     if event == 'Рассчитать':

         if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

             # os.execl(sys.executable, sys.executable, *sys.argv)
             window.close()
             return('Отменено')




         a = values[0]

         a = float(a)

         try:
             window.close()
             return def_cos2a(a)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_tg2a(a):
    x = (2*math.tan(a))/(1-(math.tan(a)**2))
    return x
def tg2a():
    while True:
     window = sg.Window('tg2α', tg2a_layout())
     event, values = window.read()
     print(event, values)
     if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
         # os.execl(sys.executable, sys.executable, *sys.argv)
         window.close()
         return('Отменено')




     if event == 'Рассчитать':

         if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':

             # os.execl(sys.executable, sys.executable, *sys.argv)
             window.close()
             return('Отменено')




         a = values[0]

         a = float(a)

         try:
             window.close()
             return def_tg2a(a)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break

def author_layout():
    author_layout = [[sg.T('ку')],[sg.Button(image_data=images.mccree)]]
    return author_layout
def author():
     window = sg.Window('author', author_layout())
     while True:
      event, values = window.read()
      print(event, values)
      if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
          # os.execl(sys.executable, sys.executable, *sys.argv)
          window.close()
          break

# def layout():
#
#     layout = [ [sg.TabGroup([[sg.Tab('Алгебра', tab1_layout()), sg.Tab('Геометрия', tab2_layout()) , sg.Tab('Информатика', inf_layout()) , sg.Tab('Физика', fuz_layout())]])],
#
#               [sg.Button('Exit',background_color='#F3FB62'), sg.Button('debug')],
#
#              [sg.Menu(menu_def())]]
#     return layout
# s=(None, None), auto_size_text=None, click_submits=None, enable_events=False,
#                 font=None, text_color=None, background_color=None, justification=None, pad=None,
#                 key=None, k=None, right_click_menu=None, tooltip=None, visible=True, metadata=None
def  window_main(title='Main',size=(1280, 720),s=(None, None), auto_size_text=None, click_submits=None, enable_events=False,font=None, text_color=None,
                 background_color='y', justification=None, pad=None,key=None, k=None, right_click_menu=None, tooltip=None, visible=True, metadata=None):

     layout = [ [sg.TabGroup([[sg.Tab('Алгебра', tab1_layout()), sg.Tab('Геометрия', tab2_layout()) , sg.Tab('Информатика', inf_layout()) , sg.Tab('Физика', fuz_layout())]])],
              [sg.Button('Выход',image_data=None, key='-EXIT-'), sg.Button('debug')],
             [sg.Menu(menu_def())]]
     return sg.Window(title, layout,size,background_color='#F3FB62',return_keyboard_events=True,finalize=True,right_click_menu=right_click_menu_layout(),icon='name.ico')
recording = have_data = False
def Main(a):
    #
    # if a == 1:
    #  # if window:
    #  #     del window;window.close()
    #

    window = window_main()
    #     бинды и курсоры здесь!!!!!!
    #window['Exit'].set_cursor(cursor='no')
    window['-EXIT-'].set_cursor(cursor='X_cursor')
    window.bind('<F10>', 'Hard_exit')
    while True:
       #window = sg.Window('Main',layout())

       event, values = window.read() #timeout=100
       # УБРАТЬ print() ПЕРЕД КОМПИЛЯЦИЕЙ!!!!!!!!!!!!!!!!!!
       print(event, values)
       if (event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit' or event == '-EXIT-' or event == 'Escape:27') and sg.popup_yes_no('Вы уверены, что хотите выйти?') == 'Yes':
           global main_exit
           main_exit = True
           window.close()
           break
       if event == 'Hard_exit':
           window.close()
           exit()
           break
       if event == 'Квадрат суммы (a+b)^2':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(summakvadrata())
           break
       if event == 'Квадрат разности (a-b)^2':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(raznostkvadrata())
           break
       if event == 'Куб суммы (a+b)^3':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(summakuba())
           break
       if event == 'Куб разности (a+b)^3':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(raznostkuba())
           break
       if event == 'Разность кубов a^2-b^2':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(raznostkubov())
           break
       if event == 'Площадь Прямоугольного треугольника S=a*b*0.5':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(ploshadtriugolnika())
           break
       if event == 'Квадратное уравнение по дискриминанту':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(kv_ur_dis())
           break
       if event == 'Квадратное уравнение по теореме Виета':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(kv_ur_vi())
           break
       if event == 'Диагональ параллелепипеда  d=(a**2+b**2+c**2)**0.5':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(diag_paralel())
           break
       if event == 'log':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(log())
           break
       if event == 'Автор...':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           author()
           break
       if event == 'arccos':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(arccos())
           break
       if event == 'arcsin':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(arcsin())
           break
       if event == 'arctan':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(arctan())
           break
       if event == 'sin':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(sin())
           break
       if event == 'cos':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(cos())
           break
       if event == 'tan':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(tan())
           break
       if event == 'Sin(α+β)':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(Sin_sum())
           break
       if event == 'Sin(α-β)':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(Sin_razn())
           break
       if event == 'Cos(α+β)':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(Cos_sum())
           break
       if event == 'Cos(α-β)':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           otvet(Cos_razn())
           break
       if event == 'tg(α+β)':
          window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          otvet(tg_sum())
          break
       if event == 'tg(α-β)':
          window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          otvet(tg_razn())
          break
       if event == 'sin2α':
          window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          otvet(sin2a())
          break
       if event == 'cos2α':
          window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          otvet(cos2a())
          break
       if event == 'tg2α':
          window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          otvet(tg2a())
          break






       if event == 'debug':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           debug()

           break











#def delarg(a):
#   try:
#       del [a]
#  except:
if __name__ == '__main__':
     while True:
         Main('start_program')
         if main_exit == True:
             #del main_exit
             break

del x
del a
#delarg(b)
#os.execl(sys.executable, sys.executable, *sys.argv)
