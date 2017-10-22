
trend_type = ['three_day_up', '5_perc_up', '3_perc_up', '1_perc_up',\
              'three_day_down', '5_perc_down', '3_perc_down', '1_perc_down', \
              '1_perc_var', 'NA']

def get_trend_type(close_price):

    if (len(close_price) >= 4):
        if (close_price[0] > close_price[1]) and (close_price[1] > close_price[2]) \
            and (close_price[2] > close_price[3]):
            return 'three_day_up'

        if (close_price[0] < close_price[1]) and (close_price[1] < close_price[2]) \
            and (close_price[2] < close_price[3]):
            return 'three_day_down'

        var = 100 * (close_price[0] - close_price[3]) / close_price[3]
        #print('var=',var)
        if (var >= 5.0):
            return '5_perc_up'
        elif (var >= 3.0):
            return '3_perc_up'
        elif (var >= 1.0):
            return '1_perc_up'
        elif(var <= -5.0):
            return '5_perc_down'
        elif(var <= -3.0):
            return '3_perc_down'
        elif(var <= -1.0):
            return '1_perc_down'
        else:
            return '1_perc_var'
    else:
        return 'NA'

if __name__ == '__main__':
    price1 = [105, 103, 101, 100]
    price2 = [103, 102, 101, 100]
    price3 = [101, 99, 99, 100]
    price4 = [94, 99, 99, 100]
    price5 = [96, 99, 99, 100]
    price6 = [98, 99, 99, 100]
    price7 = [99.5, 99.0, 99.0, 100.0]
    price8 = [100.5, 99.0, 99.0, 100.0]
    price9 = [110, 100, 90]
    price10 = [105, 99, 101, 100]
    price11 = [103.5, 99, 101, 100]

    print(get_trend_type(price1))
    print(get_trend_type(price2))
    print(get_trend_type(price3))
    print(get_trend_type(price4))
    print(get_trend_type(price5))
    print(get_trend_type(price6))
    print(get_trend_type(price7))
    print(get_trend_type(price8))
    print(get_trend_type(price9))
    print(get_trend_type(price10))
    print(get_trend_type(price11))

