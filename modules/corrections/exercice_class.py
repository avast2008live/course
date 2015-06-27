# -*- coding: utf-8 -*-

from __future__ import print_function

from IPython.display import HTML

from exercice import log_correction, font_style, header_font_style

default_correction_columns = 40, 30, 30

def error_line(text, width=3):
    return "<tr style='background-color:red'><td colspan={}>{}</td></tr>"\
        .format(width, text)

class ScenarioClass(list):
    """
    Describes a scenario that can be applied to a class

    Typically we want to create an instance (using some args),
    and then run some methods (still with some args)

    So a class scenario in its simpler form is defined as a list
    of couples of the form 
    ( method_name, Args_object )
    """

    def __init__(self):
        list.__init__(self)

    def set_init_args(self, args):
        if self and self[0][0] == '__init__':
            print("Only one __init__ step is allowed")
            return
        self.insert(0, ('__init__', args))

    def add_step (self, methodname, args):
        self.append( (methodname, args,) )

class ExerciceClass(object):
    """
    Much like the Exercice class, this allows to define
    an exercice as
    (*) a solution which is the correct implementation of a class
    (*) a list of scenarios that will be executed on that class
    """
    
    def __init__(self, solution, scenarios, format=None):
        self.solution = solution
        self.scenarios = scenarios
        # in some weird cases this won't exist
        self.name = getattr(solution, '__name__', "no_name")
        # applicable to all cells whose Args instance has not specified a format
        self.format = format

    def correction (self, student_class):

        overall = True

        # should be customizable
        columns = default_correction_columns
        c1, c2, c3 = columns
        
        html = ""
        html += u"<table style='{}'>".format(font_style)
        html += u"<tr style='{}'><th>Arguments</th><th>Attendu</th>"\
                u"<th>Obtenu</th></tr>".format(header_font_style)
    
        ref_class = self.solution
        print("Solution = {}".format(self.solution))
        print("Student class = {}".format(student_class))
        for i, scenario in enumerate(self.scenarios):
            # skip empty scenarios
            if not scenario: continue
            
            # start of scenario
            html += "<tr><th colspan=3 style='text-align:center;'>Scenario {}</th></tr>"\
                    .format(i)

            # first step has to be a constructor
            methodname, args = scenario[0]
            if methodname != '__init__':
                html += error_line("Error in scenario - first step must be a constructor")
                continue
            # initialize both objects
            objects = [ args.init_obj(klass) for klass in (ref_class, student_class) ]
            
            # other steps of that scenario
            for methodname, args in scenario[1:]:
                print("dealing with step {} - {}".format(methodname, args))
                result = [ args.call_obj(o, methodname) for o in objects ]
                print("OK" if result[0] == result[1] else "KO")

        log_correction(self.name, overall)

        html += "</table>"
        html = "<h2>Overall = {}</h2>".format(overall) + html

        print(html)

        return HTML(html)
