from data import Piston

class Input_Validator:
    def __init__(self, piston):
        self.brand = piston.brand
        self.model = piston.model
        self.tact = piston.tact
        self.code = piston.code
        self.diameter = piston.diameter
        self.total_height = piston.total_height
        self.pin_diameter = piston.pin_diameter
        self.compression = piston.compression
        self.oversize = piston.oversize

    def validate_numerics(self):
        if self.total_height.replace('.', '', 1).isdigit() and self.compression.replace('.', '', 1).isdigit() and self.diameter.replace('.', '', 1).isdigit() and self.pin_diameter.replace('.', '', 1).isdigit():
            return 1

    def result_only_numbers(self):
        if self.validate_numerics() != 1:
            print('Fields "total_height", "compression", "diameter", "oversize", "pin_diameter" '
                  'should contain only numbers')
            return False
        else:
            print('Validation success')
            return True


# piston1 = Piston('honda', 'crf', '4T', '', '21.5', '12.5',
#                  '12.5', '12.5', '12')
# validator = Input_Validator(piston1)
# print(validator.result_only_numbers())
