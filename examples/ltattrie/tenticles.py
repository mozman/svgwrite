#!/usr/bin/env python
# Author:  L. Tattrie
# Purpose: svgwrite examples
# Created: 2012/5/31
# Copyright (C) 2012, L. Tattrie
# License: LGPL
# Python version 2.7
import math, sys
import random
import svgwrite

# globals

PROGNAME = sys.argv[0].rstrip('.py')

file_log = ''
dwg = ''


def gen_colour(start_p, end_p, n_p):
    """
    gen_colour generates a list of colours from start to end. Colours are linearly interpreted between start and end.
    start and end must be (int, int, int), n integer is how many colours are to be generated.
    """
    c_start = start_p
    c_end = end_p
    n = n_p
    # yielding a c_end separately gives the exact c_end thus not something that is 99.99% c_end which is slightly off colour.
    for i in range(n):
        ccolour = (int(c_start[0] + (float(i) / float(n))*(c_end[0] - c_start[0])),
                   int(c_start[1] + (float(i) / float(n))*(c_end[1] - c_start[1])),
                   int(c_start[2] + (float(i) / float(n))*(c_end[2] - c_start[2])))
        yield ccolour
    yield c_end


def gen_incr_num():
    i = 0
    while True:
        i += 1
        yield i
unique_num = gen_incr_num()


class tendrile:
    #global angle_max
    #global angle_min
    global file_log
    global dwg
    global unique_num

    def __init__(self, p_x, p_y, p_width, p_angle, p_step, p_v, p_curl, p_n, p_scolour, p_ecolour, p_can_branch):
        """tendrile class instance for each arm """
        self.x = p_x
        self.y = p_y
        self.width = p_width
        #self.angle = max(min(p_angle, angle_max), angle_min)  # limit value of angle
        self.angle_set(p_angle)  # limit value of angle
        self.step = p_step
        self.v = p_v
        self.curl = p_curl
        self.n = p_n        # length of tendrile
        self.scolour = p_scolour  # starting colour
        self.ecolour = p_ecolour  # ending colour
        self.can_branch = p_can_branch  # Can tendrile branch?
        self.stroke_width = 1
        self.lin_colour = gen_colour(self.scolour, self.ecolour, self.n)
        self.r = self.width
        # The purpose of having a group for all of the circles is be able to add all of the circles
        # of a tendrile to the drawing at the same time. If a tendrile branches, creating a new
        # tendrile the new tendrile will be drawn completely before the older tendrile is drawn.
        # This puts the new tendrile in the background and the old tendrile in front.  When the
        # program had been written to start writting the old tendrile, write the new tendrile, then
        # finish the old tendrile there was a problem that slivers of some of the new tendrile's
        # colour was over top of the old tendrile causing a confusing mix of colour.
        # Using a group does create a small problem. The whole new tendrile is in the background of
        # the whole old tendrile. This is not perspectively correct because if a old tendrile
        # branches near the end of the tendrile the new tendrile should be in front of any part of
        # of the beginning part of the old tendrile but instead the new tendrile will be behind all
        # of the old tendrile.
        self.group = dwg.g(id='branch' + str(next(unique_num)))
        #file_log.write("new tend x="+ str(self.x)+
        #    " y="+str(self.y)+
        #    " width="+str(self.width)+
        #    " angle="+str(self.angle)+
        #    " step="+str(self.step)+
        #    " v="+str(self.v)+
        #    " curl="+str(self.curl)+
        #    " n="+str(self.n)+
        #    "\n")

    def angle_set(self, p_val):
        # limit the angle to range -2*math.pi to 2*math.pi  which is +- full circle.
        # Use math.fmod because % returns with the sign of the second number.
        self.angle = math.fmod(p_val, (2 * math.pi))

    def create(self):
        global file_log
        #green_light1 =(102, 229, 132) # starting colour. Colour will linearly change to ending colour.
        #green_dark1=(25, 76, 37)
        #v =0.0
        #branch_at = (self.n * 1) / 10
        for i in range(self.n):
            if i != 0:
                # if (i == 2)
                #random.randint(1, 100)
                #if (i == branch_at) and self.can_branch:
                if (random.randint(1, 100) == 1) and self.can_branch:
                    distance = self.r * .8  # The new circle is % of the previouse circle's width
                    x_temp = self.x + math.cos(self.angle) * distance
                    y_temp = self.y + math.sin(self.angle) * distance
                    # separate angles for branches
                    #v_rand = 3*random.uniform(-self.step, self.step)
                    #v_rand = random.uniform(-self.step, self.step)
                    v_delta_split = math.pi / 31.4  # .05 degrees
                    #v_rand = random.uniform(0.0, self.step) +math.pi/6.0 #30 degrees
                    self.v = self.v + v_delta_split + random.uniform(-self.step, self.step)
                    self.v *= 0.9 + self.curl * 0.1
                    #self.angle += self.v
                    self.angle_set(self.angle + self.v)  # limit value of angle
                    #self.angle   = max(min(self.angle, angle_max), angle_min)  # limit value of angle
                    # draw branch
                    #tend = tendrile(x_temp, y_temp, self.r, angle_temp, self.step, self.v, (-1*self.curl), (self.n-i-1), new_colour, self.ecolour, False)

                    #file_log.write("before new tend x="+ str(self.x)+
                    #  " y="+str(self.y)+
                    #  " r="+str(self.r)+
                    #  " angle="+str(self.angle)+
                    #  " step="+str(self.step)+
                    #  " curl="+str(self.curl)+
                    #  " i="+str(i)+
                    #  " v="+str(self.v)+
                    #  "\n")
                    #file_log.write("******************************************************************"+
                    #"\n")
                    ## Branch creating a new smaller tendrile
                    #pink1=(251,170,176)  # debug
                    #tend = tendrile(x_temp, y_temp, self.r, self.angle, (self.step*1.2), (-1.0*self.v), self.curl, (self.n-i-1), green_dark1, green_light1, False)
                    # create the tendrile
                    # The use of the original colour, usually darker green, to start the new tendrile gives a slight look
                    # of shadow on the the start of the new tendrile. It also gives a clear visual
                    # separation between the existing tendrile and the new tendrile.
                    tend = tendrile(x_temp, y_temp, self.r, self.angle, (self.step * 1.2), (-1.0 * self.v),
                            self.curl, (self.n - i - 1), self.scolour, self.ecolour, False)
                    # create the tendrile as svg elements
                    tend.create()
                    # draw the tendrile as svg elements
                    tend.draw()
                    #file_log.write("******************************************************************"+
                    #"\n")
                    #file_log.write("after tend x="+ str(self.x)+
                    #  " y="+str(self.y)+
                    #  " r="+str(self.r)+
                    #  " angle="+str(self.angle)+
                    #  " step="+str(self.step)+
                    #  " curl="+str(self.curl)+
                    #  " i="+str(i)+
                    #  " v="+str(self.v)+
                    #  "\n")
                    #self.v = self.v - v_rand -math.pi/6.0 # change angle of tendrile
                    #self.v = self.v - v_rand
                    #self.v *= 0.9 + self.curl*0.1
                    #self.angle += self.v
                    self.x += math.cos(self.angle) * distance
                    self.y += math.sin(self.angle) * distance
                    # set up angle for next circle
                    self.v += random.uniform(-self.step, self.step)
                    self.v *= 0.9 + self.curl * 0.1
                    self.angle_set(self.angle + self.v)  # limit value of angle
                    #self.angle += self.v
                    #self.angle   = max(min(self.angle, angle_max), angle_min)  # limit value of angle
                else:
                    distance = self.r * .8  # The new circle is % of the previouse circle's width
                    self.x += math.cos(self.angle) * distance
                    self.y += math.sin(self.angle) * distance
                    #file_log.write("tend x="+ str(self.x)+
                    #  " y="+str(self.y)+
                    #  " r="+str(self.r)+
                    #  " angle="+str(self.angle)+
                    #  " step="+str(self.step)+
                    #  " curl="+str(self.curl)+
                    #  " i="+str(i)+
                    #  " v="+str(self.v)+
                    #  "\n")
                    self.v += random.uniform(-self.step, self.step)
                    self.v *= 0.9 + self.curl * 0.1
                    #self.angle += self.v
                    self.angle_set(self.angle + self.v)  # limit value of angle
                    #self.angle   = max(min(self.angle, angle_max), angle_min)  # limit value of angle
            self.r = (1 - float(i) / self.n) * self.width  # radius size gradually decreases.
            ##
            new_colour = next(self.lin_colour)
            stroke_colour = 'rgb(%s,%s,%s)' % new_colour
            fill_colour = 'rgb(%s,%s,%s)' % new_colour
            self.group.add(dwg.circle(center=(self.x, self.y), r=self.r, fill=fill_colour, stroke=stroke_colour,
                              stroke_width=3))

    def draw(self):
        global file_log
        dwg.add(self.group)


def create_svg(name):
    """
    Create many circles in a curling tentril fashion.
    """
    global file_log
    global dwg
    svg_size_width = 900
    svg_size_height = 900
    dwg = svgwrite.Drawing(name, (svg_size_width, svg_size_height), debug=True)
    # Background will be black so the background does not overwhelm the colors.
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), rx=None, ry=None, fill='black'))
    #angle_max = 2*math.pi      # maximum angle allowed. 360 degrees.
    #angle_min = -1 * angle_max # minimum angle allowed -360 degrees.
    #file_log = open("tendriles_branch.log", "w")
    # Create effect instance and apply it.
    # option values.
    n = 100         # number of circles default 100
    #n = 20         # number of circles default 100
    num_arms = 5  # number of tendriles default 5
    #num_arms = 10  # number of tendriles default 5
    #num_arms = 1  # number of tendriles default 5

    d_width = svg_size_width
    d_height = svg_size_height

    ###########################
    #x_org = d_height / 10
    #y_org = d_width / 10
    #delta_x = d_width / 6
    #delta_y = d_width / 10
    ###########################
    stroke_width = 1
    #n = 200   #number of circles
    #n = 75   #number of circles
    #num_arms = 9
    #step = 0.05
    #step = 0.02
    step = 4.0 / n
    #curl = 1.0
    #c_width= d_width/12.0
    #c_width= d_width/50.0
    green_light1 = (102, 229, 132)  # starting colour. Colour will linearly change to ending colour.
    green_dark1 = (25, 76, 37)
    salmon1 = (240, 184, 178)
    pink1 = (251, 170, 176)
    pink2 = (255, 170, 204)
    pink2light = (255, 215, 231)
    pink2dsat = (247, 225, 234)
    blue1 = (193, 197, 251)
    grey7_5 = (236, 236, 236)
    grey80 = (51, 51, 51)
    # starting colour. Colour will linearly change to ending colour.
    #start_colour = pink2light
    #end_colour = blue1
    start_colour = green_dark1
    end_colour = green_light1
    #distance = 9.0
    #distance = c_width/3.0  # The next circle is 1/3 the original circle's width from the centre.
    #n         - number of circles in each tendrile.
    #num_arms  - number of arms that is tendriles.
    # x, y     - centre of current circle, 0,0 is top left of screen
    # c_width  - initial circle width.
    # r        - radius of current circle. gradually decreases.
    # distance - length to next circle.
    # angle    - angle to next circle. value -pi to +pi.
    # step     - range of randomness of angle. constant.
    # curl     - how much curl will happen. constant. .1*curl incremented to v, angle.
    # v        - change in angle. random value -step to +step plus curl
    # can_branch - true or false. Can this tendrile branch?
    can_branch = True
    #can_branch = False

    ###########################
    # The change in the starting colour is small so all of the tenticles seem like a group but
    # still have a very slight variation to give individuality. If the starting colour is too
    # different the arms look like they are not connected at the centre.
    #start_lin_colour = gen_colour(start_colour, blue1, num_arms) # debug
    start_lin_colour = gen_colour(start_colour, end_colour, num_arms * 8)
    # Create all tendriles
    for j in range(num_arms):
        # set start of arm x y
        x = d_height / 2
        y = d_width / 2
        angle = random.uniform((-1.0 * math.pi), math.pi)  # random angle in radians. 2*pi radians = 360 degrees
        v = 0.0
        # variety to the size of the starting circle
        c_width = random.uniform((d_width * .015), (d_width * .025))
        r = random.uniform((c_width * .9), (c_width * 1.1))
        new_start_colour = next(start_lin_colour)
        #curl = random.choice((-1, 1))  # random.choice picks random item from list
        #curl = random.choice((-1.1, 1.1))  # random.choice picks random item from list
        #curl = random.choice((-1.05, 1.05))  # random.choice picks random item from list
        #curl = 1.1
        curl = 1.0
        # create a tendrile
        tend = tendrile(x, y, r, angle, step, v, curl, n, new_start_colour, end_colour, can_branch)
        #tend = tendrile(x, y, r, angle, step, v, curl, n, blue1, end_colour, can_branch)
        # create the tendrile as svg elements
        tend.create()
        # draw the tendrile as svg elements
        tend.draw()
    #file_log.close()
    dwg.save()


if __name__ == '__main__':
    create_svg(PROGNAME + '.svg')

# vim: expandtab shiftwidth=4 tabstop=8 softtabstop=4 textwidth=99
