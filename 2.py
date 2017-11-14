import ui

def calculate_button_touch_up_inside(sender):
	  
	  g = 9.81
	  time = int(view['time_textfield'].text)
	  gs = time * g
	  height = 100 - (1/2)(gs*2)
	  view['answer_label'].text = 'the height of the object is' + ''.format(height)

v = ui.load_view()
v.present('fullscreen')
