from tr_option.base import KWTR

# [ opt10007 : 시세표성정보요청 ]
class Opt10007(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = "opt10007"
        self.record_name = '시세표성정보'
        self.header = [
            '종목명', '종목코드', '날짜', '시간', '전일종가', '전일거래량', '상한가', '하한가', '전일거래대금', '상장주식수',
            '현재가', '부호', '등락률', '전일비', '시가', '고가', '저가', '체결량', '거래량', '거래대금',
            '예상체결가', '예상체결량', '예상매도우선호가', '예상매수우선호가', '거래시작일', '행사가격', '최고가', '최저가', '최고가일', '최저가일',
            '매도1호가', '매도2호가', '매도3호가', '매도4호가', '매도5호가', '매도6호가', '매도7호가', '매도8호가', '매도9호가', '매도10호가',
            '매수1호가', '매수2호가', '매수3호가', '매수4호가', '매수5호가', '매수6호가', '매수7호가', '매수8호가', '매수9호가', '매수10호가',
            '매도1호가잔량', '매도2호가잔량', '매도3호가잔량', '매도4호가잔량', '매도5호가잔량', '매도6호가잔량', '매도7호가잔량', '매도8호가잔량', '매도9호가잔량', '매도10호가잔량',
            '매수1호가잔량', '매수2호가잔량', '매수3호가잔량', '매수4호가잔량', '매수5호가잔량', '매수6호가잔량', '매수7호가잔량', '매수8호가잔량', '매수9호가잔량', '매수10호가잔량',
            '매도1호가직전대비', '매도2호가직전대비', '매도3호가직전대비', '매도4호가직전대비', '매도5호가직전대비', '매도6호가직전대비', '매도7호가직전대비', '매도8호가직전대비', '매도9호가직전대비', '매도10호가직전대비',
            '매수1호가직전대비', '매수2호가직전대비', '매수3호가직전대비', '매수4호가직전대비', '매수5호가직전대비', '매수6호가직전대비', '매수7호가직전대비', '매수8호가직전대비', '매수9호가직전대비', '매수10호가직전대비',
            '매도1호가건수', '매도2호가건수', '매도3호가건수', '매도4호가건수', '매도5호가건수',
            '매수1호가건수', '매수2호가건수', '매수3호가건수', '매수4호가건수', '매수5호가건수',
            'LP매도1호가잔량', 'LP매도2호가잔량', 'LP매도3호가잔량', 'LP매도4호가잔량', 'LP매도5호가잔량', 'LP매도6호가잔량', 'LP매도7호가잔량', 'LP매도8호가잔량', 'LP매도9호가잔량', 'LP매도10호가잔량',
            'LP매수1호가잔량', 'LP매수2호가잔량', 'LP매수3호가잔량', 'LP매수4호가잔량', 'LP매수5호가잔량', 'LP매수6호가잔량', 'LP매수7호가잔량', 'LP매수8호가잔량', 'LP매수9호가잔량', 'LP매수10호가잔량',
            '총매수잔량', '총매도잔량', '총매수건수', '총매도건수',
        ]


    def tr_opt(self, code, prev_next, screen_no):

        self.core.set_input_value("종목코드", code)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        return self.core.receive_tr_data_handler


    def tr_opt_data(self, tr_code, rq_name, index):
        ret = {
            'header' : self.header,
            'rows' : [
                [ self.core.get_comm_data(tr_code, rq_name, index, column) for column in self.header ]
            ]
        }

        return ret


    def tr_opt_data_ex(self, tr_code, rq_name):
        ret = {
            'header' : self.header,
            'rows' : self.core.get_comm_data_ex(tr_code, rq_name)
        }

        return ret