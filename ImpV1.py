# Attempt implementation of Visual tool, version 1
# Cheng Chang 02/06/20

from psychopy import core, visual, event, logging
logging.console.setLevel(logging.CRITICAL)

# General param
scr_res = [1920, 1080]
monitor = "TonysLaptopMon"
scr_units = "pix"
pos_1 = (0, 300)
pos_2 = (0, -300)
key_req = ["1", "2", "3", "4", "5"]

# Group of color used
color_white = [1,1,1]
color_black = [-1,-1,-1]
color_grey = [0,0,0]
color_skyBlue = [0.53,0.81,0.92]

# Text used
welcome = "Hello! This is an attempted implementation of visual part of the stimuli.\n"
instruction = "On a scale of 1 to 5, Please rate the picture showing on the screen according to your immediate feelings about them.\n"
prompt_next_scr = "Press any key to continue...\n"
prompt_next_pic = "Press 1-5 on the keypad to continue\n"
end = "This is the end of the visual test, thank you for your participation."
extra_line= "\n"

# Scale (hopefully this will work)
ratingNum = "       1             2             3              4              5   \n"
ratingtxt = "Disturbing                                              Pleasant\n"
 
# Image used
black_img = "Pics/BlackImg.jpg"
pic_lib = ["Pics/0.png", "Pics/1.png", "Pics/2.png", "Pics/3.png", 
             "Pics/4.png", "Pics/5.png", "Pics/6.png", "Pics/7.png"]



# Create log file
log = logging.LogFile(
    f = "ImpV1Log.txt",
)

# Create logger
logger = logging._Logger()
logger.addTarget(log)

# Create background
win = visual.Window(
    size = scr_res,
    color = color_black,
    units = scr_units,
    fullscr = False,
    mon = monitor
)

# Initialize image
img = visual.ImageStim(
    win = win,
    image = black_img,
    units = scr_units
)
img.autoDraw = True
size_x = img.size[0]
size_y = img.size[1]
img.size = [size_x * 2, size_y * 1.5]

# Initialize main instruction
main_ins = visual.TextStim(
    win = win,
    text = "",
    color = color_white
)
main_ins.autoDraw = True
main_ins.bold = True

# Initialize sub instruction
sub_ins = visual.TextStim(
    win = win,
    text = "",
    color = color_white
)
sub_ins.autoDraw = True



# Start of display

# Welcome screen
main_ins.text = welcome + extra_line + instruction + extra_line + prompt_next_scr
win.flip()
event.waitKeys()

# Text
main_ins.text = instruction
main_ins.pos = pos_1
main_ins.color = color_skyBlue
sub_ins.text = ratingNum + ratingtxt + extra_line + prompt_next_pic
sub_ins.pos = pos_2

# Image
for i in range(0,7):
    img.image = pic_lib[i]
    win.flip()
    output = event.waitKeys(keyList = key_req, clearEvents = True)
    logger.log(output[0], level = CRITICAL)






