import os
import time
import datetime


def formatElement(lc_tick_0, lc_timestamp_0, matchObj):
    '''
    :param lc_tick_0: RTC时间所对应tick值
    :param lc_timestamp_0: RTC时间
    :param matchObj: 读取并切片后的log信息
    :return: str 格式化后的信息
    '''
    lc_tick = matchObj[0]
    lc_id = matchObj[1]
    lc_type = matchObj[2]
    lc_status = matchObj[3][:-1]
    tick_diff = int(lc_tick) - int(lc_tick_0)
    lc_timestamp_ms = tick_diff + int(lc_timestamp_0) * 1000
    lc_localtime = lc_timestamp_ms / 1000
    lc_localtime2 = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(lc_localtime))
    lc_localtime_sec = lc_timestamp_ms % 1000
    time_stamp = "%s.%03d" % (lc_localtime2, lc_localtime_sec)
    str = [lc_timestamp_ms, lc_id, lc_type, lc_status, time_stamp]
    return str


def formatElementLevel(lc_tick_0, lc_timestamp_0, matchObj):
    '''
    :param lc_tick_0: RTC时间所对应tick值
    :param lc_timestamp_0: RTC时间
    :param matchObj: 读取并切片后的log信息
    :return: str 格式化后的信息(tick时间，电量，本地时间)
    '''
    lc_tick = matchObj[0]
    lc_status = matchObj[3][:-1]
    lc_timestamp_ms = (int(lc_tick) - int(lc_tick_0)) + int(lc_timestamp_0) * 1000
    lc_localtime = lc_timestamp_ms / 1000
    lc_localtime2 = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(lc_localtime))
    lc_localtime_sec = lc_timestamp_ms % 1000
    time_stamp = "%s.%03d" % (lc_localtime2, lc_localtime_sec)
    str = '{timestamp:%s, powervalue:%s, localtime:"%s"},\n' % (lc_timestamp_ms, lc_status, time_stamp)
    # str = '{timestamp:%s, powervalue:%s},\n' % (lc_timestamp_ms, lc_status)
    return str


def formatList(list):
    '''
    区间处理，并除去可能会叠加的区间
    :param list: 经setForm处理后的数据列表
    :return: 最终保存为js数据
    '''
    list2 = []
    sig = type = 9  # 标记，用于判断log类型以区分不同状态
    n = 0  # 标记，用于判断状态是否改变
    for i in range(0, len(list)):
        k = 0  # 标记，用于判断状态是否改变
        if sig == list[i][1] and type == list[i][2]:
            continue
        elif list[i][3] != '0':
            k = 1
            for j in range(i, len(list)):
                if list[j][3] == '0' and list[i][2] == list[j][2]:  # 状态有改变的数据块
                    n += 1
                    str = '{timestamp1:%d, timestamp2:%d, lc_id:%s, lc_type:%s, lc_status1:%s, ' \
                          'lc_status2:%s, localtime1:"%s", localtime2:"%s"},\n' % (
                              list[i][0], list[j][0], list[i][1], list[i][2], list[i][3],
                              list[j][3], list[i][4], list[j][4])
                    list2.append(str)
                    break
        if k != 0 and n == 0:  # 在log结束前，状态仍然未改变的数据块
            type = list[i][2]
            sig = list[i][1]
            str = '{timestamp1:%d, timestamp2:%d, lc_id:%s, lc_type:%s, lc_status1:%s, lc_status2:%s, ' \
                  'localtime1:"%s", localtime2:"%s"},\n' % (
                      list[i][0], list[len(list) - 1][0], list[i][1], list[i][2],
                      list[i][3], list[len(list) - 1][3], list[i][4], list[len(list) - 1][4])
            list2.append(str)
    return list2
