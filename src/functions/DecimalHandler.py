import jsonpickle

class DecimalHandler(jsonpickle.handlers.BaseHandler):
    def flatten(self, obj, data):
        return obj.__str__() #Convert to json friendly format