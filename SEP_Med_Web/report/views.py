from jinja2 import Environment, FileSystemLoader
from .utils import make_score_editable,create_pivot,get_data_as_dataframe
from django.http import HttpResponse

# 从数据库中读取数据，并整理
def create_report_view(request):
    # 从数据库中获取数据，这里函数的参数应该是任务的id，TODO 生成报告时获得任务的ID然后作为这个函数的参数
    df, creator, created_time = get_data_as_dataframe(1)
    assessment_report = create_pivot(df)

    # 创建一个jinja环境env,获取html模板
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("report/templates/report/report.html")
    # print(assessment_report.to_html())
    template_vars ={
                    "title" : "Safety Assessment Report",
                    "creator" : creator,
                    "created_time" : created_time,
                    # escape 参数控制是否对 HTML 中的特殊字符进行转义。如果设置为 True，则会转义这些字符，防止潜在的 XSS（跨站点脚本）攻击
                    "safety_assessment_table": make_score_editable(assessment_report.to_html()),
                    }
    # 使用这些变量渲染HTML
    html_out = template.render(template_vars)
    return HttpResponse(html_out)
