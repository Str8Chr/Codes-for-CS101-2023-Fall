# 又是一年双十一，某猫一如既往推出一系列活动，去年尝到甜头的Casper希望今年继续。
# 今年他希望从m个店铺中购买n个商品，每个商品可能在一个或多个店铺中以不同的标价出售。
# 此次跨店满减的活动升级为每满300减50，此外每个店铺也可能有多张不同档位的店铺券”q-x“，
# 希望你能够帮助Casper算出他最少花多少钱买到这n个商品（每个商品只买一件）

# 注意，每一家店铺的店铺券只能用一张，对于任意一张店铺券”q-x“，
# 他表示在当前商铺购买的所有商品标价达到q时，最终应付款可以减x。
# 而跨店满减活动可以叠加使用，它是指所有商品标价之和每满300，可以减去50。


def plans(n, price, count, all_plans, plan):  # 递归列出所有购买方案
    if count == n + 1:
        all_plans.append(plan[:])
        return
    for i in price[count].keys():
        plan.append(i)
        plans(n, price, count + 1, all_plans, plan)
        plan.pop()


def buy(n, m, price, coupon):
    all_plans = list()  # 列出所有购买方案
    plans(n, price, 1, all_plans, [])
    # for i in all_plans:
    #     print(i)
    final_price = list()  # 每个方案的最终价格
    for plan in all_plans:  # 对每个购买方案
        totals_rsp = list()  # 每个店铺的总价
        prices = [price[i][plan[i - 1]] for i in range(1, n + 1)]  # 每个商品的价格
        total = sum(prices)  # 所有商品的总价
        total -= total // 300 * 50  # 跨店满减
        for i in range(1, m + 1):  # 对每个店铺
            prices_rsp = [price[j + 1][plan[j]] for j in range(n) if plan[j] == i]  # 每个商品在该店铺的价格
            totals_rsp.append(sum(prices_rsp))  # 该店铺的总价
        store = 0
        for total_rsp in totals_rsp:
            store += 1
            discount = 0
            for j in coupon[store]:
                if total_rsp >= j[0]:
                    discount = max(j[1], discount)
            total -= discount
        final_price.append(total)
    # print(final_price)
    return min(final_price)


n, m = map(int, input().split())
price = dict()
coupon = dict()
for i in range(n):
    price_i = dict()
    price_raw = list(input().split())
    for j in price_raw:
        price_i[int(list(j.split(':'))[0])] = int(list(j.split(':'))[1])
    price[i + 1] = price_i
for i in range(m):
    coupon_i = list()
    coupon_raw = list(input().split())
    for j in range(len(coupon_raw)):
        coupon_i.append(tuple(map(int, coupon_raw[j].split('-'))))
    coupon[i + 1] = coupon_i
# print(n, m, price, coupon)
print(buy(n, m, price, coupon))