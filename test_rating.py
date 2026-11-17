from rating import calc_rating, needed_perf

PERFS = [112, 485, 478, 703, 921, 994, 553, 1102, 992, 1123, 798, 1163, 1130, 508, 1030, 1214, 1045, 1097, 1219, 1463, 1067, 959, 1044, 1209, 1315, 1023, 1005, 1351, 1475]


def test_first_contest():
    # AtCoder上の実際のレーティングは6
    assert abs(calc_rating(PERFS[:1]) - 6) <= 3


def test_full_history():
    # AtCoder上の実際のレーティングは1142
    assert abs(calc_rating(PERFS) - 1142) <= 3


def test_needed_perf():
    p = needed_perf(PERFS, 1200, 1)
    assert calc_rating(PERFS + [p]) >= 1200
    assert calc_rating(PERFS + [p - 10]) < 1200