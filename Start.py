import PySimpleGUI as sg
import Main002 as m
import otvet as o
import images as i
import layouts as l
import winsound
main_exit = None
def  window_main(title='Main',size=(1280, 720),s=(None, None), auto_size_text=None, click_submits=None, enable_events=False,font=None, text_color=None,
                 background_color='y', justification=None, pad=None,key=None, k=None, right_click_menu=None, tooltip=None, visible=True, metadata=None):

     layout = [ [sg.TabGroup([[sg.Tab('Алгебра', l.tab1_layout()), sg.Tab('Геометрия', l.tab2_layout()) , sg.Tab('Информатика', l.inf_layout()) #, sg.Tab('Физика', l.fuz_layout()
     ]])],
              [sg.Button('Выход',image_data=None, key='-EXIT-'), sg.Button('debug')],
             [sg.Menu(l.menu_def())]]
     return sg.Window(title, layout,size,background_color='#F3FB62',return_keyboard_events=True,finalize=True,right_click_menu=l.right_click_menu_layout(),icon=i.mccree)
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
       global main_exit
       #window = sg.Window('Main',layout())
       if main_exit == True:
           break
       event, values = window.read() #timeout=100
       # УБРАТЬ print() ПЕРЕД КОМПИЛЯЦИЕЙ!!!!!!!!!!!!!!!!!!
       #  print(event, values)
       if (event == 'Cancel' or event == 'Exit' or event == '-EXIT-' or event == 'Escape:27') and sg.popup_yes_no('Вы уверены, что хотите выйти?') == 'Yes':
           main_exit = True
           window.close()
           break
       if (event == sg.WIN_CLOSED):
           if sg.popup_yes_no('Вы уверены, что хотите выйти?') == 'Yes':
               main_exit = True
               window.close()
               break
           else:
               Main('start_program')
       if event == 'Hard_exit':
           window.close()
           exit()
           break
       if event == 'Квадрат суммы (a+b)^2':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.summakvadrata())
           # break
       if event == 'Квадрат разности (a-b)^2':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.raznostkvadrata())
           # break
       if event == 'Куб суммы (a+b)^3':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.summakuba())
           # break
       if event == 'Куб разности (a+b)^3':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.raznostkuba())
           # break
       if event == 'Разность кубов a^2-b^2':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.raznostkubov())
           # break
       if event == 'Площадь Прямоугольного треугольника S=a*b*0.5':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.ploshadtriugolnika())
           # break
       if event == 'Площадь Круга S=π*r^2':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.plodhadkruga())
           # break
       if event == 'Площадь треугольника по формуле Герона\n S=(p(p-a)(p-b)(p-c))^0.5':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.plodhadgerron())
           # break
       if event == 'Площадь Прямоугольника S=ab':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.plodhadprugol())
           # break
       if event == 'Площадь параллелограмма через стороны и угол S=ab*Sinα':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.plodhadparugol())
           # break
       if event == 'Площадь трапеции через основания и высоту S=(a+b)/2*h':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.plodhadtrap())
           # break
       if event == 'Площадь ромба по стороне и углу a^2*Sinα':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.plodhadromb())
           break
       if event == 'Формула площади правильного многоугольника':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.plodhadmnugol())
           # break
       if event == 'Квадратное уравнение по дискриминанту':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.kv_ur_dis())
           # break
       if event == 'Квадратное уравнение по теореме Виета':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.kv_ur_vi())
           # break
       if event == 'Диагональ параллелепипеда  d=(a**2+b**2+c**2)**0.5':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.diag_paralel())
           # break
       if event == 'log':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.log())
           # break
       if event == 'Автор...':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           m.author()
           # break
       if event == 'arccos':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.arccos())
           # break
       if event == 'arcsin':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.arcsin())
           # break
       if event == 'arctan':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.arctan())
           # break
       if event == 'sin':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.sin())
           # break
       if event == 'cos':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.cos())
           # break
       if event == 'tan':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.tan())
           # break
       if event == 'Sin(α+β)':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.Sin_sum())
           # break
       if event == 'Sin(α-β)':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.Sin_razn())
           # break
       if event == 'Cos(α+β)':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.Cos_sum())
           # break
       if event == 'Cos(α-β)':
           # window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           o.otvet(m.Cos_razn())
           # break
       if event == 'tg(α+β)':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.tg_sum())
          # break
       if event == 'tg(α-β)':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.tg_razn())
          # break
       if event == 'sin2α':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.sin2a())
          # break
       if event == 'cos2α':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.cos2a())
          # break
       if event == 'tg2α':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.tg2a())
          # break
       if event == 'Sinα + Sinβ':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.sins_sum())
          # break
       if event == 'Sinα - Sinβ':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.sins_razn())
          # break
       if event == 'Cosα + Cosβ':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.coss_sum())
          # break
       if event == 'Cosα - Cosβ':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.coss_razn())
          # break
       if event == 'Перевод из градусов в радианы':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.radians())
          # break
       if event == 'Перевод из радиан в градусы':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.degrees())
          # break
       if event == 'Площадь поверхности Куба 6a^2':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.plpovkuba())
          # break
       if event == 'Длина диагонали куба':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.diagkuba())
          # break
       if event == 'Площадь поверхности параллелепипеда':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.plpovpar())
          # break
       if event == 'Объём цилиндра πR^2h':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.obcil())
          # break
       if event == 'Площадь поверхности цилиндра':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.plpovcil())
          # break
       if event == 'Объём конуса':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.obkon())
          # break
       if event == 'Площадь поверхности конуса':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.plpovkon())
          # break
       if event == 'Объём шара':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.obshar())
          # break
       if event == 'Площадь поверхности шара':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.plpovshar())
          # break
       if event == 'Мощность алфавита N = 2^i':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.alfabet())
          # break
       if event == 'Кол-во информации I = K * i':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.kolinfo())
          # break
       if event == 'Кол-во разных сообщений Q = N^L':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.kolsoob())
          # break
       if event == 'Формула Хартли: I = log2 N':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.hartl())
          # break
       if event == 'Перевод любого числа любой системы счисления в любую другую':
          # window.close()
          winsound.PlaySound("ButtonClick.wav", 1)
          o.otvet(m.convert_base())
          # break






       if event == 'debug':
           window.close()
           winsound.PlaySound("ButtonClick.wav", 1)
           m.debug()

           break


'''
A= F *s**cosα




'''


# def delarg(a):
#   try:
#       del [a]
#  except:
if __name__ == '__main__':
     while True:
         Main('start_program')
         if main_exit == True:
             #del main_exit
             break
try:
    del x
    del a
except:
    None
