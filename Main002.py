try:
    import PySimpleGUI as sg
except:
    print('Пожалуйста установите модуль PySimpleGUI')
import os
import sys
# import imp
#import supervisor
import math
import winsound
import images
import images as i
import layouts as l
# import webbrowser ля интеграции веб ссылок  [sg.Text('www.PySimpleGUI.org', font='default 12 underline', text_color='blue', enable_events=True, key='-LINK-')],
#elif event == '-LINK-':
        # if the text was clicked, open a browser using the text as the address
       # webbrowser.open(window['-LINK-'].DisplayText)   # accessing DisplayText isn't something you'll see often

# тест на плагин атома вроде говно, а вроде и робит
x = 0

a = 1

cursors = ('X_cursor', 'no', 'arrow','based_arrow_down','based_arrow_up','boat','bogosity','bottom_left_corner','bottom_right_corner','bottom_side','bottom_tee','box_spiral','center_ptr','circle','clock','coffee_mug','cross','cross_reverse','crosshair','diamond_cross','dot','dotbox','double_arrow','draft_large','draft_small','draped_box','exchange','fleur','gobbler','gumby','hand1','hand2','heart','icon','iron_cross','left_ptr','left_side','left_tee','leftbutton','ll_angle','lr_angle','man','middlebutton','mouse','no','pencil','pirate','plus','question_arrow','right_ptr','right_side','right_tee','rightbutton','rtl_logo','sailboat','sb_down_arrow','sb_h_double_arrow','sb_left_arrow','sb_right_arrow','sb_up_arrow','sb_v_double_arrow','shuttle','sizing','spider','spraycan','star','target','tcross','top_left_arrow','top_left_corner','top_right_corner','top_side','top_tee','trek','ul_angle','umbrella','ur_angle','watch','xterm','arrow','center_ptr','crosshair','fleur','ibeam','icon','sb_h_double_arrow','sb_v_double_arrow','watch','xterm','no','starting','size','size_ne_sw','size_ns','size_nw_se','size_we','uparrow','wait','arrow','cross','crosshair','ibeam','plus','watch','xterm')

event, values = 0, 0

# print = sg.Print =======================================================================================
# sg.theme('Black')
# event, values = sg.Window('Где файл сука?', [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).read(close=True)
sg.theme('DefaultNoMoreNagging')   # Add a touch of color
# All the stuff inside your window.


# def otvet_layout():
#     otvet_layout = [[sg.Multiline('  '+a+'  ')],[sg.Button('Exit')]]
#     return otvet_layout
# def otvet(otvet):
#     global a
#     a = otvet
#     a = str(a)
#     window_o = sg.Window('otvet',otvet_layout(),icon=i.ico)
#     while True:
#         event, values = window_o.read()
#         # print(event, values)
#         if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Exit':
#
#            window_o.close()
#            break


def debug():
    while True:
       window = sg.Window('debug123', l.layout123(), icon='name.ico')
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
    x = float(a)**2 + 2 * float(a) * float(b) + float(b)**2
    return x
def summakvadrata():
   while True:
     window = sg.Window('Квадрат суммы (a+b)^2', l.summakvadrata_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
      window = sg.Window('Квадрат разности (a-b)^2', l.raznostkvadrata_layout(),icon=i.ico)
      event, values = window.read()
      # print(event, values)
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
    x = float(a)**3 + 3 * (float(a)**2) * float(b) + 3 * float(a) * (float(b)**2) + float(b)**3
    return x
def summakuba():
    while True:
      window = sg.Window('Сумма куба (a-b)^3', l.summakuba_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
      window = sg.Window('Разность куба (a-b)^3', l.raznostkuba_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
      window = sg.Window('Разность кубов a^2-b^2', l.raznostkubov_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
      window = sg.Window('Площадь Прямоугольного треугольника S=a*b*0.5', l.ploshadtriugolnika_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
      window = sg.Window('Квадратное уравнение по дискриминанту', l.kv_ur_dis_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
      window = sg.Window('Квадратное уравнение по теореме Виета', l.kv_ur_vi_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
      window = sg.Window('Диагональ параллелепипеда  d=(a**2+b**2+c**2)**0.5', l.diag_paralel_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
      window = sg.Window('log', l.log_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
    a = float(a)
    a = math.radians(a)
    x = (math.sin(float(a))*math.cos(float(b)))+((math.cos(float(a))*math.sin(float(b))))
    return (x)


def Sin_sum():
     while True:
      window = sg.Window('Sin(α+β)', l.Sin_sum_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
    a = float(a)
    a = math.radians(a)
    return (math.acos(float(a)))

def arccos():
    while True:
      window = sg.Window('arccos', l.arccos_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
    a = float(a)
    a = math.radians(a)
    return (math.asin(float(a)))
def arcsin():
    while True:
      window = sg.Window('arcsin', l.arcsin_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
    a = float(a)
    a = math.radians(a)
    return (math.atan(float(a)))
def arctan():
    while True:
      window = sg.Window('arctan', l.arctan_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
    a = float(a)
    a = math.radians(a)
    return (math.sin(float(a)))
def sin():
    while True:
      window = sg.Window('sin', l.sin_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
    a = float(a)
    a = math.radians(a)
    return (math.cos(float(a)))
def cos():
    while True:
      window = sg.Window('cos', l.cos_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
    a = float(a)
    a = math.radians(a)
    return (math.tan(float(a)))

def tan():
    while True:
      window = sg.Window('tan', l.tan_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
    a = float(a)
    b = float(b)
    a = math.radians(a)
    b = math.radians(b)
    x = (math.sin(float(a))*math.cos(float(b)))-((math.cos(float(a))*math.sin(float(b))))
    return (x)


def Sin_razn():
     while True:
      window = sg.Window('Sin(α-β)', l.Sin_razn_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
    a = float(a)
    b = float(b)
    a = math.radians(a)
    b = math.radians(b)
    x = (math.cos(float(a))*math.cos(float(b)))-(math.sin(float(a))*math.sin(float(b)))
    return (x)


def Cos_sum():
     while True:
      window = sg.Window('Cos(α+β)', l.Cos_sum_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
    a = float(a)
    b = float(b)
    a = math.radians(a)
    b = math.radians(b)
    x = (math.cos(float(a))*math.cos(float(b)))+(math.cos(float(a))*math.cos(float(b)))
    return x

def Cos_razn():
     while True:
      window = sg.Window('Cos(α-β)', l.Cos_razn_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
    a = float(a)
    b = float(b)
    a = math.radians(a)
    b = math.radians(b)
    x = (math.tan(float(a))+math.tan(float(b)))/(1-(math.tan(float(a))*math.tan(float(b))))
    return x
def tg_sum():
     while True:
      window = sg.Window('tg(α+β)', l.tg_sum_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
    a = float(a)
    b = float(b)
    a = math.radians(a)
    b = math.radians(b)
    x = (math.tan(float(a))-math.tan(float(b)))/(1+(math.tan(float(a))*math.tan(float(b))))
    return x

def tg_razn():
     while True:
      window = sg.Window('tg(α-β)', l.tg_razn_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
    a = float(a)
    a = math.radians(a)
    x = (2*math.sin(float(a)))*math.cos(float(a))
    return x
def sin2a():
    while True:
     window = sg.Window('sin2α', l.sin2a_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
    a = float(a)
    a = math.radians(a)
    x = (math.cos(a)**2)-(math.sin(a)**2)
    return x
def cos2a():
    while True:
     window = sg.Window('cos2α', l.cos2a_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
    a = math.radians(a)
    x = (2*math.tan(a))/(1-(math.tan(a)**2))
    return x
def tg2a():
    while True:
     window = sg.Window('tg2α', l.tg2a_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
    a = math.radians(a)
    b = math.radians(b)
    x = ((2*math.sin((a+b)/2))*(math.cos((a-b)/2)))
    return x
def sins_sum():
     while True:
      window = sg.Window('Sinα + Sinβ', l.sins_sum_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
    a = math.radians(a)
    b = math.radians(b)
    x = ((2*math.sin((a-b)/2))*(math.cos((a+b)/2)))
    return x
def sins_razn():
     while True:
      window = sg.Window('Sinα - Sinβ', l.sins_razn_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
    a = math.radians(a)
    b = math.radians(b)
    x = ((2*math.cos((a+b)/2))*(math.cos((a-b)/2)))
    return x
def coss_sum():
     while True:
      window = sg.Window('Cosα + Cosβ', l.coss_sum_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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
    a = math.radians(a)
    b = math.radians(b)
    x = ((2*math.sin((a-b)/2))*(math.sin((a+b)/2)))
    return x
def coss_razn():
     while True:
      window = sg.Window('Cosα - Cosβ', l.coss_razn_layout(),icon=i.ico)
      event, values = window.read()
      #print(event, values)
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

def def_plodhadkruga(a):
    x = math.pi*(a**2)
    return x
def plodhadkruga():
    while True:
     window = sg.Window('Площадь Круга S=π*r^2', l.plodhadkruga_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_plodhadkruga(a)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break

def def_plodhadgerron(a,b,c):
    p = (a+b+c)/2
    x = (p*((p-a)*(p-b)*(p-c)))**0.5
    del p
    return x

def plodhadgerron():
    while True:
     window = sg.Window('Площадь треугольника по формуле Герона\n S=(p(p-a)(p-b)(p-c))^0.5', l.plodhadgerron_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
         c = values[2]
         a = float(a)
         b = float(b)
         c = float(c)

         try:
             window.close()
             return def_plodhadgerron(a,b,c)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_plodhadprugol(a,b):
    x = a*b
    return x
def plodhadprugol():
    while True:
     window = sg.Window('Площадь Прямоугольника S=ab', l.plodhadprugol_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_plodhadprugol(a,b)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_plodhadparugol(a,b,c):
    c = math.radians(c)
    x = (a*b)*math.sin(c)
    return x
def plodhadparugol():
    while True:
     window = sg.Window('Площадь параллелограмма через стороны и угол S=ab*Sinα', l.plodhadparugol_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
         c = values[2]
         a = float(a)
         b = float(b)
         c = float(c)

         try:
             window.close()
             return def_plodhadparugol(a,b,c)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_plodhadtrap(a,b,c):
    x = (a+b)/2*c
    return x
def plodhadtrap():
    while True:
     window = sg.Window('Площадь трапеции через основания и высоту S=(a+b)/2*h', l.plodhadtrap_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
         c = values[2]
         a = float(a)
         b = float(b)
         c = float(c)

         try:
             window.close()
             return def_plodhadtrap(a,b,c)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_plodhadromb(a,b):
    b = math.radians(b)
    x = a**2*math.sin(b)
    return x
def plodhadromb():
    while True:
     window = sg.Window('Площадь ромба по стороне и углу a^2*Sinα', l.plodhadromb_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_plodhadromb(a,b)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_plodhadmnugol(a,b):
    t = 180/b
    t = math.radians(t)
    x = (b*(a**2))/(4*math.tan(t))
    del t
    return x
def plodhadmnugol():
    while True:
     window = sg.Window('Формула площади правильного многоугольника', l.plodhadmnugol_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_plodhadmnugol(a,b)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_radians(a):
    x = math.radians(a)
    return x
def radians():
    while True:
     window = sg.Window('Перевод из градусов в радианы', l.radians_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_radians(a)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_degrees(a):
    x = math.degrees(a)
    return x
def degrees():
    while True:
     window = sg.Window('Перевод из радиан в градусы', l.degrees_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_degrees(a)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break

def def_plpovkuba(a):
    x = a**2*6
    return x
def plpovkuba():
    while True:
     window = sg.Window('Площадь поверхности Куба 6a^2', l.plpovkuba_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_plpovkuba(a)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_diagkuba(a):
    x = a * (3**0.5)
    return x
def diagkuba():
    while True:
     window = sg.Window('Длина диагонали куба', l.diagkuba_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_diagkuba(a)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_plpovpar(a,b,c):
    x = (2*a*b)+(2*a*c)+(2*b*c)
    return x
def plpovpar():
    while True:
     window = sg.Window('Площадь поверхности параллелепипеда', l.plpovpar_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
         c = values[2]

         a = float(a)
         b = float(b)
         c = float(c)

         try:
             window.close()
             return def_plpovpar(a,b,c)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_obcil(a,b):
    x = math.pi*(a**2)*b
    return x
def obcil():
    while True:
     window = sg.Window('Объём цилиндра πR^2h', l.obcil_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_obcil(a,b)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_plpovcil(a,b):
    x = (2*math.pi*(a**2))+(2*math.pi*a*b)
    return x
def plpovcil():
    while True:
     window = sg.Window('Площадь поверхности цилиндра', l.plpovcil_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_plpovcil(a,b)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_obkon(a,b):
    x = (math.pi*(a**2))/3*b
    return x
def obkon():
    while True:
     window = sg.Window('Объём конуса', l.obkon_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_obkon(a,b)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break

def def_plpovkon(a,b):
    l = ((a**2)+(b**2))**0.5
    x = math.pi*(a**2)+math.pi*a*l
    del l
    return x
def plpovkon():
    while True:
     window = sg.Window('Площадь поверхности конуса', l.plpovkon_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_plpovkon(a,b)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_obshar(a):
    x = math.pi*(a**3)/3*4
    return x
def obshar():
    while True:
     window = sg.Window('Объём шара', l.obshar_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_obshar(a)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_plpovshar(a):
    x = 4*math.pi*(a**2)
    return x
def plpovshar():
    while True:
     window = sg.Window('Площадь поверхности шара', l.plpovshar_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_plpovshar(a)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_alfabet(a):
    x = 2**a
    return x
def alfabet():
    while True:
     window = sg.Window('Мощность алфавита N = 2^i', l.alfabet_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_alfabet(a)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_kolinfo(a,b):
    x = a*b
    return x
def kolinfo():
    while True:
     window = sg.Window('Кол-во информации I = K * i', l.kolinfo_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_kolinfo(a,b)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break

def def_kolsoob(a,b):
    x = a**b
    return x

def kolsoob():
    while True:
     window = sg.Window('Кол-во разных сообщений Q = N^L', l.kolsoob_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_kolsoob(a,b)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_hartl(a):
    x = math.log2(a)
    return x
def hartl():
    while True:
     window = sg.Window('Формула Хартли: I = log2 N', l.hartl_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
             return def_hartl(a)
         except:
            window.close()
            return('Ошибка')
         window.close()
         break
def def_convert_base(a,b,c):
    num = a
    from_base = int(b)
    to_base = int(c)

    # (num, from_base=10, to_base=10)
    # first convert to decimal number
    n = int(num, from_base) if isinstance(num, str) else num
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n,m = divmod(n, to_base)
        res += alphabet[m]
    return res[::-1]
def convert_base():
    while True:
     window = sg.Window('Перевод любого числа любой системы счисления в любую другую', l.convert_base_layout(),icon=i.ico)
     event, values = window.read()
     #print(event, values)
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
         c = values[2]


         try:
             window.close()
             return def_convert_base(a,b,c)
         except:
             window.close()
             return('Ошибка')
         window.close()
         break

def author():
     window = sg.Window('Автор', l.author_layout(),icon=i.ico)
     while True:
      event, values = window.read()
      #print(event, values)
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
# s=(None, None), auto_size_text=None, click_submits=None, Иenable_events=False,
#                 font=None, text_color=None, background_color=None, justification=None, pad=None,
#                 key=None, k=None, right_click_menu=None, tooltip=None, visible=True, metadata=None
if __name__ == '__main__':
    print('Пожалуйста запустите исполнительный файл')
