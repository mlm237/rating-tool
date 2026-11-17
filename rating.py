import math


def _g(x):
    return 2.0 ** (x / 800.0)


def _g_inv(y):
    return 800.0 * math.log2(y)


def _penalty(n):
    # 参加回数が少ないときのマイナス補正
    def F(m):
        return math.sqrt(sum(0.81 ** i for i in range(1, m + 1))) / sum(0.9 ** i for i in range(1, m + 1))

    f_inf = math.sqrt(0.81 / 0.19) / 9.0
    return (F(n) - f_inf) / (F(1) - f_inf) * 1200.0


def calc_rating(perfs):
    """パフォーマンスの履歴（古い順）からレーティングを計算する"""
    if not perfs:
        raise ValueError("履歴が空です")
    hist = list(perfs)
    hist[0] = (hist[0] - 800) * 1.5 + 800  # 初回だけ補正がかかる
    num = den = 0.0
    for i, p in enumerate(reversed(hist), start=1):  # 新しい回ほど重い
        w = 0.9 ** i
        num += _g(p) * w
        den += w
    r = _g_inv(num / den) - _penalty(len(hist))
    if r < 400:  # 400未満は滑らかに圧縮される
        r = 400 * math.exp((r - 400) / 400)
    return r


def needed_perf(perfs, target, n_future):
    """今後n_future回、同じパフォーマンスを取り続けるとき、targetに届くのに必要なパフォーマンス"""
    lo, hi = 0.0, 4000.0
    for _ in range(60):  # 二分探索
        mid = (lo + hi) / 2
        if calc_rating(list(perfs) + [mid] * n_future) >= target:
            hi = mid
        else:
            lo = mid
    return hi