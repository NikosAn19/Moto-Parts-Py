from data import Piston


class Generator:
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

    def select_query(self):
        query_dict = {}
        ex1 = "'"
        ex2 = "'"
        if (
                (self.code is None or self.code == '') and
                (self.diameter is None or self.diameter == '') and
                (self.total_height is None or self.total_height == '') and
                (self.compression is None or self.compression == '') and
                (self.pin_diameter is None or self.pin_diameter == '') and
                (self.tact is None or self.tact == '') and
                (self.brand is None or self.brand == '') and
                (self.model is None or self.model == '') and
                (self.oversize is None or self.oversize == '')
        ):
            query = self.zero_argument_query()
        else:
            if self.code is not None and self.code != '':
                query_dict['pistonCode'] = ex1 + str(self.code) + ex2
            if self.diameter is not None and self.diameter != '':
                query_dict['diameter'] = ex1 + str(self.diameter) + ex2
            if self.total_height is not None and self.total_height != '':
                query_dict['totalHeight'] = ex1 + str(self.total_height) + ex2
            if self.compression is not None and self.compression != '':
                query_dict['compressionHeight'] = ex1 + str(self.compression) + ex2
            if self.pin_diameter is not None and self.pin_diameter != '':
                query_dict['pinDiameter'] = ex1 + str(self.pin_diameter) + ex2
            if self.brand is not None and self.brand != '':
                query_dict['brand'] = ex1 + str(self.brand) + ex2
            if self.model is not None and self.model != '':
                query_dict['model'] = ex1 + str(self.model) + ex2
            if self.tact is not None and self.tact != '':
                query_dict['tact'] = ex1 + str(self.tact) + ex2
            if self.oversize is not None and self.oversize != '':
                query_dict['oversize'] = ex1 + str(self.oversize) + ex2
            query = self.full_query(query_dict)
        print(query)
        return query

    def zero_argument_query(self):
        query = 'SELECT * FROM PISTONS;'
        return query

    def full_query(self, query_dict):
        query_part = ""
        query = 'SELECT * FROM PISTONS WHERE '

        element_counter = 1
        dict_size = len(query_dict)
        for key in query_dict:
            if element_counter == dict_size:
                query_part = query_part + 'PISTONS.' + key + ' = ' + query_dict[key] + ';'
            else:
                query_part = query_part + 'PISTONS.' + key + ' = ' + query_dict[key] + ' AND '
            element_counter = element_counter + 1

        query = query + query_part
        # print(query)
        return query

    def update_query(self, brand, model, tact):
        query_dict = {}
        ex1 = "'"
        ex2 = "'"
        if (
                (self.code is None or self.code == '') and
                (self.diameter is None or self.diameter == '') and
                (self.total_height is None or self.total_height == '') and
                (self.compression is None or self.compression == '') and
                (self.pin_diameter is None or self.pin_diameter == '') and
                (self.tact is None or self.tact == '') and
                (self.brand is None or self.brand == '') and
                (self.model is None or self.model == '') and
                (self.oversize is None or self.oversize == '')
        ):
            print('Everything empty')
            query = ''
        else:
            if self.code is not None and self.code != '':
                query_dict['pistonCode'] = ex1 + str(self.code) + ex2
            if self.diameter is not None and self.diameter != '':
                query_dict['diameter'] = ex1 + str(self.diameter) + ex2
            if self.total_height is not None and self.total_height != '':
                query_dict['totalHeight'] = ex1 + str(self.total_height) + ex2
            if self.compression is not None and self.compression != '':
                query_dict['compressionHeight'] = ex1 + str(self.compression) + ex2
            if self.pin_diameter is not None and self.pin_diameter != '':
                query_dict['pinDiameter'] = ex1 + str(self.pin_diameter) + ex2
            if self.brand is not None and self.brand != '':
                query_dict['brand'] = ex1 + str(self.brand) + ex2
            if self.model is not None and self.model != '':
                query_dict['model'] = ex1 + str(self.model) + ex2
            if self.tact is not None and self.tact != '':
                query_dict['tact'] = ex1 + str(self.tact) + ex2
            if self.oversize is not None and self.oversize != '':
                query_dict['oversize'] = ex1 + str(self.oversize) + ex2

            # brand_stm = ""
            # model_stm = ""
            # tact_stm = ""
            # if brand == 'IS NULL':
            #     brand_stm = ' WHERE PISTONS.brand = ' + brand
            # else:
            #     brand = ' WHERE PISTONS.brand = ' + ex1 + brand + ex2
            # if model == 'IS NULL':
            #     model_stm = ' WHERE PISTONS.model = ' + model
            # else:
            #     model_stm = ' PISTONS.model = ' + ex1 + model + ex2
            # if tact == 'IS NULL':
            #     tact_stm = ' WHERE PISTONS.tact = ' + tact
            # else:
            #     tact_stm = ' PISTONS.tact = ' + ex1 + tact + ex2
            where_statement = ' WHERE brand = ' + ex1 + brand + ex2 + ' and ' + ' model = ' + ex1 + model + ex2 + ' and ' + ' tact = ' + ex1 + tact + ex2 + ";"
            query = self.form_update_query(query_dict, where_statement)
        return query

    def form_update_query(self, query_dict, where_statement):
        query = 'UPDATE PISTONS SET '
        query_part = ''
        element_counter = 1
        dict_size = len(query_dict)
        for key in query_dict:
            if element_counter < dict_size:
                query_part = query_part + key + ' = ' + query_dict[key] + ', '

            if element_counter == dict_size:
                query_part = (query_part + key + ' = ' + query_dict[key] + where_statement)
            element_counter = element_counter + 1
        query = query + query_part
        print(query)
        return query

    # def form_delete_query(self):
    #     query = ("DELETE FROM PISTONS WHERE brand=? and model=? and tact=? and pistonCode=? and diameter=? and "
    #              "totalHeight=? and pinDiameter=? and compressionHeight=? and oversize=?")

# piston = Piston('yamaha', 'xt', '4T', 'ybfs', '51.5', '23.4',
#                 '12.3', '23.4', '344-2445-6')
# piston1 = Piston('honda', 'crf', '4T', '', '21.5', '12.5',
#                  '', '', '')
# generator = Generator(piston1)
# generator.update_query('ybfs')
