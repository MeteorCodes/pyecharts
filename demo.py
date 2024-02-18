from flask import Flask
from pyecharts.charts import Bar, Line, Scatter, EffectScatter, HeatMap, PictorialBar, Geo, Map, Pie, Funnel, Gauge, \
    Liquid, Graph, Polar, Radar, Sunburst, WordCloud, Scatter3D, Line3D, Bar3D
from jinja2.utils import markupsafe
from pyecharts.globals import CurrentConfig

'''
函数速查表：
一.直角坐标系图表
  1.直方图-table_1-example_1.html
  2.折线图-table_2-example_2.html
  3.散点图-table_3-example_3.html
  4.带涟漪效果散点图-table_4-example_4.html
  5.热力图-table_5-example_5.html
  6.象形图-table_6-example_6.html
  7.层叠图-table_7-example_7.html
二.地理图表
  8.Geo地理坐标系(数据不准确)-table_8-example_8.html
  9.Map地理坐标系-table_9-example_9.html
三.基本图表
  10.饼图-table_10-example_10.html
  11.漏斗图-table_11-example_11.html
  12.仪表盘-table_12-example_12.html
  13.水球图-table_13-example_13.html
  14.关系图-table_14-example_14.html
  15.极坐标系-table_15-example_15.html
  16.雷达图-table_16-example_16.html
  17.旭日图-table_17-example_17.html
  18.词云-table_18-example_18.html
  19.表格-table_19-example_19.html
四.3D图标
  20.3D散点图-table_20-example_20.html
  21.3D折线图-table_21-example_21.html
  22.3D直方图-table_22-example_22.html
'''

app = Flask(__name__)

# Pyecharts图表生成需要一些静态资源文件，通过下面代码更改为kesci提供的资源，提高加载速度～
CurrentConfig.ONLINE_HOST = "https://cdn.kesci.com/lib/pyecharts_assets/"


def table_1():
    # 直方图
    bar = Bar()
    x_data = ['Apple', 'HuaWei', 'OPPO', 'Google', 'Vivo']
    y_data = [25, 30, 26, 21, 27]
    bar.add_xaxis(x_data)
    bar.add_yaxis("商家", y_data)
    bar.render('templates\example_1.html')
    return bar


def table_2():
    # 折线图
    line = Line()
    x_data = ['Apple', 'HuaWei', 'OPPO', 'Google', 'Vivo']
    y_data = [25, 30, 26, 21, 27]
    line.add_xaxis(x_data)
    line.add_yaxis("商家", y_data)
    line.render('templates\example_2.html')
    return line


def table_3():
    # 散点图
    scatter = Scatter()
    x_data = ['Apple', 'HuaWei', 'OPPO', 'Google', 'Vivo']
    y_data = [25, 30, 26, 21, 27]
    scatter.add_xaxis(x_data)
    scatter.add_yaxis("商家", y_data)
    scatter.render('templates\example_3.html')
    return scatter


def table_4():
    # 带涟漪效果散点图
    effectscatter = EffectScatter()
    x_data = ['Apple', 'HuaWei', 'OPPO', 'Google', 'Vivo']
    y_data = [25, 30, 26, 21, 27]
    effectscatter.add_xaxis(x_data)
    effectscatter.add_yaxis("商家", y_data)
    effectscatter.render('templates\example_4.html')
    return effectscatter


def table_5():
    # 热力图
    heatmap = HeatMap()
    import random
    '''
    b和a分别是行和列的索引，数据是random.randint(0, 100)生成随机数
    data = [
    [0, 0, 47], [0, 1, 82], [0, 2, 18], [0, 3, 53], [0, 4, 61], [0, 5, 22], [0, 6, 68],
    [1, 0, 33], [1, 1, 56], [1, 2, 75], [1, 3, 12], [1, 4, 39], [1, 5, 58], [1, 6, 87]
    ...#类似于这样24行
    ]
    '''
    data = [[a, b, random.randint(0, 100)] for a in range(24) for b in range(7)]
    x_data = [str(i) for i in range(24)]
    y_data = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']
    heatmap.add_xaxis(x_data)
    heatmap.add_yaxis("本周热力", y_data, data)
    heatmap.render('templates\example_5.html')
    return heatmap


def table_6():
    # 象形图
    pictorialbar = PictorialBar()
    x_data = ['Apple', 'HuaWei', 'OPPO', 'Google', 'Vivo']
    y_data = [25, 30, 26, 21, 27]
    pictorialbar.add_xaxis(x_data)
    pictorialbar.add_yaxis("商家", y_data)
    pictorialbar.render('templates\example_6.html')
    return pictorialbar


def table_7():
    # 层叠图：直方图+折线图
    x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
    y_data_bar = [123, 153, 89, 107, 98, 23]
    y_data_line = [153, 107, 23, 89, 123, 107]
    bar = Bar()
    bar.add_xaxis(x_data)
    bar.add_yaxis("直方图", y_data_bar)

    line = Line()
    line.add_xaxis(x_data)
    line.add_yaxis("折线图", y_data_line)

    overlap = bar.overlap(line)  # 目前只知道overlap只是交换颜色
    overlap.render('templates\example_7.html')
    return overlap


def table_8():
    # Geo地理坐标系：这个表数据不准确（实测example_8.html）
    geo = Geo()
    data = [('山西', 99), ('河北', 71), ('安徽', 117), ('河南', 88), ('山东', 64), ('西藏', 142)]
    geo.add_schema(maptype="china")
    geo.add("数据", data)
    geo.render('templates\example_8.html')
    return geo


def table_9():
    # Map地理坐标系
    map = Map()
    data = [('广东', 118), ('湖北', 97), ('湖南', 126), ('四川', 107), ('重庆', 66), ('黑龙江', 76), ('浙江', 88),
            ('山西', 123), ('河北', 79), ('安徽', 93), ('河南', 61), ('山东', 97), ('西藏', 131)]
    map.add("数据", data, maptype="china")
    map.render('templates\example_9.html')
    return map


def table_10():
    # 饼图
    pie = Pie()
    data = [('Apple', 123), ('Huawei', 153), ('Xiaomi', 89), ('Oppo', 107), ('Vivo', 98), ('Meizu', 23)]
    pie.add("商家", data)
    pie.render('templates\example_10.html')
    return pie


def table_11():
    # 漏斗图
    funnel = Funnel()
    data = [('Apple', 123), ('Huawei', 153), ('Xiaomi', 89), ('Oppo', 107), ('Vivo', 98), ('Meizu', 23)]
    funnel.add("数据", data)
    funnel.render('templates\example_11.html')
    return funnel


def table_12():
    # 仪表盘
    gauge = Gauge()
    gauge.add("数据", [('转化率', 56), ('结合率', 42)])
    gauge.render('templates\example_12.html')
    return gauge


def table_13():
    # 水球图
    liquid = Liquid()
    liquid.add("数据", [0.52, 0.44])  # 上限和下限
    liquid.render('templates\example_13.html')
    return liquid


def table_14():
    # 关系图
    graph = Graph()
    nodes = [
        {"name": "A"}, {"name": "B"}, {"name": "C"}, {"name": "D"}
    ]
    # source的关系是target,比如{"source": "A", "target": "B"}的意思是A和B的关系连线(双向)
    links = [
        {"source": "A", "target": "B"}, {"source": "A", "target": "C"}, {"source": "B", "target": "C"},
        {"source": "C", "target": "D"}, {"source": "D", "target": "A"}, {"source": "D", "target": "C"}
    ]
    graph.add("关系图示例", nodes, links)
    graph.render('templates\example_14.html')
    return graph


def table_15():
    # 极坐标系
    from pyecharts import options as opts
    polar = Polar()
    cate = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
    data = [123, 153, 89, 107, 98, 23]
    polar.add_schema(radiusaxis_opts=opts.RadiusAxisOpts(data=cate, type_="category"))
    polar.add("商家", data, type_='bar')
    polar.render('templates\example_15.html')
    return polar


def table_16():
    # 雷达图
    from pyecharts import options as opts
    radar = Radar()
    data = [
        [115, 125, 110, 65, 70, 83],
        [105, 95, 90, 90, 90, 60],
        [120, 100, 50, 60, 90]
    ]
    schema = [
        opts.RadarIndicatorItem(name="语文", max_=150),
        opts.RadarIndicatorItem(name="数学", max_=150),
        opts.RadarIndicatorItem(name="英语", max_=150),
        opts.RadarIndicatorItem(name="物理", max_=100),
        opts.RadarIndicatorItem(name="生物", max_=100),
        opts.RadarIndicatorItem(name="化学", max_=100)
    ]
    radar.add_schema(schema=schema)
    radar.add("成绩表雷达图", data)
    radar.render('templates\example_16.html')
    return radar


def table_17():
    # 旭日图
    sunburst = Sunburst()
    data = [
        {"name": "湖南",
         "children": [
             {"name": "长沙",
              "children": [
                  {"name": "雨花区", "value": 55}
              ]},
             {"name": "常德",
              "children": [
                  {"name": "武陵区", "value": 156},
                  {"name": "鼎城区", "value": 134},
              ]}
         ],
         },
        {"name": "湖北",
         "children": [
             {"name": "武汉",
              "children": [
                  {"name": "洪山区", "value": 55},
                  {"name": "东湖高新", "value": 78}
              ]},
             {"name": "鄂州", "value": 67}
         ],
         }
    ]
    sunburst.add("数据", data_pair=data)
    sunburst.render("templates/example_17.html")
    return sunburst


def table_18():
    # 词云
    wordcloud = WordCloud()
    word = [
        ("he", 15), ("she", 25), ("it", 17), ("you", 20), ("i", 19),
    ]
    wordcloud.add("词云", word)
    wordcloud.render("templates/example_18.html")
    return wordcloud


def table_19():
    # 表格
    from pyecharts.components import Table
    table = Table()
    header = ["品牌", "月销售量/台", "好评率/%"]
    rows = [
        ["Apple", 255, 75], ["Huawei", 500, 100], ["Google", 213, 50]
    ]
    table.add(header, rows)
    table.render("templates/example_19.html")
    return table


def table_20():
    # 3D散点图
    import random
    scatter3d = Scatter3D()
    # data数据是坐标形式：(20, 30, 50)分别表示X，Y，Z坐标轴坐标
    data = [(random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)) for _ in range(50)]
    # data = [(20, 30, 50), (50, 40, 20), (40, 20, 55)]
    scatter3d.add("数据", data)
    scatter3d.render("templates/example_20.html")
    return scatter3d


def table_21():
    # 3D折线图
    from pyecharts import options as opts
    line3d = Line3D()
    # data数据不要写成坐标形式，写成列表：[12, 17, 21]
    data = [[12, 17, 21], [20, 14, 31], [32, 47, 11]]
    line3d.add("数据", data, xaxis3d_opts=opts.Axis3DOpts(type_="value"), yaxis3d_opts=opts.Axis3DOpts(type_="value"))
    line3d.render("templates/example_21.html")
    return line3d


def table_22():
    # 3D直方图
    import random
    from pyecharts import options as opts
    # data数据是列表形式[1, 1, 32]
    data = [[i, j, random.randint(0, 100)] for i in range(24) for j in range(7)]
    hour_list = [str(i) for i in range(24)]
    week_list = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']

    bar3d = Bar3D()
    bar3d.add("数据", data,
              xaxis3d_opts=opts.Axis3DOpts(hour_list, type_="category"),
              yaxis3d_opts=opts.Axis3DOpts(week_list, type_="category"),
              zaxis3d_opts=opts.Axis3DOpts(type_="value"),
              )
    bar3d.render("templates/example_22.html")
    return bar3d


# 测试
@app.route('/')
def test():
    test = table_9()
    return markupsafe.Markup(test.render_embed())


if __name__ == '__main__':
    app.run(debug=True)
