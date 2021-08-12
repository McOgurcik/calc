import PySimpleGUI as sg 
import os
import sys
# import imp
#import supervisor
import math
import winsound
import images
import layouts as l
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
       window = sg.Window('debug123', l.layout123(),icon='name.ico')
       event, values = window.read()
       print(event, values)
       if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
           return('Отменено')
           window.close()
           break
       if event == 'Print':
           print(l.layout_all())
           window.close()
           break


def defsummakvadrata(a,b):
    x = float(a)**2 + 2 * float(a)*float(b) + float(b)**2
    return x
def summakvadrata():
   while True:
     window = sg.Window('Квадрат суммы (a+b)^2', l.summakvadrata_layout())
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
      window = sg.Window('Квадрат разности (a-b)^2', l.raznostkvadrata_layout())
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
      window = sg.Window('Сумма куба (a-b)^3', l.summakuba_layout())
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
      window = sg.Window('Разность куба (a-b)^3', l.raznostkuba_layout())
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
      window = sg.Window('Разность кубов a^2-b^2', l.raznostkubov_layout())
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
      window = sg.Window('Площадь Прямоугольного треугольника S=a*b*0.5', l.ploshadtriugolnika_layout())
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
      window = sg.Window('Квадратное уравнение по дискриминанту', l.kv_ur_dis_layout())
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
      window = sg.Window('Квадратное уравнение по теореме Виета', l.kv_ur_vi_layout())
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
      window = sg.Window('Диагональ параллелепипеда  d=(a**2+b**2+c**2)**0.5', l.diag_paralel_layout())
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
      window = sg.Window('log', l.log_layout())
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
      window = sg.Window('Sin(α+β)', l.Sin_sum_layout())
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
      window = sg.Window('arccos', l.arccos_layout())
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
      window = sg.Window('arcsin', l.arcsin_layout())
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
      window = sg.Window('arctan', l.arctan_layout())
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
      window = sg.Window('sin', l.sin_layout())
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
      window = sg.Window('cos', l.cos_layout())
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
      window = sg.Window('tan', l.tan_layout())
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
      window = sg.Window('Sin(α-β)', l.Sin_razn_layout())
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
      window = sg.Window('Cos(α+β)', l.Cos_sum_layout())
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
      window = sg.Window('Cos(α-β)', l.Cos_razn_layout())
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
      window = sg.Window('tg(α+β)', l.tg_sum_layout())
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
      window = sg.Window('tg(α-β)', l.tg_razn_layout())
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
     window = sg.Window('sin2α', l.sin2a_layout())
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
     window = sg.Window('cos2α', l.cos2a_layout())
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
     window = sg.Window('tg2α', l.tg2a_layout())
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
def def_sins_sum(a,b):
    x = ((2*math.sin((a+b)/2))*(math.cos((a-b)/2)))
    return x
def sins_sum():
     while True:
      window = sg.Window('Sinα + Sinβ', l.sins_sum_layout())
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
          a = float(a)
          b = float(b)
          try:
              window.close()
              return def_sins_sum(a,b)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break

def def_sins_razn(a,b):
    x = ((2*math.sin((a-b)/2))*(math.cos((a+b)/2)))
    return x
def sins_razn():
     while True:
      window = sg.Window('Sinα - Sinβ', l.sins_razn_layout())
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
          a = float(a)
          b = float(b)

          try:
              window.close()
              return def_sins_razn(a,b)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break

def def_coss_sum(a,b):
    x = ((2*math.cos((a+b)/2))*(math.cos((a-b)/2)))
    return x
def coss_sum():
     while True:
      window = sg.Window('Cosα + Cosβ', l.coss_sum_layout())
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
          a = float(a)
          b = float(b)
          try:
              window.close()
              return def_coss_sum(a,b)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break

def def_coss_razn(a,b):
    x = ((2*math.sin((a-b)/2))*(math.sin((a+b)/2)))
    return x
def coss_razn():
     while True:
      window = sg.Window('Cosα - Cosβ', l.coss_razn_layout())
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
          a = float(a)
          b = float(b)
          try:
              window.close()
              return def_coss_razn(a,b)
          except:
             window.close()
             return('Ошибка')
          window.close()
          break









def author():
     window = sg.Window('author', l.author_layout())
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

     layout = [ [sg.TabGroup([[sg.Tab('Алгебра', l.tab1_layout()), sg.Tab('Геометрия', l.tab2_layout()) , sg.Tab('Информатика', l.inf_layout()) , sg.Tab('Физика', l.fuz_layout())]])],
              [sg.Button('Выход',image_data=None, key='-EXIT-'), sg.Button('debug')],
             [sg.Menu(l.menu_def())]]
     return sg.Window(title, layout,size,background_color='#F3FB62',return_keyboard_events=True,finalize=True,right_click_menu=l.right_click_menu_layout(),icon='name.ico')
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
       if event == 'Sinα + Sinβ':
          window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          otvet(sins_sum())
          break
       if event == 'Sinα - Sinβ':
          window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          otvet(sins_razn())
          break
       if event == 'Cosα + Cosβ':
          window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          otvet(coss_sum())
          break
       if event == 'Cosα - Cosβ':
          window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          otvet(coss_razn())
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
