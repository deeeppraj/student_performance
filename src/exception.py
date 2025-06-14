import sys

def custom_error_message(error,detail:sys):
    _,_,error_tb = detail.exc_info()
    filename = error_tb.tb_frame.f_code.co_filename
    message = f'Error detected in {filename} , line no {error_tb.tb_lineno} , with the message {str(error)} '
    return message

class CustomException(Exception):
    def __init__(self,error,detail:sys):
        super().__init__(error)
        self.error = custom_error_message(error,detail)

    def __str__(self):
        return self.error